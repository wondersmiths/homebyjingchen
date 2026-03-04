# Deployment Guide: homesbyjingchen.com

**100% Free Stack** — no paid plugins or subscriptions required.

---

## Free Tech Stack

| Need | Free Solution | Replaces |
|------|--------------|----------|
| Page Builder | **Elementor Free** + **Kadence Blocks** | Elementor Pro |
| Theme | **Astra Free** (already installed) | Astra Pro |
| Forms | **Contact Form 7** + **Flamingo** (stores entries) | WPForms Pro |
| Valuation Funnel | **Custom HTML** (included in this repo) | WPForms multi-step |
| Caching | **LiteSpeed Cache** or **WP Super Cache** | WP Rocket |
| Image Optimization | **ShortPixel** (free: 100 imgs/mo) or **Smush** free | Paid optimizer |
| SEO | **Yoast SEO Free** (already installed) | Paid SEO |
| Analytics | **GA4 + Site Kit by Google** (free) | GTM paid tools |
| Tag Manager | **GTM4WP** (free) | — |
| Custom Code | **Code Snippets** (free) | functions.php edits |
| IDX/MLS | **Jetrail/Starter IDX** free plan or manual listings | IDX Broker paid |

**Total cost: $0/year** (beyond your existing hosting)

---

## Current State → Target State

| Now | After |
|-----|-------|
| 5 thin pages | 20+ content-rich pages |
| Purple color scheme | Navy + Gold luxury branding |
| No lead capture | Multi-step valuation funnel + contact forms |
| No analytics | GA4 + Meta Pixel + conversion tracking |

---

## Phase 1: Install Free Plugins (Day 1)

### 1.1 Install Plugins

**Plugins → Add New**, search and install each:

| Plugin | Purpose |
|--------|---------|
| **Elementor** (free) | Visual page builder — drag and drop |
| **Kadence Blocks** | Advanced Gutenberg blocks (tabs, accordions, icon lists) |
| **Contact Form 7** | Contact forms — unlimited forms, free |
| **Flamingo** | Saves CF7 form submissions in WordPress dashboard |
| **WP Super Cache** | Page caching for speed |
| **ShortPixel** or **Smush** | Image compression + WebP |
| **Code Snippets** | Add custom PHP without editing theme files |
| **GTM4WP** | Google Tag Manager container |
| **Site Kit by Google** | GA4 setup wizard (free, by Google) |

Activate all after installing. You already have Yoast SEO — keep it.

### 1.2 Apply Color & Typography

**Appearance → Customize**, change these settings:

**Global → Colors:**
- Primary: `#1B2A4A` (Navy) — replaces the purple
- Accent: `#C9A84C` (Gold)
- Heading text: `#1B2A4A`
- Body text: `#333333`
- Link: `#1B2A4A`
- Link hover: `#C9A84C`

**Global → Typography:**
- Body font: **Inter** (select from Google Fonts list)
- Body size: 16px, line-height 1.7
- Heading font: **Playfair Display**, weight 700

**Global → Buttons:**
- Background: `#C9A84C`, Text: `#FFFFFF`
- Hover background: `#B8973E`
- Border radius: 6px
- Padding: 16px top/bottom, 32px left/right
- Font: Inter, 700

**Header Builder:**
- Upload Jing's logo
- Add phone number text: (408) XXX-XXXX
- Add button: "Schedule a Call" → link to /contact/

**Footer Builder:**
- Background: `#1B2A4A`
- Text: white
- Add DRE license # and Equal Housing logo

### 1.3 Paste Custom CSS

**Appearance → Customize → Additional CSS**

Paste entire contents of → `deploy/css/global-custom.css`

### 1.4 Add Custom Functions

**Plugins → Code Snippets → Add New**, paste → `deploy/wordpress-config/functions-snippet.php`

Save and activate the snippet.

---

## Phase 2: Create Page Structure (Day 1-2)

### 2.1 Rename Existing Pages

| Current | Rename To | Slug |
|---------|-----------|------|
| /about/ | About Jing Chen | /about/ |
| /offerings/ | Buyer Services | /buy/ |
| /properties/ | Featured Listings | /listings/ |
| /contact/ | Contact | /contact/ |
| /resources/ | Resources | /resources/ |
| /home/ | Delete (use root) | — |

### 2.2 Create New Pages

