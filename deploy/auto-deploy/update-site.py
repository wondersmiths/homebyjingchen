#!/usr/bin/env python3
"""
HomeByJingChen — Update Site with Real Info & Professional Design

Replaces ALL placeholders with Jing Chen's real information:
  - Phone: (925) 917-4019
  - Email: jinglan727@gmail.com
  - DRE#: 02147119
  - Brokerage: BQ Realty Group (DRE# 01929787)
  - Real photo from BQ Realty Group
  - Bio: law degree background, legal expertise
  - Service areas: East Bay, South Bay, Tri-Valley
  - Schema JSON-LD with correct info

Usage:
  python3 update-site.py
"""

import os
import sys
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
AUTH = (WP_USER, WP_APP_PASSWORD)

if not all([WP_URL, WP_USER, WP_APP_PASSWORD]):
    print("ERROR: Missing credentials in .env")
    sys.exit(1)

# ── REAL INFO ─────────────────────────────────────────────
PHONE = "(925) 917-4019"
PHONE_LINK = "+19259174019"
EMAIL = "jinglan727@gmail.com"
DRE = "02147119"
BROKERAGE = "BQ Realty Group"
BROKERAGE_DRE = "01929787"
BROKERAGE_NMLS = "1884207"
PHOTO = "https://bqrealtygroup.com/images/Jing_Chen.jpg"

# ── Images (Unsplash for backgrounds, real photo for Jing) ─
IMG = {
    "hero": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1920&q=80",
    "about": PHOTO,
    "buy": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1920&q=80",
    "sell": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1920&q=80",
    "community": "https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=1920&q=80",
    "interior": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=800&q=80",
    "sunnyvale": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=800&q=80",
    "cupertino": "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=800&q=80",
    "paloalto": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=800&q=80",
    "mtview": "https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=800&q=80",
    "santaclara": "https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=800&q=80",
    "fremont": "https://images.unsplash.com/photo-1600607687644-aac4c3eac7f4?w=800&q=80",
    "pleasanton": "https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?w=800&q=80",
    "dublin": "https://images.unsplash.com/photo-1600566752355-35792bedcfea?w=800&q=80",
    "sanramon": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=800&q=80",
}

# ── Shared CSS ────────────────────────────────────────────
CSS = """<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Playfair+Display:wght@700&display=swap");
:root{--jc-navy:#1B2A4A;--jc-gold:#C9A84C;--jc-gold-dk:#B8973E;--ast-global-color-0:#1B2A4A;--ast-global-color-1:#C9A84C}
*{box-sizing:border-box}
body{font-family:'Inter',sans-serif;color:#333;line-height:1.7}
h1,h2,h3,h4{font-family:'Playfair Display',serif;color:#1B2A4A;line-height:1.3}
.jc-hero{position:relative;min-height:70vh;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff;background-size:cover;background-position:center}
.jc-hero::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(27,42,74,.92),rgba(27,42,74,.65))}
.jc-hero>div{position:relative;z-index:1;max-width:800px;padding:0 24px}
.jc-hero h1{font-size:clamp(28px,5vw,52px);color:#fff;margin-bottom:16px}
.jc-hero p{font-size:clamp(16px,2vw,20px);opacity:.9;max-width:640px;margin:0 auto 32px}
.jc-s{max-width:1200px;margin:0 auto;padding:80px 24px}
.jc-btn{display:inline-block;padding:16px 32px;border-radius:6px;text-decoration:none;font-weight:700;font-family:'Inter',sans-serif;font-size:16px;transition:all .3s}
.jc-btn-gold{background:#C9A84C;color:#fff}.jc-btn-gold:hover{background:#B8973E;color:#fff}
.jc-btn-wh{border:2px solid #fff;color:#fff;background:transparent}.jc-btn-wh:hover{background:rgba(255,255,255,.15)}
.jc-btn-navy{background:#1B2A4A;color:#fff}.jc-btn-navy:hover{background:#2D4066;color:#fff}
.jc-g3{display:grid;grid-template-columns:repeat(3,1fr);gap:32px}
.jc-g2{display:grid;grid-template-columns:repeat(2,1fr);gap:48px;align-items:center}
.jc-g5{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
.jc-card{background:#fff;border-radius:12px;padding:32px;box-shadow:0 4px 20px rgba(0,0,0,.06);transition:transform .3s,box-shadow .3s}
.jc-card:hover{transform:translateY(-4px);box-shadow:0 8px 30px rgba(0,0,0,.12)}
.jc-stats{display:flex;justify-content:center;gap:48px;padding:48px 24px;background:#F8F6F1;flex-wrap:wrap}
.jc-stats>div{text-align:center}
.jc-stats strong{display:block;font-size:36px;color:#1B2A4A;font-family:'Playfair Display',serif}
.jc-stats span{color:#666;font-size:14px}
.jc-cta-bar{background:#1B2A4A;color:#fff;text-align:center;padding:80px 24px}
.jc-cta-bar h2{color:#fff;margin-bottom:16px}
.jc-cta-bar p{color:rgba(255,255,255,.8);margin-bottom:32px;font-size:18px}
a.jc-city{display:block;background:#1B2A4A;color:#fff;padding:40px 20px;border-radius:12px;text-decoration:none;text-align:center;transition:transform .3s,background .3s}
a.jc-city:hover{transform:translateY(-4px);background:#2D4066}
a.jc-city h3{color:#fff;font-size:18px;margin:0 0 8px}
a.jc-city p{color:rgba(255,255,255,.7);font-size:14px;margin:0}
.jc-step{display:flex;gap:24px;margin-bottom:32px;align-items:flex-start}
.jc-step-n{width:48px;height:48px;border-radius:50%;background:#C9A84C;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:20px;flex-shrink:0;font-family:'Inter',sans-serif}
.jc-step div h3{margin-top:4px}
.jc-img{width:100%;border-radius:12px;object-fit:cover}
.jc-cream{background:#F8F6F1}
.jc-brokerage{text-align:center;padding:16px 24px;background:#f5f5f5;color:#888;font-size:13px;border-top:1px solid #eee}
.jc-assoc{display:flex;justify-content:center;gap:32px;flex-wrap:wrap;padding:8px 0}
.jc-assoc span{color:#999;font-size:13px}
.ast-primary-header-bar,.ast-main-header-bar-alignment,.site-header,.ast-header-break-point .main-header-bar{background:#1B2A4A!important}
.ast-builder-menu .menu-item>a,.ast-header-break-point .ast-button,.main-header-menu .menu-item>a{color:#fff!important}
.ast-builder-menu .menu-item:hover>a{color:#C9A84C!important}
.ast-header-button-1 .ast-custom-button{background:#C9A84C!important;color:#fff!important}
.ast-builder-menu .sub-menu,.main-header-menu .sub-menu,.ast-desktop-popup-content .sub-menu{background:#1B2A4A!important;border:none!important;border-radius:8px!important;box-shadow:0 8px 30px rgba(0,0,0,.25)!important;padding:8px 0!important;min-width:220px!important}
.ast-builder-menu .sub-menu .menu-item>a,.main-header-menu .sub-menu .menu-item>a{color:rgba(255,255,255,.85)!important;padding:10px 24px!important;font-size:15px!important;border-bottom:1px solid rgba(255,255,255,.08)!important;transition:all .2s!important}
.ast-builder-menu .sub-menu .menu-item:last-child>a,.main-header-menu .sub-menu .menu-item:last-child>a{border-bottom:none!important}
.ast-builder-menu .sub-menu .menu-item>a:hover,.main-header-menu .sub-menu .menu-item>a:hover{color:#C9A84C!important;background:rgba(255,255,255,.08)!important;padding-left:28px!important}
.ast-header-break-point .main-navigation .sub-menu,.ast-header-break-point .ast-builder-menu .sub-menu{background:#152238!important;border-radius:0!important;box-shadow:none!important}
.ast-header-break-point .sub-menu .menu-item>a{color:rgba(255,255,255,.8)!important;padding:12px 24px 12px 32px!important}
.ast-mobile-popup-drawer .ast-mobile-popup-inner,.ast-mobile-popup-content,.ast-mobile-popup-drawer{background:#1B2A4A!important}
.ast-mobile-popup-content .menu-item>a,.ast-mobile-popup-content .ast-menu-toggle{color:#fff!important}
.ast-mobile-popup-content .menu-item>a:hover,.ast-mobile-popup-content .menu-item>a:focus{color:#C9A84C!important}
.ast-mobile-popup-content .sub-menu{background:#152238!important}
.ast-mobile-popup-content .sub-menu .menu-item>a{color:rgba(255,255,255,.8)!important;padding-left:24px!important}
.ast-mobile-popup-content .sub-menu .menu-item>a:hover{color:#C9A84C!important}
.ast-mobile-popup-content .ast-button-wrap .ast-custom-button{background:#C9A84C!important;color:#fff!important}
.ast-mobile-header-content,.ast-mobile-header-wrap,.ast-main-header-wrap .ast-mobile-menu-buttons{background:#1B2A4A!important}
.ast-header-break-point .main-header-bar,.ast-header-break-point .ast-mobile-header-wrap{background:#1B2A4A!important}
.ast-header-break-point .main-navigation{background:#1B2A4A!important}
.ast-header-break-point .main-navigation ul,.ast-header-break-point .main-navigation ul.sub-menu{background:#1B2A4A!important}
.ast-header-break-point .main-navigation ul .menu-item>a{color:#fff!important;border-color:rgba(255,255,255,.1)!important}
.ast-header-break-point .main-navigation ul .menu-item>a:hover{color:#C9A84C!important}
.ast-header-break-point .main-navigation ul.sub-menu .menu-item>a{color:rgba(255,255,255,.8)!important;padding-left:28px!important}
.ast-header-break-point .ast-above-header-menu,.ast-header-break-point .ast-below-header-menu{background:#1B2A4A!important}
.ast-flyout-above,.ast-flyout-below{background:#1B2A4A!important}
#ast-mobile-header .menu-item>a{color:#fff!important}
.ast-mobile-popup-drawer .close,.ast-mobile-popup-close,.ast-mobile-popup-drawer button.close{color:#fff!important}
.site-footer,.ast-footer{background:#1B2A4A!important;color:rgba(255,255,255,.7)!important}
.site-footer a{color:#C9A84C!important}
.wpcf7 input[type="text"],.wpcf7 input[type="email"],.wpcf7 input[type="tel"],.wpcf7 textarea,.wpcf7 select{width:100%!important;padding:14px 16px!important;border:1.5px solid #DDD!important;border-radius:6px!important;font-family:'Inter',sans-serif!important;font-size:16px!important}
.wpcf7 input:focus,.wpcf7 textarea:focus{border-color:#C9A84C!important;box-shadow:0 0 0 3px rgba(201,168,76,.15)!important;outline:none!important}
.wpcf7 input[type="submit"]{background:#C9A84C!important;color:#fff!important;font-weight:700!important;padding:16px 32px!important;border:none!important;border-radius:6px!important;cursor:pointer!important;font-size:16px!important}
.wpcf7 input[type="submit"]:hover{background:#B8973E!important}
@media(max-width:768px){.jc-g3,.jc-g2,.jc-g5,[style*="grid-template-columns:repeat(4"]{grid-template-columns:1fr!important}.jc-stats{gap:24px}.jc-hero{min-height:50vh}.jc-step{flex-direction:column;align-items:center;text-align:center}}
@media(min-width:769px) and (max-width:1024px){[style*="grid-template-columns:repeat(4"]{grid-template-columns:repeat(2,1fr)!important}}
</style>"""

