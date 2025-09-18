"""SaaS Idea Finder Main Execution Script."""

import os
import sys

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

        # User input
        print("\n" + "=" * 50)
        print("🚀 Welcome to SaaS Idea Finder!")
        print("=" * 50)

        topic = input("\n📝 Please enter the topic or idea you want to analyze: ").strip()

        if not topic:
            print("❌ Please enter a topic.")
            sys.exit(1)

        print(f"\n🔍 Starting comprehensive analysis for '{topic}'...")
        print("⏳ Analysis may take several minutes.")

        # Execute analysis
        result = crew.analyze_saas_idea(topic)

        # Print the result
        print("\n" + "=" * 50)
        print("📊 Analysis Results")
        print("=" * 50)

        # Generate and output summary report
        summary = crew.generate_summary_report(result)
        print(summary)

        # Save results to file
        output_file = f"analysis_result_{topic.replace(' ', '_')}.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(summary)

        print(f"\n💾 Detailed results saved to '{output_file}' file.")

    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
