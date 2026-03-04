#!/usr/bin/env python3
"""
HomeByJingChen — Auto-Deploy Script
Pushes all pages, content, CSS, and config to WordPress via REST API.

Usage:
  1. Follow setup.md to create Application Password
  2. Copy .env.example to .env and fill in credentials
  3. Run: python3 deploy.py

Requirements: pip3 install requests python-dotenv markdown
"""

import os
import sys
import json
import time
import base64
import requests
from pathlib import Path
from dotenv import load_dotenv

# ============================================
# CONFIG
# ============================================

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent.parent  # root of repo
load_dotenv(SCRIPT_DIR / ".env")

WP_URL = os.getenv("WP_URL", "").rstrip("/")
WP_USER = os.getenv("WP_USER", "")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD", "")

if not all([WP_URL, WP_USER, WP_APP_PASSWORD]):
    print("ERROR: Missing credentials. Copy .env.example to .env and fill in values.")
    sys.exit(1)

API = f"{WP_URL}/wp-json/wp/v2"
AUTH = (WP_USER, WP_APP_PASSWORD)

# ============================================
# HELPERS
# ============================================

def api_get(endpoint, params=None):
    r = requests.get(f"{API}/{endpoint}", auth=AUTH, params=params or {})
    r.raise_for_status()
    return r.json()

def api_post(endpoint, data):
    r = requests.post(f"{API}/{endpoint}", auth=AUTH, json=data)
    if r.status_code not in (200, 201):
        print(f"  ERROR {r.status_code}: {r.text[:200]}")
        return None
    return r.json()

def api_put(endpoint, data):
    # WordPress REST API uses POST for updates too, with the ID in the URL
    r = requests.post(f"{API}/{endpoint}", auth=AUTH, json=data)
    if r.status_code not in (200, 201):
        print(f"  ERROR {r.status_code}: {r.text[:200]}")
        return None
    return r.json()

def md_to_html(md_text):
    """Convert markdown to HTML. Falls back to basic conversion if markdown module unavailable."""
    try:
        import markdown
        return markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    except ImportError:
        # Basic fallback: wrap paragraphs, convert headers
        lines = md_text.split('\n')
        html_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('### '):
                html_lines.append(f'<h3>{stripped[4:]}</h3>')
            elif stripped.startswith('## '):
                html_lines.append(f'<h2>{stripped[3:]}</h2>')
            elif stripped.startswith('# '):
                html_lines.append(f'<h1>{stripped[2:]}</h1>')
            elif stripped.startswith('- '):
                html_lines.append(f'<li>{stripped[2:]}</li>')
            elif stripped.startswith('> '):
                html_lines.append(f'<blockquote>{stripped[2:]}</blockquote>')
            elif stripped == '---':
                html_lines.append('<hr>')
            elif stripped:
                html_lines.append(f'<p>{stripped}</p>')
        return '\n'.join(html_lines)

def read_file(path):
    return Path(path).read_text(encoding='utf-8')

def find_page_by_slug(slug):
    """Find an existing page by slug."""
    pages = api_get("pages", {"slug": slug, "status": "any", "per_page": 1})
    return pages[0] if pages else None

# ============================================
# PAGE DEFINITIONS
# ============================================

PAGES = [
    # (title, slug, parent_slug, content_file, content_type)
    ("Home", "", None, "03-homepage-wireframe/homepage-wireframe.md", "md"),
    ("About Jing Chen", "about", None, "04-about-page/about-page-copy.md", "md"),
    ("Buyer Services", "buy", None, "05-buyer-services/buyer-services-copy.md", "md"),
    ("Home Search", "home-search", "buy", None, None),
    ("Seller Services", "sell", None, "06-seller-services/seller-services-copy.md", "md"),
    ("Home Valuation", "home-valuation", "sell", "deploy/forms/home-valuation-form.html", "html"),
    ("Communities", "communities", None, None, None),
    ("Sunnyvale", "sunnyvale", "communities", "07-community-pages/sunnyvale.md", "md"),
    ("Cupertino", "cupertino", "communities", "07-community-pages/cupertino.md", "md"),
    ("Palo Alto", "palo-alto", "communities", "07-community-pages/palo-alto.md", "md"),
    ("Mountain View", "mountain-view", "communities", "07-community-pages/mountain-view.md", "md"),
    ("Santa Clara", "santa-clara", "communities", "07-community-pages/santa-clara.md", "md"),
    ("Featured Listings", "listings", None, None, None),
    ("Success Stories", "success-stories", None, "08-testimonials/testimonials-layout.html", "html"),
    ("Resources", "resources", None, None, None),
    ("Contact", "contact", None, None, None),
    ("Thank You - Valuation", "thank-you-valuation", None, None, None),
    ("Thank You - Consultation", "thank-you-consultation", None, None, None),
    ("Thank You - Contact", "thank-you-contact", None, None, None),
]

