"""MVP Feature Suggester Agent.

Suggests MVP features for improving existing successful services.
"""

from typing import Any

from crewai import Agent, Task
from langchain_openai import ChatOpenAI


class MvpFeatureSuggesterAgent:
    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key, temperature=0.7)

        self.agent = Agent(
            role="MVP Feature Suggestion Expert",
            goal="Suggest MVP features for improving existing successful services",
            backstory="""You are an expert in product development and MVP design. 
            Your specialty is identifying key features that can differentiate a new service 
            from existing competitors while maintaining simplicity and focus.""",
            tools=[],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    def create_mvp_suggestion_task(self, competitive_data: dict[str, Any]) -> Task:
        """Create MVP feature suggestion task."""
        return Task(
            description=f"""
            Suggest MVP features for improving existing successful services:
            
            Competitive analysis data: {competitive_data}
            
            For each service analyzed, suggest MVP features that could create a competitive advantage:
            
            1. Core Feature Enhancements:
               - Essential features that address main pain points
               - User experience improvements
               - Performance optimizations
               - Integration capabilities
               - Mobile responsiveness
            
            2. Differentiation Features:
               - Unique value propositions
               - Innovative functionality
               - Better user interface design
               - Advanced automation features
               - AI-powered capabilities
            
            3. Market-Specific Features:
               - Industry-specific functionality
               - Localization and regional features
               - Compliance and security features
               - Integration with popular tools
               - Customization options
            
            4. Technical Improvements:
               - Modern technology stack
               - Better API design
               - Real-time capabilities
               - Scalability improvements
               - Security enhancements
            
            5. Business Model Innovations:
               - Flexible pricing options
               - Freemium features
               - White-label solutions
               - Partnership opportunities
               - Revenue sharing models
            
            MVP Feature Prioritization:
            
            High Priority (Must Have):
            - Core functionality that solves the main problem
            - Essential user experience features
            - Basic integration capabilities
            - Security and reliability features
            - Simple pricing model
            
            Medium Priority (Should Have):
            - Advanced features that differentiate
            - Mobile app or responsive design
            - Analytics and reporting
            - Customer support features
            - Marketing and onboarding tools
            
            Low Priority (Nice to Have):
            - Advanced automation
            - AI-powered features
            - Advanced integrations
            - White-label options
            - Enterprise features
            
            For each suggested MVP:
            - Feature description and benefits
            - Implementation complexity (1-10 scale)
            - Development time estimate
            - Required technical skills
            - Market validation approach
            - Revenue potential assessment
            
            Deliverables:
            - MVP feature suggestions for each service
            - Prioritized feature roadmap
            - Implementation complexity analysis
            - Market validation strategies
            - Revenue potential estimates
            """,
            agent=self.agent,
            expected_output="""
            MVP Feature Suggestion Report:
            1. Core feature enhancements for each service
            2. Differentiation features and unique value props
            3. Market-specific feature recommendations
            4. Technical improvement suggestions
            5. Business model innovations
            6. Prioritized MVP feature roadmap
            7. Implementation complexity and timeline estimates
            """,
        )

    def suggest_mvp_features(self, competitive_data: dict[str, Any]) -> dict[str, Any]:
        """Execute MVP feature suggestion."""
        task = self.create_mvp_suggestion_task(competitive_data)

        # Execute agent
        result = self.agent.execute_task(task)

        return {"competitive_data": competitive_data, "mvp_suggestions": result, "status": "completed"}
