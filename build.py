#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hyperclear Consulting — site build script.

WHY THIS EXISTS
Every page is assembled here from one shared header, one shared footer,
and one shared stylesheet (assets/css/style.css). To make a sitewide
change (add a nav item, change footer contact info, tweak a color),
edit it ONCE in this file or the CSS, then re-run:

    python3 build.py

...and every page regenerates consistently. Don't hand-edit the
generated .html files directly — edits will be lost next run, and
pages will drift out of sync with each other.

TO ADD NEW CONTENT LATER (a new case study, article, news item):
Scroll to the relevant PAGE CONTENT section below, add an entry
following the existing pattern, and re-run this script.
"""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------
# MAINTENANCE MODE
# Set to True to publish a simple "check back soon" holding page on
# every URL instead of the real site (useful while placeholder
# content is still being filled in). Set back to False and re-run
# to publish the full real site again. Nothing else needs to change.
# ------------------------------------------------------------------
MAINTENANCE_MODE = False

NAV_ITEMS = [
    ("about.html", "About / Leadership"),
    ("services.html", "Services"),
    ("case-studies.html", "Case Studies"),
    ("news-insights.html", "News & Insights"),
    ("contact.html", "Contact"),
]

# ------------------------------------------------------------------
# SHARED HEADER / FOOTER
# ------------------------------------------------------------------

def header(active_file):
    links = []
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active_file else ''
        links.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
    links_html = "\n          ".join(links)
    return f"""
  <header class="site-header">
    <div class="container">
      <a href="index.html"><img class="logo" src="assets/img/logo.png" alt="Hyperclear Consulting"></a>
      <button class="nav-toggle" aria-label="Menu" onclick="document.querySelector('.nav-links').classList.toggle('open')">&#9776;</button>
      <ul class="nav-links">
          {links_html}
      </ul>
    </div>
  </header>
"""

INSTAGRAM_ICON = """<svg viewBox="0 0 24 24" width="42" height="42" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="24" height="24" rx="5" fill="#A7A8AA"/><path d="M12 8.2a3.8 3.8 0 1 0 0 7.6 3.8 3.8 0 0 0 0-7.6Zm0 6.27a2.47 2.47 0 1 1 0-4.94 2.47 2.47 0 0 1 0 4.94Z" fill="#fff"/><circle cx="16.1" cy="7.9" r="0.9" fill="#fff"/><path d="M16.7 4H7.3A3.3 3.3 0 0 0 4 7.3v9.4A3.3 3.3 0 0 0 7.3 20h9.4a3.3 3.3 0 0 0 3.3-3.3V7.3A3.3 3.3 0 0 0 16.7 4Zm2 12.7a2 2 0 0 1-2 2H7.3a2 2 0 0 1-2-2V7.3a2 2 0 0 1 2-2h9.4a2 2 0 0 1 2 2v9.4Z" fill="#fff"/></svg>"""

LINKEDIN_ICON = """<svg viewBox="0 0 24 24" width="42" height="42" xmlns="http://www.w3.org/2000/svg"><rect width="24" height="24" rx="5" fill="#A7A8AA"/><svg x="5" y="5.5" width="14" height="13" viewBox="0 0 448 512"><path fill="#fff" d="M100.28 448H7.4V148.9h92.88zm-46.44-338.7C24.09 109.3 0 85.15 0 54.55a54.55 54.55 0 0 1 109.1 0c0 30.6-24.1 54.75-54.83 54.75zM447.9 448h-92.68V302.4c0-34.7-.7-79.3-48.29-79.3-48.29 0-55.7 37.7-55.7 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.7-48.3 87.9-48.3 94 0 111.28 61.9 111.28 142.3V448z"/></svg></svg>"""


def footer():
    return f"""
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <h4>Hyperclear Consulting</h4>
          <p>Fractional CMO leadership in marketing strategy, crisis communications, and digital growth.</p>
        </div>
        <div>
          <h4>Contact</h4>
          <p><a href="mailto:owen@hyperclearconsulting.com">owen@hyperclearconsulting.com</a><br>
          <a href="tel:2156800155">215.680.0155</a></p>
        </div>
        <div>
          <h4>Connect</h4>
          <div class="social-links">
            <a href="https://www.linkedin.com/company/11852988" target="_blank" rel="noopener" aria-label="Hyperclear Consulting on LinkedIn">{LINKEDIN_ICON}</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        &copy; 2026 Hyperclear Consulting. All rights reserved.
      </div>
    </div>
  </footer>