# Thank you page content
THANK_YOU_CONTENT = {
    "thank-you-valuation": """
        <div style="text-align:center;padding:60px 20px;max-width:600px;margin:0 auto;">
        <div style="width:64px;height:64px;background:#2D8B4E;border-radius:50%;color:#fff;font-size:32px;display:flex;align-items:center;justify-content:center;margin:0 auto 24px;">&#10003;</div>
        <h2 style="color:#1B2A4A;">Your Valuation Request Has Been Received!</h2>
        <p style="color:#555;line-height:1.7;">Jing will personally review your property and send you a detailed home valuation within 24 hours.</p>
        <p style="margin-top:24px;"><a href="/communities/" style="color:#C9A84C;font-weight:600;">Explore Communities</a> &middot;
        <a href="/sell/" style="color:#C9A84C;font-weight:600;">Selling Process</a></p></div>
    """,
    "thank-you-consultation": """
        <div style="text-align:center;padding:60px 20px;max-width:600px;margin:0 auto;">
        <div style="width:64px;height:64px;background:#2D8B4E;border-radius:50%;color:#fff;font-size:32px;display:flex;align-items:center;justify-content:center;margin:0 auto 24px;">&#10003;</div>
        <h2 style="color:#1B2A4A;">Your Consultation Is Requested!</h2>
        <p style="color:#555;line-height:1.7;">Jing will confirm your consultation time shortly. In the meantime, feel free to explore.</p>
        <p style="margin-top:24px;"><a href="/buy/" style="color:#C9A84C;font-weight:600;">Buyer Services</a> &middot;
        <a href="/communities/" style="color:#C9A84C;font-weight:600;">Communities</a></p></div>
    """,
    "thank-you-contact": """
        <div style="text-align:center;padding:60px 20px;max-width:600px;margin:0 auto;">
        <div style="width:64px;height:64px;background:#2D8B4E;border-radius:50%;color:#fff;font-size:32px;display:flex;align-items:center;justify-content:center;margin:0 auto 24px;">&#10003;</div>
        <h2 style="color:#1B2A4A;">Thanks for Reaching Out!</h2>
        <p style="color:#555;line-height:1.7;">Jing will get back to you within 24 hours.</p>
        <p style="margin-top:24px;"><a href="/listings/" style="color:#C9A84C;font-weight:600;">Browse Listings</a> &middot;
        <a href="/resources/" style="color:#C9A84C;font-weight:600;">Resources</a></p></div>
    """,
}

# Contact page with CF7 placeholder
CONTACT_CONTENT = """
<div style="max-width:720px;margin:0 auto;padding:40px 20px;">
<h1 style="font-family:'Playfair Display',serif;color:#1B2A4A;text-align:center;">Let's Talk About Your Goals</h1>
<p style="text-align:center;color:#555;margin-bottom:40px;">Whether you're buying, selling, or just exploring — I'd love to hear from you. No pressure, no obligation.</p>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;">
<div>
<h3 style="color:#1B2A4A;">Send a Message</h3>
<p><strong>After creating your Contact Form 7 form, replace this text with the shortcode:</strong></p>
<p><code>[contact-form-7 id="FORM_ID" title="Contact Form"]</code></p>
</div>
<div>
<h3 style="color:#1B2A4A;">Contact Directly</h3>
<p><strong>Phone:</strong> <a href="tel:+14081234567">(408) XXX-XXXX</a></p>
<p><strong>Email:</strong> <a href="mailto:jing@homesbyjingchen.com">jing@homesbyjingchen.com</a></p>
<p><strong>Office:</strong><br>Sunnyvale, CA</p>
<p><strong>Languages:</strong> English, 中文 (Mandarin)</p>
<p><strong>License:</strong> DRE# XXXXXXX</p>
</div>
</div>
</div>
"""

