# WordPress Performance Optimization Checklist

## Priority: Critical (Do First)

### 1. Hosting Configuration
- [ ] Use Cloudways (DigitalOcean 2GB+ droplet) or SiteGround (GoGeek plan)
- [ ] Enable server-level caching (Cloudways Varnish / SiteGround SuperCacher)
- [ ] Use PHP 8.2+ (latest stable version)
- [ ] Set memory limit to at least 256MB (`WP_MEMORY_LIMIT`)
- [ ] Enable GZIP compression at server level
- [ ] Ensure HTTP/2 is enabled

### 2. Caching Plugin: WP Rocket
- [ ] Install and activate WP Rocket
- [ ] **Cache tab:**
  - Enable page caching for mobile devices (separate cache)
  - Set cache lifespan to 10 hours
- [ ] **File Optimization tab:**
  - Minify CSS files
  - Combine CSS files (test carefully — may break Elementor styles)
  - Minify JavaScript files
  - Defer JavaScript loading
  - Delay JavaScript execution (add exceptions for critical scripts)
- [ ] **Media tab:**
  - Enable LazyLoad for images
  - Enable LazyLoad for iframes/videos
  - Add missing image dimensions
  - Enable WebP compatibility (works with image optimization plugins)
- [ ] **Preload tab:**
  - Enable sitemap-based preloading
  - Preload fonts (add Google Fonts URLs)
  - Add prefetch DNS for external domains:
    - `fonts.googleapis.com`
    - `fonts.gstatic.com`
    - `www.google-analytics.com`
    - `www.googletagmanager.com`
    - `connect.facebook.net` (if using Meta Pixel)
    - IDX Broker domain
- [ ] **Advanced Rules tab:**
  - Never cache: `/wp-admin/`, cart/checkout (if applicable)
  - Exclude dynamic IDX pages from cache if needed
- [ ] **CDN tab:**
  - Enable CDN and enter CDN URL

### 3. CDN Setup
- [ ] Set up Cloudflare (free plan is sufficient)
  - Point DNS to Cloudflare
  - Enable "Full (Strict)" SSL mode
  - Enable Auto Minify (HTML, CSS, JS)
  - Enable Brotli compression
  - Set Browser Cache TTL to 1 month
  - Enable "Always Use HTTPS"
  - Create page rule: bypass cache for `/wp-admin/*`
- [ ] **OR** use BunnyCDN / KeyCDN with WP Rocket integration

---

## Priority: High (Do Next)

### 4. Image Optimization
- [ ] Install **ShortPixel** or **Imagify** plugin
- [ ] Configure settings:
  - Compression level: Lossy (best size reduction, minimal quality loss)
  - Convert to WebP automatically
  - Resize large images to max 2560px width
  - Enable bulk optimization for existing media