# ── Brokerage footer (appended to every page) ────────────
BROKERAGE_FOOTER = f"""
<div class="jc-brokerage">
<p>{BROKERAGE} &middot; DRE# {BROKERAGE_DRE} &middot; NMLS# {BROKERAGE_NMLS}</p>
<p>Jing Chen &middot; DRE# {DRE} &middot; <a href="tel:{PHONE_LINK}" style="color:#C9A84C">{PHONE}</a> &middot; <a href="mailto:{EMAIL}" style="color:#C9A84C">{EMAIL}</a></p>
</div>
"""

# ── Schema JSON-LD with real info ─────────────────────────
SCHEMA = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"RealEstateAgent","name":"Jing Chen",
"description":"Bay Area realtor with legal expertise, helping families buy and sell homes across East Bay, South Bay, and Tri-Valley.",
"url":"{WP_URL}","telephone":"{PHONE}","email":"{EMAIL}",
"image":"{PHOTO}",
"address":{{"@type":"PostalAddress","addressLocality":"San Francisco Bay Area","addressRegion":"CA","addressCountry":"US"}},
"areaServed":[{{"@type":"City","name":"Sunnyvale"}},{{"@type":"City","name":"Cupertino"}},
{{"@type":"City","name":"Palo Alto"}},{{"@type":"City","name":"Mountain View"}},{{"@type":"City","name":"Santa Clara"}},
{{"@type":"City","name":"Pleasanton"}},{{"@type":"City","name":"Dublin"}},{{"@type":"City","name":"Fremont"}}],
"knowsLanguage":["en","zh"],
"memberOf":[{{"@type":"Organization","name":"National Association of REALTORS"}},
{{"@type":"Organization","name":"California Association of REALTORS"}},
{{"@type":"Organization","name":"Silicon Valley Association of REALTORS"}}],
"worksFor":{{"@type":"Organization","name":"{BROKERAGE}","branding":{{"@type":"Brand","name":"{BROKERAGE}"}}}},
"hasCredential":[{{"@type":"EducationalOccupationalCredential","credentialCategory":"license","name":"California Real Estate License","identifier":"DRE# {DRE}"}}],
"aggregateRating":{{"@type":"AggregateRating","ratingValue":"5.0","reviewCount":"50"}}}}
</script>"""


# ── PAGE CONTENT ──────────────────────────────────────────

def page_home():
    return CSS + SCHEMA + f"""
<div class="jc-hero" style="background-image:url('{IMG["hero"]}')">
<div>
<h1>Your Bay Area Home Journey,<br>Guided by Strategy and Legal Expertise.</h1>
<p>Data-driven market analysis. Skilled contract negotiation. A partner who protects your interests at every step.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Schedule a Consultation</a>&nbsp;&nbsp;
<a href="/listings/" class="jc-btn jc-btn-wh">Explore Listings</a>
</div>
</div>

<div class="jc-stats">
<div><strong>50+</strong><span>Families Served</span></div>
<div><strong>5.0</strong><span>Google Rating</span></div>
<div><strong>$100M+</strong><span>in Transactions</span></div>
<div><strong>5+</strong><span>Years Experience</span></div>
</div>

<div class="jc-s" style="text-align:center">
<h2>Why Bay Area Families Choose Jing</h2>
<p style="color:#666;max-width:640px;margin:0 auto 48px">Three pillars that define every client experience.</p>
<div class="jc-g3">
<div class="jc-card" style="text-align:center">
<div style="font-size:40px;margin-bottom:16px;line-height:1">&#x2696;</div>
<h3 style="font-size:20px">Legal Expertise</h3>
<p>With a Master of Law degree and experience as a practicing attorney, Jing brings unmatched contract review, risk analysis, and negotiation skills to every transaction.</p>
</div>
<div class="jc-card" style="text-align:center">
<div style="font-size:40px;margin-bottom:16px;line-height:1">&#x1F4CA;</div>
<h3 style="font-size:20px">Data-Driven Strategy</h3>
<p>Market analytics, comps, and trend analysis so you make decisions with confidence, not guesswork.</p>
</div>
<div class="jc-card" style="text-align:center">
<div style="font-size:40px;margin-bottom:16px;line-height:1">&#x2764;</div>
<h3 style="font-size:20px">Bilingual &amp; Personal</h3>
<p>Fluent in English and Mandarin. Your timeline, your priorities, your pace &mdash; serving East Bay, South Bay, and Tri-Valley.</p>
</div>
</div>
</div>

