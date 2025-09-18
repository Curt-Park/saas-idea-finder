"""Technical Feasibility Analyzer Agent.

Analyzes whether it can be implemented with simple tech stack for solo entrepreneurs to develop and maintain.
"""

from typing import Any

from crewai import Agent, Task
from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain_openai import ChatOpenAI


class TechFeasibilityAnalyzerAgent:
    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key, temperature=0.3)

        # Tool setup
        self.search_tool = SerperDevTool()
        self.website_tool = WebsiteSearchTool()

        self.agent = Agent(
            role="Technical Feasibility Analysis Expert",
            goal="Analyze tech stack and implementation difficulty for solo entrepreneurs",
            backstory="""You are an expert in software development and technical architecture. 
            Your specialty is recommending tech stacks and implementation methods 
            that solo developers can efficiently develop and maintain.""",
            tools=[self.search_tool, self.website_tool],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    def create_tech_feasibility_task(self, market_analysis_data: dict[str, Any]) -> Task:
        """Create technical feasibility analysis task."""
        return Task(
            description=f"""
            Analyze technical feasibility based on market analysis results:
            
            Market analysis data: {market_analysis_data}
            
            Analysis items:
            
            1. Core Feature Analysis:
               - Identify core features needed for MVP (Minimum Viable Product)
               - Evaluate technical complexity of each feature
               - Suggest development order by priority
            
            2. Tech Stack Recommendations:
               - Frontend: Choose from React, Vue, Svelte, etc.
               - Backend: Choose from Node.js, Python, Go, etc.
               - Database: Choose from PostgreSQL, MongoDB, SQLite, etc.
               - Cloud: Choose from AWS, GCP, Vercel, Netlify, etc.
            
            3. Development Difficulty Assessment:
               - Features implementable by beginners (1-3 months)
               - Intermediate developer level features (3-6 months)
               - Advanced developer level features (6+ months)
               - External tool/API dependency analysis
            
            4. Maintainability Analysis:
               - Expected code complexity
               - Deployment and operation automation possibilities
               - Monitoring and debugging tool requirements
               - Security and performance optimization requirements
            
            5. Cost Analysis:
               - Development tools and license costs
               - Cloud infrastructure costs
               - External API usage costs
               - Maintenance personnel costs
            
            6. Scalability Considerations:
               - Scaling plan for user growth
               - Microservice transition necessity
               - Database optimization strategies
               - CDN and caching strategies
            
            Deliverables:
            - Recommended tech stack
            - Development difficulty assessment (1-10 scale)
            - Expected development timeline
            - Cost predictions
            - Scalability roadmap
            """,
            agent=self.agent,
            expected_output="""
            Technical Feasibility Analysis Report:
            1. Core features and priorities
            2. Recommended tech stack
            3. Development difficulty assessment
            4. Maintainability analysis
            5. Cost predictions
            6. Scalability roadmap
            7. Implementation recommendations
            """,
        )

    def analyze_tech_feasibility(self, market_analysis_data: dict[str, Any]) -> dict[str, Any]:
        """Execute technical feasibility analysis."""
        task = self.create_tech_feasibility_task(market_analysis_data)

        # Execute agent
        result = self.agent.execute_task(task)

        return {"market_analysis_data": market_analysis_data, "tech_feasibility": result, "status": "completed"}