# Listings placeholder
LISTINGS_CONTENT = """
<div style="text-align:center;padding:60px 20px;max-width:800px;margin:0 auto;">
<h1 style="font-family:'Playfair Display',serif;color:#1B2A4A;">Featured Properties</h1>
<p style="color:#555;margin-bottom:40px;">Handpicked listings in Silicon Valley's most sought-after neighborhoods.</p>
<p style="color:#888;font-style:italic;">Listings are updated regularly. Contact Jing directly for the latest availability and to schedule a showing.</p>
<p style="margin-top:30px;"><a href="/contact/" style="background:#C9A84C;color:#fff;padding:16px 32px;border-radius:6px;text-decoration:none;font-weight:700;">Schedule a Showing</a></p>
</div>
"""

# Communities hub page
COMMUNITIES_CONTENT = """
<div style="text-align:center;padding:60px 20px;max-width:900px;margin:0 auto;">
<h1 style="font-family:'Playfair Display',serif;color:#1B2A4A;">Explore Silicon Valley Communities</h1>
<p style="color:#555;margin-bottom:40px;">Discover what makes each neighborhood unique — schools, lifestyle, market trends, and available homes.</p>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:24px;margin-top:40px;">
<a href="/communities/sunnyvale/" style="background:#1B2A4A;color:#fff;padding:40px 24px;border-radius:12px;text-decoration:none;text-align:center;"><h3 style="color:#fff;font-family:'Playfair Display',serif;">Sunnyvale</h3><p style="color:rgba(255,255,255,0.7);font-size:14px;">Tech hub, top schools, family-friendly</p></a>
<a href="/communities/cupertino/" style="background:#1B2A4A;color:#fff;padding:40px 24px;border-radius:12px;text-decoration:none;text-align:center;"><h3 style="color:#fff;font-family:'Playfair Display',serif;">Cupertino</h3><p style="color:rgba(255,255,255,0.7);font-size:14px;">Apple HQ, #1 rated schools</p></a>
<a href="/communities/palo-alto/" style="background:#1B2A4A;color:#fff;padding:40px 24px;border-radius:12px;text-decoration:none;text-align:center;"><h3 style="color:#fff;font-family:'Playfair Display',serif;">Palo Alto</h3><p style="color:rgba(255,255,255,0.7);font-size:14px;">Stanford, culture, prestige</p></a>
<a href="/communities/mountain-view/" style="background:#1B2A4A;color:#fff;padding:40px 24px;border-radius:12px;text-decoration:none;text-align:center;"><h3 style="color:#fff;font-family:'Playfair Display',serif;">Mountain View</h3><p style="color:rgba(255,255,255,0.7);font-size:14px;">Google HQ, vibrant downtown</p></a>
<a href="/communities/santa-clara/" style="background:#1B2A4A;color:#fff;padding:40px 24px;border-radius:12px;text-decoration:none;text-align:center;"><h3 style="color:#fff;font-family:'Playfair Display',serif;">Santa Clara</h3><p style="color:rgba(255,255,255,0.7);font-size:14px;">Great value, major employers</p></a>
</div>
</div>
"""

# Resources hub
RESOURCES_CONTENT = """
<div style="text-align:center;padding:60px 20px;max-width:800px;margin:0 auto;">
<h1 style="font-family:'Playfair Display',serif;color:#1B2A4A;">Silicon Valley Real Estate Resources</h1>
<p style="color:#555;margin-bottom:40px;">Guides, market insights, and tools to help you make informed decisions.</p>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:24px;text-align:left;">
<div style="background:#F5F5F5;padding:32px;border-radius:12px;"><h3 style="color:#1B2A4A;">Buyer's Guide</h3><p style="color:#555;font-size:14px;">Everything you need to know about buying in Silicon Valley.</p><a href="/buy/" style="color:#C9A84C;font-weight:600;">Read More →</a></div>
<div style="background:#F5F5F5;padding:32px;border-radius:12px;"><h3 style="color:#1B2A4A;">Seller's Guide</h3><p style="color:#555;font-size:14px;">How to sell your home for maximum value.</p><a href="/sell/" style="color:#C9A84C;font-weight:600;">Read More →</a></div>
<div style="background:#F5F5F5;padding:32px;border-radius:12px;"><h3 style="color:#1B2A4A;">Community Guides</h3><p style="color:#555;font-size:14px;">Explore neighborhoods, schools, and market trends.</p><a href="/communities/" style="color:#C9A84C;font-weight:600;">Explore →</a></div>
</div>
</div>
"""

