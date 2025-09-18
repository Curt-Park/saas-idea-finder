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

## 🛠️ Installation and Setup

### 1. Install Dependencies

```bash
# Install mise
curl https://mise.run | sh

# Install dependencies
make setup
```

### 2. Environment Variables Setup

```bash
# Create .env file
cp env.example .env

# Edit .env file to set API keys
# OPENAI_API_KEY=your-openai-api-key-here
# SERPER_API_KEY=your-serper-api-key-here (optional)
# REDDIT_CLIENT_ID=your-reddit-client-id-here
# REDDIT_CLIENT_SECRET=your-reddit-client-secret-here
# REDDIT_USER_AGENT=SaaS Idea Finder Bot 1.0
```

### 3. Required API Keys

- **OpenAI API Key** (Required): Needed for GPT model usage
- **Serper API Key** (Optional): Needed for web search functionality
- **Reddit API Credentials** (Required): Needed for Reddit data scraping

#### Reddit API Setup

To use Reddit data scraping, you need to create a Reddit app:

1. **Create Reddit App**:
   - Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps)
   - Click "Create App" or "Create Another App"
   - Choose "script" as the app type
   - Fill in the name and description
   - Copy the client ID (under the app name) and client secret
   - Add them to your `.env` file

2. **Reddit API Rate Limits**:
   - 60 requests per minute for authenticated requests
   - 100 requests per minute for unauthenticated requests
   - The tool automatically handles rate limiting

3. **Required Reddit App Settings**:
   - **App Type**: Script
   - **Name**: SaaS Idea Finder Bot (or any name you prefer)
   - **Description**: Tool for analyzing Reddit trends for SaaS opportunities
   - **About URL**: (optional)
   - **Redirect URI**: (leave empty for script apps)

#### OpenAI API Setup

