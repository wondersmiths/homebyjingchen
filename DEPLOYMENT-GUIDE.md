# Deployment Guide: homesbyjingchen.com

Your existing WordPress + Astra site has 5 placeholder pages. This guide transforms it into the full redesign using the deliverables and deploy-ready code in this repo.

---

## Current State → Target State

| Now | After |
|-----|-------|
| 5 thin pages (Home, About, Offerings, Properties, Contact) | 20+ content-rich pages |
| Purple color scheme | Navy + Gold luxury branding |
| Stock photos only | Professional photos + structured content |
| No lead capture | Multi-step valuation funnel + forms |
| No IDX/MLS | Live listing search integration |
| No analytics | GA4 + Meta Pixel + conversion tracking |

---

## Phase 1: Theme & Branding Reset (Day 1)

### 1.1 Install Required Plugins

**Plugins → Add New**, install and activate:

| Plugin | Purpose | Cost |
|--------|---------|------|
| Elementor Pro | Page builder | ~$59/yr |
| Astra Pro (addon) | Theme features | ~$49/yr |
| WPForms Pro | Lead forms | ~$99/yr |
| WP Rocket | Caching/performance | ~$59/yr |
| ShortPixel | Image optimization | Free tier |
| Code Snippets | Custom PHP safely | Free |
| GTM4WP | Tag Manager integration | Free |

You already have Yoast SEO — keep it.

### 1.2 Apply Color & Typography Reset

**Appearance → Customize**, apply every setting from:
→ `deploy/wordpress-config/astra-customizer-settings.json`