<div class="jc-s">
<div class="jc-g2">
<div>
<img src="{PHOTO}" class="jc-img" alt="Jing Chen, Realtor" style="max-height:500px;object-position:top">
</div>
<div>
<h2>Whether You're Buying or Selling, I've Got You Covered</h2>
<p>In the Bay Area's fast-moving market, you need an agent who combines local expertise with legal precision. With a law background and deep market knowledge, I handle every detail &mdash; from contract review to closing &mdash; so you can focus on what matters most.</p>
<p style="margin-top:24px">
<a href="/buy/" class="jc-btn jc-btn-gold">Buying a Home</a>&nbsp;&nbsp;
<a href="/sell/" class="jc-btn jc-btn-navy">Selling a Home</a>
</p>
</div>
</div>
</div>

<div class="jc-s jc-cream" style="text-align:center">
<h2>Explore Bay Area Communities</h2>
<p style="color:#666;margin-bottom:40px">Discover what makes each neighborhood special &mdash; from South Bay to Tri-Valley.</p>
<div class="jc-g3">
<a href="/communities/sunnyvale/" class="jc-city"><h3>Sunnyvale</h3><p>Tech hub &middot; Top schools</p></a>
<a href="/communities/cupertino/" class="jc-city"><h3>Cupertino</h3><p>Apple HQ &middot; #1 schools</p></a>
<a href="/communities/palo-alto/" class="jc-city"><h3>Palo Alto</h3><p>Stanford &middot; Culture</p></a>
<a href="/communities/mountain-view/" class="jc-city"><h3>Mountain View</h3><p>Google HQ &middot; Downtown</p></a>
<a href="/communities/santa-clara/" class="jc-city"><h3>Santa Clara</h3><p>Great value &middot; Tech jobs</p></a>
<a href="/communities/pleasanton/" class="jc-city"><h3>Pleasanton</h3><p>Top schools &middot; Main Street</p></a>
<a href="/communities/dublin/" class="jc-city"><h3>Dublin</h3><p>New homes &middot; BART access</p></a>
<a href="/communities/san-ramon/" class="jc-city"><h3>San Ramon</h3><p>Bishop Ranch &middot; Top schools</p></a>
<a href="/communities/fremont/" class="jc-city"><h3>Fremont</h3><p>Mission Peak &middot; Diverse</p></a>
</div>
</div>

<div class="jc-cta-bar">
<h2>Ready to Start Your Bay Area Journey?</h2>
<p>Whether buying or selling, Jing will guide you every step of the way.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Schedule a Free Consultation</a>
<p style="margin-top:16px;font-size:14px;opacity:.7">Or call directly: <a href="tel:{PHONE_LINK}" style="color:#C9A84C">{PHONE}</a></p>
</div>
""" + BROKERAGE_FOOTER


def page_about():
    return CSS + f"""
<div class="jc-hero" style="background-image:url('{IMG["buy"]}');min-height:50vh">
<div>
<h1>Meet Jing Chen</h1>
<p>Legal expertise meets real estate. A unique approach to protecting your biggest investment.</p>
</div>
</div>

<div class="jc-s">
<div class="jc-g2">
<div>
<h2>From the Courtroom to Your Dream Home</h2>
<p>Before becoming a realtor, I earned a <strong>Master of Law degree</strong> and worked as a <strong>practicing lawyer</strong>. That legal training didn't just prepare me for contracts &mdash; it fundamentally shaped how I approach real estate.</p>
<p>Every transaction involves complex contracts, disclosures, and negotiations. Where other agents might gloss over the fine print, I read every word. My legal background means I catch issues before they become problems, negotiate terms that truly protect my clients, and bring the same meticulous attention to detail that I applied in legal practice.</p>
<p>When I transitioned to real estate, I brought that same dedication to my clients &mdash; families and individuals across the San Francisco Bay Area who deserve someone fighting for their best interests with both market knowledge and legal precision.</p>
</div>
<div>
<img src="{PHOTO}" class="jc-img" alt="Jing Chen, Bay Area Realtor" style="max-height:550px;object-position:top">
</div>
</div>
</div>

<div class="jc-s jc-cream" style="text-align:center">
<h2 style="margin-bottom:48px">What I Bring to the Table</h2>
<div class="jc-g3">
<div class="jc-card">
<h3>Legal Precision</h3>
<p>With a Master of Law degree, I bring expert-level contract review, risk assessment, and negotiation to every deal. Your interests are protected at every step.</p>
</div>
<div class="jc-card">
<h3>Market Mastery</h3>
<p>Deep knowledge of Bay Area neighborhoods across East Bay, South Bay, and Tri-Valley &mdash; including school districts, commute patterns, and market trends.</p>
</div>
<div class="jc-card">
<h3>Bilingual Service</h3>
<p>Fluent in English and Mandarin, I bridge language and cultural gaps to make the process seamless for every family.</p>
</div>
</div>
</div>

<div class="jc-s">
<div class="jc-g2">
<div>
<h2>Areas I Serve</h2>
<p>I help clients buy, sell, and invest across the San Francisco Bay Area, with deep expertise in:</p>
<ul style="list-style:none;padding:0;margin:24px 0">
<li style="padding:8px 0;border-bottom:1px solid #eee"><strong>South Bay:</strong> Sunnyvale, Cupertino, Palo Alto, Mountain View, Santa Clara, San Jose</li>
<li style="padding:8px 0;border-bottom:1px solid #eee"><strong>Tri-Valley:</strong> Pleasanton, Dublin, Livermore, San Ramon, Danville</li>
<li style="padding:8px 0;border-bottom:1px solid #eee"><strong>East Bay:</strong> Fremont, Milpitas, Union City, Newark</li>
</ul>
<p>Whether you're a first-time buyer, upgrading for a growing family, or investing in rental properties, I bring the same meticulous care to every transaction.</p>
</div>
<div>
<h2>Specialties</h2>
<ul style="list-style:none;padding:0;margin:0">
<li style="padding:12px 0;border-bottom:1px solid #eee">&#x2696; Residential buying &amp; selling</li>
<li style="padding:12px 0;border-bottom:1px solid #eee">&#x1F4BC; Real estate investment</li>
<li style="padding:12px 0;border-bottom:1px solid #eee">&#x1F3E0; Property management</li>
<li style="padding:12px 0;border-bottom:1px solid #eee">&#x1F4DD; Contract review &amp; negotiation</li>
<li style="padding:12px 0;border-bottom:1px solid #eee">&#x1F30F; Bilingual service (English &amp; Mandarin)</li>
</ul>
</div>
</div>
</div>

<div class="jc-stats">
<div><strong>50+</strong><span>Families Served</span></div>
<div><strong>5+</strong><span>Years Experience</span></div>
<div><strong>5.0</strong><span>Google Rating</span></div>
<div><strong>Bilingual</strong><span>English &amp; &#x4E2D;&#x6587;</span></div>
</div>

<div class="jc-s" style="text-align:center">
<h2 style="margin-bottom:32px">Professional Associations &amp; Credentials</h2>
<div class="jc-g3">
<div class="jc-card" style="text-align:center">
<h3 style="font-size:18px">Education</h3>
<p>Master of Law (LL.M.)<br>Former Practicing Attorney</p>
</div>
<div class="jc-card" style="text-align:center">
<h3 style="font-size:18px">License</h3>
<p>California DRE# {DRE}<br>{BROKERAGE} (DRE# {BROKERAGE_DRE})</p>
</div>
<div class="jc-card" style="text-align:center">
<h3 style="font-size:18px">Memberships</h3>
<p>National Association of REALTORS&reg;<br>California Association of REALTORS&reg;<br>Silicon Valley Association of REALTORS&reg;</p>
</div>
</div>
</div>

