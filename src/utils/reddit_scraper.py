"""Reddit Data Scraper.

Scrapes Reddit data using asyncpraw for true async support.
"""

import asyncio
import os
from datetime import datetime
from typing import Any

import asyncpraw
from dotenv import load_dotenv

from .config import DEFAULT_LIMITS, PAIN_POINT_QUERIES, SUBREDDITS


class RedditScraper:
    """Reddit data scraper using asyncpraw."""

    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Store credentials for creating Reddit instance in async context
        self.client_id = os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = os.getenv("REDDIT_CLIENT_SECRET")
        self.user_agent = os.getenv("REDDIT_USER_AGENT", "SaaS Idea Finder Bot")

        # Target subreddits from config
        self.subreddits = SUBREDDITS

    async def _scrape_subreddit_posts(
        self, subreddit_name: str, post_type: str, limit: int
    ) -> tuple[str, list[dict[str, Any]]]:
        """Scrape posts from a single subreddit asynchronously."""
        try:
            print(f"📊 Scraping {post_type} posts from r/{subreddit_name}...")

            async with asyncpraw.Reddit(
                client_id=self.client_id,
                client_secret=self.client_secret,
                user_agent=self.user_agent,
            ) as reddit:
                subreddit = await reddit.subreddit(subreddit_name)
                posts = []

                # Get posts based on type
                if post_type == "hot":
                    post_iter = subreddit.hot(limit=limit)
                elif post_type == "new":
                    post_iter = subreddit.new(limit=limit)
                elif post_type == "top":
                    post_iter = subreddit.top(time_filter="week", limit=limit)
                else:
                    post_iter = subreddit.hot(limit=limit)

                async for post in post_iter:
                    post_data = self._create_post_data(post, subreddit_name, post_type)
                    posts.append(post_data)

            print(f"✅ Scraped {len(posts)} {post_type} posts from r/{subreddit_name}")
            return subreddit_name, posts

        except Exception as e:
            print(f"❌ Error scraping r/{subreddit_name}: {str(e)}")
            return subreddit_name, []

    async def _search_pain_points_in_subreddit(
        self, subreddit_name: str, limit_per_subreddit: int
    ) -> tuple[str, list[dict[str, Any]]]:
        """Search for pain points in a single subreddit asynchronously."""
        try:
            print(f"🔍 Searching for pain points in r/{subreddit_name}...")

            async with asyncpraw.Reddit(
                client_id=self.client_id,
                client_secret=self.client_secret,
                user_agent=self.user_agent,
            ) as reddit:
                subreddit = await reddit.subreddit(subreddit_name)
                posts = []

                # Search for each pain point query
                for query in PAIN_POINT_QUERIES:
                    search_results = subreddit.search(query, limit=2, sort="relevance")
                    async for post in search_results:
                        post_data = self._create_post_data(post, subreddit_name, "pain_point", query)
                        posts.append(post_data)

                # Remove duplicates based on URL
                seen_urls = set()
                unique_posts = []
                for post in posts:
                    if post["url"] not in seen_urls:
                        seen_urls.add(post["url"])
                        unique_posts.append(post)

                result_posts = unique_posts[:limit_per_subreddit]
                print(f"✅ Found {len(result_posts)} pain point posts in r/{subreddit_name}")
                return subreddit_name, result_posts

        except Exception as e:
            print(f"❌ Error searching pain points in r/{subreddit_name}: {str(e)}")
            return subreddit_name, []

    def _create_post_data(self, post: Any, subreddit_name: str, post_type: str, query: str = None) -> dict[str, Any]:
        """Create standardized post data dictionary."""
        post_data = {
            "title": post.title,
            "url": f"https://reddit.com{post.permalink}",
            "score": post.score,
            "num_comments": post.num_comments,
            "created_utc": post.created_utc,
            "created_date": datetime.fromtimestamp(post.created_utc).strftime("%Y-%m-%d %H:%M:%S"),
            "author": str(post.author) if post.author else "[deleted]",
            "selftext": post.selftext[:200] if post.selftext else "",  # Limit text length for token optimization
            "subreddit": subreddit_name,
            "upvote_ratio": post.upvote_ratio,
            "is_self": post.is_self,
            "link_flair_text": post.link_flair_text,
            "num_awards": post.total_awards_received,
            "post_type": post_type,
        }

        # Add query-specific fields
        if query:
            post_data["pain_point_query"] = query

        return post_data

    async def scrape_hot_posts_async(self, limit_per_subreddit: int = None) -> dict[str, list[dict[str, Any]]]:
        """Scrape hot posts from all subreddits asynchronously."""
        if limit_per_subreddit is None:
            limit_per_subreddit = DEFAULT_LIMITS["hot_posts"]

        tasks = [
            self._scrape_subreddit_posts(subreddit_name, "hot", limit_per_subreddit) for subreddit_name in self.subreddits
        ]

        results = await asyncio.gather(*tasks, return_exceptions=True)

        all_posts = {}
        for result in results:
            if isinstance(result, Exception):
                print(f"❌ Task failed: {result}")
                continue
            subreddit_name, posts = result
            all_posts[subreddit_name] = posts

        return all_posts

    async def scrape_weekly_top_posts_async(self, limit_per_subreddit: int = None) -> dict[str, list[dict[str, Any]]]:
        """Scrape weekly top posts from all subreddits asynchronously."""
        if limit_per_subreddit is None:
            limit_per_subreddit = DEFAULT_LIMITS["top_posts"]

        tasks = [
            self._scrape_subreddit_posts(subreddit_name, "top", limit_per_subreddit) for subreddit_name in self.subreddits
        ]

        results = await asyncio.gather(*tasks, return_exceptions=True)

        all_posts = {}
        for result in results:
            if isinstance(result, Exception):
                print(f"❌ Task failed: {result}")
                continue
            subreddit_name, posts = result
            all_posts[subreddit_name] = posts

        return all_posts

    async def get_pain_point_posts_async(self, limit_per_subreddit: int = None) -> dict[str, list[dict[str, Any]]]:
        """Search for pain points across all subreddits asynchronously."""
        if limit_per_subreddit is None:
            limit_per_subreddit = DEFAULT_LIMITS["pain_point_posts"]

        tasks = [
            self._search_pain_points_in_subreddit(subreddit_name, limit_per_subreddit) for subreddit_name in self.subreddits
        ]

        results = await asyncio.gather(*tasks, return_exceptions=True)

        all_pain_point_posts = {}
        for result in results:
            if isinstance(result, Exception):
                print(f"❌ Task failed: {result}")
                continue
            subreddit_name, posts = result
            all_pain_point_posts[subreddit_name] = posts

        return all_pain_point_posts
