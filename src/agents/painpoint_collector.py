"""Painpoint Collector Agent.

Identifies painpoints and new needs from Reddit, social media, Google Trends, etc.
"""

from typing import Any

from crewai import Agent, Task
from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain_openai import ChatOpenAI


class PainpointCollectorAgent:
    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key, temperature=0.3)

        # Tool setup
        self.search_tool = SerperDevTool()
        self.website_tool = WebsiteSearchTool()

        self.agent = Agent(
            role="Painpoint Collection Expert",
            goal="Identify painpoints and new needs from Reddit, social media, and Google Trends",
            backstory="""You are an expert in consumer behavior and market trend analysis. 
            Your specialty is accurately identifying problems people face and 
            new needs across various social platforms and online communities.""",
            tools=[self.search_tool, self.website_tool],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    def create_painpoint_collection_task(self, topic: str) -> Task:
        """Create painpoint collection task."""
        return Task(
            description=f"""
            Topic: {topic}
            
            Follow these steps to collect painpoints and needs:
            
            1. Reddit Analysis:
               - Collect user complaints and requests from relevant subreddits
               - Search for keywords like "I wish", "I need", "frustrated", "annoying"
               - Prioritize complaints with high upvotes
            
            2. Social Media Analysis:
               - Search for relevant hashtags and keywords on Twitter, Instagram, TikTok
               - Collect user complaints and requests
               - Identify needs from viral content
            
            3. Google Trends Analysis:
               - Analyze search trends for related keywords
               - Analyze search patterns like "how to", "best", "alternative"
               - Identify regional and temporal trend changes
            
            4. Organize Collected Information:
               - Analyze frequency and severity of each painpoint
               - Prioritize unresolved needs
               - Identify potential business opportunities
            
            Deliverables:
            - Painpoint list (by frequency)
            - New needs list
            - Trend analysis results
            - Business opportunity suggestions
            """,
            agent=self.agent,
            expected_output="""
            Painpoint Collection Report:
            1. Main painpoints (by frequency)
            2. New needs list
            3. Trend analysis results
            4. Business opportunity suggestions
            """,
        )

    def collect_painpoints(self, topic: str) -> dict[str, Any]:
        """Execute painpoint collection."""
        task = self.create_painpoint_collection_task(topic)

        # Execute agent
        result = self.agent.execute_task(task)

        return {"topic": topic, "painpoints": result, "status": "completed"}
