# SaaS Idea Finder

A multi-agent tool built with crewAI that comprehensively analyzes the market potential and feasibility of SaaS ideas.

## 🚀 Key Features

1. **Reddit Trend Analysis**: Analyzes Reddit communities to identify trending pain points and opportunities with detailed references and dates
2. **Successful Project Research**: Researches and analyzes recent successful micro-SaaS projects (launched within 1-2 years) with launch dates and growth trajectories
3. **Competitive Landscape Analysis**: Analyzes existing services to identify gaps and improvement opportunities
4. **MVP Feature Suggestions**: Suggests specific features to differentiate from competitors
5. **Problem Analysis**: Identifies key problems to solve for implementing suggested features
6. **Revenue Analysis**: Analyzes expected revenue and profitability for suggested services
7. **Comprehensive Reports**: Generates detailed Markdown reports with professional formatting

## 📄 Report Generation

The tool generates comprehensive reports in Markdown format:
- **Markdown (.md)**: For easy reading, editing, and sharing
- **Professional formatting**: Clean, structured reports with proper headings and formatting
- **Timestamped files**: Reports are automatically saved with timestamps in the `report/` directory

## 🛠️ Installation and Setup

### 1. Install Dependencies

```bash
# Install mise
curl https://mise.run | sh

# Install dependencies
make setup
```

### 2. Required API Keys

- **OpenAI API Key** (Required): Needed for GPT model usage
- **Serper API Key** (Optional): Needed for web search functionality
- **Reddit API Credentials** (Required): Needed for Reddit data scraping

### 3. Environment Variables Setup

```bash
# Create .env file
cp env.example .env

# Edit .env file to set API keys
# OPENAI_API_KEY=your-openai-api-key-here
# SERPER_API_KEY=your-serper-api-key-here (optional)
# REDDIT_CLIENT_ID=your-reddit-client-id-here
# REDDIT_CLIENT_SECRET=your-reddit-client-secret-here
# REDDIT_USER_AGENT="SaaS Idea Finder Bot"
```

## 🎯 Usage

### Basic Usage

```bash
python main.py
```

The tool focuses on analyzing successful projects and suggesting improvements based on Reddit trends and market research.

### Programmatic Usage

```python
from src import SaasIdeaFinderCrew

# Initialize crew
crew = SaasIdeaFinderCrew()

# Analyze successful projects and suggest improvements
result = crew.analyze_successful_projects()

# Generate summary report
summary = crew.generate_summary_report(result)
print(summary)
```

## 🏗️ Architecture

```
src/
├── agents/           # Various agents
│   ├── reddit_trend_analyzer.py           # Reddit trend analysis agent
│   ├── successful_project_researcher.py   # Successful project research agent
│   ├── competitive_landscape_analyzer.py  # Competitive landscape analysis agent
│   ├── mvp_feature_suggester.py          # MVP feature suggestion agent
│   ├── problem_analyzer.py                # Problem analysis agent
│   └── revenue_analyzer.py               # Revenue analysis agent
├── crew/            # Crew orchestration
│   └── saas_idea_finder_crew.py    # Main crew
└── __init__.py
```

## 🔧 Development Tools

```bash
# Code formatting
make format

# Linting
make lint

# Install dependencies
make setup
```

## ⚠️ Important Notes

- This tool generates results based on AI analysis
- Additional verification is required for actual business decisions
- Costs may be incurred based on API usage

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ❓ FAQ

### Frequently Asked Questions

**Q: How much does it cost to run the analysis?**
A: The main cost is from OpenAI API usage. Each analysis typically costs $0.50-$2.00 depending on the amount of Reddit data processed.

**Q: How long does the analysis take?**
A: Typically 5-15 minutes depending on Reddit API response times and the amount of data being processed.

**Q: Can I run this without Reddit API credentials?**
A: No, Reddit API credentials are required for data collection. The tool needs to access Reddit posts to perform meaningful analysis.

**Q: What Reddit subreddits are analyzed?**
A: The tool analyzes 20 subreddits including r/entrepreneur, r/SaaS, r/smallbusiness, r/productivity, r/webdev, r/startups, r/indiehackers, and many more.

**Q: How much Reddit data is collected?**
A: The tool collects up to 10 posts per subreddit (hot posts, weekly top posts, and pain point posts), totaling up to 1,200 posts across all subreddits.

**Q: What format are the reports saved in?**
A: Reports are saved in Markdown (.md) format with professional formatting, making them easy to read, edit, and share.

**Q: Can I customize which subreddits are analyzed?**
A: Yes, you can modify the `subreddits` list in `src/utils/reddit_scraper.py` to include or exclude specific subreddits.

**Q: Is the Reddit data stored locally?**
A: No, the tool only processes Reddit data in memory and doesn't store it permanently. Only the analysis results are saved to files.

**Q: Can I run this on a schedule?**
A: Yes, you can set up a cron job or use GitHub Actions to run the analysis automatically. Be mindful of API rate limits.

**Q: Which OpenAI model should I use?**
A: 
- **gpt-4o-mini** (default): Best balance of cost and quality, recommended for most users
- **gpt-4o**: Highest quality but more expensive, use for critical analyses
- **gpt-4-turbo**: Good balance between speed and quality
- **gpt-3.5-turbo**: Fastest and cheapest, but lower quality results

**Q: What temperature setting should I use?**
A:
- **0.1-0.3** (default): More focused and consistent results, recommended for analysis
- **0.5-0.7**: Balanced creativity and consistency
- **0.8-1.0**: More creative and varied results, use with caution for analysis tasks

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for details.