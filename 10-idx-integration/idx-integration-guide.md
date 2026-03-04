# MLS/IDX Integration Guide: WordPress + Elementor

## Overview

This guide covers integrating IDX (Internet Data Exchange) listing search into your WordPress + Elementor website. IDX pulls live MLS data so visitors can search and view active listings directly on your site.

**Recommended Options:**
1. **IDX Broker** — Most popular, best Elementor compatibility
2. **iHomeFinder** — Strong alternative with good SEO features

---

## Option A: IDX Broker Integration

### Step 1: Sign Up for IDX Broker

1. Visit IDX Broker and sign up for a Platinum plan (required for full customization)
2. You'll need your MLS board credentials — contact your broker/MLS for access
3. IDX Broker will request MLS approval (takes 3-7 business days)
4. Once approved, you'll receive your IDX Broker dashboard access

### Step 2: Install the IDX Broker WordPress Plugin

1. In WordPress admin: **Plugins → Add New**
2. Search for "IDX Broker"
3. Install and activate the official **IDX Broker Plugin**
4. Go to **IDX → Initial Setup**
5. Enter your API key (found in your IDX Broker dashboard under **Account → API Key**)
6. Click **Save Changes** and verify the connection

### Step 3: Configure IDX Broker Settings

**In the IDX Broker dashboard (not WordPress):**