**Pages → Add New** for each. Set template to "Elementor Full Width":

```
Seller Services               → /sell/
Home Valuation                → /sell/home-valuation/
Home Search                   → /buy/home-search/
Communities                   → /communities/
Sunnyvale                     → /communities/sunnyvale/
Cupertino                     → /communities/cupertino/
Palo Alto                     → /communities/palo-alto/
Mountain View                 → /communities/mountain-view/
Santa Clara                   → /communities/santa-clara/
Success Stories               → /success-stories/
Thank You - Valuation         → /thank-you/valuation/
Thank You - Consultation      → /thank-you/consultation/
Thank You - Contact           → /thank-you/contact/
```

### 2.3 Update Navigation Menu

**Appearance → Menus:**

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

---

## Phase 3: Build Pages (Day 2-7)

### Elementor Free Limitations & Workarounds

Elementor Free lacks some Pro widgets. Here's how to handle it:

| Pro Feature Missing | Free Workaround |
|--------------------|-----------------|
| Posts widget (blog grid) | Use **Kadence Blocks** Posts block in a Gutenberg section |
| Testimonial carousel | Use testimonials HTML widget (included in repo) |
| Form widget | Use **Contact Form 7** shortcodes |
| Theme Builder | Use Astra's built-in header/footer builder |
| Counter/animated numbers | Use custom HTML with CSS counters (included in CSS) |
| Mega Menu | Use Astra's dropdown menus (simpler but works) |

### Build Order

**Day 2-3: Homepage** → `03-homepage-wireframe/homepage-wireframe.md`

Build 9 sections using Elementor Free widgets:

1. **Hero:** Container (90vh) + Background image + Heading + Text + 2 Buttons
2. **3 Pillars:** 3-column layout + Icon + Heading + Text in each
3. **Stats Bar:** HTML widget — paste this:
```html
<div style="background:#1B2A4A;padding:48px 20px;display:flex;justify-content:center;gap:60px;flex-wrap:wrap;text-align:center;">
  <div><span style="font-size:48px;font-weight:700;color:#C9A84C;">150+</span><br><span style="color:#fff;font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:0.05em;">Families Served</span></div>
  <div><span style="font-size:48px;font-weight:700;color:#C9A84C;">$200M+</span><br><span style="color:#fff;font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:0.05em;">Transaction Volume</span></div>
  <div><span style="font-size:48px;font-weight:700;color:#C9A84C;">98%</span><br><span style="color:#fff;font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:0.05em;">Client Satisfaction</span></div>
  <div><span style="font-size:48px;font-weight:700;color:#C9A84C;">5.0★</span><br><span style="color:#fff;font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:0.05em;">Google Rating</span></div>
</div>
```
4. **Featured Listings:** 3-column Image Box widgets (manually add listing photos + details)
5. **Why Jing:** 2-column — Image left, Text + list right
6. **Testimonials:** HTML widget — paste from `08-testimonials/testimonials-layout.html`
7. **Market Insights:** Heading + 3 Image Box widgets linking to blog posts
8. **Communities:** HTML widget with community cards (or 5 Image Box widgets)
9. **Final CTA:** Navy background container + centered Heading + Button

**Day 3: About** → `04-about-page/about-page-copy.md`
- Simple single-column text sections with images between paragraphs
- Works perfectly with Elementor Free (Heading + Text Editor + Image widgets)

**Day 4: Buy + Sell** → `05-buyer-services/` + `06-seller-services/`
- Numbered process steps: Heading widget (big gold number) + Text widget
- Works with Elementor Free's basic widgets

**Day 5: Community Pages (x5)** → `07-community-pages/*.md`
- Build Sunnyvale first → Right-click section → Save as Template → reuse for other 4
- Tables for schools/market data: use HTML widget with `<table>` tags

**Day 6: Success Stories** → `08-testimonials/testimonials-layout.html`
- Single HTML widget, paste the entire file

**Day 7: Contact + remaining pages**
- Embed Contact Form 7 shortcodes (see Phase 4)

---

## Phase 4: Forms with Contact Form 7 (Day 7-8)

### 4.1 Contact Form

**Contact → Add New**, name it "Contact Form":

