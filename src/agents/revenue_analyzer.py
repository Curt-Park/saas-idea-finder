"""Revenue Analyzer Agent.

Analyzes expected revenue and profitability for suggested services.
"""

from typing import Any

from crewai import Agent, Task
from langchain_openai import ChatOpenAI


class RevenueAnalyzerAgent:
    def __init__(self, openai_api_key: str, model: str = "gpt-4o-mini", temperature: float = 0.3):
        self.llm = ChatOpenAI(model=model, api_key=openai_api_key, temperature=temperature)

        self.agent = Agent(
            role="Revenue Analysis Expert",
            goal="Analyze expected revenue and profitability for suggested services",
            backstory="""You are an expert in revenue analysis and financial modeling for SaaS businesses. 
            Your specialty is analyzing market potential, pricing strategies, and revenue projections 
            for micro-SaaS businesses.""",
            tools=[],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    def create_revenue_analysis_task(self, problem_data: dict[str, Any]) -> Task:
        """Create revenue analysis task."""
        return Task(
            description=f"""
            Analyze expected revenue and profitability for suggested services:
            
            Problem analysis data: {problem_data}
            
            For each suggested service, provide COMPACT revenue analysis:
            
            **For Each Service:**
            1. **Revenue Potential** (key metrics):
               - Target market size and opportunity
               - Pricing strategy and model
               - Revenue projections (Year 1-3)
            
            2. **Financial Viability** (brief assessment):
               - Break-even timeline
               - Key success factors
               - Main risks and mitigation
            
            Focus on:
            - Realistic revenue projections for solopreneurs
            - Simple pricing models
            - Clear break-even analysis
            """,
            agent=self.agent,
            expected_output="""
            Revenue Analysis Report:
            For each service:
            1. **Revenue Potential**: Market size, pricing strategy, and revenue projections
            2. **Financial Viability**: Break-even timeline, success factors, and risks
            """,
        )

    def analyze_revenue(self, problem_data: dict[str, Any]) -> dict[str, Any]:
        """Execute revenue analysis."""
        task = self.create_revenue_analysis_task(problem_data)

        # Execute agent
        result = self.agent.execute_task(task)

        return {"problem_data": problem_data, "revenue_analysis": result, "status": "completed"}
