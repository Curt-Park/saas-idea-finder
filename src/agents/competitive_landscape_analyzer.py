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
            
            IMPORTANT: 
            1. If no successful projects were found in the research data, analyze the Reddit pain points and suggest potential service ideas instead
            2. If successful projects were found, analyze their competitive landscape
            3. If research data is empty or contains errors, focus on analyzing the market gaps identified in Reddit trends
            
            ANALYSIS APPROACH:
            A. If successful projects were found: Analyze their competitive landscape
            B. If no successful projects found: Analyze Reddit pain points and suggest service ideas
            
            For each successful project identified, provide a COMPACT analysis with these sections:
            
            **For Each Service:**
            1. **Strengths** (2-3 key points):
               - Unique value propositions
               - Key competitive advantages
               - Market recognition factors
            
            2. **Weaknesses** (2-3 key points):
               - Feature limitations or gaps
               - User experience issues
               - Pricing or support concerns
            
            3. **Market Opportunities and Gaps** (2-3 key points):
               - Underserved customer segments
               - Feature gaps in the market
               - Pricing or geographic opportunities
            
            Focus on identifying:
            - Services with high revenue but significant user complaints
            - Markets with limited competition
            - Niche opportunities within broader markets
            - Underserved professional groups
            - Geographic or industry-specific gaps
            
            Deliverables:
            - Detailed competitive analysis for each service (if found)
            - Market gap identification
            - Improvement opportunity matrix
            - Competitive advantage recommendations
            - Market entry strategy suggestions
            - Service idea suggestions (if no existing services found)
            
            B. If no successful projects found, provide SERVICE IDEA SUGGESTIONS:
            
            1. Reddit Pain Point Analysis:
               - Identify the most critical pain points from Reddit analysis
               - Assess market opportunity for each pain point
               - Evaluate technical feasibility for solopreneur implementation
            
            2. Service Idea Suggestions:
               - For each major pain point, suggest 2-3 potential service ideas
               - Include target audience, core features, and business model
               - Explain how each idea addresses the specific Reddit pain point
               - Note: These are SUGGESTED IDEAS, not existing services
            
            3. Market Gap Analysis:
               - Explain why no existing solutions were found
               - Identify barriers to entry for these markets
               - Suggest validation approaches for proposed ideas
            """,  # noqa
            agent=self.agent,
            expected_output="""
            Competitive Landscape Analysis Report:
            For each service (if found):
            1. **Service Name**: Brief overview
            2. **Strengths**: 2-3 key competitive advantages
            3. **Weaknesses**: 2-3 key limitations or gaps
            4. **Market Opportunities and Gaps**: 2-3 key opportunities
            
            If no services found:
            1. **Reddit Pain Point Analysis**: Key pain points identified
            2. **Service Idea Suggestions**: 2-3 potential service ideas with brief descriptions
            """,
        )

    def analyze_competitive_landscape(self, research_data: dict[str, Any]) -> dict[str, Any]:
        """Execute competitive landscape analysis."""
        task = self.create_competitive_analysis_task(research_data)

        # Execute agent
        result = self.agent.execute_task(task)

        return {"research_data": research_data, "competitive_analysis": result, "status": "completed"}
