"""Competitor Analyzer Agent.

Checks for similar existing services and summarizes their overview, pros/cons, and revenue status if found.
"""

from typing import Any

from crewai import Agent, Task
from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain_openai import ChatOpenAI


class CompetitorAnalyzerAgent:
    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key, temperature=0.3)

        # Tool setup
        self.search_tool = SerperDevTool()
        self.website_tool = WebsiteSearchTool()

        self.agent = Agent(
            role="Competitor Analysis Expert",
            goal="Analyze market status, pros/cons, and revenue models of similar services to derive competitive advantages",
            backstory="""You are an expert in competitive analysis and market research. 
            Your specialty is analyzing success/failure factors of existing services 
            and developing differentiation strategies.""",
            tools=[self.search_tool, self.website_tool],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    def create_competitor_analysis_task(self, proposal_data: dict[str, Any]) -> Task:
        """Create competitor analysis task."""
        return Task(
            description=f"""
            Perform competitor analysis for the proposed business idea:
            
            Proposal data: {proposal_data}
            
            Analysis items:
            
            1. Competitor Identification:
               - Direct competitors (providing same solution)
               - Indirect competitors (solving similar problems)
               - Potential competitors (large company entry possibilities)
               - Domestic/international competitor classification
            
            2. Detailed Analysis of Each Competitor:
               - Company overview (founding year, size, funding status)
               - Service features and functionality
               - Target customer segments
               - Pricing policy
               - Revenue model
               - Marketing strategy
            
            3. Competitor Pros/Cons Analysis:
               - Strengths (differentiation factors, technical capabilities, brand power)
               - Weaknesses (user complaints, feature gaps, pricing policy)
               - Market share and growth rate
               - User reviews and rating analysis
            
            4. Profitability Analysis:
               - Revenue status of each competitor (based on public information)
               - Funding history and valuation
               - Customer size and growth rate
               - Marketing cost to revenue ratio
            
            5. Market Positioning:
               - Market position mapping by competitor
               - Market segmentation by price range
               - Differentiation points by feature
               - Competitive landscape by target customer
            
            6. Opportunity Analysis:
               - Needs missed by competitors
               - Market gap analysis
               - Entry barriers and bypass methods
               - Differentiation strategy suggestions
            
            7. Threat Factors:
               - Large company market entry possibilities
               - Technical entry barriers
               - Capital gap
               - Regulatory and legal risks
            
            Deliverables:
            - Competitor status summary
            - Competitive advantage analysis
            - Differentiation strategy suggestions
            - Market entry strategy
            """,
            agent=self.agent,
            expected_output="""
            Competitor Analysis Report:
            1. Competitor status summary
            2. Detailed analysis by competitor
            3. Pros/cons comparison analysis
            4. Profitability analysis
            5. Market positioning
            6. Opportunity and threat analysis
            7. Differentiation strategy suggestions
            """,
        )

    def analyze_competitors(self, proposal_data: dict[str, Any]) -> dict[str, Any]:
        """Execute competitor analysis."""
        task = self.create_competitor_analysis_task(proposal_data)

        # Execute agent
        result = self.agent.execute_task(task)

        return {"proposal_data": proposal_data, "competitor_analysis": result, "status": "completed"}