# Home Search placeholder
SEARCH_CONTENT = """
<div style="text-align:center;padding:60px 20px;max-width:800px;margin:0 auto;">
<h1 style="font-family:'Playfair Display',serif;color:#1B2A4A;">Search Silicon Valley Homes</h1>
<p style="color:#555;margin-bottom:40px;">Browse available properties across Sunnyvale, Cupertino, Palo Alto, Mountain View, and Santa Clara.</p>
<p style="color:#888;font-style:italic;">MLS listing search coming soon. In the meantime, contact Jing directly for current listings tailored to your needs.</p>
<p style="margin-top:30px;"><a href="/contact/" style="background:#C9A84C;color:#fff;padding:16px 32px;border-radius:6px;text-decoration:none;font-weight:700;">Contact Jing for Listings</a></p>
</div>
"""

# SEO meta data
SEO_DATA = {
    "": {
        "title": "Jing Chen, Realtor — Silicon Valley Real Estate Expert",
        "description": "Data-driven Silicon Valley realtor helping families buy and sell homes in Sunnyvale, Cupertino, Palo Alto, Mountain View, and Santa Clara."
    },
    "about": {
        "title": "About Jing Chen — Your Trusted Silicon Valley Real Estate Partner",
        "description": "Meet Jing Chen: 10+ years of Silicon Valley real estate expertise, 150+ families served, bilingual in English and Mandarin."
    },
    "buy": {
        "title": "Buy a Home in Silicon Valley — Jing Chen, Realtor",
        "description": "Expert buyer representation in Silicon Valley. Data-driven home search, competitive offer strategy, and personal guidance."
    },
    "sell": {
        "title": "Sell Your Silicon Valley Home for Maximum Value — Jing Chen",
        "description": "Strategic pricing, professional marketing, expert negotiation. Get a free home valuation today."
    },
    "home-valuation": {
        "title": "Free Home Valuation — What's Your Silicon Valley Home Worth?",
        "description": "Get a complimentary, expert-prepared home valuation for your Silicon Valley property."
    },
    "sunnyvale": {
        "title": "Sunnyvale Homes for Sale — Jing Chen, Realtor",
        "description": "Explore Sunnyvale homes for sale. Top schools, tech hub proximity, family-friendly neighborhoods."
    },
    "cupertino": {
        "title": "Cupertino Homes for Sale — Jing Chen, Realtor",
        "description": "Find Cupertino homes for sale. Top-rated schools, Apple headquarters, family-friendly living."
    },
    "palo-alto": {
        "title": "Palo Alto Homes for Sale — Jing Chen, Realtor",
        "description": "Explore Palo Alto homes for sale. Stanford University, top schools, premier Silicon Valley living."
    },
    "mountain-view": {
        "title": "Mountain View Homes for Sale — Jing Chen, Realtor",
        "description": "Find Mountain View homes for sale. Home to Google, vibrant downtown, excellent living."
    },
    "santa-clara": {
        "title": "Santa Clara Homes for Sale — Jing Chen, Realtor",
        "description": "Explore Santa Clara homes for sale. Affordable entry point, great schools, tech employers."
    },
    "listings": {
        "title": "Featured Silicon Valley Listings — Jing Chen, Realtor",
        "description": "Browse featured homes for sale in Sunnyvale, Cupertino, Palo Alto, Mountain View, and Santa Clara."
    },
    "success-stories": {
        "title": "Client Success Stories & Reviews — Jing Chen, Realtor",
        "description": "Read what Silicon Valley families say about working with Jing Chen. 5.0-star Google rating."
    },
    "contact": {
        "title": "Contact Jing Chen — Silicon Valley Real Estate Consultation",
        "description": "Schedule a free consultation. Bilingual service in English and Mandarin."
    },
    "communities": {
        "title": "Silicon Valley Communities — Jing Chen, Realtor",
        "description": "Explore Sunnyvale, Cupertino, Palo Alto, Mountain View, and Santa Clara neighborhoods."
    },
    "resources": {
        "title": "Silicon Valley Real Estate Resources — Jing Chen",
        "description": "Market reports, buyer and seller guides, and neighborhood insights."
    },
}

# ============================================
# DEPLOY FUNCTIONS
# ============================================

def test_connection():
    """Verify WordPress API access."""
    print("Testing WordPress API connection...")
    try:
        r = requests.get(f"{WP_URL}/wp-json/wp/v2/users/me", auth=AUTH)
        if r.status_code == 200:
            user = r.json()
            print(f"  Connected as: {user.get('name', 'unknown')}")
            return True
        else:
            print(f"  FAILED: HTTP {r.status_code}")
            print(f"  {r.text[:200]}")
            return False
    except Exception as e:
        print(f"  FAILED: {e}")
        return False

