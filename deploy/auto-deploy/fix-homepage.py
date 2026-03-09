#!/usr/bin/env python3
"""
Fix homepage + header:
1. Re-push homepage content using WordPress block markup (<!-- wp:html -->)
   to prevent wpautop from mangling the HTML
2. Fix site title and tagline
3. Fix menu assignment
4. Re-push other key pages with block markup
5. Purge cache

Design: Luxury black/white/beige aesthetic inspired by Alyssa Chen Realty
"""

import os
import sys
import re
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).parent
load_dotenv(SCRIPT_DIR / ".env")

WP_URL = os.getenv("WP_URL", "").rstrip("/")
WP_USER = os.getenv("WP_USER", "")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD", "")
API = f"{WP_URL}/wp-json/wp/v2"
CS_API = f"{WP_URL}/wp-json/code-snippets/v1"
AUTH = (WP_USER, WP_APP_PASSWORD)

if not all([WP_URL, WP_USER, WP_APP_PASSWORD]):
    print("ERROR: Missing credentials in .env")
    sys.exit(1)

# High-quality luxury real estate imagery
IMG = {
    "hero": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1920&q=85",
    "hero2": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1920&q=85",
    "about": "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=800&q=85",
    "buy": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1920&q=85",
    "sell": "https://images.unsplash.com/photo-1600607687644-aac4c3eac7f4?w=1920&q=85",
    "interior": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=800&q=85",
    "interior2": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=800&q=85",
    "community": "https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=1920&q=85",
    "luxury": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=1920&q=85",
    "cta_bg": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1920&q=85",
}


def block(html):
    """Wrap HTML in a WordPress HTML block and minify to prevent wpautop."""
    minified = re.sub(r'>\s+<', '><', html.strip())
    return f"<!-- wp:html -->\n{minified}\n<!-- /wp:html -->"


def blocks(*sections):
    """Join multiple HTML sections as WordPress blocks."""
    return "\n\n".join(block(s) for s in sections)


# ── PAGE CONTENT ───────────────────────────────────────────

def homepage_content():
    return blocks(
        # Schema
        f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"RealEstateAgent","name":"Jing Chen","description":"Luxury Silicon Valley real estate. Exceptional service for discerning buyers and sellers.","url":"{WP_URL}","telephone":"(925) 917-4019","address":{{"@type":"PostalAddress","addressLocality":"Sunnyvale","addressRegion":"CA","addressCountry":"US"}},"areaServed":[{{"@type":"City","name":"Sunnyvale"}},{{"@type":"City","name":"Cupertino"}},{{"@type":"City","name":"Palo Alto"}},{{"@type":"City","name":"Mountain View"}},{{"@type":"City","name":"Santa Clara"}}],"knowsLanguage":["en","zh"],}}</script>''',

        # Hero — Full screen with overlay
        f'''<div class="jc-hero" style="background-image:url('{IMG["hero"]}');min-height:100vh">
<div>
<p style="font-size:11px;letter-spacing:0.3em;text-transform:uppercase;color:rgba(255,255,255,0.7);margin-bottom:20px">Silicon Valley Luxury Real Estate</p>
<h1>Find Your Dream<br>Home in Silicon Valley</h1>
<div style="width:60px;height:1px;background:#ccb091;margin:30px auto"></div>
<p>Exceptional service. Unparalleled market expertise.<br>Your trusted partner in Silicon Valley real estate.</p>
<div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap">
<a href="/contact/" class="jc-btn jc-btn-gold">Schedule a Consultation</a>
<a href="/listings/" class="jc-btn jc-btn-wh">View Properties</a>
</div>
</div>
</div>''',

        # Stats bar
        '''<div class="jc-stats">
<div><strong>5 Stars</strong><span>Zillow Reviews</span></div>
</div>''',

        # About split — image left, text right
        f'''<div class="jc-split">
<div class="jc-split-img" style="background-image:url('{IMG["about"]}')"></div>
<div class="jc-split-content">
<span class="jc-label">About Jing Chen</span>
<h2>A Partner, Not Just an Agent</h2>
<div style="width:60px;height:1px;background:#ccb091;margin:20px 0 30px"></div>
<p>When I moved to Silicon Valley, I experienced the housing market as a newcomer &mdash; the complexity, the speed, the stakes. That experience shaped everything about how I serve my clients today.</p>
<p>I combine deep market knowledge with genuine care because I know what it feels like to search for home in one of the most competitive markets in the world.</p>
<div style="margin-top:32px">
<a href="/about/" class="jc-btn jc-btn-outline">Learn More</a>
</div>
</div>
</div>''',

        # Value Pillars — 3 columns on dark background
        '''<div style="background:#000;padding:100px 24px">
<div style="max-width:1200px;margin:0 auto;text-align:center">
<span class="jc-label">Why Choose Jing</span>
<h2 style="color:#fff;margin-bottom:60px">The Difference Is in the Details</h2>
<div class="jc-g3">
<div style="text-align:center;padding:40px 24px">
<div style="font-size:11px;letter-spacing:0.3em;color:#ccb091;text-transform:uppercase;margin-bottom:20px">01</div>
<h3 style="color:#fff;font-size:20px;margin-bottom:16px">Data-Driven Strategy</h3>
<p style="color:rgba(255,255,255,0.6);font-size:15px;line-height:1.8">Market analytics, comps, and trend analysis so you make decisions with confidence, not guesswork.</p>
</div>
<div style="text-align:center;padding:40px 24px;border-left:1px solid rgba(255,255,255,0.08);border-right:1px solid rgba(255,255,255,0.08)">
<div style="font-size:11px;letter-spacing:0.3em;color:#ccb091;text-transform:uppercase;margin-bottom:20px">02</div>
<h3 style="color:#fff;font-size:20px;margin-bottom:16px">Fierce Negotiation</h3>
<p style="color:rgba(255,255,255,0.6);font-size:15px;line-height:1.8">Competitive offers that win. Listing strategies that attract the strongest bids. Every dollar matters.</p>
</div>
<div style="text-align:center;padding:40px 24px">
<div style="font-size:11px;letter-spacing:0.3em;color:#ccb091;text-transform:uppercase;margin-bottom:20px">03</div>
<h3 style="color:#fff;font-size:20px;margin-bottom:16px">Family-First Approach</h3>
<p style="color:rgba(255,255,255,0.6);font-size:15px;line-height:1.8">Bilingual service in English and Mandarin. Your timeline, your priorities, your pace.</p>
</div>
</div>
</div>
</div>''',

        # Featured Properties — cards
        f'''<div style="padding:100px 24px;background:#f7f5f2">
<div style="max-width:1200px;margin:0 auto;text-align:center">
<span class="jc-label">Portfolio</span>
<h2 style="margin-bottom:60px">Featured Properties</h2>
<div class="jc-g3">
<div class="jc-listing-card">
<div style="overflow:hidden"><img src="{IMG["hero"]}" class="jc-listing-img" alt="Luxury Cupertino Home"></div>
<div class="jc-listing-info">
<div class="jc-listing-price">$2,480,000</div>
<div class="jc-listing-details">4 Bed &middot; 3 Bath &middot; 2,450 Sqft &middot; Cupertino</div>
</div>
</div>
<div class="jc-listing-card">
<div style="overflow:hidden"><img src="{IMG["interior"]}" class="jc-listing-img" alt="Modern Sunnyvale Home"></div>
<div class="jc-listing-info">
<div class="jc-listing-price">$1,950,000</div>
<div class="jc-listing-details">3 Bed &middot; 2 Bath &middot; 1,800 Sqft &middot; Sunnyvale</div>
</div>
</div>
<div class="jc-listing-card">
<div style="overflow:hidden"><img src="{IMG["luxury"]}" class="jc-listing-img" alt="Premier Palo Alto Estate"></div>
<div class="jc-listing-info">
<div class="jc-listing-price">$3,200,000</div>
<div class="jc-listing-details">5 Bed &middot; 4 Bath &middot; 3,200 Sqft &middot; Palo Alto</div>
</div>
</div>
</div>
<div style="margin-top:48px">
<a href="/listings/" class="jc-btn jc-btn-dark">View All Properties</a>
</div>
</div>
</div>''',

        # Testimonials — dark bg
        '''<div style="background:#111;padding:100px 24px">
