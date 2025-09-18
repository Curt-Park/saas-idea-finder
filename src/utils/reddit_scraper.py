"""Reddit Data Scraper.

Scrapes Reddit data using PRAW (Python Reddit API Wrapper).
"""

import os
from datetime import datetime
from typing import Any

import praw
from dotenv import load_dotenv


class RedditScraper:
    """Reddit data scraper using PRAW."""

    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Reddit API credentials
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT", "SaaS Idea Finder Bot"),
        )

        # Target subreddits
        self.subreddits = [
            "entrepreneur",
            "SaaS",
            "smallbusiness",
            "freelance",
            "productivity",
            "webdev",
            "startups",
            "indiehackers",
            "remotework",
            "digitalnomad",
            "MachineLearning",
            "artificial",
            "OpenAI",
            "ChatGPT",
            "LocalLLaMA",
            "StableDiffusion",
            "LangChain",
            "MLOps",
            "datascience",
            "AutoGPT",
        ]

    def scrape_hot_posts(self, limit_per_subreddit: int = 10) -> dict[str, list[dict[str, Any]]]:
        """Scrape hot posts from target subreddits.

        Args:
            limit_per_subreddit: Number of posts to scrape per subreddit

        Returns:
            Dictionary with subreddit names as keys and lists of post data as values
        """
        all_posts = {}

        for subreddit_name in self.subreddits:
            try:
                print(f"📊 Scraping r/{subreddit_name}...")
                subreddit = self.reddit.subreddit(subreddit_name)
                posts = []

                # Get hot posts
                for post in subreddit.hot(limit=limit_per_subreddit):
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
                    }
                    posts.append(post_data)

                all_posts[subreddit_name] = posts
                print(f"✅ Scraped {len(posts)} posts from r/{subreddit_name}")

            except Exception as e:
                print(f"❌ Error scraping r/{subreddit_name}: {str(e)}")
                all_posts[subreddit_name] = []

        return all_posts

    def scrape_recent_posts(self, limit_per_subreddit: int = 10) -> dict[str, list[dict[str, Any]]]:
        """Scrape recent posts from target subreddits.

        Args:
            limit_per_subreddit: Number of posts to scrape per subreddit

        Returns:
            Dictionary with subreddit names as keys and lists of post data as values
        """
        all_posts = {}

        for subreddit_name in self.subreddits:
            try:
                print(f"📊 Scraping recent posts from r/{subreddit_name}...")
                subreddit = self.reddit.subreddit(subreddit_name)
                posts = []

                # Get new posts
                for post in subreddit.new(limit=limit_per_subreddit):
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
                    }
                    posts.append(post_data)

                all_posts[subreddit_name] = posts
                print(f"✅ Scraped {len(posts)} recent posts from r/{subreddit_name}")

            except Exception as e:
                print(f"❌ Error scraping r/{subreddit_name}: {str(e)}")
                all_posts[subreddit_name] = []

        return all_posts

    def search_posts(self, query: str, limit_per_subreddit: int = 20) -> dict[str, list[dict[str, Any]]]:
        """Search for posts containing specific keywords.

        Args:
            query: Search query
            limit_per_subreddit: Number of posts to return per subreddit

        Returns:
            Dictionary with subreddit names as keys and lists of post data as values
        """
        all_posts = {}

        for subreddit_name in self.subreddits:
            try:
                print(f"🔍 Searching '{query}' in r/{subreddit_name}...")
                subreddit = self.reddit.subreddit(subreddit_name)
                posts = []

                # Search for posts
                for post in subreddit.search(query, limit=limit_per_subreddit, sort="relevance"):
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
                        "search_query": query,
                    }
                    posts.append(post_data)

                all_posts[subreddit_name] = posts
                print(f"✅ Found {len(posts)} posts matching '{query}' in r/{subreddit_name}")

            except Exception as e:
                print(f"❌ Error searching r/{subreddit_name}: {str(e)}")
                all_posts[subreddit_name] = []

        return all_posts

    def get_pain_point_posts(self, limit_per_subreddit: int = 5) -> dict[str, list[dict[str, Any]]]:
        """Search for posts that likely contain pain points.

        Args:
            limit_per_subreddit: Number of posts to return per subreddit

        Returns:
            Dictionary with subreddit names as keys and lists of post data as values
        """
        pain_point_queries = [
            "I wish there was",
            "frustrated with",
            "annoying",
            "pain point",
            "problem with",
            "need a tool",
            "looking for",
            "can't find",
            "struggling with",
            "difficult to",
            "waste of time",
            "manual process",
            "automate this",
            "boring task",
            "repetitive",
        ]

        all_posts = {}

        for subreddit_name in self.subreddits:
            try:
                print(f"🔍 Searching for pain points in r/{subreddit_name}...")
                subreddit = self.reddit.subreddit(subreddit_name)
                posts = []

                # Search for each pain point query
                for query in pain_point_queries:
                    for post in subreddit.search(query, limit=2, sort="relevance"):
                        post_data = {
                            "title": post.title,
                            "url": f"https://reddit.com{post.permalink}",
                            "score": post.score,
                            "num_comments": post.num_comments,
                            "created_utc": post.created_utc,
                            "created_date": datetime.fromtimestamp(post.created_utc).strftime("%Y-%m-%d %H:%M:%S"),
                            "author": str(post.author) if post.author else "[deleted]",
                            "selftext": post.selftext[:200]
                            if post.selftext
                            else "",  # Limit text length for token optimization
                            "subreddit": subreddit_name,
                            "upvote_ratio": post.upvote_ratio,
                            "is_self": post.is_self,
                            "link_flair_text": post.link_flair_text,
                            "num_awards": post.total_awards_received,
                            "pain_point_query": query,
                        }
                        posts.append(post_data)

                # Remove duplicates based on URL
                seen_urls = set()
                unique_posts = []
                for post in posts:
                    if post["url"] not in seen_urls:
                        seen_urls.add(post["url"])
                        unique_posts.append(post)

                all_posts[subreddit_name] = unique_posts[:limit_per_subreddit]
                print(f"✅ Found {len(all_posts[subreddit_name])} pain point posts in r/{subreddit_name}")

            except Exception as e:
                print(f"❌ Error searching pain points in r/{subreddit_name}: {str(e)}")
                all_posts[subreddit_name] = []

        return all_posts
