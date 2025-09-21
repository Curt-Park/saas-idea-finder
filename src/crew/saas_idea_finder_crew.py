"""SaaS Idea Finder Crew.

Orchestrates all agents to perform comprehensive SaaS idea analysis.
"""

import os
import time
from typing import Any

from crewai import Crew, Process
from dotenv import load_dotenv

from ..agents.competitive_landscape_analyzer import CompetitiveLandscapeAnalyzerAgent
from ..agents.mvp_feature_suggester import MvpFeatureSuggesterAgent
from ..agents.problem_analyzer import ProblemAnalyzerAgent
from ..agents.reddit_trend_analyzer import RedditTrendAnalyzerAgent
from ..agents.revenue_analyzer import RevenueAnalyzerAgent
from ..agents.service_integrator import ServiceIntegratorAgent
from ..agents.successful_project_researcher import SuccessfulProjectResearcherAgent


class SaasIdeaFinderCrew:
    def __init__(self, model: str = "gpt-4o-mini", temperature: float = 0.3):
        # Load environment variables
        load_dotenv()

        # Check OpenAI API key
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set.")

        # Store model and temperature settings
        self.model = model
        self.temperature = temperature

        # Initialize agents for successful project analysis
        self.reddit_trend_analyzer = RedditTrendAnalyzerAgent(self.openai_api_key, model, temperature)
        self.successful_project_researcher = SuccessfulProjectResearcherAgent(self.openai_api_key, model, temperature)
        self.competitive_landscape_analyzer = CompetitiveLandscapeAnalyzerAgent(self.openai_api_key, model, temperature)
        self.mvp_feature_suggester = MvpFeatureSuggesterAgent(self.openai_api_key, model, temperature)
        self.problem_analyzer = ProblemAnalyzerAgent(self.openai_api_key, model, temperature)
        self.revenue_analyzer = RevenueAnalyzerAgent(self.openai_api_key, model, temperature)
        self.service_integrator = ServiceIntegratorAgent(self.openai_api_key, model, temperature)

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

        # Initialize timing tracking
        step_times = {}
        total_start_time = time.time()

        # Step 1: Reddit trend analysis
        print("📱 Step 1: Analyzing Reddit trends and pain points...")
        step_start = time.time()
        reddit_result = self.reddit_trend_analyzer.analyze_reddit_trends()
        step_times["reddit_analysis"] = time.time() - step_start
        print(f"⏱️  Reddit analysis completed in {step_times['reddit_analysis']:.1f} seconds")

        # Step 2: Research successful projects (using Reddit trend analysis summary)
        print("💰 Step 2: Researching successful micro-SaaS projects based on Reddit trends...")
        step_start = time.time()
        successful_projects = self.successful_project_researcher.research_successful_projects(
            reddit_result["reddit_trend_analysis"]
        )
        step_times["successful_projects_research"] = time.time() - step_start
        print(f"⏱️  Successful projects research completed in {step_times['successful_projects_research']:.1f} seconds")

        # Step 3: Competitive landscape analysis
        print("🏢 Step 3: Analyzing competitive landscape...")
        step_start = time.time()
        competitive_result = self.competitive_landscape_analyzer.analyze_competitive_landscape(successful_projects)
        step_times["competitive_analysis"] = time.time() - step_start
        print(f"⏱️  Competitive analysis completed in {step_times['competitive_analysis']:.1f} seconds")

        # Step 4: MVP feature suggestions
        print("💡 Step 4: Suggesting MVP features for improvements...")
        step_start = time.time()
        mvp_result = self.mvp_feature_suggester.suggest_mvp_features(competitive_result)
        step_times["mvp_suggestions"] = time.time() - step_start
        print(f"⏱️  MVP suggestions completed in {step_times['mvp_suggestions']:.1f} seconds")

        # Step 5: Problem analysis
        print("🔧 Step 5: Analyzing implementation problems...")
        step_start = time.time()
        problem_result = self.problem_analyzer.analyze_problems(mvp_result)
        step_times["problem_analysis"] = time.time() - step_start
        print(f"⏱️  Problem analysis completed in {step_times['problem_analysis']:.1f} seconds")

        # Step 6: Revenue analysis
        print("📊 Step 6: Analyzing revenue potential...")
        step_start = time.time()
        revenue_result = self.revenue_analyzer.analyze_revenue(problem_result)
        step_times["revenue_analysis"] = time.time() - step_start
        print(f"⏱️  Revenue analysis completed in {step_times['revenue_analysis']:.1f} seconds")

        # Step 7: Service integration
        print("🔗 Step 7: Integrating all analysis results by service...")
        step_start = time.time()
        integration_data = {
            "reddit_trends": reddit_result,
            "successful_projects": successful_projects,
            "competitive_analysis": competitive_result,
            "mvp_suggestions": mvp_result,
            "problem_analysis": problem_result,
            "revenue_analysis": revenue_result,
        }
        service_integration = self.service_integrator.integrate_services(integration_data)
        step_times["service_integration"] = time.time() - step_start
        print(f"⏱️  Service integration completed in {step_times['service_integration']:.1f} seconds")

        # Calculate total time
        total_time = time.time() - total_start_time
        step_times["total_time"] = total_time

        # Return comprehensive results
        final_result = {
            "reddit_trends": reddit_result,
            "successful_projects": successful_projects,
            "competitive_analysis": competitive_result,
            "mvp_suggestions": mvp_result,
            "problem_analysis": problem_result,
            "revenue_analysis": revenue_result,
            "service_integration": service_integration,
            "step_times": step_times,
            "status": "completed",
        }

        print(f"✅ Successful project analysis completed in {total_time:.1f} seconds!")
        return final_result

    def generate_summary_report(self, analysis_result: dict[str, Any]) -> str:
        """Generate summary report based on analysis results.

        Args:
            analysis_result: Analysis results

        Returns:
            Summary report
        """
        from datetime import datetime

        # Get timing information
        step_times = analysis_result.get("step_times", {})
        total_time = step_times.get("total_time", 0)

        # Format timing information
        timing_section = ""
        if step_times:
            timing_section = f"""
## ⏱️ Analysis Performance

### Step-by-Step Timing
- **Reddit Trend Analysis**: {step_times.get("reddit_analysis", 0):.1f} seconds
- **Successful Projects Research**: {step_times.get("successful_projects_research", 0):.1f} seconds
- **Competitive Landscape Analysis**: {step_times.get("competitive_analysis", 0):.1f} seconds
- **MVP Feature Suggestions**: {step_times.get("mvp_suggestions", 0):.1f} seconds
- **Problem Analysis**: {step_times.get("problem_analysis", 0):.1f} seconds
- **Revenue Analysis**: {step_times.get("revenue_analysis", 0):.1f} seconds
- **Service Integration**: {step_times.get("service_integration", 0):.1f} seconds

### Total Analysis Time
- **Overall Duration**: {total_time:.1f} seconds ({total_time / 60:.1f} minutes)
- **Average Step Time**: {total_time / 7:.1f} seconds per step

"""

        # 서비스별 통합 리포트 생성
        service_integration = analysis_result.get("service_integration", {})
        services_analysis = service_integration.get("service_integration", "Service integration not available")

        report = f"""
# Successful Project Analysis Report

## 📋 Analysis Overview
- **Analysis Type**: Successful Project Analysis
- **Focus**: Analyzing successful micro-SaaS projects and suggesting improvements
- **Analysis Date**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **Total Processing Time**: {total_time:.1f} seconds ({total_time / 60:.1f} minutes)

{timing_section}
## 🎯 Key Findings

### 1. Reddit Trend Analysis
{analysis_result.get("reddit_trends", {}).get("reddit_trend_analysis", "Not available")}

### 2. Successful Projects Research
{services_analysis}

## 🚀 Next Steps Recommendations
1. Validate the suggested improvements with potential customers
2. Create detailed technical specifications for MVP features
3. Develop implementation roadmap based on problem analysis
4. Conduct market validation using revenue projections
5. Start prototype development for highest-potential ideas
6. Consider competitive advantages and differentiation strategies

---
*This report is generated by AI-based analysis. Additional verification is required for actual business decisions.*
        """  # noqa

        return report