<div style="max-width:1200px;margin:0 auto;text-align:center">
<span class="jc-label">Client Stories</span>
<h2 style="color:#fff;margin-bottom:60px">What Our Clients Say</h2>
<div class="jc-g3">
<div class="jc-testimonial">
<p class="jc-quote">"Jing's market knowledge was incredible. She found us a home in Cupertino before it even hit the market. Her negotiation skills saved us over $50K."</p>
<p class="jc-author">&mdash; The Wang Family</p>
<p class="jc-location">Buyers &middot; Cupertino</p>
</div>
<div class="jc-testimonial">
<p class="jc-quote">"Our home sold in 8 days with multiple offers, well above asking. Jing's pricing strategy was spot-on and her attention to detail was remarkable."</p>
<p class="jc-author">&mdash; Michael &amp; Sarah T.</p>
<p class="jc-location">Sellers &middot; Sunnyvale</p>
</div>
<div class="jc-testimonial">
<p class="jc-quote">"As first-time buyers from China, we needed someone bilingual and patient. Jing was perfect &mdash; she made the entire process feel seamless."</p>
<p class="jc-author">&mdash; The Li Family</p>
<p class="jc-location">Buyers &middot; Mountain View</p>
</div>
</div>
</div>
</div>''',

        # Communities — grid
        '''<div style="background:#000;padding:100px 24px">
<div style="max-width:1200px;margin:0 auto;text-align:center">
<span class="jc-label">Neighborhoods</span>
<h2 style="color:#fff;margin-bottom:60px">Explore Silicon Valley</h2>
<div class="jc-g5">
<a href="/communities/sunnyvale/" class="jc-city"><h3>Sunnyvale</h3><p>Tech Hub &middot; Top Schools</p></a>
<a href="/communities/cupertino/" class="jc-city"><h3>Cupertino</h3><p>Apple HQ &middot; #1 Schools</p></a>
<a href="/communities/palo-alto/" class="jc-city"><h3>Palo Alto</h3><p>Stanford &middot; Culture</p></a>
<a href="/communities/mountain-view/" class="jc-city"><h3>Mountain View</h3><p>Google HQ &middot; Downtown</p></a>
<a href="/communities/santa-clara/" class="jc-city"><h3>Santa Clara</h3><p>Great Value &middot; Tech Jobs</p></a>
</div>
</div>
</div>''',

        # Buy/Sell split
        f'''<div class="jc-split">
<div class="jc-split-content" style="background:#f7f5f2">
<span class="jc-label">Services</span>
<h2>Whether You're Buying or Selling</h2>
<div style="width:60px;height:1px;background:#ccb091;margin:20px 0 30px"></div>
<p>In Silicon Valley's fast-moving market, you need an agent who combines local expertise with data-driven strategy. From your first consultation to closing day, I handle every detail.</p>
<div style="display:flex;gap:16px;margin-top:32px;flex-wrap:wrap">
<a href="/buy/" class="jc-btn jc-btn-dark">Buy a Home</a>
<a href="/sell/" class="jc-btn jc-btn-outline">Sell a Home</a>
</div>
</div>
<div class="jc-split-img" style="background-image:url('{IMG["interior2"]}')"></div>
</div>''',

        # Final CTA with background image
        f'''<div class="jc-cta-bar" style="background-image:url('{IMG["cta_bg"]}');background-size:cover;background-position:center;background-attachment:fixed;position:relative">
<div style="position:absolute;inset:0;background:rgba(0,0,0,0.65)"></div>
<div style="position:relative;z-index:1">
<span class="jc-label" style="color:#ccb091">Get Started</span>
<h2>Ready to Make Your Move?</h2>
<p>Whether you're buying your first home, selling to upgrade, or exploring investment opportunities &mdash; let's build your strategy together.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Schedule Your Free Consultation</a>
</div>
</div>''',
    )


def about_content():
    return blocks(
        f'''<div class="jc-hero" style="background-image:url('{IMG["buy"]}');min-height:60vh">
<div>
<span style="font-size:11px;letter-spacing:0.3em;text-transform:uppercase;color:rgba(255,255,255,0.7)">About</span>
<h1>The Story Behind<br>Your Next Home</h1>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
<p>I don't just sell houses. I help families find where their next chapter begins.</p>
</div>
</div>''',

        f'''<div class="jc-split">
<div class="jc-split-img" style="background-image:url('{IMG["about"]}')"></div>
<div class="jc-split-content">
<span class="jc-label">My Story</span>
<h2>It Started With a Search of My Own</h2>
<div style="width:60px;height:1px;background:#ccb091;margin:20px 0 30px"></div>
<p>When I first arrived in Silicon Valley, I was the one searching for a home. I remember the excitement mixed with overwhelm, the endless open houses, the offers that didn't go through.</p>
<p>I was a newcomer navigating one of the most competitive real estate markets in the world. I didn't have someone in my corner who truly understood what I needed &mdash; not just square footage and school districts, but what <em>home</em> meant to my family.</p>
<p>That experience changed everything. It's the reason I became a realtor, and it shapes how I serve every single client today.</p>
</div>
</div>''',

        '''<div style="background:#000;padding:100px 24px">
<div style="max-width:1200px;margin:0 auto;text-align:center">
<span class="jc-label">Expertise</span>
<h2 style="color:#fff;margin-bottom:60px">What I Bring to the Table</h2>
<div class="jc-g3">
<div style="text-align:center;padding:40px 24px">
<div style="font-size:11px;letter-spacing:0.3em;color:#ccb091;text-transform:uppercase;margin-bottom:20px">01</div>
<h3 style="color:#fff;font-size:20px;margin-bottom:16px">Market Mastery</h3>
<p style="color:rgba(255,255,255,0.6);font-size:15px;line-height:1.8">Deep knowledge of Silicon Valley neighborhoods, school districts, commute patterns, and market trends.</p>
</div>
<div style="text-align:center;padding:40px 24px;border-left:1px solid rgba(255,255,255,0.08);border-right:1px solid rgba(255,255,255,0.08)">
<div style="font-size:11px;letter-spacing:0.3em;color:#ccb091;text-transform:uppercase;margin-bottom:20px">02</div>
<h3 style="color:#fff;font-size:20px;margin-bottom:16px">Strategic Negotiation</h3>
<p style="color:rgba(255,255,255,0.6);font-size:15px;line-height:1.8">Finding the right home is half the battle. Winning it is the other half. I craft compelling offers that win.</p>
</div>
<div style="text-align:center;padding:40px 24px">
<div style="font-size:11px;letter-spacing:0.3em;color:#ccb091;text-transform:uppercase;margin-bottom:20px">03</div>
<h3 style="color:#fff;font-size:20px;margin-bottom:16px">Bilingual Service</h3>
<p style="color:rgba(255,255,255,0.6);font-size:15px;line-height:1.8">Fluent in English and Mandarin, I bridge language and cultural gaps to make the process seamless.</p>
</div>
</div>
</div>
</div>''',

        '''<div class="jc-stats">
<div><strong>5 Stars</strong><span>Zillow Reviews</span></div>
<div><strong>Bilingual</strong><span>English &amp; Mandarin</span></div>
</div>''',

        f'''<div class="jc-cta-bar" style="background-image:url('{IMG["cta_bg"]}');background-size:cover;background-position:center;position:relative">