"""


def maintenance_header():
    return """
  <header class="site-header">
    <div class="container" style="justify-content:center;">
      <img class="logo" src="assets/img/logo.png" alt="Hyperclear Consulting">
    </div>
  </header>
"""

HOLDING_BODY = """
  <section class="hero section-white text-center" style="padding:120px 0;">
    <div class="container">
      <div class="eyebrow" style="justify-content:center;display:flex;">Hyperclear Consulting</div>
      <h1>We're Putting the Finishing Touches on Something Great.</h1>
      <p class="lede" style="margin:0 auto;">Our new site is almost ready. In the meantime, reach out directly &mdash; we'd love to talk about your marketing, communications, or crisis planning needs.</p>
      <p style="margin-top:28px;">
        <a class="btn" href="mailto:owen@hyperclearconsulting.com">owen@hyperclearconsulting.com</a>
      </p>
      <p style="margin-top:10px;color:var(--color-grey-section);">215.680.0155 &nbsp;&middot;&nbsp; <a href="https://www.linkedin.com/in/owenmmurphy" target="_blank" rel="noopener">linkedin.com/in/owenmmurphy</a></p>
    </div>
  </section>
"""


def page(title, description, active_file, body_html):
    if MAINTENANCE_MODE:
        head_html = maintenance_header()
        content_html = HOLDING_BODY
    else:
        head_html = header(active_file)
        content_html = body_html
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Hyperclear Consulting</title>
<meta name="description" content="{description}">
<meta name="robots" content="{'noindex, nofollow' if MAINTENANCE_MODE else 'index, follow'}">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{head_html}
{content_html}
{footer()}
</body>
</html>
"""

# ------------------------------------------------------------------
# PAGE CONTENT
# ------------------------------------------------------------------

INDUSTRIES = [
    "Healthcare", "Wellness", "Fitness", "Staffing",
    "Legal", "Concierge Medicine", "Commercial Real Estate", "Real Estate Lending & Investing",
    "Consumer Products", "Retail", "Insurance", "Pharma & Pharma Consulting",
    "Professional Services", "SaaS", "Executive Leadership Coaching", "Non-Profits",
]

def industries_grid():
    tiles = "\n        ".join(f'<div class="tile">{i}</div>' for i in INDUSTRIES)
    return f'<div class="tile-grid">\n        {tiles}\n      </div>'


# ---- HOME ----------------------------------------------------------
home_body = f"""
  <section class="hero section-white">
    <div class="container">
      <div class="eyebrow">Marketing Strategy &ndash; Crisis Communication &ndash; fCMO Support</div>
      <h1>Marketing leadership, without the full-time overhead.</h1>
      <p class="lede">Hyperclear Consulting gives growing companies senior marketing strategy, crisis-ready communications, and hands-on execution — scaled to exactly what the engagement needs.</p>
      <a class="btn" href="contact.html">Start a Conversation</a>
    </div>
  </section>

  <section class="section section-grey">
    <div class="container text-center">
      <h2>Established 2018</h2>
      <p style="max-width:760px;margin:0 auto;">Hyperclear Consulting offers fractional Chief Marketing Officer support for B2B and B2C companies across pharmaceuticals, healthcare, staffing, commercial real estate, leadership development, and more — including marketing strategy, crisis planning and management, media training, value proposition development, branding, digital marketing, content development, public relations, and thought leadership.</p>
    </div>
  </section>

  <section class="section section-white">
    <div class="container">
      <h2>Where Hyperclear Helps</h2>
      <div class="card-grid">
        <div class="card">
          <span class="card-eyebrow">Crisis-Ready</span>
          <h3>Crisis Planning &amp; Communication</h3>
          <p>Preparation, messaging, and media response built before you need it — not scrambled together during it.</p>
        </div>
        <div class="card">
          <span class="card-eyebrow">Growth</span>
          <h3>Digital Marketing</h3>
          <p>Email, organic and paid social strategy that's built to convert, not just publish.</p>
        </div>
        <div class="card">
          <span class="card-eyebrow">Modernize</span>
          <h3>AI Adoption in Marketing</h3>
          <p>Practical integration of AI into marketing processes and tooling — without losing the brand's voice.</p>
        </div>
      </div>
      <p style="margin-top:28px;"><a href="services.html">See the full fCMO Services page &rarr;</a></p>
    </div>
  </section>

  <section class="section section-white" style="padding-top:0;">
    <div class="container">
      <h2>Industries Served</h2>
      {industries_grid()}
    </div>
  </section>
"""

