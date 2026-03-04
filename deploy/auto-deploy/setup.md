# Auto-Deploy Setup — ONE thing to do first

## Create an Application Password in WordPress

1. Log in to WordPress admin
2. Go to **Users → Your Profile**
3. Scroll to **Application Passwords**
4. Name: `deploy-script`
5. Click **Add New Application Password**
6. **Copy the password** (shown once only)

## Create .env file

```bash
cd deploy/auto-deploy
cp .env.example .env
```

Edit `.env`:
```
WP_URL=https://homesbyjingchen.com
WP_USER=your_username
WP_APP_PASSWORD=the_password_you_just_copied
GA4_MEASUREMENT_ID=G-XXXXXXXXXX    # optional
META_PIXEL_ID=123456789            # optional
```

## Run

```bash
pip3 install -r requirements.txt
python3 deploy.py
```

## What it deploys automatically

Everything:

- 19 pages with full HTML content
- Custom CSS (navy/gold branding, fonts, form styles)
- Google Fonts (Inter + Playfair Display)
- Contact Form 7 forms (contact + consultation)
- Home valuation 3-step funnel
- Testimonials section with HTML/CSS/JS
- Navigation menu with dropdowns
- Homepage setting
- Yoast SEO titles + meta descriptions for all pages
- Schema markup (RealEstateAgent) on homepage
- GA4 tracking code (if ID provided)
- Meta Pixel code (if ID provided)
- Phone/email click tracking
- Form submission conversion tracking
- Old pages moved to draft

## Re-running

Safe to re-run anytime — it updates existing pages instead of creating duplicates.