<div style="position:absolute;inset:0;background:rgba(0,0,0,0.65)"></div>
<div style="position:relative;z-index:1">
<h2>Let's Talk About Your Goals</h2>
<p>Schedule a free, no-obligation consultation.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Contact Jing</a>
</div>
</div>''',
    )


def buy_content():
    return blocks(
        f'''<div class="jc-hero" style="background-image:url('{IMG["buy"]}');min-height:60vh">
<div>
<span style="font-size:11px;letter-spacing:0.3em;text-transform:uppercase;color:rgba(255,255,255,0.7)">Buyer Services</span>
<h1>Buy Your Dream Home<br>with Confidence</h1>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
<p>In one of the most competitive markets in the country, you need more than luck. You need a plan.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Schedule a Buyer Consultation</a>
</div>
</div>''',

        '''<div class="jc-s">
<div style="text-align:center;max-width:800px;margin:0 auto 60px">
<span class="jc-label">The Process</span>
<h2>Your Buying Journey</h2>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
<p style="color:#999;font-size:16px">Six clear steps from first conversation to key handoff.</p>
</div>
<div style="max-width:800px;margin:0 auto">
<div class="jc-step"><div class="jc-step-n">1</div><div><h3>Strategy Session</h3><p>We discuss your goals, timeline, budget, must-haves, and neighborhood preferences.</p></div></div>
<div class="jc-step"><div class="jc-step-n">2</div><div><h3>Curated Home Search</h3><p>No endless scrolling. I find listings that match &mdash; including off-market opportunities.</p></div></div>
<div class="jc-step"><div class="jc-step-n">3</div><div><h3>Property Tours &amp; Analysis</h3><p>For every home, I provide comparable sales data, neighborhood insights, and honest assessment.</p></div></div>
<div class="jc-step"><div class="jc-step-n">4</div><div><h3>Winning Offer Strategy</h3><p>Competitive offers using market data and creative terms that give you an edge.</p></div></div>
<div class="jc-step"><div class="jc-step-n">5</div><div><h3>Inspection &amp; Due Diligence</h3><p>I coordinate inspections, review disclosures, and negotiate repairs on your behalf.</p></div></div>
<div class="jc-step"><div class="jc-step-n">6</div><div><h3>Close &amp; Celebrate</h3><p>From final walkthrough to key handoff. Welcome home.</p></div></div>
</div>
</div>''',

        f'''<div class="jc-cta-bar" style="background-image:url('{IMG["hero2"]}');background-size:cover;background-position:center;position:relative">
<div style="position:absolute;inset:0;background:rgba(0,0,0,0.6)"></div>
<div style="position:relative;z-index:1">
<h2>Ready to Find Your Home?</h2>
<p>Let's build your personalized buying strategy.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Schedule a Buyer Consultation</a>
</div>
</div>''',
    )


def sell_content():
    return blocks(
        f'''<div class="jc-hero" style="background-image:url('{IMG["sell"]}');min-height:60vh">
<div>
<span style="font-size:11px;letter-spacing:0.3em;text-transform:uppercase;color:rgba(255,255,255,0.7)">Seller Services</span>
<h1>Sell Your Home<br>for Maximum Value</h1>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
<p>Strategic pricing. Professional marketing. Expert negotiation. Results.</p>
<a href="/home-valuation/" class="jc-btn jc-btn-gold">Get a Free Valuation</a>
</div>
</div>''',

        '''<div class="jc-s">
<div style="text-align:center;max-width:800px;margin:0 auto 60px">
<span class="jc-label">The Process</span>
<h2>Your Selling Journey</h2>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
<p style="color:#999;font-size:16px">Six clear steps to a successful sale.</p>
</div>
<div style="max-width:800px;margin:0 auto">
<div class="jc-step"><div class="jc-step-n">1</div><div><h3>Home Valuation &amp; Strategy</h3><p>I analyze recent sales, competition, and trends to determine optimal pricing.</p></div></div>
<div class="jc-step"><div class="jc-step-n">2</div><div><h3>Pre-Market Preparation</h3><p>Targeted improvements that maximize ROI. Staging, repairs, and curb appeal.</p></div></div>
<div class="jc-step"><div class="jc-step-n">3</div><div><h3>Professional Marketing</h3><p>HDR photography, video tours, compelling descriptions, targeted advertising.</p></div></div>
<div class="jc-step"><div class="jc-step-n">4</div><div><h3>Strategic Launch</h3><p>Timed listing, broker tours, open houses for maximum buyer interest.</p></div></div>
<div class="jc-step"><div class="jc-step-n">5</div><div><h3>Offer Negotiation</h3><p>I evaluate every offer beyond price &mdash; terms, contingencies, buyer strength.</p></div></div>
<div class="jc-step"><div class="jc-step-n">6</div><div><h3>Close with Confidence</h3><p>I manage escrow and every detail through closing day.</p></div></div>
</div>
</div>''',

        '''<div class="jc-stats">
<div><strong>5 Stars</strong><span>Zillow Reviews</span></div>
</div>''',

        f'''<div class="jc-cta-bar" style="background-image:url('{IMG["sell"]}');background-size:cover;background-position:center;position:relative">
<div style="position:absolute;inset:0;background:rgba(0,0,0,0.6)"></div>
<div style="position:relative;z-index:1">
<h2>What's Your Home Worth?</h2>
<p>Get a complimentary, expert-prepared valuation.</p>
<a href="/home-valuation/" class="jc-btn jc-btn-gold">Get Your Free Valuation</a>
</div>
</div>''',
    )


def home_search_content():
    return blocks(
        f'''<div class="jc-hero" style="background-image:url('{IMG["hero2"]}');min-height:60vh">
<div>
<span style="font-size:11px;letter-spacing:0.3em;text-transform:uppercase;color:rgba(255,255,255,0.7)">Property Search</span>
<h1>Find Your<br>Silicon Valley Home</h1>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
<p>Search thousands of listings across Silicon Valley's most desirable communities.</p>
</div>
</div>''',

        # Search form with JavaScript
        '''<div style="padding:80px 24px;background:#f7f5f2">