# ---- ABOUT / LEADERSHIP --------------------------------------------
about_body = f"""
  <section class="section section-white">
    <div class="container">
      <div class="eyebrow" style="font-family:var(--font-heading);color:var(--color-grey-section);text-transform:uppercase;letter-spacing:.08em;font-size:.85rem;font-weight:700;margin-bottom:14px;">About &amp; Leadership</div>
      <div class="bio-block">
        <img class="headshot" src="assets/img/owen-headshot.jpg" alt="Owen Murphy, Founder &amp; CEO, Hyperclear Consulting">
        <div>
          <h1>Owen Murphy</h1>
          <p style="font-family:var(--font-heading);font-weight:700;color:var(--color-grey-section);margin-top:-8px;">Founder &amp; CEO, Hyperclear Consulting</p>

          <p>The firm is led by Owen Murphy, a 25-year marketing veteran whose career began in public relations agencies, building thought leadership programs, media outreach, and crisis planning for clients. That grounding in messaging that drives action still shapes the practice today.</p>

          <p>Often engaged as a fractional CMO, Owen is brought in when leadership suspects competitors are pulling ahead or when a marketing department has stalled — bringing an outside assessment of the martech stack, personnel, and channel mix, followed by a specific plan across paid and organic social, email, content, and AI-informed marketing automation. His approach draws on experience building and leading marketing departments at organizations ranging from early-stage startups to $400M-revenue, high-growth companies.</p>

          <p>Crisis readiness runs through all of it: the plans, message frameworks, media training, and spokesperson preparation get built in advance, well ahead of day one of an actual crisis — the same instinct for control and message discipline rooted in Owen's PR agency background. Whether the mandate is stalled growth, underperforming campaigns, or a live reputational threat, engagements come without the red tape of a permanent seat.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-grey">
    <div class="container">
      <h2>Not a Solo Operation</h2>
      <p style="max-width:760px;">Engagements don't stop at strategy. Depending on the size and scope of the work, Owen brings in a vetted team spanning graphic design, content and collateral development, and full-scale brand development — so a fractional engagement can flex from a single strategic workstream up to a complete company rebrand, without the client needing to source and manage separate vendors.</p>
      <p><a class="btn btn-outline" href="assets/downloads/Top-3-Scenarios-to-Hire-a-fCMO.pdf" target="_blank">Read: The 3 Scenarios for Hiring a fCMO</a></p>
    </div>
  </section>

  <section class="section section-white">
    <div class="container">
      <h2>Industries Served</h2>
      {industries_grid()}
    </div>
  </section>
"""

# ---- SERVICES (two-column: fCMO / Crisis Comms & PR) -----------------
FCMO_ASSESSMENT_ITEMS = [
    "Business goals alignment — is marketing focused on the right priorities and driving measurable impact on company objectives?",
    "Market and competitive landscape — what are the market dynamics, trends, and competitors doing, and how should we respond?",
    "Audience and personas — do we have a clear understanding of our target audiences, their needs, pain points, motivations, and decision drivers?",
    "Messaging and value proposition — is our core messaging compelling, differentiated, and resonating with the audiences that matter most?",
    "Brand strategy and positioning — is our brand distinct, relevant, and consistently expressed across all touchpoints?",
    "Go-to-market strategy — is the path to market clear, differentiated, and aligned with how buyers want to buy?",
    "Marketing strategy and annual plan — is there a clear, prioritized roadmap with the right mix of initiatives to drive growth?",
    "Demand generation and pipeline — are we consistently generating the right leads and advancing quality pipeline?",
    "Content strategy and assets — do we have the right content, for the right audiences, in the right formats, at the right stages?",
    "Channel strategy and mix — are we investing in the most effective channels to reach and convert our audiences?",
    "Customer journey and experience — is the end-to-end experience seamless, relevant, and built to convert and retain?",
    "Martech stack review — are the right tools in place, underused, or redundant?",
    "Data and analytics — are we tracking the right metrics, leveraging data for insights, and making decisions based on facts?",
    "Marketing performance and reporting — are we measuring what matters and clearly showing impact on business outcomes?",
    "Personnel and job roles — is the team structured to succeed, or set up to struggle?",
    "Vendor usage — is work being outsourced that doesn’t need to be, or is an in-house team stretched too thin without enough vendor support?",
    "Budget and resource allocation — is the budget aligned to priorities and being invested for maximum impact?",
    "Sales and marketing alignment — are we working together toward shared goals with clear handoffs and feedback loops?",
    "Customer and market feedback — are we listening to customers and the market to inform strategy and continuous improvement?",
]