def get_all_pages():
    """Fetch all existing pages."""
    pages = []
    page_num = 1
    while True:
        batch = api_get("pages", {"per_page": 100, "page": page_num, "status": "any"})
        if not batch:
            break
        pages.extend(batch)
        if len(batch) < 100:
            break
        page_num += 1
    return {p["slug"]: p for p in pages}

def cleanup_old_pages(existing_pages):
    """Offer to remove old/duplicate pages."""
    old_slugs = ["about-us", "contact-us", "offerings", "home"]
    for slug in old_slugs:
        if slug in existing_pages:
            page = existing_pages[slug]
            print(f"  Found old page: /{slug}/ (ID: {page['id']}) — setting to draft")
            api_put(f"pages/{page['id']}", {"status": "draft"})

def create_or_update_page(title, slug, content, parent_id=0, existing_pages=None):
    """Create a page or update if it exists."""
    existing = existing_pages.get(slug) if existing_pages else find_page_by_slug(slug)

    data = {
        "title": title,
        "slug": slug,
        "content": content,
        "status": "publish",
        "parent": parent_id,
        "template": "elementor_header_footer",  # Full width with header/footer
    }

    if existing:
        page_id = existing["id"]
        print(f"  Updating: /{slug}/ (ID: {page_id})")
        result = api_put(f"pages/{page_id}", data)
    else:
        print(f"  Creating: /{slug}/")
        result = api_post("pages", data)

    if result:
        return result["id"]
    return None

def set_yoast_meta(page_id, slug):
    """Set Yoast SEO meta via REST API (requires Yoast SEO active)."""
    seo = SEO_DATA.get(slug)
    if not seo:
        return

    # Yoast exposes meta via the standard post meta API
    data = {
        "meta": {
            "yoast_wpseo_title": seo["title"],
            "yoast_wpseo_metadesc": seo["description"],
        }
    }
    api_put(f"pages/{page_id}", data)

def push_custom_css():
    """Push custom CSS via the customizer API (custom_css custom post type)."""
    css_file = PROJECT_DIR / "deploy" / "css" / "global-custom.css"
    if not css_file.exists():
        print("  CSS file not found, skipping")
        return

    css_content = css_file.read_text()

    # WordPress stores custom CSS as a custom post type 'custom_css'
    # for the active theme
    r = requests.get(f"{WP_URL}/wp-json/wp/v2/themes", auth=AUTH)
    if r.status_code == 200:
        themes = r.json()
        active_theme = None
        for theme in themes:
            if theme.get("status") == "active":
                active_theme = theme.get("stylesheet")
                break

        if active_theme:
            # Try to find existing custom CSS post
            css_posts = requests.get(
                f"{API}/custom_css",
                auth=AUTH,
                params={"per_page": 1}
            )
            if css_posts.status_code == 200 and css_posts.json():
                css_post = css_posts.json()[0]
                api_put(f"custom_css/{css_post['id']}", {"content": {"raw": css_content}})
                print(f"  Updated custom CSS (ID: {css_post['id']})")
            else:
                # Create new — may need the customize endpoint instead
                print("  Custom CSS push requires manual paste into Customize → Additional CSS")
                print(f"  File ready at: deploy/css/global-custom.css")
    else:
        print("  Could not detect active theme for CSS push — paste manually")

def set_homepage(page_id):
    """Set a page as the static front page."""
    # This requires the settings API
    r = requests.post(
        f"{WP_URL}/wp-json/wp/v2/settings",
        auth=AUTH,
        json={
            "show_on_front": "page",
            "page_on_front": page_id,
        }
    )
    if r.status_code == 200:
        print(f"  Homepage set to page ID: {page_id}")
    else:
        print(f"  Could not set homepage automatically. Go to Settings → Reading → set static page.")

def create_menu():
    """Create navigation menu via REST API."""
    # WordPress menu API requires the nav-menus endpoint (WP 5.9+)
    menu_items = [
        {"title": "Home", "url": "/", "order": 1},
        {"title": "About", "url": "/about/", "order": 2},
        {"title": "Buy", "url": "/buy/", "order": 3},
        {"title": "Sell", "url": "/sell/", "order": 4},
        {"title": "Communities", "url": "/communities/", "order": 5},
        {"title": "Listings", "url": "/listings/", "order": 6},
        {"title": "Success Stories", "url": "/success-stories/", "order": 7},
        {"title": "Contact", "url": "/contact/", "order": 8},
    ]
    print("  Menu creation via REST API has limited support.")
    print("  Please set up navigation in Appearance → Menus manually.")
    print("  Menu structure is defined in DEPLOYMENT-GUIDE.md")

