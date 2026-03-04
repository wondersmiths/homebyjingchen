# Website Information Architecture: HomeByJingChen

## Sitemap Overview

```
HOME
├── ABOUT
│   └── About Jing Chen
│
├── BUY
│   ├── Buyer Services Overview
│   ├── First-Time Buyer Guide
│   ├── Home Search (IDX Integration)
│   └── Buyer Resources
│
├── SELL
│   ├── Seller Services Overview
│   ├── Home Valuation (Lead Funnel)
│   ├── Selling Process Guide
│   └── Seller Resources
│
├── COMMUNITIES
│   ├── Sunnyvale
│   ├── Cupertino
│   ├── Palo Alto
│   ├── Mountain View
│   ├── Santa Clara
│   └── [Expandable for future cities]
│
├── LISTINGS
│   ├── Featured Listings
│   ├── All Listings (IDX)
│   ├── Sold Listings
│   └── Open Houses
│
├── SUCCESS STORIES
│   ├── Client Testimonials
│   └── Case Studies
│
├── RESOURCES
│   ├── Blog / Market Insights
│   ├── Mortgage Calculator
│   ├── Neighborhood Guides
│   └── FAQ
│
├── CONTACT
│   ├── Contact Form
│   ├── Schedule a Consultation
│   └── Office Info / Map
│
└── UTILITY PAGES
    ├── Privacy Policy
    ├── Terms of Service
    └── Sitemap (XML)
```

---

## Page Hierarchy & Purpose

### Tier 1: Primary Navigation (Always Visible)
| Page | Purpose | Primary CTA |
|------|---------|-------------|
| Home | First impression, brand promise, social proof | "Let's Talk About Your Goals" |
| About | Build trust, tell Jing's story | "Schedule a Consultation" |
| Buy | Convert buyer leads | "Start Your Home Search" |
| Sell | Convert seller leads | "Get Your Home Valuation" |
| Communities | SEO + local authority | "Explore [City] Listings" |
| Contact | Direct lead capture | Form submission |

### Tier 2: Secondary Navigation / Footer
| Page | Purpose | Primary CTA |
|------|---------|-------------|
| Listings | Showcase properties, IDX search | "Schedule a Showing" |
| Success Stories | Social proof + trust | "Read More Stories" |
| Resources | SEO content hub + value delivery | "Download Guide" / "Subscribe" |

### Tier 3: Utility
| Page | Purpose |
|------|---------|
| Privacy Policy | Legal compliance |
| Terms of Service | Legal compliance |
| XML Sitemap | Search engine indexing |

---

## Internal Linking Strategy

### Hub-and-Spoke Model
Each primary page acts as a **hub** linking to related **spoke** pages:

```
BUY (Hub)
  → First-Time Buyer Guide (Spoke)
  → Home Search / IDX (Spoke)
  → Buyer Resources (Spoke)
  → Communities pages (Cross-link)
  → Success Stories: Buyer testimonials (Cross-link)
```

### Cross-Linking Rules

1. **Every community page** links to:
   - Featured Listings filtered by that community
   - Home Valuation page (for sellers in that area)
   - Buyer Services page
   - Related blog posts about that market

2. **Every service page (Buy/Sell)** links to:
   - Relevant Success Stories
   - Community pages
   - Contact / Schedule Consultation

3. **Every blog post** links to:
   - Relevant service page (Buy or Sell)
   - Related community page
   - Contact page

4. **Homepage** links to all Tier 1 pages + Featured Listings

### Sticky/Persistent Elements
- **Header:** Logo, primary nav, phone number, "Schedule a Call" button
- **Footer:** Full sitemap links, social icons, contact info, DRE license #, equal housing logo
- **Floating CTA:** "Get Your Home Valuation" or "Schedule a Call" (mobile-optimized)
- **Exit-Intent Popup:** "Get Silicon Valley Market Insights" email capture (desktop only)

---

## URL Structure

```
homebyjingchen.com/                          → Home
homebyjingchen.com/about/                    → About
homebyjingchen.com/buy/                      → Buyer Services
homebyjingchen.com/buy/first-time-buyers/    → First-Time Buyer Guide
homebyjingchen.com/buy/home-search/          → IDX Search
homebyjingchen.com/sell/                     → Seller Services
homebyjingchen.com/sell/home-valuation/      → Valuation Funnel
homebyjingchen.com/communities/              → Communities Hub
homebyjingchen.com/communities/sunnyvale/    → Sunnyvale
homebyjingchen.com/communities/cupertino/    → Cupertino
homebyjingchen.com/communities/palo-alto/    → Palo Alto
homebyjingchen.com/communities/mountain-view/→ Mountain View
homebyjingchen.com/communities/santa-clara/  → Santa Clara
homebyjingchen.com/listings/                 → Featured Listings
homebyjingchen.com/listings/sold/            → Sold Properties
homebyjingchen.com/success-stories/          → Testimonials
homebyjingchen.com/resources/                → Resource Hub
homebyjingchen.com/resources/blog/           → Blog Index
homebyjingchen.com/contact/                  → Contact
```

---

## Navigation UX Specifications

### Desktop Header
```
[Logo]    Home  |  About  |  Buy ▾  |  Sell ▾  |  Communities ▾  |  Listings  |  Resources ▾    [Phone]  [Schedule a Call]
```

### Mobile Header
```
[Logo]                                [Hamburger Menu]     [Phone Icon]
```

### Mega Menu: Buy
```
┌─────────────────────────────────────────────┐
│  Buyer Services          Resources          │
│  ─────────────           ─────────          │
│  Our Buyer Process       First-Time Guide   │
│  Home Search (IDX)       Mortgage Calc      │
│  Open Houses             Buyer FAQ          │
│                                             │
│  [Start Your Home Search →]                 │
└─────────────────────────────────────────────┘
```

### Mega Menu: Communities
```
┌─────────────────────────────────────────────┐
│  Silicon Valley Communities                 │
│  ─────────────────────────                  │
│  Sunnyvale    Palo Alto     Santa Clara     │
│  Cupertino    Mountain View                 │
│                                             │
│  [Explore All Communities →]                │
└─────────────────────────────────────────────┘
```

---

## Conversion Points Per Page

| Page | Primary Conversion | Secondary Conversion |
|------|-------------------|---------------------|
| Home | Schedule Consultation | Email Signup |
| About | Schedule Consultation | — |
| Buy | Start Home Search | Download Buyer Guide |
| Sell | Home Valuation | Schedule Consultation |
| Communities | Explore Listings | Home Valuation |
| Listings | Schedule Showing | Save Search |
| Success Stories | Schedule Consultation | — |
| Resources | Email Signup | Download Guide |
| Contact | Form Submission | Phone Call |
| Blog Post | Email Signup | Related Listings |

---

## SEO Architecture Notes

1. **Community pages** are the primary SEO drivers — target "[City] homes for sale", "[City] real estate agent"
2. **Blog/Resources** targets long-tail keywords: "best neighborhoods in Sunnyvale for families", "Cupertino school ratings 2026"
3. **Service pages** target intent keywords: "sell my home in Palo Alto", "buy a house in Silicon Valley"
4. **Schema markup** on every page: LocalBusiness, RealEstateAgent, FAQPage (where applicable), Review (testimonials)
5. **Breadcrumbs** enabled on all Tier 2+ pages for navigation and structured data