CRISIS_ITEMS = [
    "Executive thought leadership — programs engineered from the ground up to establish executives as credible voices in their industries and generate meaningful media coverage",
    "Media relations and earned media — identifying the right stories, reporters and opportunities to generate coverage that supports business and reputation objectives",
    "Executive media training — preparing executives at every level to communicate clearly and effectively, including high-risk, hostile and adversarial interview scenarios",
    "Crisis communication planning — playbooks built in advance so leadership has a defined, rehearsed plan the moment a challenge arises — not a scramble to build one",
    "Crisis response and counsel — helping leadership assess the situation, determine what to say, when to say it and who needs to hear it as events unfold",
    "Issues and risk assessment — identifying reputational vulnerabilities, emerging issues and scenarios that could create communications risk before they become crises",
    "Crisis messaging — developing holding statements, talking points, FAQs, executive remarks and stakeholder communications that are clear, credible and defensible",
    "Executive spokesperson preparation — preparing leaders to handle media scrutiny, difficult questions and rapidly changing situations while staying on message without sounding scripted",
    "Internal crisis communications — helping employees understand what is happening, what the organization is doing about it and what they should — and should not — communicate externally",
    "Stakeholder communications — developing tailored communications for customers, employees, partners, investors, regulators, media and other audiences affected by an issue",
    "Reputation management — assessing how the organization is perceived and developing communications strategies to strengthen credibility, trust and authority",
    "Post-crisis recovery — helping organizations move beyond the immediate response, address lingering reputation issues, and rebuild confidence with key audiences",
]

def _bullets(items):
    lis = "\n          ".join(f"<li>{item}</li>" for item in items)
    return f"<ul>\n          {lis}\n        </ul>"

services_body = f"""
  <section class="section section-white">
    <div class="container">
      <h1>Services</h1>
      <p class="lede">Hyperclear Consulting works with clients in two ways: as a fractional CMO leading marketing strategy and execution, and as a crisis communications and public relations partner advancing, protecting, and building reputation. Some engagements draw on one. Many draw on both.</p>

      <div class="services-columns">
        <div class="service-column">
          <h2>Fractional CMO Services</h2>
          <p>Every engagement starts the same way: by understanding where things actually stand before recommending where they should go.</p>

          <h3><span class="step-num">1.</span> Assessment</h3>
          <p>A clear-eyed evaluation of the current marketing function — what's working, what isn't, and what's missing entirely. This includes:</p>
          {_bullets(FCMO_ASSESSMENT_ITEMS)}

          <h3><span class="step-num">2.</span> Recommendations</h3>
          <p>Findings translate into a specific set of strategies and tactics built for the business's actual situation — not a generic playbook.</p>

          <h3><span class="step-num">3.</span> Implementation</h3>
          <p>Execution starts with quick wins to build early momentum, followed by longer-term initiatives designed for sustained yield.</p>

          <h3><span class="step-num">4.</span> Measurement</h3>
          <p>KPIs are agreed upon upfront and tracked on an ongoing basis, so there's a clear, shared view of whether the right things are happening — and whether they're producing the expected results.</p>
        </div>

        <div class="service-column">
          <h2>Crisis Communications &amp; Public Relations</h2>
          <p>Reputation is built long before a crisis happens. And when a crisis does happen, the quality and speed of the response can have a lasting impact. Our PR and communications work spans both — building visibility and credibility when things are going well, while preparing leadership to respond when they aren't.</p>
          {_bullets(CRISIS_ITEMS)}
        </div>
      </div>

      <p class="text-center" style="margin-top:48px;"><a class="btn" href="contact.html">Talk Through Your Scope</a></p>
    </div>
  </section>
"""

