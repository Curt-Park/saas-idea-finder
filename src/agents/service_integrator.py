"""
Service Integrator Agent

This agent integrates all analysis results for each service and creates
a comprehensive service-by-service analysis report.
"""

from crewai import Agent, Task
from langchain_openai import ChatOpenAI


class ServiceIntegratorAgent:
    """Agent that integrates all analysis results for each service."""

    def __init__(self, openai_api_key: str, model: str = "gpt-4o-mini", temperature: float = 0.3):
        """Initialize the Service Integrator Agent."""
        self.openai_api_key = openai_api_key
        self.model = model
        self.temperature = temperature
        
        self.llm = ChatOpenAI(
            model=model,
            temperature=temperature,
            api_key=openai_api_key
        )
        
        self.agent = Agent(
            role="Service Integration Specialist",
            goal="Integrate all analysis results for each service into comprehensive service profiles",
            backstory="""You are an expert at synthesizing complex business analysis data. 
            Your specialty is taking multiple analysis perspectives (competitive, MVP, problem, revenue) 
            and creating unified, actionable service profiles that provide complete insights for each service.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def create_service_integration_task(self, analysis_data: dict) -> Task:
        """Create a task for integrating all analysis results by service."""
        return Task(
            description=f"""
            Integrate all analysis results for each service into comprehensive service profiles:
            
            Analysis data: {analysis_data}
            
            For each service identified in the analysis, create a comprehensive profile that includes:
            
            **For Each Service:**
            1. **Service Name**: [Service Name]
            2. **Overview**: [Service description and what it does]
            3. **Addresses Pain Point**: [Which Reddit pain point this service addresses]
            4. **Launch Date**: [When the service was launched]
            5. **Current Revenue**: [Revenue information if available]
            6. **Founder Background**: [Information about the founder/team]
            7. **Marketing Strategies**: [How they market their service]
            8. **Pain Point Solution**: [How they solve the specific pain point]
            9. **Strengths**: [Key competitive advantages from competitive analysis]
            10. **Weaknesses**: [Areas for improvement from competitive analysis]
            11. **Market Opportunities and Gaps**: [Opportunities identified in competitive analysis]
            12. **MVP Feature Suggestions**: [Suggested improvements from MVP analysis]
            13. **Key Implementation Challenges**: [Challenges identified in problem analysis]
            14. **Revenue Analysis**: [Revenue potential and financial viability]
            
            Focus on:
            - Creating complete service profiles that tell the full story
            - Connecting all analysis perspectives for each service
            - Providing actionable insights for each service
            - Making the information easily scannable and comprehensive
            
            Deliverables:
            - Comprehensive service profiles with all analysis integrated
            - Clear connection between pain points and solutions
            - Actionable insights for each service
            """,
            agent=self.agent,
            expected_output="""
            Integrated Service Analysis Report:
            For each service:
            1. **Service Name**: Clear service identification
            2. **Overview**: What the service does and its purpose
            3. **Addresses Pain Point**: Which Reddit pain point it addresses
            4. **Launch Date**: When it was launched
            5. **Current Revenue**: Revenue information
            6. **Founder Background**: Founder/team information
            7. **Marketing Strategies**: How they market
            8. **Pain Point Solution**: How they solve the pain point
            9. **Strengths**: Key competitive advantages
            10. **Weaknesses**: Areas for improvement
            11. **Market Opportunities and Gaps**: Opportunities identified
            12. **MVP Feature Suggestions**: Suggested improvements
            13. **Key Implementation Challenges**: Implementation challenges
            14. **Revenue Analysis**: Revenue potential and viability
            """
        )

    def integrate_services(self, analysis_data: dict) -> dict:
        """Integrate all analysis results for each service."""
        try:
            task = self.create_service_integration_task(analysis_data)
            result = self.agent.execute_task(task)
            
            return {
                "service_integration": result.raw,
                "status": "success"
            }
        except Exception as e:
            return {
                "service_integration": f"Error in service integration: {str(e)}",
                "status": "error"
            }
