"""Reddit Trend Analyzer Agent.

Analyzes Reddit communities to identify trending topics and pain points for SaaS opportunities.
"""

import asyncio
from typing import Any

from crewai import Agent, Task
from langchain_openai import ChatOpenAI

from ..utils.reddit_scraper import RedditScraper


class RedditTrendAnalyzerAgent:
    def __init__(self, openai_api_key: str, model: str = "gpt-4o-mini", temperature: float = 0.3):
        self.llm = ChatOpenAI(model=model, api_key=openai_api_key, temperature=temperature)

        # Reddit scraper
        self.reddit_scraper = RedditScraper()

        self.agent = Agent(
            role="Reddit Trend Analysis Expert",
            goal="Analyze Reddit communities to identify trending topics and pain points for SaaS opportunities",
            backstory="""You are an expert in Reddit community analysis and trend identification. 
            Your specialty is analyzing Reddit posts, comments, and discussions to identify 
            recurring pain points, unmet needs, and emerging opportunities for SaaS businesses.
            You have access to real Reddit data scraped from various subreddits.""",
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    def create_reddit_trend_analysis_task(self, reddit_data: dict[str, Any]) -> Task:
        """Create Reddit trend analysis task."""
        return Task(
            description=f"""
            Analyze the following Reddit data to identify trending topics and SaaS opportunities:
            
            REDDIT DATA TO ANALYZE:
            {reddit_data}
            
            Analysis Instructions:
            
            1. Pain Point Identification:
               - Identify recurring complaints and frustrations from the Reddit posts
               - Look for "I wish there was a tool for..." type posts
               - Find workflow inefficiencies and manual processes that could be automated
               - Note integration gaps between tools mentioned
               - For each pain point found, extract:
                 * Direct Reddit post URL and title
                 * Post date and engagement metrics (upvotes, comments)
                 * Key quotes from users expressing the pain point
                 * Subreddit where the discussion occurred
                 * Severity and frequency indicators
            
            2. Trending Topics Analysis:
               - Identify the most upvoted and commented posts
               - Look for emerging needs and demands
               - Note technology adoption patterns
               - Identify workflow changes and adaptations
               - Include post dates and engagement metrics for trending topics
            
            3. Market Gaps Identification:
               - Find tools that don't exist but are needed
               - Identify existing tools with significant limitations
               - Look for niche markets with limited solutions
               - Find underserved professional groups
               - Reference specific Reddit discussions that highlight these gaps
            
            4. Success Stories Analysis:
               - Look for successful tool launches mentioned
               - Find user testimonials and recommendations
               - Identify revenue and growth discussions
               - Note pricing and business model insights
               - Find marketing and customer acquisition strategies
               - Include dates and sources for success stories
            
            5. Competitive Landscape:
               - Identify popular tools and services mentioned
               - Find user complaints about existing solutions
               - Look for feature requests and improvements
               - Note pricing discussions and concerns
               - Identify switching behavior and reasons
               - Reference specific Reddit posts discussing these topics
            
            Deliverables:
            - Top 10 trending pain points (ranked by frequency and severity) with:
              * Direct Reddit post references (URLs, titles, dates)
              * Engagement metrics (upvotes, comments)
              * Key user quotes
              * Subreddit sources
            - Emerging market opportunities with source references
            - Underserved niches with potential and supporting Reddit discussions
            - Success patterns from existing solutions with dates and sources
            - Competitive gaps and opportunities with specific Reddit post references
            
            IMPORTANT: 
            1. Keep the analysis concise and focused
            2. Prioritize the most significant pain points and opportunities
            3. Limit detailed examples to the top 3-5 most important findings to avoid token limit issues
            4. For each pain point, provide clear, actionable descriptions that can be matched to specific SaaS solutions
            5. Include specific keywords and phrases that successful projects might use in their marketing
            """,
            agent=self.agent,
            expected_output="""
            Reddit Trend Analysis Report:
            1. Top trending pain points (ranked by frequency and severity) with:
               - Direct Reddit post references (URLs, titles, dates)
               - Engagement metrics (upvotes, comments)
               - Key user quotes
               - Subreddit sources
            2. Emerging market opportunities with source references
            3. Underserved niches with potential and supporting Reddit discussions
            4. Success patterns from existing solutions with dates and sources
            5. Competitive gaps and opportunities with specific Reddit post references
            6. Recommended focus areas for SaaS development
            """,
        )

    async def analyze_reddit_trends_async(self) -> dict[str, Any]:
        """Execute Reddit trend analysis asynchronously."""
        print("🔍 Collecting Reddit data asynchronously...")

        # Run all scraping operations concurrently
        hot_posts_task = self.reddit_scraper.scrape_hot_posts_async(limit_per_subreddit=10)
        weekly_top_posts_task = self.reddit_scraper.scrape_weekly_top_posts_async(limit_per_subreddit=10)
        pain_point_posts_task = self.reddit_scraper.get_pain_point_posts_async(limit_per_subreddit=10)
        
        # Wait for all tasks to complete
        hot_posts, weekly_top_posts, pain_point_posts = await asyncio.gather(
            hot_posts_task,
            weekly_top_posts_task,
            pain_point_posts_task,
            return_exceptions=True
        )
        
        # Handle any exceptions
        reddit_data = {}
        reddit_data["hot_posts"] = hot_posts if not isinstance(hot_posts, Exception) else {}
        reddit_data["weekly_top_posts"] = weekly_top_posts if not isinstance(weekly_top_posts, Exception) else {}
        reddit_data["pain_point_posts"] = pain_point_posts if not isinstance(pain_point_posts, Exception) else {}
        
        print("✅ Reddit data collection completed")

        # Create analysis task with real data
        task = self.create_reddit_trend_analysis_task(reddit_data)

        # Execute agent
        result = self.agent.execute_task(task)

        return {"reddit_trend_analysis": result, "reddit_data": reddit_data, "status": "completed"}

    def analyze_reddit_trends(self) -> dict[str, Any]:
        """Execute Reddit trend analysis (sync wrapper)."""
        return asyncio.run(self.analyze_reddit_trends_async())