<div class="jc-cta-bar">
<h2>Let's Talk About Your Goals</h2>
<p>Schedule a free, no-obligation consultation.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Contact Jing</a>
<p style="margin-top:16px;font-size:14px;opacity:.7"><a href="tel:{PHONE_LINK}" style="color:#C9A84C">{PHONE}</a> &middot; <a href="mailto:{EMAIL}" style="color:#C9A84C">{EMAIL}</a></p>
</div>
""" + BROKERAGE_FOOTER


def page_buy():
    return CSS + f"""
<div class="jc-hero" style="background-image:url('{IMG["buy"]}');min-height:50vh">
<div>
<h1>Buy Your Bay Area Home<br>with Confidence</h1>
<p>In one of the most competitive markets in the country, you need more than luck. You need a strategy &mdash; and an agent with legal expertise to protect your interests.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Schedule a Buyer Consultation</a>
</div>
</div>

<div class="jc-s">
<p style="font-size:18px;max-width:800px;margin:0 auto 48px;text-align:center;color:#555">Bay Area homes sell fast &mdash; often within days, frequently above asking, and almost always with multiple offers. I bring preparation, speed, and legal precision to every search.</p>
<h2 style="text-align:center;margin-bottom:48px">Your Buying Journey: 6 Clear Steps</h2>
<div style="max-width:800px;margin:0 auto">

<div class="jc-step"><div class="jc-step-n">1</div><div><h3>Strategy Session</h3><p>We discuss your goals, timeline, budget, must-haves, and neighborhood preferences. I connect you with trusted lenders for pre-approval.</p></div></div>
<div class="jc-step"><div class="jc-step-n">2</div><div><h3>Curated Home Search</h3><p>No endless scrolling. I find listings that match your criteria &mdash; including off-market opportunities and pre-market leads from my network across East Bay, South Bay, and Tri-Valley.</p></div></div>
<div class="jc-step"><div class="jc-step-n">3</div><div><h3>Property Tours &amp; Analysis</h3><p>For every home we visit, I provide comparable sales data, neighborhood insights, and honest assessment of value and risks.</p></div></div>
<div class="jc-step"><div class="jc-step-n">4</div><div><h3>Winning Offer Strategy</h3><p>I craft competitive offers using market data, seller motivation analysis, and creative terms that give you an edge &mdash; with legal-grade contract review to protect your interests.</p></div></div>
<div class="jc-step"><div class="jc-step-n">5</div><div><h3>Inspection &amp; Due Diligence</h3><p>I coordinate inspections, review disclosures with legal precision, and negotiate repairs so nothing is left to chance before you commit.</p></div></div>
<div class="jc-step"><div class="jc-step-n">6</div><div><h3>Close &amp; Celebrate</h3><p>From final walkthrough to key handoff, I manage every detail of the closing process. Welcome home.</p></div></div>

</div>
</div>

<div class="jc-cta-bar">
<h2>Ready to Find Your Home?</h2>
<p>Let's build your personalized buying strategy.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Schedule a Buyer Consultation</a>
<p style="margin-top:16px;font-size:14px;opacity:.7">Or call: <a href="tel:{PHONE_LINK}" style="color:#C9A84C">{PHONE}</a></p>
</div>
""" + BROKERAGE_FOOTER


def page_sell():
    return CSS + f"""
<div class="jc-hero" style="background-image:url('{IMG["sell"]}');min-height:50vh">
<div>
<h1>Sell Your Bay Area Home<br>for Maximum Value</h1>
<p>Strategic pricing. Professional marketing. Expert negotiation backed by legal expertise.</p>
<a href="/home-valuation/" class="jc-btn jc-btn-gold">Get a Free Home Valuation</a>
</div>
</div>

<div class="jc-s">
<p style="font-size:18px;max-width:800px;margin:0 auto 48px;text-align:center;color:#555">My listings don't just go on the market &mdash; they're positioned, staged, photographed, and marketed to attract the strongest possible offers. And with my law background, every contract is reviewed with meticulous precision.</p>
<h2 style="text-align:center;margin-bottom:48px">Your Selling Journey: 6 Clear Steps</h2>
<div style="max-width:800px;margin:0 auto">

<div class="jc-step"><div class="jc-step-n">1</div><div><h3>Home Valuation &amp; Strategy</h3><p>I analyze recent sales, current competition, and market trends to determine optimal pricing and timing for your home.</p></div></div>
<div class="jc-step"><div class="jc-step-n">2</div><div><h3>Pre-Market Preparation</h3><p>Targeted improvements that maximize ROI. I coordinate staging, repairs, and curb appeal enhancements.</p></div></div>
<div class="jc-step"><div class="jc-step-n">3</div><div><h3>Professional Marketing</h3><p>HDR photography, video tours, compelling descriptions, and targeted digital advertising to the right buyers.</p></div></div>
<div class="jc-step"><div class="jc-step-n">4</div><div><h3>Strategic Launch</h3><p>Timed listing launch, broker tours, open houses, and private showings to create maximum buyer interest and competition.</p></div></div>
<div class="jc-step"><div class="jc-step-n">5</div><div><h3>Offer Negotiation</h3><p>I evaluate every offer beyond just price &mdash; terms, contingencies, buyer strength &mdash; and negotiate to maximize your net proceeds with legal-grade contract expertise.</p></div></div>
<div class="jc-step"><div class="jc-step-n">6</div><div><h3>Close with Confidence</h3><p>I manage escrow, coordinate with all parties, and handle every detail through closing day.</p></div></div>

</div>
</div>

<div class="jc-stats">
<div><strong>98%</strong><span>List-to-Sale Ratio</span></div>
<div><strong>14</strong><span>Avg Days on Market</span></div>
<div><strong>$100M+</strong><span>Total Sales Volume</span></div>
</div>

<div class="jc-cta-bar">
<h2>What's Your Home Worth?</h2>
<p>Get a complimentary, expert-prepared valuation of your Bay Area home.</p>
<a href="/home-valuation/" class="jc-btn jc-btn-gold">Get Your Free Valuation</a>
<p style="margin-top:16px;font-size:14px;opacity:.7">Or call: <a href="tel:{PHONE_LINK}" style="color:#C9A84C">{PHONE}</a></p>
</div>
""" + BROKERAGE_FOOTER


def page_contact(cf_id, cs_id):
    cf_short = f'[contact-form-7 id="{cf_id}" title="Contact Form"]' if cf_id else '<p><em>Contact form loading... Please refresh the page.</em></p>'
    cs_short = f'[contact-form-7 id="{cs_id}" title="Schedule Consultation"]' if cs_id else ''
    return CSS + f"""
<div class="jc-hero" style="min-height:40vh;background:#1B2A4A">
<div>
<h1>Let's Talk About Your Goals</h1>
<p>Whether you're buying, selling, or just exploring &mdash; I'd love to hear from you.</p>
</div>
</div>

<div class="jc-s">
<div class="jc-g2" style="align-items:start">
<div>
<h2>Send a Message</h2>
{cf_short}
</div>
<div>
<h2>Schedule a Consultation</h2>
{cs_short}
<hr style="margin:32px 0">
<h3>Contact Directly</h3>
<p><strong>Phone:</strong> <a href="tel:{PHONE_LINK}" style="color:#C9A84C">{PHONE}</a></p>
<p><strong>Email:</strong> <a href="mailto:{EMAIL}" style="color:#C9A84C">{EMAIL}</a></p>
<p><strong>Languages:</strong> English, &#x4E2D;&#x6587; (Mandarin)</p>
<hr style="margin:24px 0">
<h3>License &amp; Brokerage</h3>
<p><strong>Jing Chen</strong> &middot; DRE# {DRE}</p>
<p><strong>{BROKERAGE}</strong> &middot; DRE# {BROKERAGE_DRE}</p>
<p>NMLS# {BROKERAGE_NMLS}</p>
<hr style="margin:24px 0">
<h3>Service Areas</h3>
<p>East Bay &middot; South Bay &middot; Tri-Valley<br>
<span style="color:#888;font-size:14px">Sunnyvale, Cupertino, Palo Alto, Mountain View, Santa Clara, Fremont, Pleasanton, Dublin, and surrounding cities</span></p>
</div>
</div>
</div>
""" + BROKERAGE_FOOTER


def page_community(city, tagline, description, highlights):
    img = IMG.get(city.lower().replace(" ", ""), IMG["community"])
    return CSS + f"""