# ============================================
# MAIN DEPLOY
# ============================================

def deploy():
    print("=" * 60)
    print("  HomeByJingChen — Auto Deploy")
    print(f"  Target: {WP_URL}")
    print("=" * 60)
    print()

    # Step 1: Test connection
    if not test_connection():
        print("\nDeploy aborted. Check your .env credentials.")
        sys.exit(1)
    print()

    # Step 2: Fetch existing pages
    print("Fetching existing pages...")
    existing_pages = get_all_pages()
    print(f"  Found {len(existing_pages)} existing pages: {', '.join(existing_pages.keys())}")
    print()

    # Step 3: Clean up old pages
    print("Cleaning up old/duplicate pages...")
    cleanup_old_pages(existing_pages)
    print()

    # Step 4: Create/update all pages
    print("Creating/updating pages...")
    page_ids = {}  # slug -> page_id

    for title, slug, parent_slug, content_file, content_type in PAGES:
        # Determine parent ID
        parent_id = 0
        if parent_slug and parent_slug in page_ids:
            parent_id = page_ids[parent_slug]

        # Determine content
        content = ""
        if content_file and content_type:
            filepath = PROJECT_DIR / content_file
            if filepath.exists():
                raw = read_file(filepath)
                if content_type == "md":
                    # Strip front matter (SEO titles, meta descriptions at top of md files)
                    lines = raw.split('\n')
                    clean_lines = []
                    skip = False
                    for line in lines:
                        if line.startswith('**SEO Title:') or line.startswith('**Meta Description:') or line.startswith('**Target Keywords:'):
                            continue
                        clean_lines.append(line)
                    content = md_to_html('\n'.join(clean_lines))
                elif content_type == "html":
                    content = raw
            else:
                print(f"  WARNING: Content file not found: {content_file}")

        # Use special content for specific pages
        if slug in THANK_YOU_CONTENT:
            content = THANK_YOU_CONTENT[slug]
        elif slug == "contact":
            content = CONTACT_CONTENT
        elif slug == "listings":
            content = LISTINGS_CONTENT
        elif slug == "communities" and not content:
            content = COMMUNITIES_CONTENT
        elif slug == "resources" and not content:
            content = RESOURCES_CONTENT
        elif slug == "home-search":
            content = SEARCH_CONTENT

        # Create or update
        page_id = create_or_update_page(
            title, slug or "home-page",
            content, parent_id, existing_pages
        )
        if page_id:
            actual_slug = slug or ""
            page_ids[actual_slug] = page_id

            # Set Yoast SEO meta
            set_yoast_meta(page_id, slug)

        time.sleep(0.3)  # Rate limiting

    print(f"\n  Created/updated {len(page_ids)} pages")
    print()

    # Step 5: Set homepage
    print("Setting homepage...")
    home_id = page_ids.get("") or page_ids.get("home-page")
    if home_id:
        set_homepage(home_id)
    print()

    # Step 6: Push custom CSS
    print("Pushing custom CSS...")
    push_custom_css()
    print()

    # Step 7: Menu
    print("Navigation menu...")
    create_menu()
    print()

    # Done
    print("=" * 60)
    print("  DEPLOY COMPLETE")
    print("=" * 60)
    print()
    print("Pages created/updated. Remaining manual steps:")
    print()
    print("  1. PASTE CUSTOM CSS (if not auto-pushed):")
    print("     Appearance → Customize → Additional CSS")
    print(f"     File: deploy/css/global-custom.css")
    print()
    print("  2. ADD CODE SNIPPET:")
    print("     Code Snippets → Add New → paste functions-snippet.php")
    print(f"     File: deploy/wordpress-config/functions-snippet.php")
    print()
    print("  3. SET UP NAVIGATION MENU:")
    print("     Appearance → Menus → see DEPLOYMENT-GUIDE.md")
    print()
    print("  4. CREATE CONTACT FORM 7 FORMS:")
    print("     Contact → Add New → see DEPLOYMENT-GUIDE.md Phase 4")
    print()
    print("  5. CONFIGURE THEME COLORS:")
    print("     Appearance → Customize → apply settings from")
    print(f"     File: deploy/wordpress-config/astra-customizer-settings.json")
    print()
    print("  6. SET UP ANALYTICS:")
    print("     Install Site Kit → connect GA4 (free)")
    print()
    print(f"  Visit your site: {WP_URL}")
    print()

if __name__ == "__main__":
    deploy()