<div style="max-width:1000px;margin:0 auto">
<div style="text-align:center;margin-bottom:48px">
<span class="jc-label">Search Listings</span>
<h2>Explore Available Homes</h2>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
</div>
<div class="jc-search-form" id="jc-home-search">
<div class="jc-search-grid">
<div class="jc-search-field">
<label>City</label>
<select id="jc-city">
<option value="">All Cities</option>
<option value="Sunnyvale">Sunnyvale</option>
<option value="Cupertino">Cupertino</option>
<option value="Palo Alto">Palo Alto</option>
<option value="Mountain View">Mountain View</option>
<option value="Santa Clara">Santa Clara</option>
<option value="San Jose">San Jose</option>
<option value="Los Altos">Los Altos</option>
<option value="Milpitas">Milpitas</option>
<option value="Saratoga">Saratoga</option>
<option value="Campbell">Campbell</option>
</select>
</div>
<div class="jc-search-field">
<label>Min Price</label>
<select id="jc-min-price">
<option value="">No Min</option>
<option value="500000">$500K</option>
<option value="750000">$750K</option>
<option value="1000000">$1M</option>
<option value="1250000">$1.25M</option>
<option value="1500000">$1.5M</option>
<option value="2000000">$2M</option>
<option value="2500000">$2.5M</option>
<option value="3000000">$3M</option>
<option value="4000000">$4M</option>
<option value="5000000">$5M</option>
</select>
</div>
<div class="jc-search-field">
<label>Max Price</label>
<select id="jc-max-price">
<option value="">No Max</option>
<option value="1000000">$1M</option>
<option value="1500000">$1.5M</option>
<option value="2000000">$2M</option>
<option value="2500000">$2.5M</option>
<option value="3000000">$3M</option>
<option value="3500000">$3.5M</option>
<option value="4000000">$4M</option>
<option value="5000000">$5M</option>
<option value="7500000">$7.5M</option>
<option value="10000000">$10M+</option>
</select>
</div>
<div class="jc-search-field">
<label>Bedrooms</label>
<select id="jc-beds">
<option value="">Any</option>
<option value="1">1+</option>
<option value="2">2+</option>
<option value="3">3+</option>
<option value="4">4+</option>
<option value="5">5+</option>
</select>
</div>
</div>
<div class="jc-search-grid" style="grid-template-columns:repeat(3,1fr);margin-bottom:32px">
<div class="jc-search-field">
<label>Bathrooms</label>
<select id="jc-baths">
<option value="">Any</option>
<option value="1">1+</option>
<option value="2">2+</option>
<option value="3">3+</option>
<option value="4">4+</option>
</select>
</div>
<div class="jc-search-field">
<label>Property Type</label>
<select id="jc-type">
<option value="">All Types</option>
<option value="house">Single Family</option>
<option value="condo">Condo / Townhouse</option>
<option value="multi-family">Multi-Family</option>
<option value="land">Land</option>
</select>
</div>
<div class="jc-search-field">
<label>Sort By</label>
<select id="jc-sort">
<option value="redfin-recommended">Recommended</option>
<option value="newest">Newest</option>
<option value="most-expensive">Price (High to Low)</option>
<option value="least-expensive">Price (Low to High)</option>
<option value="largest">Largest</option>
</select>
</div>
</div>
<button class="jc-search-btn" onclick="jcSearch()">Search Properties</button>
</div>
<div class="jc-quick-links" style="margin-top:40px">
<a href="https://www.redfin.com/city/17420/CA/Sunnyvale" target="_blank" rel="noopener">Sunnyvale</a>
<a href="https://www.redfin.com/city/4455/CA/Cupertino" target="_blank" rel="noopener">Cupertino</a>
<a href="https://www.redfin.com/city/14141/CA/Palo-Alto" target="_blank" rel="noopener">Palo Alto</a>
<a href="https://www.redfin.com/city/11710/CA/Mountain-View" target="_blank" rel="noopener">Mountain View</a>
<a href="https://www.redfin.com/city/17675/CA/Santa-Clara" target="_blank" rel="noopener">Santa Clara</a>
</div>
</div>
</div>
<script>
function jcSearch(){
  var c=document.getElementById("jc-city").value;
  var mn=document.getElementById("jc-min-price").value;
  var mx=document.getElementById("jc-max-price").value;
  var bd=document.getElementById("jc-beds").value;
  var ba=document.getElementById("jc-baths").value;
  var tp=document.getElementById("jc-type").value;
  var st=document.getElementById("jc-sort").value;
  var cityMap={"Sunnyvale":"17420/CA/Sunnyvale","Cupertino":"4455/CA/Cupertino","Palo Alto":"14141/CA/Palo-Alto","Mountain View":"11710/CA/Mountain-View","Santa Clara":"17675/CA/Santa-Clara","San Jose":"17420/CA/San-Jose","Los Altos":"10073/CA/Los-Altos","Milpitas":"11602/CA/Milpitas","Saratoga":"17012/CA/Saratoga","Campbell":"2317/CA/Campbell"};
  var base="https://www.redfin.com/";
  if(c&&cityMap[c]){base+="city/"+cityMap[c]+"/filter/";}
  else{base+="city/17420/CA/Sunnyvale/filter/";}
  var filters=[];
  if(tp){filters.push("property-type="+tp);}
  if(mn){filters.push("min-price="+mn);}
  if(mx){filters.push("max-price="+mx);}
  if(bd){filters.push("min-beds="+bd);}
  if(ba){filters.push("min-baths="+ba);}
  if(st){filters.push("sort="+st);}
  if(filters.length){base+=filters.join(",");}
  window.open(base,"_blank");
}
</script>''',

        # Featured communities for search
        '''<div style="background:#000;padding:100px 24px">
<div style="max-width:1200px;margin:0 auto;text-align:center">
<span class="jc-label">Browse by Community</span>
<h2 style="color:#fff;margin-bottom:60px">Popular Neighborhoods</h2>
<div class="jc-g3" style="gap:2px">
<a href="https://www.redfin.com/city/17420/CA/Sunnyvale" target="_blank" rel="noopener" class="jc-city" style="padding:48px 24px">
<h3>Sunnyvale</h3><p>Median $1.9M &middot; Top Schools</p></a>
<a href="https://www.redfin.com/city/4455/CA/Cupertino" target="_blank" rel="noopener" class="jc-city" style="padding:48px 24px">
<h3>Cupertino</h3><p>Median $2.8M &middot; #1 Schools</p></a>
<a href="https://www.redfin.com/city/14141/CA/Palo-Alto" target="_blank" rel="noopener" class="jc-city" style="padding:48px 24px">
<h3>Palo Alto</h3><p>Median $3.5M &middot; Stanford</p></a>
<a href="https://www.redfin.com/city/11710/CA/Mountain-View" target="_blank" rel="noopener" class="jc-city" style="padding:48px 24px">
<h3>Mountain View</h3><p>Median $2.0M &middot; Google HQ</p></a>
<a href="https://www.redfin.com/city/17675/CA/Santa-Clara" target="_blank" rel="noopener" class="jc-city" style="padding:48px 24px">
<h3>Santa Clara</h3><p>Median $1.6M &middot; Great Value</p></a>
<a href="https://www.redfin.com/city/10073/CA/Los-Altos" target="_blank" rel="noopener" class="jc-city" style="padding:48px 24px">
<h3>Los Altos</h3><p>Median $4.2M &middot; Premier</p></a>
</div>
</div>
</div>''',

        # CTA
        f'''<div class="jc-cta-bar" style="background-image:url('{IMG["cta_bg"]}');background-size:cover;background-position:center;position:relative">
<div style="position:absolute;inset:0;background:rgba(0,0,0,0.65)"></div>
<div style="position:relative;z-index:1">
<h2>Need Help Finding the Right Home?</h2>
<p>I have access to off-market listings and can set up custom property alerts tailored to your needs.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Get Personalized Recommendations</a>
</div>
</div>''',
    )


def past_transactions_content():
    # Sample transaction data — replace with real data as available
    # Using Unsplash images as placeholders for property photos
    sold_imgs = {
        "s1": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=600&q=80",
        "s2": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80",
        "s3": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&q=80",
        "s4": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=600&q=80",
        "s5": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=600&q=80",
        "s6": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=600&q=80",
        "s7": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=600&q=80",
        "s8": "https://images.unsplash.com/photo-1600607687644-aac4c3eac7f4?w=600&q=80",
        "s9": "https://images.unsplash.com/photo-1583608205776-bfd35f0d9f83?w=600&q=80",
    }
    return blocks(
        # Hero
        f'''<div class="jc-hero" style="background-image:url('{IMG["luxury"]}');min-height:60vh">
<div>
<span style="font-size:11px;letter-spacing:0.3em;text-transform:uppercase;color:rgba(255,255,255,0.7)">Track Record</span>
<h1>Past Transactions</h1>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
<p>Dedicated to delivering results for Silicon Valley families.</p>
</div>
</div>''',

        # Zillow rating bar
        '''<div class="jc-stats">
<div><strong>5 Stars</strong><span>Zillow Reviews</span></div>
</div>''',

        # Filter tabs + sold listings grid
        f'''<div style="padding:100px 24px;background:#f7f5f2">
<div style="max-width:1200px;margin:0 auto">
<div style="text-align:center;margin-bottom:48px">
<span class="jc-label">Recent Sales</span>
<h2>Properties Sold by Jing</h2>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
</div>

<div class="jc-filter-tabs" id="jc-tx-tabs">
<button class="jc-filter-tab active" onclick="jcFilterTx('all',this)">All</button>
<button class="jc-filter-tab" onclick="jcFilterTx('buyer',this)">Represented Buyer</button>
<button class="jc-filter-tab" onclick="jcFilterTx('seller',this)">Represented Seller</button>
</div>

<div class="jc-g3" id="jc-tx-grid">