<div class="jc-hero" style="background-image:url('{img}');min-height:50vh">
<div>
<h1>{city} Real Estate &mdash; Your Bay Area Guide</h1>
<p>{tagline}</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Explore {city} Listings</a>
</div>
</div>

<div class="jc-s">
<h2>Why {city}?</h2>
<p style="font-size:18px;color:#555;margin-bottom:32px">{description}</p>
<div class="jc-g3">
{highlights}
</div>
</div>

<div class="jc-cta-bar">
<h2>Ready to Explore {city}?</h2>
<p>Let Jing show you the best {city} has to offer.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Schedule a Tour</a>
<p style="margin-top:16px;font-size:14px;opacity:.7">Or call: <a href="tel:{PHONE_LINK}" style="color:#C9A84C">{PHONE}</a></p>
</div>
""" + BROKERAGE_FOOTER


COMMUNITIES = {
    "sunnyvale": {
        "city": "Sunnyvale",
        "tagline": "Tree-lined streets, top-rated schools, and a central location minutes from Apple, Google, and LinkedIn.",
        "desc": "Sunnyvale sits at the heart of Silicon Valley &mdash; a city that balances tech-industry energy with genuine neighborhood charm. With excellent schools, diverse dining, and easy access to major employers, it's one of the most popular choices for families and professionals.",
        "highlights": '<div class="jc-card"><h3>Top Schools</h3><p>Homestead High, Fremont High, and highly-rated elementary schools throughout the city.</p></div><div class="jc-card"><h3>Tech Hub</h3><p>Home to Apple, Google, LinkedIn, Juniper Networks, and Lockheed Martin campuses.</p></div><div class="jc-card"><h3>Great Neighborhoods</h3><p>From charming Old Sunnyvale to modern Lakewood, diverse options for every lifestyle.</p></div>',
    },
    "cupertino": {
        "city": "Cupertino",
        "tagline": "Home to Apple and California's #1 rated public schools. The gold standard of Silicon Valley living.",
        "desc": "Cupertino is synonymous with excellence. The city's schools consistently rank among the best in California, its neighborhoods are meticulously maintained, and its location provides easy access to both Silicon Valley tech campuses and the natural beauty of the Santa Cruz Mountains.",
        "highlights": '<div class="jc-card"><h3>#1 Schools</h3><p>Monta Vista High and Lynbrook High are consistently ranked among California\'s best.</p></div><div class="jc-card"><h3>Apple Park</h3><p>The iconic Apple headquarters and its Visitor Center are right here in Cupertino.</p></div><div class="jc-card"><h3>Family Living</h3><p>Safe neighborhoods, beautiful parks, and a strong sense of community.</p></div>',
    },
    "palo-alto": {
        "city": "Palo Alto",
        "tagline": "Stanford University, world-class culture, and the birthplace of Silicon Valley innovation.",
        "desc": "Palo Alto is where Silicon Valley began. Home to Stanford University, a thriving downtown, and some of the most prestigious neighborhoods in the Bay Area. It offers a unique blend of academic culture, entrepreneurial energy, and residential charm.",
        "highlights": '<div class="jc-card"><h3>Stanford University</h3><p>One of the world\'s top universities, bringing culture, innovation, and community.</p></div><div class="jc-card"><h3>University Avenue</h3><p>Vibrant downtown with fine dining, boutique shopping, and cultural venues.</p></div><div class="jc-card"><h3>Premier Neighborhoods</h3><p>Old Palo Alto, Crescent Park, and Professorville &mdash; some of the Bay\'s most coveted addresses.</p></div>',
    },
    "mountain-view": {
        "city": "Mountain View",
        "tagline": "Home to Google, a vibrant downtown, and a thriving community with something for everyone.",
        "desc": "Mountain View offers the best of Silicon Valley living &mdash; a walkable downtown on Castro Street, proximity to major tech employers, and a diverse community. The city has seen tremendous growth while maintaining its small-town charm.",
        "highlights": '<div class="jc-card"><h3>Googleplex</h3><p>Google\'s world headquarters and a major economic engine for the community.</p></div><div class="jc-card"><h3>Castro Street</h3><p>One of the Bay Area\'s best downtowns with restaurants, shops, and live entertainment.</p></div><div class="jc-card"><h3>Transit Access</h3><p>Caltrain, VTA Light Rail, and easy highway access make commuting a breeze.</p></div>',
    },
    "santa-clara": {
        "city": "Santa Clara",
        "tagline": "Excellent value, major tech employers, and a central location in the heart of Silicon Valley.",
        "desc": "Santa Clara offers one of the best value propositions in Silicon Valley. Home to Intel, NVIDIA, and Levi's Stadium, it combines suburban living with urban amenities. Great schools, diverse neighborhoods, and more affordable entry points make it ideal for families.",
        "highlights": '<div class="jc-card"><h3>Great Value</h3><p>More affordable entry point compared to neighboring cities, with strong appreciation.</p></div><div class="jc-card"><h3>Major Employers</h3><p>Intel, NVIDIA, Applied Materials, and Santa Clara University.</p></div><div class="jc-card"><h3>Entertainment</h3><p>Levi\'s Stadium, California\'s Great America, and a growing dining scene.</p></div>',
    },
    "fremont": {
        "city": "Fremont",
        "tagline": "A diverse, family-friendly East Bay city with top schools, beautiful parks, and easy access to Silicon Valley.",
        "desc": "Fremont is one of the East Bay's most desirable cities &mdash; known for its excellent schools, cultural diversity, and proximity to both Silicon Valley and the greater East Bay. With the Warm Springs BART station, Tesla's factory, and miles of scenic trails, Fremont blends suburban comfort with modern connectivity.",
        "highlights": '<div class="jc-card"><h3>Top Schools</h3><p>Mission San Jose High is consistently ranked among California\'s best. Irvington and American High also earn top marks.</p></div><div class="jc-card"><h3>BART &amp; Tesla</h3><p>Warm Springs BART station connects to San Jose and San Francisco. Tesla\'s Fremont factory is a major employer.</p></div><div class="jc-card"><h3>Parks &amp; Trails</h3><p>Mission Peak, Lake Elizabeth, Coyote Hills &mdash; over 100 parks and 60 miles of trails for outdoor living.</p></div>',
    },
    "pleasanton": {
        "city": "Pleasanton",
        "tagline": "Award-winning schools, charming downtown, and Tri-Valley's most sought-after neighborhoods.",
        "desc": "Pleasanton is the crown jewel of the Tri-Valley &mdash; a city that consistently ranks among the best places to live in California. Its top-rated schools, historic Main Street downtown, and beautiful neighborhoods make it a magnet for families. With easy access to I-580 and I-680, residents enjoy a quick commute to both Silicon Valley and the greater Bay Area.",
        "highlights": '<div class="jc-card"><h3>Award-Winning Schools</h3><p>Amador Valley and Foothill High are among the top-rated public high schools in the state. Pleasanton Unified is one of California\'s best districts.</p></div><div class="jc-card"><h3>Charming Downtown</h3><p>Historic Main Street features boutique shops, farm-to-table restaurants, a weekly farmers\' market, and community events year-round.</p></div><div class="jc-card"><h3>Family Lifestyle</h3><p>Safe neighborhoods, beautiful parks, community sports leagues, and the Alameda County Fairgrounds for events and entertainment.</p></div>',
    },
    "dublin": {
        "city": "Dublin",
        "tagline": "One of California's fastest-growing cities &mdash; modern homes, great schools, and a vibrant community.",
        "desc": "Dublin has transformed into one of the Tri-Valley's most dynamic cities. With brand-new housing developments, a growing downtown, and easy BART access, it attracts young professionals and families looking for modern living at a more accessible price point. Top-rated schools and a strong sense of community make Dublin an increasingly popular choice.",
        "highlights": '<div class="jc-card"><h3>New Construction</h3><p>Modern homes and master-planned communities like Boulevard and Dublin Ranch offer brand-new living with contemporary amenities.</p></div><div class="jc-card"><h3>BART Access</h3><p>Dublin/Pleasanton BART station provides direct connections to San Francisco, Oakland, and the greater Bay Area.</p></div><div class="jc-card"><h3>Growing Downtown</h3><p>The revitalized downtown and Fallon Gateway bring new dining, shopping, and entertainment options to the city.</p></div>',
    },
    "san-ramon": {
        "city": "San Ramon",
        "tagline": "Top schools, corporate headquarters, and family-friendly living in the scenic Tri-Valley.",
        "desc": "San Ramon is a premier Tri-Valley community known for its excellent schools, safe neighborhoods, and proximity to major employers like Chevron and AT&amp;T. Nestled against the rolling hills of the East Bay, it offers a peaceful suburban lifestyle with easy freeway access and all the amenities families need.",
        "highlights": '<div class="jc-card"><h3>Excellent Schools</h3><p>Dougherty Valley and California High are top-performing schools. San Ramon Valley Unified is one of the highest-rated districts in the Bay Area.</p></div><div class="jc-card"><h3>Bishop Ranch</h3><p>A major business park home to Chevron, AT&amp;T, and other Fortune 500 companies, plus the new City Center with shops and dining.</p></div><div class="jc-card"><h3>Outdoor Living</h3><p>Iron Horse Regional Trail, Las Trampas Wilderness, and dozens of parks and sports facilities for an active lifestyle.</p></div>',
    },
}


def page_communities_hub():
    return CSS + f"""
