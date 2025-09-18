# SaaS Idea Finder

A multi-agent tool built with crewAI that comprehensively analyzes the market potential and feasibility of SaaS ideas.

## 🚀 Key Features

1. **Painpoint Collection**: Identifies painpoints and new needs from Reddit, social media, and Google Trends
2. **Market Analysis**: Analyzes success signals, marketing efficiency, and natural growth potential
3. **Technical Feasibility Analysis**: Analyzes tech stack and implementation difficulty for solo entrepreneurs
4. **Proposal Writing**: Creates executable business proposals based on analysis results
5. **Competitor Analysis**: Analyzes existing similar services, their pros/cons, and revenue models

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
```

### 3. Required API Keys

- **OpenAI API Key** (Required): Needed for GPT model usage
- **Serper API Key** (Optional): Needed for web search functionality

## 🎯 Usage

### Basic Usage

```bash
python main.py
```

### Run Examples

```bash
python examples/example_usage.py
```

### Programmatic Usage

```python
from src import SaasIdeaFinderCrew

# Initialize crew
crew = SaasIdeaFinderCrew()

# Analyze idea
result = crew.analyze_saas_idea("Digital nomad tools for remote workers")

# Generate summary report
summary = crew.generate_summary_report(result)
print(summary)
```

## 📊 Analysis Process

1. **Painpoint Collection**: Identifies user needs from Reddit, social media, and Google Trends
2. **Market Analysis**: Analyzes market size, growth rate, and marketing efficiency
3. **Technical Feasibility**: Recommends tech stack implementable by solo developers
4. **Proposal Writing**: Creates executable business models and strategies
5. **Competitor Analysis**: Analyzes existing services and derives differentiation strategies

## 🏗️ Architecture

```
src/
├── agents/           # Various agents
│   ├── painpoint_collector.py      # Painpoint collection agent
│   ├── market_analyzer.py          # Market analysis agent
│   ├── tech_feasibility_analyzer.py # Technical feasibility analysis agent
│   ├── proposal_writer.py          # Proposal writing agent
│   └── competitor_analyzer.py       # Competitor analysis agent
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