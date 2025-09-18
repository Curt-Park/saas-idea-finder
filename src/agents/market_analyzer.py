"""Market Analyzer Agent.

Performs market analysis based on collected information.
Are success signals clear? Is it a topic that can grow naturally with low marketing costs?
"""

from typing import Any

from crewai import Agent, Task
from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain_openai import ChatOpenAI


class MarketAnalyzerAgent:
    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key, temperature=0.3)

        # Tool setup
        self.search_tool = SerperDevTool()
        self.website_tool = WebsiteSearchTool()

        self.agent = Agent(
            role="Market Analysis Expert",
            goal="Analyze market opportunities and growth potential based on collected painpoints",
            backstory="""You are an expert in market analysis and business strategy development. 
            Your specialty is evaluating market opportunities based on consumer needs, 
            and analyzing marketing efficiency and natural growth potential.""",
            tools=[self.search_tool, self.website_tool],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    def create_market_analysis_task(self, painpoint_data: dict[str, Any]) -> Task:
        """Create market analysis task."""
        return Task(
            description=f"""
            Perform market analysis based on collected painpoint data:
            
            Collected data: {painpoint_data}
            
            Analysis items:
            
            1. Market Size Analysis:
               - Target market size (TAM, SAM, SOM)
               - Market growth rate and trends
               - Regional market distribution
            
            2. Success Signal Analysis:
               - Limitations of existing solutions
               - User willingness to pay
               - Market entry barriers
               - Competitive advantages
            
            3. Marketing Efficiency Analysis:
               - Viral potential (network effects)
               - SEO-friendly keywords
               - Social media marketing potential
               - Influencer marketing possibilities
            
            4. Natural Growth Potential:
               - User referral potential
               - Community formation potential
               - Content marketing effectiveness
               - Word-of-mouth spread potential
            
            5. Profitability Analysis:
               - Expected Customer Acquisition Cost (CAC)
               - Expected Customer Lifetime Value (LTV)
               - Revenue model diversity
               - Price sensitivity
            
            Deliverables:
            - Market opportunity assessment (1-10 scale)
            - Success probability analysis
            - Marketing strategy suggestions
            - Profitability predictions
            """,
            agent=self.agent,
            expected_output="""
            Market Analysis Report:
            1. Market size and growth rate
            2. Success signal analysis
            3. Marketing efficiency assessment
            4. Natural growth potential
            5. Profitability predictions
            6. Comprehensive evaluation and recommendations
            """,
        )

    def analyze_market(self, painpoint_data: dict[str, Any]) -> dict[str, Any]:
        """Execute market analysis."""
        task = self.create_market_analysis_task(painpoint_data)

        # Execute agent
        result = self.agent.execute_task(task)

        return {"painpoint_data": painpoint_data, "market_analysis": result, "status": "completed"}