# ---- CASE STUDIES -----------------------------------------------------
# To add a new case study later: append one entry here (same shape) and
# re-run this script. Its index card and detail page are both generated
# automatically — nothing else to touch.
CASE_STUDIES = [
    {
        "slug": "starbucks",
        "client": "Lauren Wimmer, Wimmer Criminal Defense",
        "industry": "Crisis Communications & Media Strategy",
        "headline": "Crisis Communications: Pressure Campaign Against Starbucks",
        "teaser": "After a Starbucks barista had two Black men wrongfully arrested at a Philadelphia location, Owen drove the media pressure campaign that led Starbucks to close 8,000+ stores for racial-bias training.",
        "timeframe": "April 2018",
        "situation": "A Starbucks barista called the police on two young Black men sitting at the Rittenhouse Square, Philadelphia location while they waited for a business contact to arrive for a meeting. When the police arrived, they removed and arrested the two men — who committed no crime — drawing immediate outrage. Attorney Lauren Wimmer, providing pro bono counsel to the two men arrested, enlisted Owen Murphy to drive a coordinated pressure campaign against Starbucks for its unjustified actions and secure national media coverage.",
        "strategy": [
            ("Media Representation", "Represented Attorney Wimmer, positioning her as the authoritative voice for national media."),
            ("Pressure Campaign", "Engineered a sustained pressure campaign highlighting the poor handling of the situation and targeted Starbucks' reputational consequences."),
            ("Media Training", "Media-trained Wimmer and constructed key messages for high-stakes national interviews."),
            ("National Placement", "Secured interviews with national outlets including NBC Nightly News with Lester Holt."),
        ],
        "stat_number": "8,000+",
        "stat_label": "U.S. store closures for racial-bias training",
        "result": "Forced to act, Starbucks — for the first time in company history — closed more than 8,000 U.S. locations to conduct racial-bias education. Beyond extensive national news coverage, Wimmer experienced a significant increase in awareness, web traffic, and criminal defense inquiries.",
    },
    {
        "slug": "binswanger",
        "client": "Binswanger",
        "industry": "Commercial Real Estate",
        "headline": "Marketing Transformation at Binswanger",
        "teaser": "An 85-year-old commercial real estate firm needed a structural overhaul — modernized brand, rebuilt CRM workflows, and scalable broker enablement tools.",
        "timeframe": "Multi-Year Engagement",
        "situation": "Binswanger, an 85-year-old commercial real estate firm with multiple service lines and markets, had strong industry credibility but an underperforming marketing function and brand in need of a refresh. Leadership needed a structured overhaul to modernize the brand, improve processes, develop client-facing materials, and build a scalable infrastructure.",
        "strategy": [
            ("Full-Scale Assessment", "Conducted a comprehensive audit of branding, CRM usage, reporting, and broker enablement across all markets."),
            ("Brand Modernization", "Refreshed visual identity and client-facing materials to reflect the firm's institutional credibility."),
            ("CRM Transformation", "Rebuilt CRM usage and reporting workflows to improve pipeline visibility and accountability."),
            ("Broker Enablement", "Developed scalable tools and resources to empower brokers with consistent, compelling presentation materials."),
        ],
        "stat_number": "35%",
        "stat_label": "Improvement in presentation-to-new-business conversion",
        "result": "Hyperclear's multi-year transformation initiative reduced deal-close timelines by 30%, improved presentation-to-new-business conversion rates by 35%, and established scalable marketing infrastructure across all service lines.",
    },
    {
        "slug": "coebra",
        "client": "COEBRA",
        "industry": "AI-Powered SaaS Platform",
        "headline": "AI SaaS GTM Launch for COEBRA",
        "teaser": "A first-to-market AI SaaS platform for healthcare value-based contracts needed a go-to-market strategy that could turn a complex product into enterprise demand from day one.",
        "timeframe": None,
        "situation": "COEBRA was a first-to-market AI-powered SaaS platform designed to manage the wealth of data necessary to manage value-based contracts for high-price drugs and therapies in healthcare. The launch required education-driven market adoption and needed a go-to-market strategy that could translate a complex, novel product into clear enterprise value and generate qualified demand from day one.",
        "strategy": [
            ("GTM Strategy", "Developed the full go-to-market strategy, positioning, and competitive differentiation framework for the platform."),
            ("Positioning & Messaging", "Built thought leadership campaigns to educate the market and establish COEBRA's authority in the AI SaaS space for value-based contracts."),
            ("Demand Generation", "Designed and launched demand generation workflows to convert awareness into qualified pipeline."),
            ("Enterprise Sales Support", "Supported enterprise sales motion, resulting in demos and landing Magellan Rx Management as a client."),
        ],
        "stat_number": "400+",
        "stat_label": "Enterprise demos produced during launch campaign",
        "result": "Hyperclear's GTM launch generated hundreds of qualified leads, produced dozens of enterprise demos, and helped secure Magellan Rx Management as a marquee client — validating the product's market fit.",
    },
    {
        "slug": "coeus",
        "client": "COEUS",
        "industry": "Pharma Consulting (100+ person firm)",
        "headline": "Brand Consolidation & Rebrand for COEUS",
        "teaser": "A pharmaceutical consulting firm operating as five fragmented business units needed one unified brand and digital presence.",
        "timeframe": "3-Year Engagement",
        "situation": "COEUS, a pharmaceutical consulting firm specializing in market access, operated through five fragmented business units with separate branding and digital identities. The disconnected presence created market confusion, diluted authority, and prevented the organization from projecting a unified value proposition to clients and partners.",
        "strategy": [
            ("Brand Unification", "Consolidated five separate business unit identities into one cohesive COEUS brand architecture."),
            ("Centralized Messaging", "Developed unified messaging framework and communications standards across all business lines."),
            ("Website & Digital", "Built a centralized website and digital presence to replace fragmented unit-level properties."),
            ("Market Positioning", "Repositioned COEUS in the market, eliminating confusion and building a recognizable institutional identity."),
        ],
        "stat_number": "$4M",
        "stat_label": "In marketing-attributed business generated",
        "result": "The rebrand more than doubled COEUS' LinkedIn following, generated $4M in marketing-attributed business, and eliminated the market confusion that had been suppressing growth across all five business units.",
    },
    {
        "slug": "globalfit",
        "client": "GlobalFit",
        "industry": "Corporate Fitness & Wellness",
        "headline": "Funnel Optimization for GlobalFit",
        "teaser": "High-intent members were abandoning at the final stage of the application process — a revenue leak more ad spend couldn't fix.",
        "timeframe": "Conversion Initiative",
        "situation": "GlobalFit experienced significant conversion drop-off late in the membership application process. High-intent users were abandoning at the final stage — creating a revenue leak that couldn't be solved by increasing ad spend or driving more top-of-funnel traffic.",
        "strategy": [
            ("Funnel Audit", "Identified the specific late-stage drop-off points and friction factors causing qualified applicants to abandon."),
            ("Disclosure Redesign", "Redesigned disclosure language and presentation to improve clarity, reduce anxiety, and increase trust."),
            ("Transparency Strategy", "Improved transparency throughout the application flow to align user expectations with the actual experience."),
            ("Implementation", "Deployed optimized flows and validated improvements through conversion tracking and incremental revenue measurement."),
        ],
        "stat_number": "24%",
        "stat_label": "Increase in application completions post-optimization",
        "result": "Hyperclear's funnel redesign increased application completions by 24%, generated substantial incremental revenue, and improved conversion efficiency — all without increasing ad spend or top-of-funnel volume.",
    },
    {
        "slug": "multifamily-leasing",
        "client": "Real Estate Developer",
        "industry": "Multifamily Development",
        "headline": "Multifamily Pre-Leasing Strategy",
        "teaser": "A redeveloped apartment building needed a distinctive identity and a full pre-leasing strategy to drive lease-up velocity before opening.",
        "timeframe": "4-Month Engagement",
        "situation": "A real estate developer required a complete pre-leasing and branding strategy for a redeveloped apartment building. The property needed a distinctive identity that would stand out in a competitive market and drive lease-up velocity before the building opened.",
        "strategy": [
            ("Brand Identity", "Developed the full property brand identity, blending art deco influences with modern industrial design aesthetics."),
            ("Website & Digital", "Built the property website and digital presence optimized for pre-leasing inquiries and prospect capture."),
            ("Social Media Strategy", "Launched social media presence with consistent visual storytelling to build anticipation and community."),
            ("Marketing Channels", "Created cohesive storytelling across all marketing channels to position the development competitively."),
        ],
        "stat_number": "100%",
        "stat_label": "Brand and digital presence delivered before opening",
        "result": "Hyperclear delivered a cohesive property brand, website, and social media presence that positioned the development competitively within the market and created consistent storytelling across all pre-leasing channels.",
    },
    {
        "slug": "source4teachers",
        "client": "Source4Teachers",
        "industry": "K-12 Workforce Solutions",
        "headline": "Workforce Acquisition Growth for Source4Teachers",
        "teaser": "A substitute-teacher staffing marketplace needed to grow applicant volume and client acquisition on both sides of a two-sided marketplace.",
        "timeframe": "Multi-Phase Engagement",
        "situation": "Source4Teachers needed to grow substitute teacher recruitment and improve workforce engagement. The company's existing marketing function wasn't generating enough applicant volume or client growth to meet expansion targets — and the brand wasn't connecting with either audience.",
        "strategy": [
            ("Marketing Rebuild", "Rebuilt the marketing function from the ground up with updated positioning, messaging, and channel strategy."),
            ("Recruitment Campaigns", "Designed and launched integrated recruitment campaigns targeting substitute teacher applicants across key markets."),
            ("Retention Strategy", "Implemented workforce engagement and retention strategies and incentives to improve substitute satisfaction and reduce churn."),
            ("Client Acquisition", "Drove client acquisition growth through positioning and outreach aligned with school district decision-makers."),
        ],
        "stat_number": "400%",
        "stat_label": "Increase in substitute teacher applicants",
        "result": "Hyperclear's marketing rebuild increased client acquisition by 150%, drove a 400% increase in substitute teacher applicants, and significantly improved substitute workforce engagement — transforming both sides of the two-sided marketplace.",
    },
]


