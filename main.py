"""SaaS Idea Finder Main Execution Script."""

import argparse
import os
import sys
from datetime import datetime

from dotenv import load_dotenv

from src import SaasIdeaFinderCrew


def main():
    """Main execution function"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="SaaS Idea Finder - Multi-agent tool for analyzing SaaS opportunities")
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o-mini",
        help="OpenAI model to use (default: gpt-4o-mini). Options: gpt-4o-mini, gpt-4o, gpt-4-turbo, gpt-3.5-turbo",
    )
    parser.add_argument("--temperature", type=float, default=0.3, help="Temperature for model generation (default: 0.3)")

    args = parser.parse_args()

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
        # Initialize crew with specified model
        print(f"🤖 Initializing SaaS Idea Finder crew with model: {args.model}...")
        crew = SaasIdeaFinderCrew(model=args.model, temperature=args.temperature)

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
        report_dir = "reports"
        os.makedirs(report_dir, exist_ok=True)

        # Generate timestamp-based filename
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        md_file = os.path.join(report_dir, f"{timestamp}.md")
        latest_file = os.path.join(report_dir, "latest-report.md")

        # Save markdown file with timestamp
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(summary)

        # Also save as latest-report.md
        with open(latest_file, "w", encoding="utf-8") as f:
            f.write(summary)

        print(f"\n💾 Detailed results saved to: '{md_file}'")
        print(f"�� Latest report also saved to: '{latest_file}'")

    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