1. **Get OpenAI API Key**:
   - Go to [OpenAI Platform](https://platform.openai.com/)
   - Sign up or log in to your account
   - Navigate to [API Keys](https://platform.openai.com/api-keys)
   - Click "Create new secret key"
   - Copy the key and add it to your `.env` file

2. **OpenAI Usage Costs**:
   - GPT-4o-mini: $0.15/1M input tokens, $0.60/1M output tokens
   - Estimated cost per analysis: $0.50-$2.00
   - Monitor usage at [OpenAI Usage Dashboard](https://platform.openai.com/usage)

#### Serper API Setup (Optional)

For web search functionality (currently not used in Reddit-focused mode):

1. **Get Serper API Key**:
   - Go to [Serper.dev](https://serper.dev/)
   - Sign up for a free account
   - Get your API key from the dashboard
   - Add it to your `.env` file

2. **Serper Pricing**:
   - Free tier: 2,500 searches per month
   - Paid plans start at $5/month for 10,000 searches

### 4. Environment Variables Example

Create a `.env` file in the project root with the following format:

```env
# Required API Keys
OPENAI_API_KEY=sk-your-openai-api-key-here
REDDIT_CLIENT_ID=your-reddit-client-id-here
REDDIT_CLIENT_SECRET=your-reddit-client-secret-here
REDDIT_USER_AGENT=SaaS Idea Finder Bot

# Optional API Keys
SERPER_API_KEY=your-serper-api-key-here
```

### 5. Troubleshooting

#### Common Issues and Solutions

**Reddit API Issues**:
- **Error**: "Invalid credentials"
  - Solution: Double-check your Reddit client ID and secret
  - Make sure you're using the correct app type (script)

- **Error**: "Rate limit exceeded"
  - Solution: The tool automatically handles rate limiting
  - Wait a few minutes before running again

- **Error**: "Forbidden" or "403"
  - Solution: Check if your Reddit app is properly configured
  - Ensure the app type is set to "script"

**OpenAI API Issues**:
- **Error**: "Invalid API key"
  - Solution: Verify your OpenAI API key is correct
  - Check if you have sufficient credits in your OpenAI account

- **Error**: "Rate limit exceeded"
  - Solution: Wait a few minutes or upgrade your OpenAI plan
  - Monitor usage at [OpenAI Usage Dashboard](https://platform.openai.com/usage)

**General Issues**:
- **Error**: "Module not found"
  - Solution: Run `pip install -r requirements.txt`
  - Ensure you're in the correct virtual environment

- **Error**: "Permission denied" when creating reports
  - Solution: Check file permissions in the `report/` directory
  - Ensure the directory is writable

### 6. Additional Resources

#### API Documentation Links
- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [PRAW Documentation](https://praw.readthedocs.io/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Serper API Documentation](https://serper.dev/docs)

#### Reddit API Best Practices
- **Rate Limiting**: Reddit API has strict rate limits
- **User Agent**: Always use a descriptive user agent
- **Respect Reddit's Terms**: Follow Reddit's API terms of service
- **Data Usage**: Be mindful of data collection and storage

#### Cost Optimization Tips
- **OpenAI**: Use GPT-4o-mini for cost efficiency
- **Reddit**: The tool automatically limits requests to stay within rate limits
- **Monitoring**: Keep track of API usage to avoid unexpected charges

#### Security Best Practices
- **Environment Variables**: Never commit API keys to version control
- **API Key Rotation**: Regularly rotate your API keys
- **Access Control**: Limit API key permissions where possible

## 🚀 Quick Start Guide

### Step-by-Step Setup

1. **Clone and Setup**:
   ```bash
   git clone <repository-url>
   cd saas-idea-finder
   make setup
   ```

2. **Get API Keys**:
   - **OpenAI**: Get API key from [OpenAI Platform](https://platform.openai.com/api-keys)
   - **Reddit**: Create app at [Reddit App Preferences](https://www.reddit.com/prefs/apps)

3. **Configure Environment**:
   ```bash
   cp env.example .env
   # Edit .env with your API keys
   ```

4. **Run Analysis**:
   ```bash
   # Use default model (gpt-4o-mini)
   python main.py
   
   # Use specific model
   python main.py --model gpt-4o
   
   # Use custom temperature
   python main.py --model gpt-4o-mini --temperature 0.5
   ```

5. **Check Results**:
   - Reports saved in `report/` directory
   - Markdown (.md) format with professional formatting

### Command Line Options

The tool supports various command line options for customization:

```bash
# Show help
python main.py --help

# Use different OpenAI models
python main.py --model gpt-4o          # Most capable model
python main.py --model gpt-4o-mini     # Cost-effective default
python main.py --model gpt-4-turbo     # Balanced option
python main.py --model gpt-3.5-turbo   # Fastest option

# Adjust creativity/temperature
python main.py --temperature 0.1       # More focused/consistent
python main.py --temperature 0.7      # More creative/varied
python main.py --temperature 1.0      # Maximum creativity
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

## 📊 Analysis Process

1. **Reddit Trend Analysis**: Analyzes Reddit communities for pain points and opportunities with:
   - Direct Reddit post references (URLs, titles, dates)
   - Engagement metrics (upvotes, comments)
   - Number of similar discussions found
   - Key user quotes and subreddit sources

2. **Successful Project Research**: Researches recent micro-SaaS projects (launched within 2-3 years) with:
   - Launch dates and timeline to success
   - Current revenue status and growth trajectory
   - Founder background and team composition
   - Marketing strategies and customer acquisition methods

3. **Competitive Landscape Analysis**: Analyzes existing services for gaps and improvements
4. **MVP Feature Suggestions**: Suggests specific features to differentiate from competitors
5. **Problem Analysis**: Identifies key problems to solve for implementation
6. **Revenue Analysis**: Analyzes expected revenue and profitability

## 📄 Report Generation

The tool generates comprehensive reports in Markdown format:
- **Markdown (.md)**: For easy reading, editing, and sharing
- **Professional formatting**: Clean, structured reports with proper headings and formatting
- **Timestamped files**: Reports are automatically saved with timestamps in the `report/` directory

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
A: The tool collects up to 20 posts per subreddit (hot posts, recent posts, and pain point posts), totaling up to 1,200 posts across all subreddits.

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

## 🔧 Development Tools

```bash
# Code formatting
make format

# Linting
make lint

# Install dependencies
make setup
```

## 📝 Output Example

Analysis results are provided in the following format:

- **Painpoint Analysis**: Major problems users are facing
- **Market Opportunities**: Market size, growth rate, marketing efficiency
- **Technical Feasibility**: Recommended tech stack, development difficulty, cost predictions
- **Business Proposal**: Revenue model, marketing strategy, operational plan
- **Competitive Environment**: Existing service analysis, differentiation strategies

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

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for details.