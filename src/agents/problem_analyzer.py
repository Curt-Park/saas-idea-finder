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
            
            For each suggested MVP feature, provide COMPACT problem analysis:
            
            **For Each Service:**
            1. **Key Implementation Challenges** (2-3 main problems):
               - Technical challenges
               - User experience issues
               - Business/market challenges
            
            2. **Solution Approaches** (brief solutions):
               - How to address each challenge
               - Required resources/skills
               - Implementation complexity
            
            Focus on:
            - Most critical problems that could prevent launch
            - Solopreneur-friendly solutions
            - Clear implementation steps
            """,
            agent=self.agent,
            expected_output="""
            Problem Analysis Report:
            For each service:
            1. **Key Implementation Challenges**: 2-3 main problems with brief descriptions
            2. **Solution Approaches**: How to address each challenge with required resources
            """,
        )

    def analyze_problems(self, mvp_data: dict[str, Any]) -> dict[str, Any]:
        """Execute problem analysis."""
        task = self.create_problem_analysis_task(mvp_data)

        # Execute agent
        result = self.agent.execute_task(task)

        return {"mvp_data": mvp_data, "problem_analysis": result, "status": "completed"}
