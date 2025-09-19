"""Reddit Scraper Configuration.

Configuration settings for Reddit data scraping.
"""

# Target subreddits for scraping
SUBREDDITS = [
    "entrepreneur",
    "SaaS",
    "smallbusiness",
    "freelance",
    "productivity",
    "webdev",
    "startups",
    "indiehackers",
    "remotework",
    "digitalnomad",
    "MachineLearning",
    "artificial",
    "OpenAI",
    "ChatGPT",
    "LocalLLaMA",
    "StableDiffusion",
    "LangChain",
    "MLOps",
    "datascience",
    "AutoGPT",
]

# Default limits for different scraping operations
DEFAULT_LIMITS = {
    "hot_posts": 10,
    "top_posts": 10,
    "pain_point_posts": 5,
}

# Pain point search queries
PAIN_POINT_QUERIES = [
    "I wish there was",
    "frustrated with",
    "annoying",
    "pain point",
    "problem with",
    "need a tool",
    "looking for",
    "can't find",
    "struggling with",
    "difficult to",
    "waste of time",
    "manual process",
    "automate this",
    "boring task",
    "repetitive",
]

# Research sources for successful project research
RESEARCH_SOURCES = [
    "Indie Hackers - Successful micro-SaaS case studies",
    "Product Hunt - Trending and successful products",
    "Starter Story - Entrepreneur interviews and case studies",
    "MicroConf - Micro-SaaS conference presentations",
    "Twitter/X - Solo entrepreneur success stories",
    "Reddit r/indiehackers - Success stories and revenue reports",
    "GitHub - Open source projects with commercial success",
    "Hacker News - Recent startup and SaaS discussions and Show HN posts",
    "Y Combinator - Recent batch companies and success stories",
    "TechCrunch - Recent startup funding and success stories",
]
