"""SaaS Idea Finder Main Execution Script."""

import os
import sys
from datetime import datetime

from dotenv import load_dotenv

from src import SaasIdeaFinderCrew


def main():
    """Main execution function"""
    # Load environment variables
    load_dotenv()

    # Check OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ OPENAI_API_KEY environment variable is not set.")
        print("Please set it as follows:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        print("or add OPENAI_API_KEY=your-api-key-here to .env file")
        sys.exit(1)

    # Check Serper API key (optional)
    if not os.getenv("SERPER_API_KEY"):
        print("⚠️  SERPER_API_KEY is not set.")
        print("Please set Serper API key to use web search functionality.")
        print("export SERPER_API_KEY='your-serper-api-key'")

    try:
        # Initialize crew
        print("🤖 Initializing SaaS Idea Finder crew...")
        crew = SaasIdeaFinderCrew()

        # Successful Project Analysis
        print("\n" + "=" * 50)
        print("🚀 Welcome to SaaS Idea Finder!")
        print("=" * 50)
        print("\n💰 Starting successful project analysis...")
        print("⏳ This will analyze Reddit trends, research successful projects, and suggest improvements...")
        print("⏳ Analysis may take several minutes.")

        # Execute successful project analysis
        result = crew.analyze_successful_projects()

        # Print the result
        print("\n" + "=" * 50)
        print("📊 Analysis Results")
        print("=" * 50)

        # Generate and output summary report
        summary = crew.generate_summary_report(result)
        print(summary)

        # Create report directory if it doesn't exist
        report_dir = "report"
        os.makedirs(report_dir, exist_ok=True)

        # Generate timestamp-based filename
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        md_file = os.path.join(report_dir, f"{timestamp}.md")

        # Save markdown file
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(summary)

        print(f"\n💾 Detailed results saved to: '{md_file}'")

    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