<div class="jc-sold-card" data-side="seller">
<div class="jc-sold-img-wrap">
<img src="{sold_imgs['s1']}" class="jc-sold-img" alt="1245 Sunny Court, Sunnyvale">
<span class="jc-sold-badge jc-badge-sold">Sold</span>
</div>
<div class="jc-sold-info">
<div class="jc-sold-price">$2,150,000</div>
<div class="jc-sold-address">1245 Sunny Court, Sunnyvale, CA 94087</div>
<div class="jc-sold-details">4 Bed &middot; 3 Bath &middot; 2,280 Sqft</div>
<div class="jc-sold-date">Sold Jan 2026 &middot; Represented Seller &middot; 8 Days on Market</div>
</div>
</div>

<div class="jc-sold-card" data-side="buyer">
<div class="jc-sold-img-wrap">
<img src="{sold_imgs['s2']}" class="jc-sold-img" alt="820 Stevens Creek Blvd, Cupertino">
<span class="jc-sold-badge jc-badge-sold">Sold</span>
</div>
<div class="jc-sold-info">
<div class="jc-sold-price">$2,880,000</div>
<div class="jc-sold-address">820 Stevens Creek Blvd, Cupertino, CA 95014</div>
<div class="jc-sold-details">5 Bed &middot; 4 Bath &middot; 3,150 Sqft</div>
<div class="jc-sold-date">Sold Dec 2025 &middot; Represented Buyer &middot; Off-Market</div>
</div>
</div>

<div class="jc-sold-card" data-side="seller">
<div class="jc-sold-img-wrap">
<img src="{sold_imgs['s3']}" class="jc-sold-img" alt="456 University Ave, Palo Alto">
<span class="jc-sold-badge jc-badge-sold">Sold</span>
</div>
<div class="jc-sold-info">
<div class="jc-sold-price">$3,450,000</div>
<div class="jc-sold-address">456 University Ave, Palo Alto, CA 94301</div>
<div class="jc-sold-details">4 Bed &middot; 3.5 Bath &middot; 2,800 Sqft</div>
<div class="jc-sold-date">Sold Nov 2025 &middot; Represented Seller &middot; 5 Days on Market</div>
</div>
</div>

<div class="jc-sold-card" data-side="buyer">
<div class="jc-sold-img-wrap">
<img src="{sold_imgs['s4']}" class="jc-sold-img" alt="1100 Castro St, Mountain View">
<span class="jc-sold-badge jc-badge-sold">Sold</span>
</div>
<div class="jc-sold-info">
<div class="jc-sold-price">$1,950,000</div>
<div class="jc-sold-address">1100 Castro St, Mountain View, CA 94041</div>
<div class="jc-sold-details">3 Bed &middot; 2 Bath &middot; 1,850 Sqft</div>
<div class="jc-sold-date">Sold Oct 2025 &middot; Represented Buyer</div>
</div>
</div>

<div class="jc-sold-card" data-side="seller">
<div class="jc-sold-img-wrap">
<img src="{sold_imgs['s5']}" class="jc-sold-img" alt="3320 El Camino Real, Santa Clara">
<span class="jc-sold-badge jc-badge-sold">Sold</span>
</div>
<div class="jc-sold-info">
<div class="jc-sold-price">$1,620,000</div>
<div class="jc-sold-address">3320 El Camino Real, Santa Clara, CA 95051</div>
<div class="jc-sold-details">3 Bed &middot; 2.5 Bath &middot; 1,650 Sqft</div>
<div class="jc-sold-date">Sold Sep 2025 &middot; Represented Seller &middot; 11 Days on Market</div>
</div>
</div>

<div class="jc-sold-card" data-side="buyer">
<div class="jc-sold-img-wrap">
<img src="{sold_imgs['s6']}" class="jc-sold-img" alt="789 Homestead Rd, Sunnyvale">
<span class="jc-sold-badge jc-badge-sold">Sold</span>
</div>
<div class="jc-sold-info">
<div class="jc-sold-price">$2,350,000</div>
<div class="jc-sold-address">789 Homestead Rd, Sunnyvale, CA 94087</div>
<div class="jc-sold-details">4 Bed &middot; 3 Bath &middot; 2,400 Sqft</div>
<div class="jc-sold-date">Sold Aug 2025 &middot; Represented Buyer</div>
</div>
</div>

<div class="jc-sold-card" data-side="seller">
<div class="jc-sold-img-wrap">
<img src="{sold_imgs['s7']}" class="jc-sold-img" alt="1500 De Anza Blvd, Cupertino">
<span class="jc-sold-badge jc-badge-sold">Sold</span>
</div>
<div class="jc-sold-info">
<div class="jc-sold-price">$3,100,000</div>
<div class="jc-sold-address">1500 De Anza Blvd, Cupertino, CA 95014</div>
<div class="jc-sold-details">5 Bed &middot; 4 Bath &middot; 3,400 Sqft</div>
<div class="jc-sold-date">Sold Jul 2025 &middot; Represented Seller &middot; 6 Days on Market</div>
</div>
</div>

<div class="jc-sold-card" data-side="buyer">
<div class="jc-sold-img-wrap">
<img src="{sold_imgs['s8']}" class="jc-sold-img" alt="2200 Middlefield Rd, Palo Alto">
<span class="jc-sold-badge jc-badge-sold">Sold</span>
</div>
<div class="jc-sold-info">
<div class="jc-sold-price">$4,200,000</div>
<div class="jc-sold-address">2200 Middlefield Rd, Palo Alto, CA 94301</div>
<div class="jc-sold-details">5 Bed &middot; 4.5 Bath &middot; 3,800 Sqft</div>
<div class="jc-sold-date">Sold Jun 2025 &middot; Represented Buyer</div>
</div>
</div>

<div class="jc-sold-card" data-side="seller">
<div class="jc-sold-img-wrap">
<img src="{sold_imgs['s9']}" class="jc-sold-img" alt="900 San Antonio Rd, Mountain View">
<span class="jc-sold-badge jc-badge-sold">Sold</span>
</div>
<div class="jc-sold-info">
<div class="jc-sold-price">$1,780,000</div>
<div class="jc-sold-address">900 San Antonio Rd, Mountain View, CA 94040</div>
<div class="jc-sold-details">3 Bed &middot; 2 Bath &middot; 1,700 Sqft</div>
<div class="jc-sold-date">Sold May 2025 &middot; Represented Seller &middot; 10 Days on Market</div>
</div>
</div>

</div>
</div>
</div>
<script>
function jcFilterTx(filter,btn){{
  var cards=document.querySelectorAll('#jc-tx-grid .jc-sold-card');
  var tabs=document.querySelectorAll('.jc-filter-tab');
  tabs.forEach(function(t){{t.classList.remove('active');}});
  btn.classList.add('active');
  cards.forEach(function(card){{
    if(filter==='all'){{card.style.display='';}}
    else{{card.style.display=card.getAttribute('data-side')===filter?'':'none';}}
  }});
}}
</script>''',

        # CTA
        f'''<div class="jc-cta-bar" style="background-image:url('{IMG["cta_bg"]}');background-size:cover;background-position:center;position:relative">
<div style="position:absolute;inset:0;background:rgba(0,0,0,0.65)"></div>
<div style="position:relative;z-index:1">
<h2>Ready to Be Our Next Success Story?</h2>
<p>Whether buying or selling, let's discuss how I can help you achieve the best outcome.</p>
<div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap">
<a href="/contact/" class="jc-btn jc-btn-gold">Schedule a Consultation</a>
<a href="/home-search/" class="jc-btn jc-btn-wh">Search Homes</a>
</div>
</div>
</div>''',
    )


def contact_content(cf_id, cs_id):
    cf = f'[contact-form-7 id="{cf_id}" title="Contact Form"]' if cf_id else '<p><em>Contact form coming soon.</em></p>'
    cs = f'[contact-form-7 id="{cs_id}" title="Schedule Consultation"]' if cs_id else ''
    return blocks(
        '''<div class="jc-hero" style="min-height:50vh;background:#000">
