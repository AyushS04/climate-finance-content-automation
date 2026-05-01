"""
Climate Finance Content Generator
Generates intelligent, engaging content focused on climate finance topics.
"""

import os
import json
from typing import Optional, Dict, List
from datetime import datetime
from src.utils.logger import get_logger
from src.utils.config import Config

logger = get_logger(__name__)


class ContentGenerator:
    """
    Generate climate finance content.
    Supports multiple formats and tones.
    """

    def __init__(self):
        self.config = Config()
        self.climate_topics = self._load_climate_topics()

    def _load_climate_topics(self) -> Dict:
        """Load climate finance topics from configuration."""
        try:
            with open('config/climate_finance_topics.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning("Climate topics file not found, using defaults")
            return self._get_default_topics()

    def _get_default_topics(self) -> Dict:
        """Return default climate finance topics."""
        return {
            "carbon_markets": {"description": "Carbon credits, emissions trading, offsets", "keywords": ["carbon", "emissions", "trading", "offset", "ETS"]},
            "esg_investing": {"description": "Environmental, Social, Governance investing", "keywords": ["ESG", "sustainable", "investing", "impact"]},
            "green_bonds": {"description": "Bonds financing environmental projects", "keywords": ["green bond", "sustainable", "fixed income"]},
            "renewable_energy": {"description": "Solar, wind, hydro financing", "keywords": ["renewable", "solar", "wind", "clean energy"]},
            "net_zero": {"description": "Net zero commitments and pathways", "keywords": ["net zero", "decarbonization", "climate goals"]},
            "climate_risk": {"description": "Climate risk assessment and management", "keywords": ["climate risk", "physical risk", "transition risk"]}
        }

    def generate(self, topic: str, format: str = "linkedin_post", tone: str = "professional", hashtags: bool = True, length: str = "medium") -> Dict[str, str]:
        """Generate climate finance content."""
        try:
            topic_info = self.climate_topics.get(topic, {})
            if not topic_info:
                raise ValueError(f"Topic '{topic}' not found")

            content = self._generate_content(topic, topic_info, format, tone, length)

            if hashtags:
                content = self._add_hashtags(content, topic)

            return {
                "content": content,
                "topic": topic,
                "format": format,
                "tone": tone,
                "generated_at": datetime.now().isoformat(),
                "status": "success"
            }

        except Exception as e:
            logger.error(f"Error generating content: {str(e)}")
            raise

    def _generate_content(self, topic: str, topic_info: Dict, format: str, tone: str, length: str) -> str:
        """Generate content based on topic and format."""
        
        templates = {
            "carbon_markets": {
                "linkedin_post": self._carbon_markets_linkedin,
                "twitter_thread": self._carbon_markets_twitter,
                "article": self._carbon_markets_article
            },
            "esg_investing": {
                "linkedin_post": self._esg_linkedin,
                "twitter_thread": self._esg_twitter,
                "article": self._esg_article
            },
            "green_bonds": {
                "linkedin_post": self._green_bonds_linkedin,
                "twitter_thread": self._green_bonds_twitter,
                "article": self._green_bonds_article
            },
            "renewable_energy": {
                "linkedin_post": self._renewable_linkedin,
                "twitter_thread": self._renewable_twitter,
                "article": self._renewable_article
            },
            "net_zero": {
                "linkedin_post": self._net_zero_linkedin,
                "twitter_thread": self._net_zero_twitter,
                "article": self._net_zero_article
            },
            "climate_risk": {
                "linkedin_post": self._climate_risk_linkedin,
                "twitter_thread": self._climate_risk_twitter,
                "article": self._climate_risk_article
            }
        }

        generator_func = templates.get(topic, {}).get(format)
        
        if generator_func:
            return generator_func(tone, length)
        else:
            return self._default_content(topic, format, tone)

    # Carbon Markets Content
    def _carbon_markets_linkedin(self, tone: str, length: str) -> str:
        return """🌍 The Global Carbon Market is Reaching Inflection Point

The carbon market has evolved dramatically over the past decade. Global carbon credit trading volume exceeded $900 billion in 2023, marking a 37% increase year-over-year. This explosive growth reflects a fundamental shift in how enterprises approach climate accountability.

Key Insights:
📊 Voluntary carbon markets (VCMs) grew 69% in value
🏭 Corporate net-zero commitments now drive 60%+ of demand
💰 Article 6 of Paris Agreement unlocking cross-border trading
🌱 Nature-based solutions commanding 40%+ premium prices

The convergence of mandatory compliance and voluntary action creates unprecedented opportunities. Organizations are no longer asking "if" they should participate in carbon markets, but "how" to maximize impact while managing risk.

What's your organization's carbon strategy for 2025?

#CarbonMarkets #ClimateAction #Sustainability #ESG #NetZero"""

    def _carbon_markets_twitter(self, tone: str, length: str) -> str:
        return """1/ 🚨 The carbon market just hit $900B in trading volume. This isn't just about compliance—it's reshaping how enterprises approach climate strategy.

2/ Voluntary Carbon Markets (VCMs) grew 69% last year. Companies like Microsoft, Google, and Shell are now major buyers. The demand side is fundamentally shifting.

3/ Article 6 of the Paris Agreement is the game-changer. For the first time, international carbon trading is standardized.

4/ Nature-based solutions are commanding 40%+ premiums. Mangrove restoration, forest conservation deliver both carbon AND biodiversity benefits.

5/ The winners? Organizations building transparent, measurable carbon strategies NOW. The losers? Those waiting for clarity.

The carbon market is maturing. Are you ready?

#CarbonMarkets #ClimateFinance #ESG"""

    def _carbon_markets_article(self, tone: str, length: str) -> str:
        return """The Carbon Market Evolution: From Compliance Tool to Strategic Asset

Executive Summary
The global carbon market has undergone a revolutionary transformation from a $900+ billion market. This article explores the drivers, opportunities, and risks in today's carbon market landscape.

Market Dynamics and Growth Drivers

The carbon market's explosive growth stems from three converging forces:

1. Corporate Net-Zero Commitments
Over 4,000 companies representing 37% of global market capitalization have made net-zero commitments backed by investment and accountability.

2. Article 6 Standardization
The Paris Agreement's Article 6 framework creates the first truly international carbon trading system with standardized methodologies.

3. Nature-Based Solutions Premium
Investors recognize nature-based solutions deliver co-benefits: carbon sequestration, biodiversity protection, community development. These command 40-60% premiums.

Strategic Implications

For CFOs and sustainability leaders, carbon markets represent dual opportunity:
- Risk Management: Offset residual emissions from operations
- Value Creation: Invest in high-quality carbon projects with financial returns

Conclusion
The carbon market is no longer a compliance burden—it's a strategic asset class.

#CarbonMarkets #ClimateFinance #SustainableInvesting"""

    # ESG Investing Content
    def _esg_linkedin(self, tone: str, length: str) -> str:
        return """📈 ESG Investing Just Hit $35 Trillion—Here's What Changed

ESG-managed assets now represent 35% of all professionally managed capital globally—$35 TRILLION. This isn't niche investing anymore. It's mainstream.

What's Driving This Shift:

🎯 Performance Data: ESG leaders outperform peers by 2-3% annually over 10-year periods
⚖️ Risk Mitigation: Companies with strong ESG scores show 25% lower volatility during downturns
🌍 Regulatory Pressure: 70+ countries now require climate/ESG disclosure
💼 Investor Demand: Asset managers face increasing pressure from LPs to integrate ESG

The Real Story: ESG Has Moved from Ethics to Economics

The best ESG investments deliver superior risk-adjusted returns. That's why BlackRock, Vanguard, and State Street have doubled down on ESG integration.

For corporate leaders: The ESG question isn't "should we?" anymore. It's "how do we scale impact while delivering shareholder value?"

What's your organization's ESG investment thesis?

#ESG #SustainableInvesting #ImpactInvesting #FinanceOfTheFuture"""

    def _esg_twitter(self, tone: str, length: str) -> str:
        return """1/ $35 TRILLION. That's how much capital is now managed with ESG criteria. ESG is mainstream finance.

2/ ESG leaders outperform peers by 2-3% annually. Better returns + better impact = unstoppable trend.

3/ ESG leaders show 25% LOWER volatility during downturns. This isn't ethics—it's risk management.

4/ 70+ countries now require climate/ESG disclosure. Companies can't ignore this.

5/ Winners integrate ESG into core operations. This is about strategic advantage.

The question isn't "should we invest in ESG?" It's "how fast can we move?"

#ESG #SustainableInvesting #Finance"""

    def _esg_article(self, tone: str, length: str) -> str:
        return """ESG Investing: How $35 Trillion Reshapes Global Capital Markets

Introduction
With $35 trillion now managed according to ESG criteria—representing 35% of all professionally managed capital—ESG has transitioned from "nice to have" to "essential."

The Performance Case for ESG

1. Return Outperformance
ESG leaders consistently outperform peers by 2-3% annually over 10-year periods.

2. Risk Reduction
Companies with strong ESG scores demonstrate 25% lower volatility during market downturns.

Market Drivers

Regulatory Mandates: SEC, EU require ESG disclosure
Institutional Pressure: Asset owners demand ESG integration
Demographic Shift: Millennials and Gen Z demand sustainable options

Conclusion
ESG investing is mainstream. For institutional investors, the question is execution.

#ESG #SustainableInvesting #FinanceOfTheFuture"""

    # Green Bonds Content
    def _green_bonds_linkedin(self, tone: str, length: str) -> str:
        return """💚 Green Bond Issuance Hit $500B in 2023—Here's Why It Matters

Green bonds have gone from niche to capital market staple. 2023 saw $500 billion in issuance—a stunning validation of sustainable finance.

Why This Matters:

🏗️ Infrastructure Funding: Renewable energy projects have capital they need
💰 Lower Cost of Capital: Green bond yields 25-50 bps lower than conventional
🌍 Corporate Scale: Apple, Google, Microsoft now issue green bonds
📈 Investor Demand: Order book 2-3x oversubscribed

The Real Innovation: Sustainability and returns aren't mutually exclusive.

Key Players:
✅ Multilateral Development Banks ($50B+ annual)
✅ Corporate Issuers (Tech, Energy, Real Estate)
✅ Sovereign Green Bonds (50+ countries)

The Next Frontier:
✨ Blue Bonds (Ocean restoration)
✨ Sustainability-Linked Bonds
✨ Emerging Market Green Bonds

For treasurers and CFOs: Green bonds are a strategic financing tool.

What's your organization's green bond strategy?

#GreenBonds #SustainableFinance #ClimateAction #ESG"""

    def _green_bonds_twitter(self, tone: str, length: str) -> str:
        return """1/ $500B in green bond issuance in 2023. That's transformational.

2/ Green bonds yield 25-50 bps LOWER than conventional. Lower cost + climate impact. Demand is exploding.

3/ Order book is 2-3x oversubscribed. Institutions desperate for sustainable options.

4/ Apple, Google, Microsoft all issuing. Mainstream adoption confirmed.

5/ Emerging market sovereigns issuing green bonds. This unlocks $100B+ in climate capital.

Green bonds prove: sustainability and returns aren't mutually exclusive.

#GreenBonds #SustainableFinance #ClimateFinance"""

    def _green_bonds_article(self, tone: str, length: str) -> str:
        return """Green Bonds: How $500B Mobilizes Climate Capital

Executive Summary
Green bonds have emerged as the most effective mechanism for mobilizing capital toward climate solutions. With $500 billion in annual issuance, they represent sustainable finance maturation.

Market Evolution

Phase 1 (2007-2015): Niche Product
ESG investors pioneered green bonds. Annual issuance under $50 billion.

Phase 2 (2016-2019): Corporate Adoption
Tech and renewable companies began large-scale issuance. Reached $250+ billion.

Phase 3 (2020-Present): Mainstream Tool
Green bonds now 5-10% of new fixed income issuance. Sovereigns, corporations compete for investor demand.

Financial Benefits

1. Yield Advantage
Green bonds yield 25-50 basis points lower than conventional. Strong investor demand.

2. Pricing Power
Order books typically 2-3x oversubscribed.

3. Access to New Capital
ESG-focused managers can only purchase green bonds.

Conclusion
Green bonds are now cornerstone of sustainable finance.

#GreenBonds #SustainableFinance #ClimateAction"""

    # Renewable Energy Content
    def _renewable_linkedin(self, tone: str, length: str) -> str:
        return """⚡ Renewable Energy Investment Just Hit $495B—The Math is Now Undeniable

Renewable energy crossed inflection point. 2023 global renewable investment reached $495 billion—surpassing fossil fuel investment first time.

This Isn't Just Environmental. It's Economics.

The Facts:
💡 Solar + wind cheaper than coal in 90% of markets
📉 Renewable costs dropped 90% over decade
💰 Renewables employ 12+ million globally
🔋 Grid-scale battery storage scaling exponentially

The Investment Case:

For CFOs, renewable passes fundamental tests:
✓ Lower levelized cost of energy (LCOE)
✓ Predictable 20-25 year cash flows
✓ Hedges energy price volatility
✓ De-risks operations

The Big Shift: Renewables about financial returns, not just climate impact.

Emerging Opportunities:
🌊 Offshore Wind: $50B+ market, 10x growth potential
🔌 Green Hydrogen: $50B+ thesis
🔋 Energy Storage: $30B+ growing 30% annually
🌍 Emerging Markets: 60%+ new investment

For corporate teams: Not locking renewable energy through PPAs? Leaving money on table.

#RenewableEnergy #CleanEnergy #SustainableInvesting #ClimateFinance"""

    def _renewable_twitter(self, tone: str, length: str) -> str:
        return """1/ $495B renewable investment in 2023. First time surpassed fossil fuels. Transition happening.

2/ Solar + wind cheaper than coal in 90% of markets. This isn't virtue—it's economics. Cheaper energy wins.

3/ Renewable costs dropped 90% in decade. Imagine every tech followed this. That's revolution.

4/ Battery storage now cost-effective. Solves intermittency problem.

5/ Offshore wind and green hydrogen are next frontiers. $50B+ each. Early movers will win.

Renewable transition is here. Are you leading or following?

#RenewableEnergy #CleanEnergy #SustainableInvesting"""

    def _renewable_article(self, tone: str, length: str) -> str:
        return """Renewable Energy: How $495B Investment Transforms Global Power Markets

Executive Overview
Renewable energy sector reached milestone. With $495 billion annual investment—surpassing fossil fuels first time—renewables no longer niche trend.

The Economics of Renewable Energy

Fundamental case is economic, not environmental:

Cost Competitiveness
Solar and wind costs declined 90% past decade. In 90% global markets, renewables offer lowest cost.

LCOE Comparison:
- Solar: $30-60/MWh
- Wind: $30-70/MWh
- Coal: $60-100/MWh

Energy Security
Renewable insulates from volatile energy prices. 20-year PPA locks stable costs.

Workforce Development
Renewables employ 12+ million globally—exceeding fossil fuel employment.

Investment Trends

1. Distributed Solar and Wind
Growing 25% annually. Organizations moving to energy independence.

2. Grid-Scale Storage
Battery costs down 90%. Now cost-competitive with gas.

3. Emerging Technologies
Green hydrogen and offshore wind = $100B+ opportunities.

Conclusion
Renewable investment reflects rational capital allocation.

#RenewableEnergy #CleanEnergy #ClimateFinance #SustainableInvesting"""

    # Net Zero Content
    def _net_zero_linkedin(self, tone: str, length: str) -> str:
        return """🎯 1,500+ Companies Committed to Net Zero—But Here's the Hard Truth

Net zero commitments everywhere. Over 4,000 companies have targets. Yet actual implementation remains exception.

Here's what separates winners from greenwashers:

The Net Zero Hierarchy:

1️⃣ Emission Reductions (Scope 1 & 2)
Reduce direct emissions 50% by 2030. Requires CAPEX, operational changes, cultural transformation.

2️⃣ Value Chain Reduction (Scope 3)
Address supply chain emissions—70-80% of total. Demands supplier engagement.

3️⃣ Residual Offsets
After genuine reductions, offset remaining through high-quality credits.

The Credibility Test:

✅ Backing targets with >$1B CAPEX
✅ Science-based targets from independent bodies
✅ Board compensation tied to milestones
✅ Transparent annual reporting

The Scorecard:

🏆 Leaders: Apple, Microsoft, Shell (massive CAPEX)
⚠️ Middlers: Mixed with some implementation
❌ Laggards: Targets without credible plans

Net zero no longer PR. Smart investors differentiating on credibility and pace.

For board and execs: "Net zero by 2050" without credible 2030 target unacceptable.

#NetZero #ClimateAction #SustainableBusiness #ESG #CorporateResponsibility"""

    def _net_zero_twitter(self, tone: str, length: str) -> str:
        return """1/ 4,000+ companies claim net-zero. 70% lack credible plans. Commitment ≠ credibility.

2/ Net-zero hierarchy matters:
1. Reduce Scope 1&2 by 50% by 2030
2. Address Scope 3
3. Offset residuals

Skip this order = greenwashing.

3/ Credibility test: >$1B capital deployment? If not, just marketing.

4/ Science-based targets from independent bodies separate leaders from laggards.

5/ Investors pricing net-zero credibility. Weak plans face capital reallocation.

Net zero is real or greenwash. No middle ground.

#NetZero #SustainableBusiness #ClimateAction"""

    def _net_zero_article(self, tone: str, length: str) -> str:
        return """Net Zero Commitments: From Promise to Performance

Executive Summary
While 4,000+ companies announced net-zero targets, implementation remains exception. This explores credible strategies from greenwashing, and financial implications.

The Net Zero Commitment Landscape

Explosion reflects diverse motivations:
- Regulatory Pressure
- Investor Demand
- Competitive Positioning
- Talent Attraction

Yet gap between commitment and implementation remains wide.

The Net Zero Hierarchy

Level 1: Direct Emissions Reduction
Reduce operational emissions 50% by 2030. Requires capital investment, technology, operational transformation.

Level 2: Value Chain Reduction
Address supply chain and customer-use emissions. 70-80% of total footprint. Demands supplier engagement, market transformation.

Level 3: Residual Offsets
After genuine reductions, offset remaining through verified projects.

Credibility Indicators

1. Capital Commitment
>$1B CAPEX toward net-zero.

2. Science-Based Targets
Validated by SBTi or equivalent.

3. Executive Accountability
Compensation tied to milestones.

4. Transparent Reporting
Annual progress with third-party verification.

Conclusion
Net zero maturing from PR to performance metric.

#NetZero #SustainableBusiness #ClimateFinance"""

    # Climate Risk Content
    def _climate_risk_linkedin(self, tone: str, length: str) -> str:
        return """⚠️ Climate Risk Just Became a $23 Trillion Financial Question

Bank regulators sounding alarms. Institutional investors demanding disclosure. Question no longer "Is climate risk material?" but "How much exposure?"

The Climate Risk Reality Check:

📊 $23 Trillion in Financial Assets at Risk
IMF estimates climate risks exceed $23 trillion by 2100. But impacts arriving faster.

🌍 Physical Risk Material NOW
2023 record insurance losses:
• Pakistan floods: $30B+ losses
• Moroccan earthquakes + European heatwaves: Billions insured
• Cascading supply chain disruptions costing billions

🔄 Transition Risk Repricing Assets
Coal, oil, gas face permanent stranding. Renewable, green tech command premiums.

The Investor Imperative:

Smart investors doing three things:

1️⃣ Climate Scenario Modeling
Stress-testing against 1.5°C, 2.0°C, 3.0°C scenarios. Reveals hidden exposures.

2️⃣ Supply Chain Mapping
Identifying geographic and sector concentrations exposed to physical risks.

3️⃣ Transition Planning Assessment
Evaluating company management of low-carbon shift.

The Regulatory Shift:

SEC Climate Disclosure Rules require material risks disclosed
TCFD Framework standardizes reporting
Central banks stress-testing for climate
EU Taxonomy forces reallocation

For Portfolio Managers: Climate risk isn't CSR. It's fiduciary duty.

For CFOs: Insurance costs, supply chain resilience depend on climate management.

Are you pricing climate risk?

#ClimateRisk #FinancialRisk #RiskManagement #ESG #InvestorResponsibility"""

    def _climate_risk_twitter(self, tone: str, length: str) -> str:
        return """1/ $23 TRILLION in financial assets at climate risk. Not theoretical—priced into markets TODAY.

2/ Physical climate risk arriving faster than models predicted. 2023 record insurance losses. Real capital loss.

3/ Transition risk repricing NOW. Coal stranding. Oil/gas permanent demand destruction. Winners/losers clear.

4/ Smart investors stress-testing 1.5°C scenarios. Unprepared will be caught off-guard.

5/ Regulators awake. SEC, ECB demand climate disclosure and stress testing. Compliance non-negotiable.

Climate risk is investment megatrend of 2020s. Ahead or behind?

#ClimateRisk #InvestorResponsibility #FinancialRisk"""

    def _climate_risk_article(self, tone: str, length: str) -> str:
        return """Climate Risk: The $23 Trillion Financial Imperative

Executive Summary
Climate risk transitioned from environmental concern to material financial. With $23 trillion at stake and regulatory scrutiny intensifying, institutional investors and corporations can't treat as optional.

The Three Pillars of Climate Risk

Physical Risk
Direct damage from climate events:
- Flooding, hurricanes destroying infrastructure
- Agricultural disruption from droughts
- Coastal real estate stranding
- Supply chain disruption

Transition Risk
Asset repricing as economy shifts:
- Oil and coal face permanent demand destruction
- Incumbents lose market share
- Carbon-intensive industries face regulatory pressure
- Consumer preference shifts

Systemic Risk
Cascading financial system impacts:
- Credit defaults from climate damage
- Insurance market disruption
- Financial contagion
- Currency and commodity volatility

The Financial Impact Scale

$23 trillion by end century. But impacts accelerating:

2000-2020: $50-100B annual insurance losses
2021-2023: Pakistan $30B, record heatwaves, agricultural losses
2024-2030: Acceleration expected

Investor Risk Management Framework

Leading investors employ comprehensive management:

1. Scenario Analysis
Stress-test against IPCC scenarios

2. Transition Risk Assessment
Evaluate business model disruption exposure

3. Physical Risk Mapping
Identify assets and supply chains exposed

4. Engagement and Advocacy
Work with portfolio companies

Conclusion
Climate risk evolved from CSR to core financial risk.

#ClimateRisk #FinancialRisk #InvestorResponsibility #SustainableFinance"""

    def _add_hashtags(self, content: str, topic: str) -> str:
        """Add relevant hashtags to content."""
        hashtags_map = {
            "carbon_markets": "#CarbonMarkets #EmissionsTrading #ClimateAction #ESG #NetZero",
            "esg_investing": "#ESG #SustainableInvesting #ImpactInvesting #FinanceOfTheFuture #GreenFinance",
            "green_bonds": "#GreenBonds #SustainableFinance #ClimateAction #FixedIncome #ESG",
            "renewable_energy": "#RenewableEnergy #CleanEnergy #SolarPower #WindEnergy #Sustainability",
            "net_zero": "#NetZero #Decarbonization #ClimateGoals #SustainableBusiness #CorporateAction",
            "climate_risk": "#ClimateRisk #FinancialRisk #InvestorResponsibility #ESG #RiskManagement"
        }
        
        hashtags = hashtags_map.get(topic, "#ClimateFinance #Sustainability #ImpactInvesting")
        return f"{content}\n\n{hashtags}"

    def _default_content(self, topic: str, format: str, tone: str) -> str:
        """Generate default content when specific template not found."""
        return f"""Climate Finance Insight: {topic.replace('_', ' ').title()}

This is an important topic in sustainable finance and climate action.

Key areas to explore:
- Market trends and developments
- Investment opportunities and risks
- Policy and regulatory landscape
- Corporate and institutional adoption
- Future outlook and emerging innovations

#ClimateFinance #Sustainability"""

    def get_available_topics(self) -> List[str]:
        """Get list of available topics."""
        return list(self.climate_topics.keys())

    def validate_content(self, content: str) -> bool:
        """Validate generated content quality."""
        checks = [
            len(content.strip()) > 50,
            len(content.split()) > 15,
            any(char.isupper() for char in content)
        ]
        return all(checks)