```
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  <p><label>First Name</label>[text* first-name]</p>
  <p><label>Last Name</label>[text* last-name]</p>
</div>
<p><label>Email</label>[email* your-email]</p>
<p><label>Phone</label>[tel* your-phone]</p>
<p><label>Message</label>[textarea your-message]</p>
<p>[submit "Send Message"]</p>
```

**Mail tab:**
- To: jing@homesbyjingchen.com
- Subject: New Contact from [first-name] [last-name]
- Body: include all fields

### 4.2 Consultation Form

**Contact → Add New**, name it "Schedule Consultation":

```
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  <p><label>First Name</label>[text* first-name]</p>
  <p><label>Last Name</label>[text* last-name]</p>
</div>
<p><label>Email</label>[email* your-email]</p>
<p><label>Phone</label>[tel* your-phone]</p>
<p><label>I'm interested in</label>[select interest "Buying" "Selling" "Both"]</p>
<p><label>Preferred Language</label>[radio language default:1 "English" "中文 (Mandarin)"]</p>
<p><label>Message (optional)</label>[textarea your-message]</p>
<p>[submit "Schedule My Consultation"]</p>
```

### 4.3 Home Valuation Funnel

CF7 doesn't support multi-step forms. Use the **standalone HTML form** instead:

→ `deploy/forms/home-valuation-form.html`

On the /sell/home-valuation/ page, add an **HTML widget** in Elementor and paste the entire file. The form includes:
- 3-step progressive disclosure
- Progress dots
- Built-in GA4 + Meta Pixel tracking
- Thank-you confirmation

**To receive submissions**, connect it to a free form backend. Update the `TODO` section in the form's JavaScript with one of:

| Free Backend | How |
|-------------|-----|
| **Formspree** (free: 50 submissions/mo) | Replace form action with `https://formspree.io/f/YOUR_ID` |
| **Getform** (free: 50/mo) | Same approach, use Getform URL |
| **Google Forms** (unlimited, free) | POST to Google Forms endpoint |
| **Email via Netlify/Cloudflare** | Serverless function (more setup) |

Easiest: sign up at formspree.io, create a form, copy the endpoint URL.

### 4.4 Embed Forms in Pages

In Elementor, use the **Shortcode widget** to embed CF7 forms:

| Page | Shortcode |
|------|-----------|
| /contact/ | `[contact-form-7 id="FORM_ID" title="Contact Form"]` and `[contact-form-7 id="FORM_ID" title="Schedule Consultation"]` |
| /buy/ (CTA section) | `[contact-form-7 id="FORM_ID" title="Schedule Consultation"]` |
| /sell/home-valuation/ | Use HTML widget with valuation form HTML |

Replace `FORM_ID` with the actual ID shown in **Contact → Contact Forms**.

### 4.5 Confirmation Redirects

Add this to each CF7 form's **Additional Settings** tab:

```
on_sent_ok: "location.replace('/thank-you/contact/');"
```

(Change the URL per form: `/thank-you/consultation/`, `/thank-you/valuation/`)

---

## Phase 5: SEO (Day 8)

### Set Meta Titles & Descriptions

For every page, scroll to **Yoast SEO** panel below the editor. Set values from:
→ `deploy/wordpress-config/yoast-seo-titles.json`

### Yoast Global Settings

**Yoast SEO → Search Appearance:**
- Site title: "Jing Chen — Silicon Valley Realtor"
- Title separator: —
- Organization: "Jing Chen, Realtor"

**Yoast → Social:**
- Add Instagram, Facebook, LinkedIn URLs

Schema markup is handled by the Code Snippets function (already added in Phase 1).

---

## Phase 6: Analytics — All Free (Day 9)

### 6.1 Google Analytics 4 (via Site Kit)

1. **Site Kit → Setup** → connect your Google account
2. It creates GA4 property automatically and adds tracking code
3. In GA4 (analytics.google.com):
   - Go to Admin → Events → mark `generate_lead` as conversion
   - The Code Snippets function already fires events on form submissions

### 6.2 Meta Pixel (manual, free)

Add to **Code Snippets** (new snippet):

```php
add_action('wp_head', 'jc_meta_pixel');
function jc_meta_pixel() {
    ?>
    <!-- Meta Pixel Code -->
    <script>
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
    n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}
    (window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', 'YOUR_PIXEL_ID');
    fbq('track', 'PageView');
    </script>
    <?php
}
```

Replace `YOUR_PIXEL_ID` with your actual Pixel ID from business.facebook.com.