1. **Design → Global Design**
   - Match your site's fonts, colors, and button styles
   - Set primary color to navy (#1B2A4A), accent to gold (#C9A84C)
   - Upload your logo

2. **Pages → Create Search Pages**
   - Create a main search page: "Home Search"
   - Create saved search pages for each community:
     - Sunnyvale Homes for Sale
     - Cupertino Homes for Sale
     - Palo Alto Homes for Sale
     - Mountain View Homes for Sale
     - Santa Clara Homes for Sale

3. **Widgets → Configure Widgets**
   - **Showcase Widget:** Featured listings carousel
   - **Quick Search Widget:** Compact search bar for homepage/sidebar
   - **City Links Widget:** Links to community search pages
   - **Lead Login Widget:** Saved search login for registered users

4. **Leads → Lead Capture Settings**
   - Enable forced registration after 5-10 property views
   - Configure lead notifications (email to Jing)
   - Connect to CRM if using one (Follow Up Boss, kvCORE)

### Step 4: Embed IDX in Elementor Pages

**Method 1: IDX Broker Shortcodes in Elementor**

1. In Elementor, add a **Shortcode** widget
2. Paste the IDX Broker shortcode for the desired widget/page:
   ```
   [idx-platinum-widget id="YOUR_WIDGET_ID"]
   ```
   or for a full search page:
   ```
   [idx-platinum-link id="YOUR_LINK_ID"]
   ```

**Method 2: IDX Broker WordPress Pages**

1. IDX Broker auto-creates WordPress pages (under **IDX → Pages**)
2. These pages can be added to your navigation menus
3. For tighter Elementor integration, create a custom Elementor page and embed the shortcode within it

**Method 3: IDX Broker Widgets in Elementor**

1. In Elementor, add the **WordPress Widget** element
2. Select the IDX Broker widget you want (Showcase, Quick Search, etc.)
3. Configure display settings within Elementor

### Step 5: Create Key Listing Pages

| Page | IDX Configuration | URL |
|------|------------------|-----|
| Home Search | Full search page with map | /buy/home-search/ |
| Featured Listings | Showcase widget (curated) | /listings/ |
| Sunnyvale Listings | Pre-filtered search: city=Sunnyvale | /communities/sunnyvale/ (embedded) |
| Cupertino Listings | Pre-filtered search: city=Cupertino | /communities/cupertino/ (embedded) |
| Palo Alto Listings | Pre-filtered search: city=Palo Alto | /communities/palo-alto/ (embedded) |
| Mountain View Listings | Pre-filtered search: city=Mountain View | /communities/mountain-view/ (embedded) |
| Santa Clara Listings | Pre-filtered search: city=Santa Clara | /communities/santa-clara/ (embedded) |
| Sold Listings | Past sales showcase | /listings/sold/ |

---

## Option B: iHomeFinder Integration

### Step 1: Sign Up

1. Contact iHomeFinder for a subscription (they offer Starter, Plus, and Max plans)
2. Provide your MLS board info for IDX feed setup
3. Await MLS approval (3-7 business days)

### Step 2: Install iHomeFinder Plugin

1. **Plugins → Add New → Upload Plugin**
2. Upload the iHomeFinder plugin (provided by iHomeFinder after signup)
3. Activate and enter your API credentials
4. Configure under **iHomeFinder → Settings**

### Step 3: Configure and Embed

1. iHomeFinder provides shortcodes and widgets similar to IDX Broker
2. Create search pages using `[ihf_quick_search]`, `[ihf_featured_listings]`, etc.
3. Embed shortcodes via Elementor's Shortcode widget
4. Style to match your design system

---

## Best Practices for Layout

### Homepage Quick Search Bar
```
┌──────────────────────────────────────────────────────────────────┐
│  Search Silicon Valley Homes                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────┐  │
│  │ City ▾   │ │ Min Price│ │ Max Price│ │ Beds ▾   │ │Search│  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────┘  │
└──────────────────────────────────────────────────────────────────┘
```
- Place on homepage below the hero or as part of the hero
- Use IDX Broker's Quick Search widget or build a custom form that links to the full search page

### Full Search Page Layout
```
┌────────────────┬───────────────────────────────────────────────┐
│                │                                               │
│  FILTERS       │  MAP VIEW                                     │
│  ──────────    │                                               │
│  City          │  [Interactive map with pins]                  │
│  Price Range   │                                               │
│  Beds / Baths  │                                               │
│  Sq Ft         │                                               │
│  Property Type │                                               │
│  Year Built    │                                               │
│                ├───────────────────────────────────────────────┤
│  [Apply]       │  LISTING CARDS                                │
│  [Reset]       │  ┌────┐ ┌────┐ ┌────┐                        │
│                │  │    │ │    │ │    │                        │
│                │  └────┘ └────┘ └────┘                        │
│                │  ┌────┐ ┌────┐ ┌────┐                        │
│                │  │    │ │    │ │    │                        │
│                │  └────┘ └────┘ └────┘                        │
└────────────────┴───────────────────────────────────────────────┘
```

### Listing Detail Page
- IDX Broker handles individual listing pages automatically
- Ensure design matches your site's theme (configure in IDX dashboard)
- Add a "Schedule a Showing" CTA button
- Add a "Ask About This Property" contact form
- Include agent branding (Jing's photo, phone, email)

---

## SEO Best Practices

### 1. Wrapper Pages Over Direct IDX Links
Don't just link to raw IDX pages. Instead:
- Create custom WordPress/Elementor pages for each community
- Add unique content (neighborhood descriptions, school info, market data) ABOVE the IDX widget
- This gives search engines crawlable content while providing IDX functionality

### 2. Avoid Duplicate Content
- IDX listings are served via JavaScript/iframes — most search engines won't index them as duplicate content
- Your unique content (community descriptions, market analysis) is what ranks
- Use canonical tags where appropriate

### 3. Community Page SEO Structure
```
[H1: City Name Homes for Sale]
[Unique 300-500 word description of the community]
[Neighborhood highlights, school info, market snapshot]

─── IDX SEARCH WIDGET (pre-filtered to this city) ───

[Additional SEO content: FAQ, local insights]
[Internal links to related pages]
```

### 4. Schema Markup
Add `RealEstateAgent` schema to your site:
```json
{
  "@context": "https://schema.org",
  "@type": "RealEstateAgent",
  "name": "Jing Chen",
  "url": "https://homebyjingchen.com",
  "telephone": "(408) XXX-XXXX",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Sunnyvale",
    "addressRegion": "CA"
  },
  "areaServed": ["Sunnyvale", "Cupertino", "Palo Alto", "Mountain View", "Santa Clara"]
}
```

### 5. Meta Tags for Listing Pages
- Each community listing page should have unique title and meta description
- Example: "Sunnyvale Homes for Sale | Search MLS Listings — Jing Chen Realtor"

---

## Lead Capture Configuration

### Registration Settings
| Setting | Recommended Value |
|---------|------------------|
| Force registration | After 5 property views |
| Registration fields | Name, Email, Phone |
| Welcome email | Auto-send with Jing's branding |
| Lead notification | Instant email to Jing |
| Lead routing | Direct to Jing (or CRM) |

### CRM Integration
If using a real estate CRM:
- **Follow Up Boss:** Direct API integration with IDX Broker
- **kvCORE:** Built-in IDX, may not need separate IDX Broker
- **LionDesk:** Zapier integration with IDX Broker

---

## Performance Considerations

1. **Lazy-load IDX widgets** — IDX JavaScript can slow page load. Load search widgets below the fold or on user interaction
2. **Minimize IDX on homepage** — Use a lightweight Quick Search widget, not the full search experience
3. **Cache non-IDX content** — WP Rocket can cache your page content while IDX remains dynamic
4. **Monitor Core Web Vitals** — IDX iframes can affect LCP and CLS. Test with PageSpeed Insights after integration