def case_study_slug_file(cs):
    return f"case-study-{cs['slug']}.html"


def case_study_card(cs):
    return f"""<div class="card">
          <span class="card-eyebrow">{cs['industry']}</span>
          <h3>{cs['headline']}</h3>
          <p>{cs['teaser']}</p>
          <a class="btn" href="{case_study_slug_file(cs)}">Read Case Study</a>
        </div>"""


def case_study_detail_body(cs):
    strategy_html = "\n        ".join(
        f'<div class="strategy-item"><h4>{title}</h4><p>{desc}</p></div>'
        for title, desc in cs["strategy"]
    )
    timeframe_html = f'<p class="card-eyebrow" style="margin-top:6px;">{cs["timeframe"]}</p>' if cs.get("timeframe") else ""
    return f"""
  <section class="section section-white">
    <div class="container">
      <p><a href="case-studies.html">&larr; Back to Case Studies</a></p>
      <span class="card-eyebrow">{cs['client']} &middot; {cs['industry']}</span>
      <h1>{cs['headline']}</h1>
      {timeframe_html}

      <h3 style="margin-top:36px;">The Situation</h3>
      <p>{cs['situation']}</p>

      <h3 style="margin-top:32px;">The Strategy</h3>
      <div class="strategy-grid">
        {strategy_html}
      </div>

      <div class="stat-callout">
        <div class="stat-number">{cs['stat_number']}</div>
        <div class="stat-label">{cs['stat_label']}</div>
      </div>

      <h3>The Result</h3>
      <p>{cs['result']}</p>
    </div>
  </section>
"""


