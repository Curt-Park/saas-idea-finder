"""Competitive Landscape Analyzer Agent.

Analyzes existing services to identify competitive advantages and market gaps.
"""

from typing import Any

from crewai import Agent, Task
from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain_openai import ChatOpenAI


class CompetitiveLandscapeAnalyzerAgent:
    def __init__(self, openai_api_key: str, model: str = "gpt-4o-mini", temperature: float = 0.3):
        self.llm = ChatOpenAI(model=model, api_key=openai_api_key, temperature=temperature)

        # Tool setup
        self.search_tool = SerperDevTool()
        self.website_tool = WebsiteSearchTool()

        self.agent = Agent(
            role="Competitive Landscape Analysis Expert",
            goal="Analyze existing services to identify competitive advantages and market gaps",
            backstory="""You are an expert in competitive analysis and market research. 
            Your specialty is analyzing existing services to identify their strengths, 
            weaknesses, and opportunities for improvement or differentiation.""",
            tools=[self.search_tool, self.website_tool],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    def create_competitive_analysis_task(self, research_data: dict[str, Any]) -> Task:
        """Create competitive analysis task."""
        return Task(
            description=f"""
            Analyze the competitive landscape for the identified successful projects:
            
            Research data: {research_data}
            
            For each successful project identified, perform detailed competitive analysis:
            
            1. Service Overview Analysis:
               - Core functionality and features
               - Target market and user personas
               - Business model and pricing
               - Market positioning and messaging
               - Brand and design approach
            
            2. Strengths Analysis:
               - Unique value propositions
               - Key differentiators
               - User experience advantages
               - Technical capabilities
               - Market recognition and reputation
               - Customer loyalty factors
            
            3. Weaknesses Analysis:
               - Feature limitations or gaps
               - User interface issues
               - Performance or reliability problems
               - Pricing concerns
               - Customer support issues
               - Integration limitations
            
            4. Market Opportunity Assessment:
               - Underserved customer segments
               - Feature gaps in the market
               - Pricing opportunities
               - Geographic expansion potential
               - Vertical market opportunities
               - Integration possibilities
            
            5. Competitive Positioning:
               - Market share and growth trajectory
               - Customer acquisition strategies
               - Marketing and branding approach
               - Partnership and integration strategies
               - Innovation and development pace
               - Customer retention strategies
            
            6. Improvement Opportunities:
               - Feature enhancements needed
               - User experience improvements
               - Pricing model optimizations
               - Market expansion opportunities
               - Technology upgrades
               - Customer service improvements
            
            Focus on identifying:
            - Services with high revenue but significant user complaints
            - Markets with limited competition
            - Niche opportunities within broader markets
            - Underserved professional groups
            - Geographic or industry-specific gaps
            
            Deliverables:
            - Detailed competitive analysis for each service
            - Market gap identification
            - Improvement opportunity matrix
            - Competitive advantage recommendations
            - Market entry strategy suggestions
            """,
            agent=self.agent,
            expected_output="""
            Competitive Landscape Analysis Report:
            1. Service overview and positioning
            2. Strengths and competitive advantages
            3. Weaknesses and improvement areas
            4. Market opportunities and gaps
            5. Competitive positioning analysis
            6. Improvement opportunity matrix
            7. Market entry strategy recommendations
            """,
        )

    def analyze_competitive_landscape(self, research_data: dict[str, Any]) -> dict[str, Any]:
        """Execute competitive landscape analysis."""
        task = self.create_competitive_analysis_task(research_data)

        # Execute agent
        result = self.agent.execute_task(task)

        return {"research_data": research_data, "competitive_analysis": result, "status": "completed"}
