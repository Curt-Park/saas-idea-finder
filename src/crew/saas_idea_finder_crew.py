"""SaaS Idea Finder Crew.

Orchestrates all agents to perform comprehensive SaaS idea analysis.
"""

import os
from typing import Any

from crewai import Crew, Process
from dotenv import load_dotenv

from ..agents.competitive_landscape_analyzer import CompetitiveLandscapeAnalyzerAgent
from ..agents.mvp_feature_suggester import MvpFeatureSuggesterAgent
from ..agents.problem_analyzer import ProblemAnalyzerAgent
from ..agents.reddit_trend_analyzer import RedditTrendAnalyzerAgent
from ..agents.revenue_analyzer import RevenueAnalyzerAgent
from ..agents.successful_project_researcher import SuccessfulProjectResearcherAgent


class SaasIdeaFinderCrew:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Check OpenAI API key
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set.")

        # Initialize agents for successful project analysis
        self.reddit_trend_analyzer = RedditTrendAnalyzerAgent(self.openai_api_key)
        self.successful_project_researcher = SuccessfulProjectResearcherAgent(self.openai_api_key)
        self.competitive_landscape_analyzer = CompetitiveLandscapeAnalyzerAgent(self.openai_api_key)
        self.mvp_feature_suggester = MvpFeatureSuggesterAgent(self.openai_api_key)
        self.problem_analyzer = ProblemAnalyzerAgent(self.openai_api_key)
        self.revenue_analyzer = RevenueAnalyzerAgent(self.openai_api_key)

        # Crew setup for successful project analysis
        self.crew = Crew(
            agents=[
                self.reddit_trend_analyzer.agent,
                self.successful_project_researcher.agent,
                self.competitive_landscape_analyzer.agent,
                self.mvp_feature_suggester.agent,
                self.problem_analyzer.agent,
                self.revenue_analyzer.agent,
            ],
            tasks=[],  # Created dynamically
            process=Process.sequential,
            verbose=True,
        )

    def analyze_successful_projects(self) -> dict[str, Any]:
        """Analyze successful projects and suggest improvements.

        Returns:
            Comprehensive analysis of successful projects with improvement suggestions
        """
        print("🔍 Starting successful project analysis...")

        # Step 1: Reddit trend analysis
        print("📱 Step 1: Analyzing Reddit trends and pain points...")
        reddit_result = self.reddit_trend_analyzer.analyze_reddit_trends()

        # Step 2: Research successful projects (using Reddit trend analysis summary)
        print("💰 Step 2: Researching successful micro-SaaS projects based on Reddit trends...")
        successful_projects = self.successful_project_researcher.research_successful_projects(
            reddit_result["reddit_trend_analysis"]
        )

        # Step 3: Competitive landscape analysis
        print("🏢 Step 3: Analyzing competitive landscape...")
        competitive_result = self.competitive_landscape_analyzer.analyze_competitive_landscape(successful_projects)

        # Step 4: MVP feature suggestions
        print("💡 Step 4: Suggesting MVP features for improvements...")
        mvp_result = self.mvp_feature_suggester.suggest_mvp_features(competitive_result)

        # Step 5: Problem analysis
        print("🔧 Step 5: Analyzing implementation problems...")
        problem_result = self.problem_analyzer.analyze_problems(mvp_result)

        # Step 6: Revenue analysis
        print("📊 Step 6: Analyzing revenue potential...")
        revenue_result = self.revenue_analyzer.analyze_revenue(problem_result)

        # Return comprehensive results
        final_result = {
            "reddit_trends": reddit_result,
            "successful_projects": successful_projects,
            "competitive_analysis": competitive_result,
            "mvp_suggestions": mvp_result,
            "problem_analysis": problem_result,
            "revenue_analysis": revenue_result,
            "status": "completed",
        }

        print("✅ Successful project analysis completed!")
        return final_result

    def generate_summary_report(self, analysis_result: dict[str, Any]) -> str:
        """Generate summary report based on analysis results.

        Args:
            analysis_result: Analysis results

        Returns:
            Summary report
        """
        report = f"""
# Successful Project Analysis Report

## 📋 Analysis Overview
- **Analysis Type**: Successful Project Analysis
- **Focus**: Analyzing successful micro-SaaS projects and suggesting improvements
- **Analysis Date**: {analysis_result.get("status", "Completed")}

## 🎯 Key Findings

### 1. Reddit Trend Analysis
{analysis_result.get("reddit_trends", {}).get("reddit_trend_analysis", "Not available")}

### 2. Successful Projects Research
{analysis_result.get("successful_projects", {}).get("successful_projects_research", "Not available")}

### 3. Competitive Landscape Analysis
{analysis_result.get("competitive_analysis", {}).get("competitive_analysis", "Not available")}

### 4. MVP Feature Suggestions
{analysis_result.get("mvp_suggestions", {}).get("mvp_suggestions", "Not available")}

### 5. Problem Analysis
{analysis_result.get("problem_analysis", {}).get("problem_analysis", "Not available")}

### 6. Revenue Analysis
{analysis_result.get("revenue_analysis", {}).get("revenue_analysis", "Not available")}

## 🚀 Next Steps Recommendations
1. Validate the suggested improvements with potential customers
2. Create detailed technical specifications for MVP features
3. Develop implementation roadmap based on problem analysis
4. Conduct market validation using revenue projections
5. Start prototype development for highest-potential ideas
6. Consider competitive advantages and differentiation strategies

## 💡 Key Insights
- **Reddit Pain Points**: {analysis_result.get("reddit_trends", {}).get("reddit_trend_analysis", "Not available")}
- **Successful Project Patterns**: {analysis_result.get("successful_projects", {}).get("successful_projects_research", "Not available")}
- **Revenue Opportunities**: {analysis_result.get("revenue_analysis", {}).get("revenue_analysis", "Not available")}

---
*This report is generated by AI-based analysis. Additional verification is required for actual business decisions.*
        """  # noqa

        return report
