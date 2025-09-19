"""MVP Feature Suggester Agent.

Suggests MVP features for improving existing successful services.
"""

from typing import Any

from crewai import Agent, Task
from langchain_openai import ChatOpenAI


class MvpFeatureSuggesterAgent:
    def __init__(self, openai_api_key: str, model: str = "gpt-4o-mini", temperature: float = 0.3):
        self.llm = ChatOpenAI(model=model, api_key=openai_api_key, temperature=temperature)

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
            
            For each service analyzed, provide COMPACT MVP feature suggestions:
            
            **For Each Service:**
            1. **Core Feature Enhancements** (2-3 key features):
               - Essential features that address main pain points
               - User experience improvements
               - Performance optimizations
            
            2. **Enhancement Rationale** (brief justification):
               - Why these features are needed
               - How they address competitive weaknesses
               - Market opportunity they create
            
            Focus on:
            - Features that directly address competitive weaknesses
            - Simple, implementable improvements
            - Clear market differentiation
            - Solopreneur-friendly development scope
            """,
            agent=self.agent,
            expected_output="""
            MVP Feature Suggestion Report:
            For each service:
            1. **Core Feature Enhancements**: 2-3 key features with brief descriptions
            2. **Enhancement Rationale**: Why these features are needed and how they address competitive weaknesses
            """,
        )

    def suggest_mvp_features(self, competitive_data: dict[str, Any]) -> dict[str, Any]:
        """Execute MVP feature suggestion."""
        task = self.create_mvp_suggestion_task(competitive_data)

        # Execute agent
        result = self.agent.execute_task(task)

        return {"competitive_data": competitive_data, "mvp_suggestions": result, "status": "completed"}
