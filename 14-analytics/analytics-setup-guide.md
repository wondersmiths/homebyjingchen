# Analytics & Conversion Tracking Setup Guide

## Overview

This guide covers integrating Google Analytics 4 (GA4), Meta Pixel, and conversion tracking for lead forms on HomeByJingChen.com.

---

## Part 1: Google Analytics 4 (GA4)

### Step 1: Create GA4 Property

1. Go to [analytics.google.com](https://analytics.google.com)
2. Click **Admin** (gear icon)
3. Click **Create Property**
4. Property name: "HomeByJingChen"
5. Time zone: Pacific Time (US & Canada)
6. Currency: USD
7. Business category: Real Estate
8. Business size: Small
9. Click **Create**

### Step 2: Create a Web Data Stream

1. In the new property, select **Data Streams → Web**
2. Website URL: `https://homebyjingchen.com`
3. Stream name: "Website"
4. Enable Enhanced Measurement (all options):
   - Page views
   - Scrolls
   - Outbound clicks
   - Site search
   - Form interactions
   - Video engagement
   - File downloads
5. Click **Create Stream**
6. Copy the **Measurement ID** (format: `G-XXXXXXXXXX`)

### Step 3: Install GA4 on WordPress

**Option A: Google Site Kit Plugin (Recommended)**
1. Install **Site Kit by Google** plugin
2. Follow setup wizard to connect your Google account
3. Select your GA4 property
4. Site Kit handles code placement automatically

**Option B: Google Tag Manager (GTM)**
1. Go to [tagmanager.google.com](https://tagmanager.google.com)
2. Create account: "HomeByJingChen"
3. Create container: "homebyjingchen.com" (Web)
4. Install GTM on WordPress:
   - Install **GTM4WP** plugin
   - Enter your GTM container ID (format: `GTM-XXXXXXX`)
5. In GTM, create a new tag:
   - Tag type: Google Analytics: GA4 Configuration
   - Measurement ID: `G-XXXXXXXXXX`
   - Trigger: All Pages
6. Publish the container

**Option C: Manual Code (if no plugin)**
Add to theme's `<head>` via **Appearance → Theme File Editor** or a code snippets plugin:
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Step 4: Configure GA4 Conversion Events

**In GA4 Admin → Events → Create Event:**

| Event Name | Trigger Condition | Purpose |
|-----------|-------------------|---------|
| `generate_lead` | Form submission (contact, valuation, consultation) | Primary conversion |
| `schedule_consultation` | Consultation form submitted | High-intent lead |
| `valuation_request` | Home valuation form submitted | Seller lead |
| `listing_view` | IDX listing detail page viewed | Engagement |
| `phone_click` | Click on phone number link | Direct contact |
| `email_click` | Click on email link | Direct contact |

**Mark as Conversions:**
1. Go to **Admin → Events**
2. Toggle the "Mark as conversion" switch for:
   - `generate_lead`
   - `schedule_consultation`
   - `valuation_request`

### Step 5: Set Up Custom Events for Forms

**For WPForms (via GTM):**

Create a GTM trigger for form submissions:

1. **Trigger:** Custom Event
   - Event name: `wpforms_submit`
   - (WPForms fires this event on submission)

2. **Tag:** GA4 Event
   - Event name: `generate_lead`
   - Parameters:
     - `form_name`: {{Form Name}}
     - `form_id`: {{Form ID}}

**Alternative: WPForms + GA4 via wp_footer:**
Add this to your theme's functions.php or via Code Snippets plugin:
```php
add_action('wpforms_process_complete', 'track_wpforms_ga4', 10, 4);
function track_wpforms_ga4($fields, $entry, $form_data, $entry_id) {
    $form_name = $form_data['settings']['form_title'];
    ?>
    <script>
        gtag('event', 'generate_lead', {
            'form_name': '<?php echo esc_js($form_name); ?>',
            'form_id': '<?php echo esc_js($form_data['id']); ?>'
        });
    </script>
    <?php
}
```

### Step 6: Track Phone & Email Clicks

**Via GTM:**

1. Enable **Click URL** built-in variable in GTM
2. Create trigger:
   - Type: Click - Just Links
   - Condition: Click URL contains `tel:`
3. Create GA4 Event tag:
   - Event name: `phone_click`
   - Trigger: Phone click trigger

Repeat for email (`mailto:`) clicks.

---

## Part 2: Meta Pixel (Facebook/Instagram Ads)

### Step 1: Create Meta Pixel

1. Go to [business.facebook.com](https://business.facebook.com)
2. Navigate to **Events Manager**
3. Click **Connect Data Sources → Web**
4. Select **Meta Pixel**
5. Name: "HomeByJingChen Pixel"
6. Enter website URL
7. Copy your **Pixel ID** (format: `123456789012345`)

### Step 2: Install Meta Pixel on WordPress

**Option A: Via GTM (Recommended if using GTM)**

1. In GTM, create a new **Custom HTML** tag:
```html
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'YOUR_PIXEL_ID');
fbq('track', 'PageView');
</script>
```
2. Trigger: All Pages
3. Publish container

**Option B: PixelYourSite Plugin**
1. Install **PixelYourSite** plugin (free version works)
2. Enter your Meta Pixel ID
3. Plugin handles base code and standard events

### Step 3: Configure Meta Pixel Events

| Meta Event | WordPress Trigger | Purpose |
|-----------|-------------------|---------|
| `PageView` | All pages (automatic) | Audience building |
| `Lead` | Contact/consultation form submitted | Lead conversion |
| `ViewContent` | Listing detail page viewed | Retargeting |
| `Schedule` | Consultation scheduled | High-value conversion |
| `FindLocation` | Community page viewed | Interest signal |

**Fire Lead event on form submission (via GTM):**

1. Use the same WPForms trigger from the GA4 setup
2. Create a Custom HTML tag:
```html
<script>
  fbq('track', 'Lead', {
    content_name: 'Contact Form',
    content_category: 'Lead Generation'
  });
</script>
```
3. Trigger: WPForms submission

**Fire ViewContent on listing pages:**
```html
<script>
  fbq('track', 'ViewContent', {
    content_type: 'listing',
    content_name: document.title
  });
</script>
```
Trigger: Page URL contains `/listings/` or IDX detail page pattern.

### Step 4: Set Up Custom Audiences (for Ad Targeting)

Create these audiences in Meta Events Manager:

| Audience | Definition | Use Case |
|----------|-----------|----------|
| All Visitors (180 days) | Anyone who visited the site | Broad retargeting |
| Listing Viewers | Viewed listing detail pages | Property-interested retargeting |
| Community Page Viewers | Viewed Sunnyvale/Cupertino/etc. pages | Location-targeted ads |
| Lead Form Viewers (no submit) | Viewed contact page but didn't submit | Abandoned lead recovery |
| Converters | Submitted any form | Lookalike audience source |

---

## Part 3: Conversion Tracking for Lead Forms

### Form Tracking Matrix

| Form | Location | GA4 Event | Meta Event | Priority |
|------|----------|-----------|------------|----------|
| Home Valuation Funnel | /sell/home-valuation/ | `valuation_request` | `Lead` | Critical |
| Schedule Consultation | /contact/ | `schedule_consultation` | `Schedule` | Critical |
| Contact Form | /contact/ | `generate_lead` | `Lead` | High |
| Buyer Consultation | /buy/ | `generate_lead` | `Lead` | High |
| Newsletter Signup | Footer / Resources | `email_signup` | `Lead` | Medium |

### Thank You Page Tracking (Alternative Method)

If forms redirect to thank-you pages, this is the simplest tracking method:

1. Create thank-you pages:
   - `/thank-you/valuation/`
   - `/thank-you/consultation/`
   - `/thank-you/contact/`

2. In GA4, create events based on page_view where page_location contains `/thank-you/`

3. In GTM, fire conversion tags on thank-you page URLs:
```
Trigger: Page View
Condition: Page URL contains /thank-you/valuation/
→ Fire GA4 event: valuation_request
→ Fire Meta Pixel: Lead
```

### WPForms Confirmation Settings
1. In WPForms, set form confirmation to "Go to URL (Redirect)"
2. Set redirect URL to the appropriate thank-you page
3. Enable "Pass form field data via query strings" if needed for CRM

---

## Part 4: Google Search Console

### Setup
1. Go to [search.google.com/search-console](https://search.google.com/search-console)
2. Add property: `https://homebyjingchen.com`
3. Verify via DNS record (recommended) or HTML tag
4. Submit sitemap: `https://homebyjingchen.com/sitemap.xml` (generated by Yoast SEO or Rank Math)

### Monitor
- **Performance:** Track impressions, clicks, CTR for real estate keywords
- **Coverage:** Ensure all pages are indexed
- **Core Web Vitals:** Monitor LCP, FID, CLS

---

## Part 5: Dashboard & Reporting

### GA4 Custom Reports to Create

**1. Lead Generation Dashboard**
- Total leads by form type (valuation, consultation, contact)
- Lead conversion rate by traffic source
- Lead conversion rate by landing page
- Top converting pages

**2. Engagement Dashboard**
- Pages per session
- Average engagement time
- Most viewed listings
- Most viewed community pages

**3. Traffic Sources**
- Organic search traffic (SEO performance)
- Paid traffic (ad campaign performance)
- Direct traffic
- Referral traffic (Zillow, Realtor.com, etc.)

### Looker Studio (Optional)
- Connect GA4 to Looker Studio for visual dashboards
- Create a monthly report template Jing can review
- Include: traffic trends, top pages, conversion funnel, lead count

---

## Verification Checklist

After setup, verify everything works:

- [ ] GA4 Real-Time report shows active users when you visit the site
- [ ] Page views are tracking on all pages
- [ ] Enhanced Measurement events fire (scroll, outbound clicks)
- [ ] Form submission events appear in GA4 Real-Time → Events
- [ ] Conversions are marked correctly in GA4
- [ ] Meta Pixel fires PageView (test with Meta Pixel Helper Chrome extension)
- [ ] Meta Pixel fires Lead event on form submission
- [ ] Phone click events track correctly
- [ ] Google Search Console shows no errors
- [ ] GTM Preview mode shows all tags firing correctly
- [ ] Thank-you page redirects work for all forms
- [ ] No duplicate tracking (check for double-firing of events)
