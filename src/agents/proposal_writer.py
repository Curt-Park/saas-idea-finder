"""Proposal Writer Agent.

Writes business proposals based on analysis results from steps 1-3
"""

from typing import Any

from crewai import Agent, Task
from langchain_openai import ChatOpenAI


class ProposalWriterAgent:
    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key, temperature=0.3)

        self.agent = Agent(
            role="Business Proposal Writing Expert",
            goal="Write systematic and executable proposals based on analysis results",
            backstory="""You are an expert in startup planning and business model design. 
            Your specialty is writing executable business proposals 
            based on market analysis and technical analysis results.""",
            tools=[],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    def create_proposal_writing_task(self, analysis_data: dict[str, Any]) -> Task:
        """Create proposal writing task."""
        return Task(
            description=f"""
            Write a comprehensive business proposal based on the following analysis data:
            
            Analysis data: {analysis_data}
            
            Proposal structure:
            
            1. Business Overview:
               - Business idea summary
               - Problems to solve
               - Target customer segments
               - Core value proposition
            
            2. Market Analysis:
               - Market size and growth rate
               - Target market characteristics
               - Market opportunity analysis
               - Competitive environment analysis
            
            3. Product/Service Plan:
               - Core features and characteristics
               - User experience design
               - Technical implementation approach
               - Development roadmap
            
            4. Business Model:
               - Revenue model
               - Pricing strategy
               - Customer acquisition strategy
               - Partnership strategy
            
            5. Marketing Strategy:
               - Target customer segmentation
               - Marketing channels
               - Branding strategy
               - Customer retention strategy
            
            6. Operations Plan:
               - Organizational structure
               - Key personnel requirements
               - Operational processes
               - Quality management measures
            
            7. Financial Plan:
               - Initial investment requirements
               - Revenue projections
               - Break-even analysis
               - Funding plan
            
            8. Risk Analysis:
               - Market risks
               - Technical risks
               - Operational risks
               - Mitigation strategies
            
            9. Execution Plan:
               - Step-by-step execution roadmap
               - Milestones and KPIs
               - Success metrics
               - Next step action items
            
            Deliverables:
            - Executable business proposal
            - Presentation materials for investors/partners
            - Technical specifications for development team
            """,
            agent=self.agent,
            expected_output="""
            Business Proposal:
            1. Business overview
            2. Market analysis
            3. Product/service plan
            4. Business model
            5. Marketing strategy
            6. Operations plan
            7. Financial plan
            8. Risk analysis
            9. Execution plan
            """,
        )

    def write_proposal(self, analysis_data: dict[str, Any]) -> dict[str, Any]:
        """Execute proposal writing."""
        task = self.create_proposal_writing_task(analysis_data)

        # Execute agent
        result = self.agent.execute_task(task)

        return {"analysis_data": analysis_data, "proposal": result, "status": "completed"}
