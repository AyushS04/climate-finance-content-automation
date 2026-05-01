# Climate Finance Content Automation

An intelligent LinkedIn content automation tool for generating, scheduling, and analyzing climate finance content. This platform helps organizations and professionals share valuable insights about climate finance, sustainable investing, and environmental initiatives.

## 🌍 Features

✨ **Smart Content Generation**
- AI-powered climate finance content creation using GPT-4
- Topic-based content suggestions for 8 major climate finance areas
- Multi-format support (LinkedIn posts, Twitter threads, articles, newsletters, video scripts)
- Customizable tone and length options

📅 **Post Scheduling**
- Schedule posts across multiple platforms (LinkedIn, Twitter, Medium)
- Optimal posting time recommendations
- Queue management and post rescheduling
- Timezone-aware scheduling

📊 **Analytics Dashboard**
- Real-time engagement metrics (views, likes, comments, shares)
- Performance tracking across platforms
- Audience insights and trending topics
- ROI analysis and export capabilities

🔄 **Cross-Platform Publishing**
- LinkedIn native integration for direct publishing
- Twitter/X API support with thread capabilities
- Medium cross-posting
- Webhook integrations for custom platforms

## 🏗️ Project Structure

```
climate-finance-content-automation/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Flask API server
│   ├── content/
│   │   ├── __init__.py
│   │   └── generator.py        # Content generation engine
│   ├── scheduler/
│   │   ├── __init__.py
│   │   └── scheduler.py        # Post scheduling system
│   ├── analytics/
│   │   ├── __init__.py
│   │   ├── tracker.py          # Engagement tracking
│   │   └── dashboard.py        # Analytics dashboard
│   ├── integrations/
│   │   ├── __init__.py
│   │   ├── linkedin_api.py     # LinkedIn integration
│   │   ├── twitter_api.py      # Twitter integration
│   │   └── medium_api.py       # Medium integration
│   └── utils/
│       ├── __init__.py
│       ├── config.py           # Configuration management
│       └── logger.py           # Logging setup
├── config/
│   ├── climate_finance_topics.json  # Topic database
│   └── templates.json              # Content templates
├── tests/
│   ├── test_content.py
│   ├── test_scheduler.py
│   └── test_analytics.py
├── requirements.txt
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## 🎯 Climate Finance Topics Covered

1. **Carbon Markets & Trading** - Carbon credits, emissions trading systems
2. **ESG Investing** - Environmental, Social, Governance investment strategies
3. **Green Bonds** - Bonds financing environmental projects
4. **Renewable Energy Finance** - Solar, wind, hydro project financing
5. **Net Zero Commitments** - Transition plans and climate pathways
6. **Climate Risk Assessment** - Physical and transition risk management
7. **Nature-Based Solutions** - Conservation and ecosystem financing
8. **Just Transition Finance** - Fair transition from fossil fuels

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- LinkedIn Developer Account & Access Token
- Twitter Developer Account (optional)
- OpenAI API Key (for GPT-4)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/AyushS04/climate-finance-content-automation.git
cd climate-finance-content-automation
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your API credentials
```

5. **Run the application**
```bash
python src/main.py
```

The API will be available at `http://localhost:5000`

## 🐳 Docker Support

Run with Docker:
```bash
docker-compose up
```

## 📖 API Documentation

### Content Generation
```bash
# Generate content for a topic
POST /api/content/generate
Body: {
  "topic": "carbon_markets",
  "format": "linkedin_post",
  "tone": "professional",
  "length": "medium"
}

# Get available topics
GET /api/content/topics
```

### Post Scheduling
```bash
# Schedule a post
POST /api/schedule/post
Body: {
  "content": "Your content here",
  "platforms": ["linkedin", "twitter"],
  "scheduled_time": "2026-05-15T10:00:00Z",
  "title": "Optional title",
  "image_url": "Optional image URL"
}

# Get scheduled posts
GET /api/schedule/posts?status=scheduled

# Cancel a post
DELETE /api/schedule/post/{post_id}
```

### Analytics
```bash
# Get analytics dashboard
GET /api/analytics/dashboard

# Get trending topics
GET /api/analytics/trending
```

## 💻 Usage Examples

### Generate Climate Finance Content
```python
from src.content.generator import ContentGenerator

generator = ContentGenerator()
content = generator.generate(
    topic="carbon_markets",
    format="linkedin_post",
    tone="professional",
    length="medium"
)
print(content)
```

### Schedule a Post
```python
from src.scheduler.scheduler import PostScheduler

scheduler = PostScheduler()
result = scheduler.schedule_post(
    content="Your content about climate finance",
    platforms=["linkedin", "twitter"],
    scheduled_time="2026-05-15T14:00:00Z"
)
print(result)
```

### Track Analytics
```python
from src.analytics.tracker import AnalyticsTracker

tracker = AnalyticsTracker()
metrics = tracker.get_performance_metrics(
    date_range=("2026-04-01", "2026-05-01")
)
print(metrics)
```

## ⚙️ Configuration

### Environment Variables (.env)
```
# LinkedIn
LINKEDIN_ACCESS_TOKEN=your_token
LINKEDIN_ORG_ID=your_org_id

# Twitter
TWITTER_API_KEY=your_key
TWITTER_BEARER_TOKEN=your_bearer_token

# OpenAI
OPENAI_API_KEY=your_api_key

# Application
DEBUG=True
LOG_LEVEL=INFO
TIMEZONE=UTC
```

## 🧪 Testing

Run tests:
```bash
pytest tests/ -v
```

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📊 Database Schema

The application uses PostgreSQL. Key tables:
- `users` - User accounts
- `posts` - Scheduled and published posts
- `content_templates` - Reusable content templates
- `analytics_events` - Tracking events
- `social_accounts` - Connected social media accounts

## 🗺️ Roadmap

- [ ] Multi-language content generation
- [ ] AI sentiment analysis for posts
- [ ] Competitor analysis
- [ ] Advanced scheduling with ML optimization
- [ ] Mobile app
- [ ] Slack integration
- [ ] Real-time collaboration features
- [ ] Advanced reporting and exports
- [ ] Community insights dashboard
- [ ] AI-powered hashtag suggestions

## 📝 License

MIT License - see LICENSE.md for details

## 🆘 Support

For support, please open an issue on GitHub or contact us.

## 🙏 Acknowledgments

- LinkedIn API Documentation
- OpenAI for GPT-4 capabilities
- Climate finance research communities
- Open source community contributors

---

**Made with ❤️ for climate action and sustainable finance** 🌍♻️