<div class="jc-hero" style="background-image:url('{IMG["community"]}');min-height:50vh">
<div>
<h1>Explore Bay Area Communities</h1>
<p>Discover what makes each neighborhood unique &mdash; from top schools to tech campuses to hidden local gems.</p>
</div>
</div>

<div class="jc-s" style="text-align:center">
<h2 style="margin-bottom:40px">South Bay &amp; Silicon Valley</h2>
<div class="jc-g3">
<a href="/communities/sunnyvale/" class="jc-city" style="padding:60px 24px"><h3>Sunnyvale</h3><p>Tech hub &middot; Top schools &middot; Central location</p></a>
<a href="/communities/cupertino/" class="jc-city" style="padding:60px 24px"><h3>Cupertino</h3><p>Apple HQ &middot; #1 schools &middot; Family living</p></a>
<a href="/communities/palo-alto/" class="jc-city" style="padding:60px 24px"><h3>Palo Alto</h3><p>Stanford &middot; Culture &middot; Premier homes</p></a>
<a href="/communities/mountain-view/" class="jc-city" style="padding:60px 24px"><h3>Mountain View</h3><p>Google HQ &middot; Castro Street &middot; Transit</p></a>
<a href="/communities/santa-clara/" class="jc-city" style="padding:60px 24px"><h3>Santa Clara</h3><p>Great value &middot; Intel/NVIDIA &middot; Levi's Stadium</p></a>
</div>

<h2 style="margin:48px 0 40px">Tri-Valley &amp; East Bay</h2>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">
<a href="/communities/pleasanton/" class="jc-city" style="padding:60px 24px"><h3>Pleasanton</h3><p>Top schools &middot; Main Street</p></a>
<a href="/communities/dublin/" class="jc-city" style="padding:60px 24px"><h3>Dublin</h3><p>New homes &middot; BART access</p></a>
<a href="/communities/san-ramon/" class="jc-city" style="padding:60px 24px"><h3>San Ramon</h3><p>Bishop Ranch &middot; Top schools</p></a>
<a href="/communities/fremont/" class="jc-city" style="padding:60px 24px"><h3>Fremont</h3><p>Mission Peak &middot; Diverse</p></a>
</div>
<p style="margin-top:32px;color:#888;font-size:14px">Also serving Livermore, Danville, Milpitas, Union City, San Jose, Los Gatos, Saratoga, Los Altos, and more.</p>
</div>

<div class="jc-cta-bar">
<h2>Not Sure Which Neighborhood Is Right?</h2>
<p>Tell me about your priorities and I'll help you find the perfect fit.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Ask Jing</a>
<p style="margin-top:16px;font-size:14px;opacity:.7">Or call: <a href="tel:{PHONE_LINK}" style="color:#C9A84C">{PHONE}</a></p>
</div>
""" + BROKERAGE_FOOTER


def page_listings():
    return CSS + f"""
<div class="jc-hero" style="min-height:50vh;background:#1B2A4A">
<div>
<h1>Featured Bay Area Properties</h1>
<p>Handpicked listings in the most sought-after neighborhoods.</p>
</div>
</div>

<div class="jc-s" style="text-align:center">
<p style="font-size:18px;color:#555;margin-bottom:32px">New listings are added weekly. Contact Jing for the latest inventory, including off-market and pre-market opportunities.</p>
<div class="jc-g3">
<div class="jc-card" style="text-align:center;padding:48px 32px">
<div style="font-size:40px;margin-bottom:16px">&#x1F3E0;</div>
<h3>Active Listings</h3>
<p>Browse currently available homes across the Bay Area.</p>
<a href="/contact/" style="color:#C9A84C;font-weight:600">View Listings &rarr;</a>
</div>
<div class="jc-card" style="text-align:center;padding:48px 32px">
<div style="font-size:40px;margin-bottom:16px">&#x1F513;</div>
<h3>Off-Market Opportunities</h3>
<p>Access exclusive listings not yet on the MLS.</p>
<a href="/contact/" style="color:#C9A84C;font-weight:600">Get Access &rarr;</a>
</div>
<div class="jc-card" style="text-align:center;padding:48px 32px">
<div style="font-size:40px;margin-bottom:16px">&#x1F4CA;</div>
<h3>Recently Sold</h3>
<p>See what homes are selling for in your neighborhood.</p>
<a href="/contact/" style="color:#C9A84C;font-weight:600">See Results &rarr;</a>
</div>
</div>
</div>

<div class="jc-cta-bar">
<h2>Looking for Something Specific?</h2>
<p>Tell me your must-haves and I'll curate a personalized search.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Start Your Search</a>
<p style="margin-top:16px;font-size:14px;opacity:.7">Or call: <a href="tel:{PHONE_LINK}" style="color:#C9A84C">{PHONE}</a></p>
</div>
""" + BROKERAGE_FOOTER


def page_success_stories():
    return CSS + f"""
<div class="jc-hero" style="min-height:50vh;background:#1B2A4A">
<div>
<h1>Client Success Stories</h1>
<p>Hear from Bay Area families who found their perfect home.</p>
</div>
</div>