- [ ] Optimize all existing images (bulk process)
- [ ] Set upload rules: resize images on upload to max 2560px
- [ ] Use proper image sizes in Elementor (don't use full-size images in small containers)
- [ ] For hero images: max 1920px wide, compress to under 200KB

### 5. Elementor Optimization
- [ ] **Elementor → Settings → Performance:**
  - Enable Improved Asset Loading
  - Enable CSS Print Method: External File
  - Disable Google Fonts loading in Elementor (load via theme/plugin instead for fewer requests)
- [ ] **Elementor → Settings → Features:**
  - Disable unused features (e.g., Optimized Markup)
  - Enable Element Caching (Elementor Pro 3.21+)
- [ ] Reduce number of Elementor sections per page (combine where possible)
- [ ] Avoid excessive use of inner sections/columns
- [ ] Use lightweight widgets over heavy ones when possible
- [ ] Minimize use of motion effects and animations (each adds CSS/JS)

### 6. Database Optimization
- [ ] Install **WP-Optimize** or use WP Rocket's database tools
- [ ] Clean up:
  - Post revisions (keep last 5)
  - Auto-drafts
  - Trashed posts
  - Spam/trashed comments
  - Transient options
  - Expired transients
- [ ] Optimize database tables
- [ ] Set revision limit in wp-config.php:
  ```php
  define('WP_POST_REVISIONS', 5);
  ```
- [ ] Schedule weekly auto-cleanup

---

## Priority: Medium (Optimization Pass)

### 7. Plugin Audit
- [ ] Remove all inactive plugins (not just deactivate — delete)
- [ ] Audit active plugins — remove any that aren't essential
- [ ] Check for plugin conflicts affecting performance
- [ ] Use **Asset CleanUp** or **Perfmatters** to disable scripts/styles per page:
  - Disable WooCommerce scripts on non-shop pages (if installed)
  - Disable WPForms scripts on pages without forms
  - Disable Contact Form 7 on pages without forms
  - Load IDX scripts only on listing pages

### 8. Font Optimization
- [ ] Self-host Google Fonts (use **OMGF** plugin or manually download)
  - Download Playfair Display and Inter from Google Fonts
  - Add to theme directory
  - Load via `@font-face` in custom CSS
- [ ] Preload critical fonts:
  ```html
  <link rel="preload" href="/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/fonts/playfair-display-700.woff2" as="font" type="font/woff2" crossorigin>
  ```
- [ ] Use `font-display: swap` for all custom fonts
- [ ] Limit font weights loaded: Inter (400, 600, 700), Playfair Display (700)

### 9. Critical CSS & Above-the-Fold Optimization
- [ ] WP Rocket handles critical CSS automatically (ensure "Remove Unused CSS" is enabled on Pro plan)
- [ ] Verify hero section loads immediately without layout shift
- [ ] Preload hero background image:
  ```html
  <link rel="preload" href="/images/hero-bg.webp" as="image">
  ```
- [ ] Ensure above-the-fold content renders without JavaScript

---

## Priority: Ongoing Maintenance

### 10. Core Web Vitals Monitoring
- [ ] Test with Google PageSpeed Insights (target 90+ mobile, 95+ desktop)
- [ ] Test with GTmetrix
- [ ] Test with WebPageTest

**Target Metrics:**
| Metric | Target | What It Measures |
|--------|--------|-----------------|
| LCP (Largest Contentful Paint) | < 2.5s | Hero image/text load time |
| FID/INP (Interaction to Next Paint) | < 200ms | Responsiveness to user input |
| CLS (Cumulative Layout Shift) | < 0.1 | Visual stability |
| TTFB (Time to First Byte) | < 800ms | Server response time |

### 11. Regular Maintenance Schedule
- [ ] **Weekly:** Review and clear cache after content updates
- [ ] **Monthly:** Run database optimization, check broken links
- [ ] **Quarterly:** Full plugin audit, update all plugins/themes, re-test Core Web Vitals
- [ ] **After every major change:** Clear all caches, test pagespeed

---

## WordPress Configuration (wp-config.php)

Add these performance-related constants:

```php
// Limit post revisions
define('WP_POST_REVISIONS', 5);

// Increase memory limit
define('WP_MEMORY_LIMIT', '256M');

// Disable WordPress CRON (use server cron instead for reliability)
define('DISABLE_WP_CRON', true);

// Autosave interval (seconds) — reduce database writes
define('AUTOSAVE_INTERVAL', 120);
```

If disabling WP_CRON, set up a server-level cron job:
```
*/5 * * * * curl -s https://homebyjingchen.com/wp-cron.php > /dev/null 2>&1
```

---

## Expected Performance Results

| Metric | Before Optimization | After Optimization |
|--------|--------------------|--------------------|
| PageSpeed Mobile | 40-60 | 85-95 |
| PageSpeed Desktop | 60-75 | 95-100 |
| Page Load Time | 4-8 seconds | 1.5-2.5 seconds |
| Page Size | 3-5 MB | 800KB-1.5MB |
| HTTP Requests | 60-100+ | 20-35 |

*Results depend on hosting quality, content complexity, and IDX integration overhead.*