# ---- CASE STUDIES (index) --------------------------------------------
_case_study_cards = "\n        ".join(case_study_card(cs) for cs in CASE_STUDIES)
case_studies_body = f"""
  <section class="section section-white">
    <div class="container">
      <h1>Case Studies</h1>
      <p class="lede">Each engagement is different. Here's how that plays out in practice.</p>

      <div class="case-grid">
        {_case_study_cards}
      </div>
    </div>
  </section>
"""

# ---- NEWS & INSIGHTS ----------------------------------------------------
news_insights_body = """
  <section class="section section-white">
    <div class="container">
      <h1>News &amp; Insights</h1>
      <p class="lede">Articles, downloads, and press coverage on fractional marketing leadership, crisis communications, and modern brand strategy.</p>

      <h2 style="margin-top:48px;">Insights</h2>
      <div class="card-grid">
        <div class="card">
          <h3>5 LinkedIn Myths Quietly Costing You Reach</h3>
          <p>What most companies assume about their LinkedIn company page — and what's actually true in 2026. Covers algorithm reach, posting frequency, personal vs. company page performance, link penalties, and the real reach decline since 2024.</p>
          <a class="btn" href="assets/downloads/LinkedIn-Myths-OnePager.pdf" target="_blank">Download PDF</a>
        </div>
        <div class="card">
          <h3>The 3 Scenarios for Hiring a Fractional CMO</h3>
          <p>Early-stage companies needing a marketing roadmap, teams with a sudden leadership gap, and companies that have plateaued — the three situations where a fCMO delivers the most value, by Owen Murphy.</p>
          <a class="btn" href="assets/downloads/Top-3-Scenarios-to-Hire-a-fCMO.pdf" target="_blank">Download PDF</a>
        </div>
      </div>

      <h2 style="margin-top:56px;">News</h2>
      <div class="card">
        <span class="card-eyebrow">The Philadelphia Inquirer &middot; April 2024</span>
        <h3>How Small Businesses Benefit from Partnering with 'Fractional' Executives</h3>
        <p>Gene Marks' piece on the rise of fractional sales and marketing executives features Owen on how fCMOs drive strategy over task execution, why industry-specific experience matters less than being "battle-tested," and how technology recommendations factor into the role.</p>
        <blockquote class="pull-quote">"They're doing what you think are all the right things, but they don't seem to be generating the results that they hoped for. A fractional CMO, for example, will help with rebranding and redefining their value proposition. They can bring in all types of approaches and a holistic view." &mdash; Owen Murphy</blockquote>
        <blockquote class="pull-quote">"Companies will get the most value when they realize that it's an opportunity to impact change in their entire organization outside of just marketing." &mdash; Owen Murphy</blockquote>
        <p style="font-size:0.85rem;color:var(--color-grey-section);">Full article is behind The Inquirer's subscription paywall.</p>
        <a class="btn" href="https://www.inquirer.com/business/small-business/marketing-sales-revenue-executives-small-business-advantage-contracts-20240402.html" target="_blank" rel="noopener">Read on Inquirer.com</a>
      </div>
    </div>
  </section>
"""