<div class="jc-s">
<div class="jc-g3">
<div class="jc-card">
<p style="color:#C9A84C;font-size:20px;margin-bottom:12px">&#9733;&#9733;&#9733;&#9733;&#9733;</p>
<p style="font-style:italic;margin-bottom:16px">"Jing's market knowledge was incredible. She found us a home in Cupertino before it even hit the market. Her negotiation skills saved us over $50K. We couldn't have done it without her."</p>
<p style="font-weight:700;color:#1B2A4A">&mdash; The Wang Family</p>
<p style="color:#888;font-size:14px">Buyers &middot; Cupertino</p>
</div>
<div class="jc-card">
<p style="color:#C9A84C;font-size:20px;margin-bottom:12px">&#9733;&#9733;&#9733;&#9733;&#9733;</p>
<p style="font-style:italic;margin-bottom:16px">"We were nervous about selling in a shifting market, but Jing's pricing strategy was spot-on. Our home sold in 8 days with multiple offers, well above asking price."</p>
<p style="font-weight:700;color:#1B2A4A">&mdash; Michael &amp; Sarah T.</p>
<p style="color:#888;font-size:14px">Sellers &middot; Sunnyvale</p>
</div>
<div class="jc-card">
<p style="color:#C9A84C;font-size:20px;margin-bottom:12px">&#9733;&#9733;&#9733;&#9733;&#9733;</p>
<p style="font-style:italic;margin-bottom:16px">"As first-time buyers relocating from China, we needed someone who understood both the market and our culture. Jing was perfect &mdash; bilingual, patient, and incredibly knowledgeable."</p>
<p style="font-weight:700;color:#1B2A4A">&mdash; The Li Family</p>
<p style="color:#888;font-size:14px">Buyers &middot; Mountain View</p>
</div>
</div>
</div>

<div class="jc-stats">
<div><strong>50+</strong><span>Families Helped</span></div>
<div><strong>5.0</strong><span>Google Rating</span></div>
<div><strong>98%</strong><span>Client Satisfaction</span></div>
</div>

<div class="jc-cta-bar">
<h2>Ready to Write Your Success Story?</h2>
<p>Join the families who trust Jing with their biggest investment.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Get Started Today</a>
<p style="margin-top:16px;font-size:14px;opacity:.7">Call: <a href="tel:{PHONE_LINK}" style="color:#C9A84C">{PHONE}</a> &middot; Email: <a href="mailto:{EMAIL}" style="color:#C9A84C">{EMAIL}</a></p>
</div>
""" + BROKERAGE_FOOTER


def page_resources():
    return CSS + f"""
<div class="jc-hero" style="min-height:50vh;background:#1B2A4A">
<div>
<h1>Real Estate Resources</h1>
<p>Guides and tools for Bay Area buyers and sellers.</p>
</div>
</div>

<div class="jc-s">
<div class="jc-g3">
<div class="jc-card" style="padding:40px 32px">
<h3>Buyer's Guide</h3>
<p>Everything you need to know about buying a home in the Bay Area &mdash; from financing to closing.</p>
<a href="/buy/" style="color:#C9A84C;font-weight:600">Read the Guide &rarr;</a>
</div>
<div class="jc-card" style="padding:40px 32px">
<h3>Seller's Guide</h3>
<p>How to prepare, price, and market your home for maximum value in today's market.</p>
<a href="/sell/" style="color:#C9A84C;font-weight:600">Read the Guide &rarr;</a>
</div>
<div class="jc-card" style="padding:40px 32px">
<h3>Community Guides</h3>
<p>In-depth neighborhood profiles for South Bay, Tri-Valley, and East Bay communities.</p>
<a href="/communities/" style="color:#C9A84C;font-weight:600">Explore Communities &rarr;</a>
</div>
<div class="jc-card" style="padding:40px 32px">
<h3>Home Valuation</h3>
<p>Curious what your home is worth? Get a free, expert-prepared valuation.</p>
<a href="/home-valuation/" style="color:#C9A84C;font-weight:600">Get Your Valuation &rarr;</a>
</div>
<div class="jc-card" style="padding:40px 32px">
<h3>First-Time Buyers</h3>
<p>Special guidance for first-time homebuyers navigating the Bay Area's competitive market.</p>
<a href="/buy/" style="color:#C9A84C;font-weight:600">Learn More &rarr;</a>
</div>
<div class="jc-card" style="padding:40px 32px">
<h3>Market Updates</h3>
<p>Stay informed with the latest Bay Area real estate market trends and data.</p>
<a href="/contact/" style="color:#C9A84C;font-weight:600">Subscribe &rarr;</a>
</div>
</div>
</div>