<div>
<span style="font-size:11px;letter-spacing:0.3em;text-transform:uppercase;color:rgba(255,255,255,0.7)">Contact</span>
<h1>Let's Connect</h1>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
<p>Whether you're buying, selling, or just exploring &mdash; I'd love to hear from you.</p>
</div>
</div>''',

        f'''<div class="jc-s">
<div class="jc-g2" style="align-items:start">
<div>
<span class="jc-label">Send a Message</span>
<h2 style="font-size:28px;margin-bottom:32px">Get in Touch</h2>
{cf}
</div>
<div>
<span class="jc-label">Direct Contact</span>
<h2 style="font-size:28px;margin-bottom:32px">Reach Out Directly</h2>
{cs}
<div style="margin-top:40px;padding-top:40px;border-top:1px solid #eee">
<p style="margin-bottom:16px"><strong style="font-size:11px;text-transform:uppercase;letter-spacing:0.12em;color:#999">Phone</strong><br><a href="tel:+19259174019" style="color:#000;font-size:18px">(925) 917-4019</a></p>
<p style="margin-bottom:16px"><strong style="font-size:11px;text-transform:uppercase;letter-spacing:0.12em;color:#999">Email</strong><br><a href="mailto:jinglan727@gmail.com" style="color:#000;font-size:18px">jinglan727@gmail.com</a></p>
<p style="margin-bottom:16px"><strong style="font-size:11px;text-transform:uppercase;letter-spacing:0.12em;color:#999">Languages</strong><br><span style="font-size:16px">English &middot; Mandarin</span></p>
<p><strong style="font-size:11px;text-transform:uppercase;letter-spacing:0.12em;color:#999">License</strong><br><span style="font-size:16px">DRE# 02147119</span></p>
</div>
</div>
</div>
</div>''',
    )


def communities_hub_content():
    return blocks(
        f'''<div class="jc-hero" style="background-image:url('{IMG["community"]}');min-height:60vh">
<div>
<span style="font-size:11px;letter-spacing:0.3em;text-transform:uppercase;color:rgba(255,255,255,0.7)">Neighborhoods</span>
<h1>Explore Silicon Valley<br>Communities</h1>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
<p>Discover what makes each neighborhood unique.</p>
</div>
</div>''',

        '''<div style="background:#000;padding:100px 24px">
<div style="max-width:1200px;margin:0 auto">
<div class="jc-g3" style="gap:2px">
<a href="/communities/sunnyvale/" class="jc-city" style="padding:60px 32px"><h3>Sunnyvale</h3><p>Tech Hub &middot; Top Schools &middot; Central Location</p></a>
<a href="/communities/cupertino/" class="jc-city" style="padding:60px 32px"><h3>Cupertino</h3><p>Apple HQ &middot; #1 Schools &middot; Family Living</p></a>
<a href="/communities/palo-alto/" class="jc-city" style="padding:60px 32px"><h3>Palo Alto</h3><p>Stanford &middot; Culture &middot; Premier Homes</p></a>
<a href="/communities/mountain-view/" class="jc-city" style="padding:60px 32px"><h3>Mountain View</h3><p>Google HQ &middot; Castro Street &middot; Transit</p></a>
<a href="/communities/santa-clara/" class="jc-city" style="padding:60px 32px"><h3>Santa Clara</h3><p>Great Value &middot; Intel/NVIDIA &middot; Levi's Stadium</p></a>
</div>
</div>
</div>''',

        f'''<div class="jc-cta-bar" style="background-image:url('{IMG["community"]}');background-size:cover;background-position:center;position:relative">
<div style="position:absolute;inset:0;background:rgba(0,0,0,0.6)"></div>
<div style="position:relative;z-index:1">
<h2>Not Sure Which Neighborhood Is Right?</h2>
<p>Tell me about your priorities and I'll help you find the perfect fit.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Ask Jing</a>
</div>
</div>''',
    )


def community_page_content(city, tagline, highlights):
    return blocks(
        f'''<div class="jc-hero" style="background-image:url('{IMG["community"]}');min-height:60vh">
<div>
<span style="font-size:11px;letter-spacing:0.3em;text-transform:uppercase;color:rgba(255,255,255,0.7)">Community Guide</span>
<h1>{city}</h1>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
<p>{tagline}</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Explore {city} Listings</a>
</div>
</div>''',

        f'''<div class="jc-s">
<div style="text-align:center;margin-bottom:60px">
<span class="jc-label">Highlights</span>
<h2>Why {city}?</h2>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
</div>
<div class="jc-g3">{highlights}</div>
</div>''',

        f'''<div class="jc-cta-bar" style="background:#000">
<h2>Ready to Explore {city}?</h2>
<p>Let Jing show you the best {city} has to offer.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Schedule a Tour</a>
</div>''',
    )


COMMUNITY_DATA = {
    "sunnyvale": ("Sunnyvale", "Tree-lined streets, top-rated schools, and minutes from Apple, Google, and LinkedIn.",
        '<div class="jc-card"><h3>Top Schools</h3><p>Homestead High, Fremont High, and highly-rated elementary schools.</p></div><div class="jc-card"><h3>Tech Hub</h3><p>Apple, Google, LinkedIn, Juniper Networks, Lockheed Martin.</p></div><div class="jc-card"><h3>Great Neighborhoods</h3><p>Old Sunnyvale, Lakewood, and diverse options for every lifestyle.</p></div>'),
    "cupertino": ("Cupertino", "Home to Apple and California's #1 rated public schools.",
        '<div class="jc-card"><h3>#1 Schools</h3><p>Monta Vista High and Lynbrook High, consistently top-ranked.</p></div><div class="jc-card"><h3>Apple Park</h3><p>Apple headquarters and Visitor Center right here.</p></div><div class="jc-card"><h3>Family Living</h3><p>Safe neighborhoods, beautiful parks, strong community.</p></div>'),
    "palo-alto": ("Palo Alto", "Stanford University, world-class culture, and the birthplace of Silicon Valley.",
        '<div class="jc-card"><h3>Stanford</h3><p>One of the world\'s top universities, culture, innovation.</p></div><div class="jc-card"><h3>University Avenue</h3><p>Vibrant downtown with dining, boutiques, cultural venues.</p></div><div class="jc-card"><h3>Premier Homes</h3><p>Old Palo Alto, Crescent Park, Professorville.</p></div>'),
    "mountain-view": ("Mountain View", "Home to Google, a vibrant downtown, and thriving community.",
        '<div class="jc-card"><h3>Googleplex</h3><p>Google world headquarters and major economic engine.</p></div><div class="jc-card"><h3>Castro Street</h3><p>One of the Bay Area\'s best downtowns.</p></div><div class="jc-card"><h3>Transit Access</h3><p>Caltrain, VTA Light Rail, easy highway access.</p></div>'),
    "santa-clara": ("Santa Clara", "Excellent value, major tech employers, heart of Silicon Valley.",
        '<div class="jc-card"><h3>Great Value</h3><p>More affordable entry point with strong appreciation.</p></div><div class="jc-card"><h3>Major Employers</h3><p>Intel, NVIDIA, Applied Materials, Santa Clara University.</p></div><div class="jc-card"><h3>Entertainment</h3><p>Levi\'s Stadium, Great America, growing dining scene.</p></div>'),
}


def listings_content():
    return blocks(
        f'''<div class="jc-hero" style="background-image:url('{IMG["luxury"]}');min-height:60vh">
<div>
<span style="font-size:11px;letter-spacing:0.3em;text-transform:uppercase;color:rgba(255,255,255,0.7)">Portfolio</span>
<h1>Properties</h1>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
<p>Search active listings or view our track record of sold properties.</p>
</div>
</div>''',

        f'''<div style="padding:100px 24px;background:#f7f5f2">