### 6.3 Google Search Console (free)

1. Go to search.google.com/search-console
2. Add property: `https://homesbyjingchen.com`
3. Verify via Yoast SEO → Webmaster Tools → paste verification code
4. Submit sitemap: `https://homesbyjingchen.com/sitemap_index.xml`

---

## Phase 7: Listings — Free Options (Day 10)

Since IDX Broker costs $50+/mo, here are free alternatives:

### Option A: Manual Featured Listings (Simplest)
- Create listing cards manually in Elementor (Image + price + details + link)
- Link "View on Zillow/Redfin" for full details
- Update manually when listings change
- **Cost: $0** | Works immediately

### Option B: Jetrail Free IDX
- Free plan available for some MLS boards
- Limited features but functional property search
- Install plugin, connect MLS credentials

### Option C: Embed Zillow/Redfin Widgets
- Zillow offers free embeddable listing widgets for agents
- Limited customization but shows live listings
- Add via Elementor HTML widget

### Recommended: Start with Option A
Build manual listing cards now. Add IDX later when budget allows. Your content, SEO, and lead capture are more important for launch.

---

## Phase 8: Performance — Free (Day 11)

### WP Super Cache
1. **Settings → WP Super Cache** → turn ON caching
2. Advanced tab: enable "Cache hits" and "Don't cache pages for known users"
3. Enable mod_rewrite caching (fastest option)

### ShortPixel / Smush
1. Configure: Lossy compression, WebP conversion
2. Bulk optimize existing media
3. Keep hero images under 200KB

### Free Cloudflare CDN
1. Sign up at cloudflare.com (free plan)
2. Point your domain DNS to Cloudflare
3. Enable SSL: Full (Strict)
4. Enable Auto Minify (HTML, CSS, JS)
5. Enable Brotli compression
6. Browser Cache TTL: 1 month

### Test
- Run PageSpeed Insights → aim for 85+ mobile
- Fix flagged issues

---

## Phase 9: Pre-Launch Checklist (Day 12)

### Content
- [ ] All placeholder text replaced (search for "XXX", "TODO")
- [ ] Real phone number, email, DRE license # inserted
- [ ] Real testimonials added (with client permission)
- [ ] Professional photos uploaded

### Functionality
- [ ] All forms submit and you receive emails
- [ ] All navigation links work on desktop + mobile
- [ ] Phone `tel:` links work on mobile
- [ ] Thank-you pages display after form submission
- [ ] Site is mobile responsive

### Legal
- [ ] Privacy Policy page completed
- [ ] DRE license # in footer
- [ ] Equal Housing Opportunity logo
- [ ] Brokerage disclaimer visible

### SEO
- [ ] Every page has SEO title + meta description (via Yoast)
- [ ] One H1 per page
- [ ] Images have alt text
- [ ] Sitemap submitted to Search Console

### Performance
- [ ] PageSpeed 80+ mobile
- [ ] Caching active
- [ ] Images optimized

---

## Launch

1. Set homepage as front page: **Settings → Reading → A static page**
2. Clear all caches (WP Super Cache + Cloudflare)
3. Test on a different device
4. Go live — announce on social media + Google Business Profile

---

## Cost Summary

| Item | Cost |
|------|------|
| All WordPress plugins | **$0** |
| Cloudflare CDN | **$0** |
| Google Analytics 4 | **$0** |
| Meta Pixel | **$0** |
| Google Search Console | **$0** |
| Formspree (form backend) | **$0** (50 submissions/mo free) |
| **Total** | **$0/year** |

Your only costs are domain registration (~$12/yr) and hosting (whatever you're already paying).

---

## Deploy Assets Reference

| File | Paste Into |
|------|-----------|
| `deploy/css/global-custom.css` | Customize → Additional CSS |
| `deploy/wordpress-config/functions-snippet.php` | Code Snippets plugin |
| `deploy/forms/home-valuation-form.html` | Elementor HTML widget on /sell/home-valuation/ |
| `deploy/wordpress-config/yoast-seo-titles.json` | Yoast SEO panel on each page |
| `deploy/schema/faq-schema-buy.json` | HTML widget on /buy/ page |
| `08-testimonials/testimonials-layout.html` | Elementor HTML widget on /success-stories/ |
| `01-07 content files` | Copy text into Elementor Text Editor widgets |
