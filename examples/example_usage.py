"""SaaS Idea Finder Usage Example."""

import os

from dotenv import load_dotenv

from src import SaasIdeaFinderCrew


def example_analysis():
    """Execute example analysis"""
    # Load environment variables
    load_dotenv()

    # Check API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Please set OPENAI_API_KEY.")
        return

    try:
        # Initialize crew
        crew = SaasIdeaFinderCrew()

        # Example topics
        example_topics = [
            "Digital nomad tools for remote workers",
            "Simple inventory management system for small businesses",
            "Side project management tools for individual developers",
            "Simple project management tools for small teams",
        ]

        print("🎯 Example analysis topics:")
        for i, topic in enumerate(example_topics, 1):
            print(f"{i}. {topic}")

        # User selection
        choice = input("\nPlease select the topic number to analyze (1-4): ").strip()

        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(example_topics):
                selected_topic = example_topics[choice_idx]
            else:
                print("❌ Invalid selection.")
                return
        except ValueError:
            print("❌ Please enter a number.")
            return

        print(f"\n🔍 Starting analysis for '{selected_topic}'...")

        # Execute analysis
        result = crew.analyze_saas_idea(selected_topic)

        # Output results
        print("\n" + "=" * 60)
        print("📊 Analysis Results Summary")
        print("=" * 60)

        # Output simple summary
        print(f"Topic: {result.get('topic', 'N/A')}")
        print(f"Status: {result.get('status', 'N/A')}")

        # Generate detailed report
        summary = crew.generate_summary_report(result)

        # Save to file
        output_file = f"example_analysis_{selected_topic.replace(' ', '_')}.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(summary)

        print(f"\n💾 Detailed results saved to '{output_file}' file.")
        print("\n✅ Analysis completed!")

    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")


if __name__ == "__main__":
    example_analysis()