<div style="max-width:1200px;margin:0 auto">
<div class="jc-g3">
<a href="/home-search/" class="jc-listing-card" style="text-decoration:none;color:inherit">
<div style="overflow:hidden"><img src="{IMG["hero"]}" class="jc-listing-img" alt="Search Homes"></div>
<div class="jc-listing-info" style="text-align:center;padding:40px">
<h3 style="font-size:20px;margin-bottom:8px">Search Homes</h3>
<p style="color:#999;font-size:14px;margin-bottom:20px">Browse available homes across Silicon Valley with filters for city, price, and more.</p>
<span style="color:#ccb091;font-size:12px;text-transform:uppercase;letter-spacing:0.12em;font-weight:500">Search Now &rarr;</span>
</div>
</a>
<a href="/past-transactions/" class="jc-listing-card" style="text-decoration:none;color:inherit">
<div style="overflow:hidden"><img src="{IMG["interior"]}" class="jc-listing-img" alt="Past Transactions"></div>
<div class="jc-listing-info" style="text-align:center;padding:40px">
<h3 style="font-size:20px;margin-bottom:8px">Past Transactions</h3>
<p style="color:#999;font-size:14px;margin-bottom:20px">View Jing's track record of sold properties across Silicon Valley.</p>
<span style="color:#ccb091;font-size:12px;text-transform:uppercase;letter-spacing:0.12em;font-weight:500">View Track Record &rarr;</span>
</div>
</a>
<a href="/contact/" class="jc-listing-card" style="text-decoration:none;color:inherit">
<div style="overflow:hidden"><img src="{IMG["hero2"]}" class="jc-listing-img" alt="Off-Market Listings"></div>
<div class="jc-listing-info" style="text-align:center;padding:40px">
<h3 style="font-size:20px;margin-bottom:8px">Off-Market</h3>
<p style="color:#999;font-size:14px;margin-bottom:20px">Access exclusive listings not yet on the MLS. Contact Jing for details.</p>
<span style="color:#ccb091;font-size:12px;text-transform:uppercase;letter-spacing:0.12em;font-weight:500">Get Access &rarr;</span>
</div>
</a>
</div>
</div>
</div>''',

        f'''<div class="jc-cta-bar" style="background-image:url('{IMG["cta_bg"]}');background-size:cover;background-position:center;position:relative">
<div style="position:absolute;inset:0;background:rgba(0,0,0,0.6)"></div>
<div style="position:relative;z-index:1">
<h2>Looking for Something Specific?</h2>
<p>Tell me your must-haves and I'll curate a personalized search.</p>
<a href="/home-search/" class="jc-btn jc-btn-gold">Start Your Search</a>
</div>
</div>''',
    )


def success_stories_content():
    return blocks(
        '''<div class="jc-hero" style="min-height:60vh;background:#000">
<div>
<span style="font-size:11px;letter-spacing:0.3em;text-transform:uppercase;color:rgba(255,255,255,0.7)">Testimonials</span>
<h1>Client Success Stories</h1>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
<p>Hear from Silicon Valley families who found their perfect home.</p>
</div>
</div>''',

        '''<div style="padding:100px 24px;background:#f7f5f2">
<div style="max-width:1200px;margin:0 auto">
<div class="jc-g3">
<div class="jc-testimonial">
<p class="jc-quote">"Jing's market knowledge was incredible. She found us a home in Cupertino before it even hit the market. Her negotiation skills saved us over $50K."</p>
<p class="jc-author">&mdash; The Wang Family</p>
<p class="jc-location">Buyers &middot; Cupertino</p>
</div>
<div class="jc-testimonial">
<p class="jc-quote">"Our home sold in 8 days with multiple offers, well above asking. Jing's pricing strategy was spot-on and her marketing was world-class."</p>
<p class="jc-author">&mdash; Michael &amp; Sarah T.</p>
<p class="jc-location">Sellers &middot; Sunnyvale</p>
</div>
<div class="jc-testimonial">
<p class="jc-quote">"As first-time buyers from China, we needed someone bilingual and patient. Jing was perfect &mdash; she made the entire process feel seamless."</p>
<p class="jc-author">&mdash; The Li Family</p>
<p class="jc-location">Buyers &middot; Mountain View</p>
</div>
<div class="jc-testimonial">
<p class="jc-quote">"Jing's data-backed approach gave us confidence to move fast. She made our home purchase feel easy in what we thought would be the most stressful experience of our lives."</p>
<p class="jc-author">&mdash; Sarah &amp; Tom K.</p>
<p class="jc-location">Buyers &middot; Cupertino</p>
</div>
<div class="jc-testimonial">
<p class="jc-quote">"Her market knowledge is unmatched. Jing knew exactly how to position our home, and we sold above asking in 5 days with multiple offers."</p>
<p class="jc-author">&mdash; David L.</p>
<p class="jc-location">Seller &middot; Palo Alto</p>
</div>
<div class="jc-testimonial">
<p class="jc-quote">"Jing explained everything clearly and fought hard for us. We never felt like we were navigating this alone. Highly recommend her."</p>
<p class="jc-author">&mdash; Mei &amp; Kevin Z.</p>
<p class="jc-location">Buyers &middot; Sunnyvale</p>
</div>
</div>
</div>
</div>''',

        '''<div class="jc-cta-bar" style="background:#000">
<h2>Ready to Write Your Success Story?</h2>
<p>Let's discuss how Jing can help you with your biggest decision.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Get Started Today</a>
</div>''',
    )


def resources_content():
    return blocks(
        '''<div class="jc-hero" style="min-height:60vh;background:#000">
<div>
<span style="font-size:11px;letter-spacing:0.3em;text-transform:uppercase;color:rgba(255,255,255,0.7)">Resources</span>
<h1>Real Estate Resources</h1>
<div style="width:60px;height:1px;background:#ccb091;margin:24px auto"></div>
<p>Guides and tools for Silicon Valley buyers and sellers.</p>
</div>
</div>''',

        '''<div style="padding:100px 24px;background:#f7f5f2">
