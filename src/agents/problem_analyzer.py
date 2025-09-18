"""Problem Analyzer Agent.

Analyzes key problems that need to be solved for implementing suggested MVP features.
"""

from typing import Any

from crewai import Agent, Task
from langchain_openai import ChatOpenAI


class ProblemAnalyzerAgent:
    def __init__(self, openai_api_key: str, model: str = "gpt-4o-mini", temperature: float = 0.3):
        self.llm = ChatOpenAI(model=model, api_key=openai_api_key, temperature=temperature)

        self.agent = Agent(
            role="Problem Analysis Expert",
            goal="Analyze key problems that need to be solved for implementing suggested MVP features",
            backstory="""You are an expert in problem analysis and solution design. 
            Your specialty is identifying and analyzing the core problems that need to be solved 
            to successfully implement new features and services.""",
            tools=[],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    def create_problem_analysis_task(self, mvp_data: dict[str, Any]) -> Task:
        """Create problem analysis task."""
        return Task(
            description=f"""
            Analyze key problems that need to be solved for implementing suggested MVP features:
            
            MVP suggestion data: {mvp_data}
            
            For each suggested MVP feature, analyze the key problems that need to be solved:
            
            1. Technical Problems:
               - Architecture and scalability challenges
               - Integration complexity with existing systems
               - Data management and storage requirements
               - Security and compliance considerations
               - Performance optimization needs
               - Cross-platform compatibility issues
            
            2. User Experience Problems:
               - User onboarding and adoption challenges
               - Interface design and usability issues
               - Learning curve and training requirements
               - Accessibility and inclusivity concerns
               - Mobile vs desktop experience gaps
               - Multi-language and localization needs
            
            3. Business Problems:
               - Market validation and customer acquisition
               - Pricing strategy and monetization
               - Competitive differentiation challenges
               - Customer support and service requirements
               - Legal and regulatory compliance
               - Intellectual property and patent considerations
            
            4. Operational Problems:
               - Development team and skill requirements
               - Project management and timeline challenges
               - Quality assurance and testing needs
               - Deployment and maintenance requirements
               - Customer feedback and iteration process
               - Scaling and growth management
            
            5. Market Problems:
               - Target audience identification and reach
               - Marketing and promotion strategies
               - Customer education and awareness
               - Competitive positioning and messaging
               - Partnership and integration opportunities
               - Market timing and adoption barriers
            
            Problem Prioritization:
            
            Critical Problems (Must Solve):
            - Core functionality that prevents launch
            - Security and compliance requirements
            - Basic user experience and usability
            - Essential business model validation
            - Legal and regulatory compliance
            
            Important Problems (Should Solve):
            - Performance and scalability issues
            - Advanced user experience features
            - Competitive differentiation
            - Customer acquisition strategies
            - Operational efficiency
            
            Nice to Have Problems (Could Solve):
            - Advanced automation features
            - Premium functionality
            - Advanced analytics and reporting
            - White-label and customization
            - Enterprise features
            
            For each problem identified:
            - Problem description and impact
            - Potential solutions and approaches
            - Implementation complexity (1-10 scale)
            - Required resources and skills
            - Timeline and dependencies
            - Risk assessment and mitigation
            
            Deliverables:
            - Comprehensive problem analysis for each MVP
            - Prioritized problem list with solutions
            - Implementation complexity and resource requirements
            - Risk assessment and mitigation strategies
            - Success criteria and validation methods
            """,
            agent=self.agent,
            expected_output="""
            Problem Analysis Report:
            1. Technical problems and solutions
            2. User experience challenges
            3. Business and operational problems
            4. Market and competitive challenges
            5. Prioritized problem list with solutions
            6. Implementation complexity and resource requirements
            7. Risk assessment and mitigation strategies
            """,
        )

    def analyze_problems(self, mvp_data: dict[str, Any]) -> dict[str, Any]:
        """Execute problem analysis."""
        task = self.create_problem_analysis_task(mvp_data)

        # Execute agent
        result = self.agent.execute_task(task)

        return {"mvp_data": mvp_data, "problem_analysis": result, "status": "completed"}
