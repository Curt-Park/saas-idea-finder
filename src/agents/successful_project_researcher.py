"""Successful Project Researcher Agent.

Researches and analyzes successful micro-SaaS projects that are already generating revenue.
"""

from typing import Any

from crewai import Agent, Task
from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain_openai import ChatOpenAI


class SuccessfulProjectResearcherAgent:
    def __init__(self, openai_api_key: str, model: str = "gpt-4o-mini", temperature: float = 0.3):
        self.llm = ChatOpenAI(model=model, api_key=openai_api_key, temperature=temperature)

        # Tool setup
        self.search_tool = SerperDevTool()
        self.website_tool = WebsiteSearchTool()

        self.agent = Agent(
            role="Successful Micro-SaaS Research Expert",
            goal="Research and analyze successful micro-SaaS projects that are generating revenue",
            backstory="""You are an expert in micro-SaaS research and market analysis. 
            Your specialty is identifying successful small-scale SaaS businesses that are 
            already generating revenue and analyzing their business models, features, and market positioning.""",
            tools=[self.search_tool, self.website_tool],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    def create_successful_project_research_task(self, reddit_trend_analysis: str) -> Task:
        """Create successful project research task."""
        return Task(
            description=f"""
            Research and analyze successful micro-SaaS projects that are already generating revenue.
            Focus on projects that address the pain points and opportunities identified in the Reddit trend analysis.

            REDDIT TREND ANALYSIS SUMMARY:
            {reddit_trend_analysis}
            
            Research sources:
            1. Indie Hackers - Successful micro-SaaS case studies
            2. Product Hunt - Trending and successful products
            3. Starter Story - Entrepreneur interviews and case studies
            4. MicroConf - Micro-SaaS conference presentations
            5. Twitter/X - Solo entrepreneur success stories
            6. Reddit r/indiehackers - Success stories and revenue reports
            7. GitHub - Open source projects with commercial success
            8. Hacker News - Startup and SaaS discussions
            
            Focus on projects with these characteristics:
            - Monthly recurring revenue (MRR) between $1K-$50K
            - Solo founder or small team (1-3 people)
            - Simple, focused functionality
            - Low competition or niche market
            - Proven product-market fit
            - Sustainable business model
            - Launched within the last 1-2 years (prioritize recent launches)
            - Still actively growing and generating revenue
            - Address similar pain points identified in Reddit trend analysis
            
            IMPORTANT: Match each successful project to specific Reddit pain points and rank them according to the pain point severity/frequency ranking from Reddit analysis.

            Analysis criteria for each project:
            
            1. Business Model Analysis:
               - Revenue model (subscription, one-time, freemium)
               - Pricing strategy and tiers
               - Customer acquisition methods
               - Churn rate and retention strategies
               - Growth trajectory and milestones
               - Launch date and timeline to revenue milestones
            
            2. Product Analysis:
               - Core features and functionality
               - Target audience and use cases
               - User interface and experience
               - Integration capabilities
               - Mobile vs desktop focus
            
            3. Market Analysis:
               - Market size and opportunity
               - Competitive landscape
               - Barriers to entry
               - Customer pain points addressed
               - Market validation methods
            
            4. Technical Analysis:
               - Technology stack used
               - Development complexity
               - Maintenance requirements
               - Scalability considerations
               - Security and compliance needs
            
            5. Success Factors:
               - Key differentiators
               - Marketing strategies that worked
               - Customer feedback and testimonials
               - Iteration and improvement process
               - Founder background and skills
            
            Deliverables:
            - Top 10 successful micro-SaaS projects RANKED BY REDDIT PAIN POINT SEVERITY/FREQUENCY:
              * For each project, specify which Reddit pain point it addresses (e.g., "Addresses Pain Point #1: AI Privacy Concerns")
              * Launch dates and timeline to success (prioritize 2023-2024 launches)
              * Current revenue status and growth trajectory
              * Founder background and team composition
              * Marketing strategies and customer acquisition methods
              * How they solve specific pain points from Reddit analysis
              * Connection to emerging market opportunities identified in Reddit analysis
            - Detailed analysis of each project including launch timeline
            - Common success patterns and strategies from recent launches
            - Market opportunities and gaps identified from recent projects
            - Implementation recommendations based on recent success stories
            - Clear mapping between Reddit pain points and successful project solutions
            """,  # noqa
            agent=self.agent,
            expected_output="""
            Successful Micro-SaaS Research Report:
            1. Top 10 successful projects RANKED BY REDDIT PAIN POINT SEVERITY/FREQUENCY:
               - For each project, specify which Reddit pain point it addresses (e.g., "Addresses Pain Point #1: AI Privacy Concerns")
               - Launch dates and timeline to success (prioritize 2023-2024 launches)
               - Current revenue status and growth trajectory
               - Founder background and team composition
               - Marketing strategies and customer acquisition methods
               - How they solve specific pain points from Reddit analysis
               - Connection to emerging market opportunities identified in Reddit analysis
            2. Detailed analysis of each project including launch timeline
            3. Common success patterns and strategies from recent launches
            4. Market opportunities and gaps identified from recent projects
            5. Implementation recommendations based on recent success stories
            6. Revenue and growth insights from recent successful projects
            7. Clear mapping between Reddit pain points and successful project solutions
            """,  # noqa
        )

    def research_successful_projects(self, reddit_trend_analysis: str) -> dict[str, Any]:
        """Execute successful project research."""
        task = self.create_successful_project_research_task(reddit_trend_analysis)

        # Execute agent
        result = self.agent.execute_task(task)

        return {"successful_projects_research": result, "status": "completed"}