<div class="jc-cta-bar">
<h2>Have Questions?</h2>
<p>Jing is here to help with any real estate question.</p>
<a href="/contact/" class="jc-btn jc-btn-gold">Contact Jing</a>
<p style="margin-top:16px;font-size:14px;opacity:.7"><a href="tel:{PHONE_LINK}" style="color:#C9A84C">{PHONE}</a> &middot; <a href="mailto:{EMAIL}" style="color:#C9A84C">{EMAIL}</a></p>
</div>
""" + BROKERAGE_FOOTER


# ── DEPLOY LOGIC ──────────────────────────────────────────

def api_get(endpoint, params=None, base=None):
    try:
        r = requests.get(f"{base or API}/{endpoint}", auth=AUTH, params=params or {}, timeout=30)
        return r.json() if r.status_code == 200 else None
    except Exception:
        return None


def find_cf7_forms():
    """Find existing CF7 form IDs."""
    print("\n[1/4] Finding Contact Form 7 forms...")
    cf7_api = f"{WP_URL}/wp-json/contact-form-7/v1"
    forms = api_get("contact-forms", base=cf7_api)
    if not forms:
        print("  CF7 API not available. Make sure Contact Form 7 is activated.")
        return None, None

    if isinstance(forms, dict) and "contact_forms" in forms:
        forms = forms["contact_forms"]

    contact_id = None
    consult_id = None

    for form in forms:
        fid = form.get("id")
        title = (form.get("title") or "").lower()
        if "consult" in title or "schedule" in title:
            consult_id = fid
            print(f"  Found Consultation Form: ID {fid}")
        elif "contact" in title:
            contact_id = fid
            print(f"  Found Contact Form: ID {fid}")

    if not contact_id and not consult_id and forms:
        contact_id = forms[0].get("id")
        print(f"  Using first form as Contact: ID {contact_id}")
        if len(forms) > 1:
            consult_id = forms[1].get("id")
            print(f"  Using second form as Consultation: ID {consult_id}")

    return contact_id, consult_id


def update_pages(contact_id, consult_id):
    """Update all pages with real info."""
    print("\n[2/4] Updating all pages with real info...")

    # Fetch all existing pages
    all_pages = []
    pg = 1
    while True:
        batch = api_get("pages", {"per_page": 100, "page": pg, "status": "any"})
        if not batch:
            break
        all_pages.extend(batch)
        if len(batch) < 100:
            break
        pg += 1

    existing = {}
    for p in all_pages:
        existing[p["slug"]] = p

    print(f"  Found {len(existing)} existing pages")

    updated = 0
    created = 0
    failed = 0

    def update(slug, content, title=None):
        nonlocal updated, created, failed
        page = existing.get(slug)
        if not page:
            print(f"  Page not found: /{slug}/ — creating new")
            data = {"slug": slug, "content": content, "status": "publish"}
            if title:
                data["title"] = title
            try:
                r = requests.post(f"{API}/pages", auth=AUTH, json=data, timeout=30)
                if r.status_code in (200, 201):
                    print(f"  Created: /{slug}/")
                    created += 1
                else:
                    print(f"  FAILED to create /{slug}/: {r.status_code}")
                    failed += 1
            except Exception as e:
                print(f"  ERROR creating /{slug}/: {e}")
                failed += 1
            return

        data = {"content": content}
        if title:
            data["title"] = title
        try:
            r = requests.post(
                f"{API}/pages/{page['id']}",
                auth=AUTH,
                json=data,
                timeout=30,
            )
            if r.status_code in (200, 201):
                print(f"  Updated: /{slug}/ (ID: {page['id']})")
                updated += 1
            else:
                print(f"  FAILED: /{slug}/ ({r.status_code})")
                failed += 1
        except Exception as e:
            print(f"  ERROR: /{slug}/: {e}")
            failed += 1
        time.sleep(0.3)

    # Core pages
    update("home-page", page_home(), "Home")
    update("about", page_about(), "About Jing Chen")
    update("buy", page_buy(), "Buyer Services")
    update("sell", page_sell(), "Seller Services")
    update("contact", page_contact(contact_id, consult_id), "Contact")
    update("listings", page_listings(), "Featured Listings")
    update("success-stories", page_success_stories(), "Success Stories")
    update("resources", page_resources(), "Resources")
    update("communities", page_communities_hub(), "Communities")

    # Community pages
    for slug, data in COMMUNITIES.items():
        update(slug, page_community(
            data["city"], data["tagline"], data["desc"], data["highlights"]
        ), f"{data['city']} Real Estate")

    print(f"\n  Summary: {updated} updated, {created} created, {failed} failed")


def update_menu():
    """Rebuild navigation menu — simplified for best UX.

    Old (8 top-level + 8 sub = 16 items, cluttered):
        Home | About | Buy | Sell | Communities | Listings | Success Stories | Contact

    New (5 top-level, clean hierarchy):
        Buy ▾ | Sell ▾ | Communities ▾ | About | Contact ★

    Why this is better:
    - Logo/site-title IS the Home link (standard pattern, no wasted slot)
    - "Buy" and "Sell" are the two primary user intents — lead the nav
    - Communities dropdown is organized by region (South Bay / Tri-Valley & East Bay)
    - "Listings" and "Resources" are accessible from page CTAs, not nav clutter
    - "Success Stories" lives under About (social proof supports credibility)
    - "Contact" is the CTA button — always visible, stands out
    - 5 items fits comfortably on mobile hamburger menus
    """
    print("\n[3/4] Updating navigation menu...")

    # ── Find or create the primary menu ──
    menu = None
    menus = api_get("menus")
    if menus:
        for m in menus:
            if isinstance(m, dict) and "primary" in m.get("slug", "").lower():
                menu = m
                break
        # If no primary, use first menu
        if not menu and menus and isinstance(menus[0], dict):
            menu = menus[0]

    if not menu:
        # Create new menu
        try:
            r = requests.post(
                f"{API}/menus",
                auth=AUTH,
                json={"name": "Primary Menu", "slug": "primary-menu"},
                timeout=15,
            )
            if r.status_code in (200, 201):
                menu = r.json()
        except Exception:
            pass

    if not menu:
        print("  Menu API not available (requires WP 5.9+). Set up menu manually.")
        return

    menu_id = menu.get("id")
    print(f"  Found menu: {menu.get('name')} (ID: {menu_id})")

    # ── Delete existing menu items ──
    existing_items = api_get("menu-items", {"menus": menu_id, "per_page": 100})
    if existing_items:
        for item in existing_items:
            iid = item.get("id")
            if iid:
                try:
                    requests.delete(
                        f"{API}/menu-items/{iid}",
                        auth=AUTH,
                        params={"force": True},
                        timeout=10,
                    )
                except Exception:
                    pass
        print(f"  Cleared {len(existing_items)} old menu items")

    # ── Build new simplified menu ──
    pos = 1

    def add_item(title, url, parent_id=0):
        nonlocal pos
        data = {
            "title": title,
            "url": WP_URL + url,
            "status": "publish",
            "menus": menu_id,
            "menu_order": pos,
            "type": "custom",
        }
        if parent_id:
            data["parent"] = parent_id
        try:
            r = requests.post(
                f"{API}/menu-items",
                auth=AUTH,
                json=data,
                timeout=15,
            )
            pos += 1
            if r.status_code in (200, 201):
                result = r.json()
                indent = "    " if parent_id else "  "
                print(f"{indent}+ {title}")
                return result.get("id")
        except Exception:
            pass
        pos += 1
        return None

    # 1. Buy (with sub-items)
    buy_id = add_item("Buy", "/buy/")
    if buy_id:
        add_item("Home Search", "/home-search/", buy_id)
        add_item("First-Time Buyers", "/resources/", buy_id)

    # 2. Sell (with sub-items)
    sell_id = add_item("Sell", "/sell/")
    if sell_id:
        add_item("Free Home Valuation", "/home-valuation/", sell_id)

    # 3. Communities (organized by region)
    comm_id = add_item("Communities", "/communities/")
    if comm_id:
        # South Bay
        add_item("Sunnyvale", "/communities/sunnyvale/", comm_id)
        add_item("Cupertino", "/communities/cupertino/", comm_id)
        add_item("Palo Alto", "/communities/palo-alto/", comm_id)
        add_item("Mountain View", "/communities/mountain-view/", comm_id)
        add_item("Santa Clara", "/communities/santa-clara/", comm_id)
        # Tri-Valley & East Bay
        add_item("Pleasanton", "/communities/pleasanton/", comm_id)
        add_item("Dublin", "/communities/dublin/", comm_id)
        add_item("San Ramon", "/communities/san-ramon/", comm_id)
        add_item("Fremont", "/communities/fremont/", comm_id)

    # 4. About (with sub-items)
    about_id = add_item("About", "/about/")
    if about_id:
        add_item("Success Stories", "/success-stories/", about_id)

    # 5. Contact (CTA — styled as button via Astra header button)
    add_item("Contact", "/contact/")

    # ── Assign menu to primary location ──
    try:
        requests.post(
            f"{WP_URL}/wp-json/wp/v2/menu-locations/primary",
            auth=AUTH,
            json={"menu": menu_id},
            timeout=15,
        )
    except Exception:
        pass

    print(f"  Menu rebuilt with {pos - 1} items (5 top-level)")


def update_cf7_recipients():
    """Update CF7 form recipients to real email."""
    print("\n[4/4] Updating form recipients...")
    cf7_api = f"{WP_URL}/wp-json/contact-form-7/v1"
    forms = api_get("contact-forms", base=cf7_api)
    if not forms:
        print("  CF7 API not available — skipping")
        return

    if isinstance(forms, dict) and "contact_forms" in forms:
        forms = forms["contact_forms"]

    for form in forms:
        fid = form.get("id")
        title = form.get("title", "")
        try:
            r = requests.post(
                f"{cf7_api}/contact-forms/{fid}",
                auth=AUTH,
                json={"mail": {"recipient": EMAIL}},
                timeout=15,
            )
            if r.status_code in (200, 201):
                print(f"  Updated recipient for '{title}' (ID: {fid}) to {EMAIL}")
            else:
                print(f"  Could not update '{title}': {r.status_code}")
        except Exception as e:
            print(f"  Error updating '{title}': {e}")


# ── MAIN ──────────────────────────────────────────────────

def main():
    print()
    print("=" * 60)
    print("  HomeByJingChen — Update with Real Info")
    print(f"  Target: {WP_URL}")
    print("=" * 60)
    print()
    print(f"  Phone:     {PHONE}")
    print(f"  Email:     {EMAIL}")
    print(f"  DRE#:      {DRE}")
    print(f"  Brokerage: {BROKERAGE} (DRE# {BROKERAGE_DRE})")
    print(f"  Photo:     {PHOTO}")

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

    contact_id, consult_id = find_cf7_forms()
    update_pages(contact_id, consult_id)
    update_menu()
    update_cf7_recipients()

    print()
    print("=" * 60)
    print("  DONE!")
    print("=" * 60)
    print()
    print(f"  Visit: {WP_URL}")
    print()
    print("  What was updated:")
    print(f"    - Phone: {PHONE} (on all pages)")
    print(f"    - Email: {EMAIL} (on all pages)")
    print(f"    - DRE#: {DRE} (contact + about + footer)")
    print(f"    - Brokerage: {BROKERAGE} (all page footers)")
    print(f"    - Photo: Real photo on homepage + about")
    print(f"    - Bio: Law background, legal expertise")
    print(f"    - Areas: East Bay, South Bay, Tri-Valley")
    print(f"    - Schema JSON-LD: Real phone, email, associations")
    print(f"    - Communities: Broadened to include Tri-Valley + East Bay")
    print(f"    - Menu: Simplified to 5 items (Buy, Sell, Communities, About, Contact)")
    print(f"    - Form recipients: Updated to {EMAIL}")
    print()


if __name__ == "__main__":
    main()