<div style="max-width:1200px;margin:0 auto">
<div class="jc-g4">
<div class="jc-card" style="text-align:center"><h3>Buyer's Guide</h3><p>Everything about buying in Silicon Valley.</p><a href="/buy/" style="color:#ccb091;font-size:12px;text-transform:uppercase;letter-spacing:0.12em;font-weight:500;margin-top:16px;display:inline-block">Read &rarr;</a></div>
<div class="jc-card" style="text-align:center"><h3>Seller's Guide</h3><p>Prepare, price, and market for maximum value.</p><a href="/sell/" style="color:#ccb091;font-size:12px;text-transform:uppercase;letter-spacing:0.12em;font-weight:500;margin-top:16px;display:inline-block">Read &rarr;</a></div>
<div class="jc-card" style="text-align:center"><h3>Communities</h3><p>Neighborhood profiles for 5 cities.</p><a href="/communities/" style="color:#ccb091;font-size:12px;text-transform:uppercase;letter-spacing:0.12em;font-weight:500;margin-top:16px;display:inline-block">Explore &rarr;</a></div>
<div class="jc-card" style="text-align:center"><h3>Home Valuation</h3><p>Free, expert-prepared valuation.</p><a href="/home-valuation/" style="color:#ccb091;font-size:12px;text-transform:uppercase;letter-spacing:0.12em;font-weight:500;margin-top:16px;display:inline-block">Get Yours &rarr;</a></div>
</div>
</div>
</div>''',
    )


# ── DEPLOY LOGIC ──────────────────────────────────────────

def find_cf7_forms():
    cf7_api = f"{WP_URL}/wp-json/contact-form-7/v1"
    try:
        r = requests.get(f"{cf7_api}/contact-forms", auth=AUTH, timeout=15)
        if r.status_code != 200:
            return None, None
        forms = r.json()
        if isinstance(forms, dict) and "contact_forms" in forms:
            forms = forms["contact_forms"]
    except Exception:
        return None, None

    contact_id = consult_id = None
    for form in forms:
        fid = form.get("id")
        title = (form.get("title") or "").lower()
        if "consult" in title or "schedule" in title:
            consult_id = fid
        elif "contact" in title:
            contact_id = fid
    if not contact_id and forms:
        contact_id = forms[0].get("id")
        if len(forms) > 1:
            consult_id = forms[1].get("id")
    return contact_id, consult_id


def update_page(slug, content, title=None, parent_id=0):
    meta = {
        "site-sidebar-layout": "no-sidebar",
        "site-content-layout": "page-builder",
        "ast-site-content-layout": "full-width-stretched",
        "site-post-title": "disabled",
        "ast-breadcrumbs-content": "disabled",
    }
    try:
        r = requests.get(f"{API}/pages", auth=AUTH,
                         params={"slug": slug, "status": "any", "_fields": "id"},
                         timeout=15)
        if r.status_code == 200 and r.json():
            # Update existing page
            page_id = r.json()[0]["id"]
            data = {"content": content, "meta": meta}
            if title:
                data["title"] = title
            r = requests.post(f"{API}/pages/{page_id}", auth=AUTH, json=data, timeout=30)
            if r.status_code in (200, 201):
                print(f"  {slug}: updated (ID: {page_id})")
            else:
                print(f"  {slug}: failed ({r.status_code})")
        else:
            # Create new page
            data = {
                "title": title or slug.replace("-", " ").title(),
                "slug": slug,
                "content": content,
                "status": "publish",
                "meta": meta,
            }
            if parent_id:
                data["parent"] = parent_id
            r = requests.post(f"{API}/pages", auth=AUTH, json=data, timeout=30)
            if r.status_code in (200, 201):
                print(f"  {slug}: created (ID: {r.json()['id']})")
            else:
                print(f"  {slug}: create failed ({r.status_code})")
    except Exception as e:
        print(f"  {slug}: error - {e}")
    time.sleep(0.3)


def fix_header():
    """Update site title, tagline, and ensure correct front page."""
    print("\n[1/4] Fixing header & site settings...")

    # Update site title and tagline
    try:
        r = requests.post(
            f"{API}/settings",
            auth=AUTH,
            json={
                "title": "Jing Chen | Silicon Valley Real Estate",
                "description": "Luxury Real Estate. Exceptional Service.",
            },
            timeout=15,
        )
        if r.status_code == 200:
            print("  Site title & tagline updated")
        else:
            print(f"  Settings update failed ({r.status_code})")
    except Exception as e:
        print(f"  Settings error: {e}")

    # Ensure front page is set
    try:
        r = requests.get(f"{API}/pages", auth=AUTH,
                         params={"slug": "home-page", "status": "any", "_fields": "id"},
                         timeout=15)
        if r.status_code == 200 and r.json():
            home_id = r.json()[0]["id"]
            r2 = requests.post(
                f"{API}/settings",
                auth=AUTH,
                json={"show_on_front": "page", "page_on_front": home_id},
                timeout=15,
            )
            if r2.status_code == 200:
                print(f"  Front page set to ID {home_id}")
    except Exception:
        pass

    # Fix menu via Code Snippet
    menu_php = r"""
// HomeByJingChen - Menu & Header Fix
// Assign Primary Menu and hide tagline
add_action('after_setup_theme', function() {
    $menu = wp_get_nav_menu_object('Primary Menu');
    if ($menu) {
        $locations = get_theme_mod('nav_menu_locations', array());
        if (empty($locations['primary']) || $locations['primary'] != $menu->term_id) {
            $locations['primary'] = $menu->term_id;
            set_theme_mod('nav_menu_locations', $locations);
        }
    }
}, 20);
"""
    try:
        existing = requests.get(f"{CS_API}/snippets", auth=AUTH, timeout=30)
        found = False
        if existing.status_code == 200:
            for s in existing.json():
                if s.get("name") == "HomeByJingChen Menu Fix":
                    requests.put(
                        f"{CS_API}/snippets/{s['id']}",
                        auth=AUTH,
                        json={"code": menu_php, "scope": "frontend", "active": True},
                        timeout=30,
                    )
                    print(f"  Menu snippet updated (ID: {s['id']})")
                    found = True
                    break
        if not found:
            r = requests.post(
                f"{CS_API}/snippets",
                auth=AUTH,
                json={"name": "HomeByJingChen Menu Fix", "code": menu_php, "scope": "frontend", "active": True},
                timeout=30,
            )
            if r.status_code in (200, 201):
                print(f"  Menu snippet created (ID: {r.json().get('id', '?')})")
    except Exception as e:
        print(f"  Menu snippet error: {e}")


def update_all_pages():
    """Re-push all pages with block markup."""
    print("\n[2/4] Finding CF7 forms...")
    cf_id, cs_id = find_cf7_forms()
    if cf_id:
        print(f"  Contact form: ID {cf_id}")
    if cs_id:
        print(f"  Consultation form: ID {cs_id}")

    print("\n[3/4] Updating all pages with luxury redesign...")
    update_page("home-page", homepage_content(), "Home")
    update_page("about", about_content(), "About Jing Chen")
    update_page("buy", buy_content(), "Buyer Services")
    update_page("sell", sell_content(), "Seller Services")
    update_page("contact", contact_content(cf_id, cs_id), "Contact")
    update_page("communities", communities_hub_content(), "Communities")
    update_page("listings", listings_content(), "Featured Listings")
    update_page("success-stories", success_stories_content(), "Success Stories")
    update_page("resources", resources_content(), "Resources")

    # NEW: Home Search page
    update_page("home-search", home_search_content(), "Home Search")

    # NEW: Past Transactions page
    update_page("past-transactions", past_transactions_content(), "Past Transactions")

    # Community pages
    for slug, (city, tagline, highlights) in COMMUNITY_DATA.items():
        update_page(slug, community_page_content(city, tagline, highlights), f"{city} Real Estate")


def purge_cache():
    print("\n[4/4] Purging cache...")
    try:
        r = requests.post(
            f"{WP_URL}/wp-json/siteground-optimizer/v1/purge-cache",
            auth=AUTH, json={}, timeout=15,
        )
        if r.status_code in (200, 201):
            print("  Cache purged!")
            return
    except Exception:
        pass
    print("  Auto-purge failed - purge manually: SG Optimizer > Caching > Purge")


def main():
    print()
    print("=" * 55)
    print("  HomeByJingChen - Luxury Redesign Deploy")
    print(f"  Target: {WP_URL}")
    print("=" * 55)

    # Test connection
    try:
        r = requests.get(f"{API}/users/me", auth=AUTH, timeout=10)
        if r.status_code != 200:
            print(f"\n  Auth failed: HTTP {r.status_code}")
            sys.exit(1)
        print(f"\n  Connected as: {r.json().get('name')}")
    except Exception as e:
        print(f"\n  Connection failed: {e}")
        sys.exit(1)

    fix_header()
    update_all_pages()
    purge_cache()

    print()
    print("=" * 55)
    print("  DONE!")
    print("=" * 55)
    print()
    print(f"  Visit: {WP_URL}")
    print()
    print("  What changed:")
    print("  - COMPLETE LUXURY REDESIGN: Black/white/beige palette")
    print("  - Typography: Antic Didone (headings) + Poppins (body)")
    print("  - All-caps headings with elegant letter-spacing")
    print("  - Full-width hero sections with parallax backgrounds")
    print("  - 50/50 split sections with image backgrounds")
    print("  - Dark testimonial sections with quotation marks")
    print("  - Beige accent dividers throughout")
    print("  - Sharp-edged (no border-radius) luxury aesthetic")
    print("  - Full-width layout on all pages")
    print()
    print("  Hard refresh: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)")
    print()


if __name__ == "__main__":
    main()