# ---- CONTACT --------------------------------------------------------------
contact_body = """
  <section class="section section-white">
    <div class="container">
      <h1>Let's Talk</h1>
      <p class="lede">If your marketing team needs direction, your brand needs a refresh, or you need someone ready to handle a crisis before it happens — that's the conversation to have.</p>
      <div class="contact-grid">
        <div class="card">
          <h3>Email</h3>
          <p><a href="mailto:owen@hyperclearconsulting.com">owen@hyperclearconsulting.com</a></p>
        </div>
        <div class="card">
          <h3>Phone</h3>
          <p><a href="tel:2156800155">215.680.0155</a></p>
        </div>
        <div class="card">
          <h3>LinkedIn</h3>
          <p><a href="https://www.linkedin.com/in/owenmmurphy" target="_blank" rel="noopener">linkedin.com/in/owenmmurphy</a></p>
        </div>
      </div>
    </div>
  </section>
"""

# ------------------------------------------------------------------
# WRITE PAGES
# ------------------------------------------------------------------

PAGES = [
    ("index.html", "Home", "Fractional CMO marketing and crisis communications leadership.", "index.html", home_body),
    ("about.html", "About & Leadership", "Meet Owen Murphy and the Hyperclear Consulting team.", "about.html", about_body),
    ("services.html", "Services", "Fractional CMO leadership and crisis communications & public relations services.", "services.html", services_body),
    ("case-studies.html", "Case Studies", "Hyperclear Consulting case studies.", "case-studies.html", case_studies_body),
    ("news-insights.html", "News & Insights", "Articles, downloads, and press coverage from Hyperclear Consulting.", "news-insights.html", news_insights_body),
    ("contact.html", "Contact", "Get in touch with Hyperclear Consulting.", "contact.html", contact_body),
]

# One page per case study, generated from CASE_STUDIES above — add a new
# case study by adding a dict to that list, not by adding a line here.
for _cs in CASE_STUDIES:
    PAGES.append((
        case_study_slug_file(_cs),
        f"Case Study: {_cs['client']}",
        f"{_cs['headline']} — a Hyperclear Consulting case study.",
        "case-studies.html",
        case_study_detail_body(_cs),
    ))

for filename, title, desc, active, body in PAGES:
    out_path = os.path.join(ROOT, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page(title, desc, active, body))
    print(f"wrote {filename}")

print("\nBuild complete.")