Key changes:
- **Global Colors**: Replace all purple (#6000cd) with Navy (#1B2A4A) and Gold (#C9A84C)
- **Typography**: Headings = Playfair Display 700, Body = Inter 400
- **Buttons**: Gold background, white text, 6px radius
- **Header**: Add "Schedule a Call" button, show phone number
- **Footer**: Navy background, 4 columns, add DRE# and Equal Housing logo

### 1.3 Paste Custom CSS

**Appearance → Customize → Additional CSS**

Paste the entire contents of:
→ `deploy/css/global-custom.css`

This overrides Astra defaults to match the design system — buttons, forms, cards, stats bars, navigation, and footer.

### 1.4 Add Custom Functions

**Plugins → Code Snippets → Add New**

Paste the contents of:
→ `deploy/wordpress-config/functions-snippet.php`

This adds: Google Fonts loading, GA4 form tracking, phone/email click tracking, schema markup, and performance tweaks.

**Save and activate the snippet.**

---

## Phase 2: Create Page Structure (Day 1-2)

### 2.1 Rename Existing Pages

| Current Page | Rename To | New Slug |
|-------------|-----------|----------|
| /about-us/ or /about/ | About Jing Chen | /about/ |
| /offerings/ | Buyer Services | /buy/ |
| /properties/ | Featured Listings | /listings/ |
| /contact-us/ or /contact/ | Contact | /contact/ |
| /resources/ | Resources | /resources/ |
| /home/ | (delete — use root as front page) | — |

Edit each page: change title, update permalink slug.

### 2.2 Create New Pages

**Pages → Add New** for each (set template to "Elementor Full Width"):

| Page | Slug | Parent |
|------|------|--------|
| Seller Services | /sell/ | — |
| Home Valuation | /sell/home-valuation/ | Seller Services |
| First-Time Buyer Guide | /buy/first-time-buyers/ | Buyer Services |
| Home Search | /buy/home-search/ | Buyer Services |
| Communities | /communities/ | — |
| Sunnyvale | /communities/sunnyvale/ | Communities |
| Cupertino | /communities/cupertino/ | Communities |
| Palo Alto | /communities/palo-alto/ | Communities |
| Mountain View | /communities/mountain-view/ | Communities |
| Santa Clara | /communities/santa-clara/ | Communities |
| Sold Listings | /listings/sold/ | Featured Listings |
| Success Stories | /success-stories/ | — |
| Thank You - Valuation | /thank-you/valuation/ | — |
| Thank You - Consultation | /thank-you/consultation/ | — |
| Thank You - Contact | /thank-you/contact/ | — |

Publish all pages (they'll be filled with content in Phase 3).

### 2.3 Update Navigation Menu

**Appearance → Menus**, update primary menu:

```
Home
About
Buy ▾
  └── Buyer Services
  └── Home Search
Sell ▾
  └── Seller Services
  └── Home Valuation
Communities ▾
  └── Sunnyvale
  └── Cupertino
  └── Palo Alto
  └── Mountain View
  └── Santa Clara
Listings
Success Stories
Contact
```

Delete old "Offerings" link. Save menu.

---

## Phase 3: Build Pages in Elementor (Day 2-7)

For each page, open → **Edit with Elementor** → build using the wireframes and copy from the corresponding deliverable file.

### Build Order (highest impact first)

**Day 2-3: Homepage**
- Source: `03-homepage-wireframe/homepage-wireframe.md`
- 9 sections: Hero → 3 Pillars → Stats → Listings → Why Jing → Testimonials → Blog → Communities → CTA
- Hero: Container 90vh, background photo with navy gradient overlay, H1 + sub + 2 buttons
- Stats bar: Container with navy BG, 4 Counter widgets (gold numbers)
- Add CSS class `jc-bg-navy` to navy sections, `jc-bg-cream` to testimonial section

**Day 3: About Page**
- Source: `04-about-page/about-page-copy.md`
- Story-driven narrative. Single column, max-width 720px for text sections
- Body font 18px with 1.8 line-height on this page
- Include 2-3 candid photos of Jing between paragraphs

**Day 4: Buy + Sell Pages**
- Buy source: `05-buyer-services/buyer-services-copy.md`
- Sell source: `06-seller-services/seller-services-copy.md`
- Both follow the same pattern: Hero → Intro → 6 numbered steps → comparison → testimonials → CTA
- Steps: Large gold number (72px) on left, text on right

**Day 5: Community Pages (x5)**
- Source: `07-community-pages/*.md`
- Build Sunnyvale first → save as Elementor Template → reuse for other 4 cities
- Each page: Hero → Why City → Neighborhoods → Schools table → Market snapshot → IDX placeholder → CTA

**Day 6: Testimonials / Success Stories**
- Source: `08-testimonials/testimonials-layout.html`
- Paste HTML directly into an **HTML widget** in Elementor
- Replace placeholder reviews with real client reviews

**Day 7: Contact + Remaining Pages**
- Contact: Heading + WPForms embed + Google Maps widget + contact details
- Resources: Hub page linking to blog, guides, calculator
- Thank You pages: Simple confirmation messages with navigation links

---

## Phase 4: Forms & Lead Capture (Day 7-8)

### 4.1 WPForms Setup

**WPForms → Add New**, create 3 forms:

**Form 1: Contact Form**
- Fields: First Name, Last Name, Email, Phone, Message
- Confirmation: Redirect to /thank-you/contact/
- Notification email to Jing

**Form 2: Schedule Consultation**
- Fields: First Name, Last Name, Email, Phone, Interest (Buying/Selling/Both), Preferred Date, Message
- Confirmation: Redirect to /thank-you/consultation/

**Form 3: Home Valuation** (if using WPForms multi-step)
- 3 pages with page breaks, following `09-lead-funnel/home-valuation-funnel.md`
- Confirmation: Redirect to /thank-you/valuation/

**Alternative: Standalone Valuation Form**
If WPForms multi-step isn't available, use the ready-to-paste HTML:
→ `deploy/forms/home-valuation-form.html`
Drop into an Elementor HTML widget on /sell/home-valuation/. Wire the form submission to Formspree or a custom endpoint.

### 4.2 Embed Forms
- /contact/ → Contact Form + Consultation Form
- /sell/home-valuation/ → Valuation funnel (full page)
- /buy/ → Consultation Form in CTA section
- /sell/ → Link to /sell/home-valuation/ in CTA section
- Footer → Newsletter email capture (single field)

---

## Phase 5: SEO Configuration (Day 8-9)

### 5.1 Set Meta Titles & Descriptions

For every page, open editor → scroll to **Yoast SEO** panel → set SEO title and meta description from:
→ `deploy/wordpress-config/yoast-seo-titles.json`

### 5.2 Yoast Global Settings

**Yoast SEO → Search Appearance:**
- Site title: "Jing Chen — Silicon Valley Realtor"
- Title separator: " — "
- Organization name: "Jing Chen, Realtor"
- Social profiles: Add Instagram, Facebook, LinkedIn, YouTube URLs

**Yoast SEO → General → Webmaster Tools:**
- Add Google Search Console verification code (from Phase 6)

### 5.3 Schema Markup

The custom functions snippet already adds RealEstateAgent schema to the homepage. For FAQ schema on the buy page, add the contents of `deploy/schema/faq-schema-buy.json` via Yoast's Schema tab or a Custom HTML widget.

---

## Phase 6: Analytics & Tracking (Day 9-10)

Follow `14-analytics/analytics-setup-guide.md` for full details. Quick version:

### 6.1 Google Tag Manager
1. Create GTM account at tagmanager.google.com
2. Create container "homesbyjingchen.com" (Web)
3. In WordPress: **GTM4WP → Settings** → enter container ID (`GTM-XXXXXXX`)

### 6.2 GA4 (via GTM)
1. Create GA4 property at analytics.google.com → copy Measurement ID (`G-XXXXXXXXXX`)
2. In GTM: New Tag → GA4 Configuration → Measurement ID → Trigger: All Pages
3. Mark conversions: `generate_lead`, `schedule_consultation`, `valuation_request`

### 6.3 Meta Pixel (via GTM)
1. Create Pixel at business.facebook.com → Events Manager
2. In GTM: New Tag → Custom HTML → paste Meta Pixel base code → Trigger: All Pages
3. Create Lead event tags triggered on thank-you page views

### 6.4 Google Search Console
1. Add property at search.google.com/search-console
2. Verify via DNS or HTML tag
3. Submit sitemap: `https://homesbyjingchen.com/sitemap_index.xml`

### 6.5 Publish GTM Container
Preview mode first → verify all tags fire → then Publish.

### 6.6 Verify
- [ ] GA4 Real-Time shows your visit
- [ ] Submit test form → conversion event appears
- [ ] Meta Pixel Helper Chrome extension shows PageView firing
- [ ] Search Console shows no errors

---

## Phase 7: IDX / MLS Integration (Day 10-14)

Follow `10-idx-integration/idx-integration-guide.md`:

1. Sign up for **IDX Broker** (Platinum plan)
2. Submit MLS credentials → wait for approval (3-7 days)
3. While waiting: add "Listings coming soon" placeholder + manual featured listings
4. Once approved:
   - Install IDX Broker WordPress plugin
   - Style to match design system (navy, gold, Inter)
   - Embed on /buy/home-search/ (full search)
   - Embed pre-filtered search on each community page
   - Embed showcase widget on /listings/
   - Configure forced registration after 5 views

---

## Phase 8: Performance Optimization (Day 14-15)

Follow `12-performance/performance-checklist.md`:

### WP Rocket Quick Config
1. Cache: Enable page caching + mobile
2. File Optimization: Minify CSS + JS, defer JS
3. Media: LazyLoad images + iframes
4. Preload: Sitemap preloading + font preload
5. CDN: Connect Cloudflare if using

### Images
- ShortPixel: Lossy compression, WebP conversion
- Bulk optimize all media
- Hero images under 200KB

### Test
- PageSpeed Insights → target 85+ mobile, 95+ desktop
- Fix any flagged issues

---

## Phase 9: Pre-Launch Checklist (Day 15-16)

### Content
- [ ] Replace all placeholder text (search for "XXX", "TODO", "VIDEO_ID")
- [ ] Insert Jing's real phone number, email, DRE license number
- [ ] Add real testimonials with client permission
- [ ] Upload professional photos (headshots, property photos, community images)
- [ ] Proofread all page copy

### Functionality
- [ ] All forms submit and send email notifications
- [ ] All navigation links work (desktop + mobile)
- [ ] All CTA buttons link to correct pages
- [ ] Phone links (`tel:`) work on mobile
- [ ] Mobile responsive — test on iPhone and Android
- [ ] Test all 3 thank-you page redirects

### Legal
- [ ] Privacy Policy page completed
- [ ] DRE license # visible in footer
- [ ] Equal Housing Opportunity logo in footer
- [ ] Brokerage name and disclaimer visible
- [ ] Cookie consent banner if needed

### SEO
- [ ] Every page has unique SEO title + meta description
- [ ] One H1 per page
- [ ] All images have alt text
- [ ] Sitemap submitted to Search Console
- [ ] No "noindex" on public pages

### Performance
- [ ] PageSpeed 85+ mobile
- [ ] All caches cleared and refreshed
- [ ] No console errors

---

## Launch

1. Clear all caches (WP Rocket + browser + CDN)
2. Confirm homepage is set as front page (**Settings → Reading**)
3. Final test on a different device
4. Announce: social media, email contacts, update Google Business Profile

---

## Post-Launch Schedule

| Cadence | Tasks |
|---------|-------|
| **Weekly** | 1 blog post, social media share, check form leads |
| **Monthly** | GA4 review, update featured listings, database optimization |
| **Quarterly** | Update market data on community pages, refresh testimonials, plugin updates, re-test PageSpeed |

---

## Deploy Assets Reference

All implementation-ready code files:

| File | What to do with it |
|------|-------------------|
| `deploy/css/global-custom.css` | Paste into Appearance → Customize → Additional CSS |
| `deploy/wordpress-config/functions-snippet.php` | Paste into Code Snippets plugin |
| `deploy/wordpress-config/astra-customizer-settings.json` | Apply values in Appearance → Customize |
| `deploy/wordpress-config/yoast-seo-titles.json` | Set in Yoast SEO panel on each page |
| `deploy/forms/home-valuation-form.html` | Paste into Elementor HTML widget on /sell/home-valuation/ |
| `deploy/schema/faq-schema-buy.json` | Add to buy page via Yoast Schema or HTML widget |
| `08-testimonials/testimonials-layout.html` | Paste into Elementor HTML widget on /success-stories/ |
| `01-06 content files` | Copy text into Elementor Text Editor widgets |
| `07-community-pages/*.md` | Copy text into Elementor for each community page |
