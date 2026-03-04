<?php
/**
 * HomeByJingChen — Custom Functions (FREE STACK)
 *
 * HOW TO ADD: Install "Code Snippets" plugin (free), create a new snippet,
 * paste this code, and activate it. Do NOT edit functions.php directly.
 */

// ============================================
// 1. LOAD GOOGLE FONTS (free from Google)
// ============================================
add_action('wp_enqueue_scripts', 'jc_enqueue_fonts');
function jc_enqueue_fonts() {
    wp_enqueue_style(
        'jc-google-fonts',
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Playfair+Display:wght@700&display=swap',
        array(),
        null
    );
}

// ============================================
// 2. LIMIT POST REVISIONS (performance)
// ============================================
if (!defined('WP_POST_REVISIONS')) {
    define('WP_POST_REVISIONS', 5);
}

// ============================================
// 3. CONTACT FORM 7: TRACK SUBMISSIONS WITH GA4
// ============================================
add_action('wp_footer', 'jc_cf7_ga4_tracking');
function jc_cf7_ga4_tracking() {
    ?>
    <script>
    document.addEventListener('wpcf7mailsent', function(event) {
        var formTitle = event.detail.contactFormId;
        // GA4 tracking
        if (typeof gtag === 'function') {
            gtag('event', 'generate_lead', {
                'form_name': 'CF7 Form ' + formTitle,
                'form_id': formTitle
            });
        }
        // Meta Pixel tracking
        if (typeof fbq === 'function') {
            fbq('track', 'Lead', {
                content_name: 'CF7 Form ' + formTitle,
                content_category: 'Lead Generation'
            });
        }
    });
    </script>
    <?php
}

// ============================================
// 4. TRACK PHONE & EMAIL CLICKS
// ============================================
add_action('wp_footer', 'jc_track_click_events');
function jc_track_click_events() {
    ?>
    <script>
    document.addEventListener('click', function(e) {
        var link = e.target.closest('a');
        if (!link) return;
        var href = link.getAttribute('href') || '';
        if (href.startsWith('tel:') && typeof gtag === 'function') {
            gtag('event', 'phone_click', { link_url: href });
        }
        if (href.startsWith('mailto:') && typeof gtag === 'function') {
            gtag('event', 'email_click', { link_url: href });
        }
    });
    </script>
    <?php
}

// ============================================
// 5. ADD SCHEMA MARKUP — RealEstateAgent (free SEO boost)
// ============================================
add_action('wp_head', 'jc_schema_markup');
function jc_schema_markup() {
    if (!is_front_page()) return;
    ?>
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "RealEstateAgent",
        "name": "Jing Chen",
        "description": "Data-driven Silicon Valley realtor helping families buy and sell homes.",
        "url": "https://homesbyjingchen.com",
        "telephone": "(408) XXX-XXXX",
        "image": "https://homesbyjingchen.com/wp-content/uploads/jing-chen-headshot.jpg",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Sunnyvale",
            "addressRegion": "CA",
            "addressCountry": "US"
        },
        "areaServed": [
            {"@type": "City", "name": "Sunnyvale"},
            {"@type": "City", "name": "Cupertino"},
            {"@type": "City", "name": "Palo Alto"},
            {"@type": "City", "name": "Mountain View"},
            {"@type": "City", "name": "Santa Clara"}
        ],
        "knowsLanguage": ["en", "zh"],
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "5.0",
            "reviewCount": "50"
        }
    }
    </script>
    <?php
}

// ============================================
// 6. STYLE CONTACT FORM 7 TO MATCH DESIGN SYSTEM
// ============================================
add_action('wp_head', 'jc_cf7_styles');
function jc_cf7_styles() {
    ?>
    <style>
    .wpcf7 input[type="text"],
    .wpcf7 input[type="email"],
    .wpcf7 input[type="tel"],
    .wpcf7 input[type="url"],
    .wpcf7 textarea,
    .wpcf7 select {
        width: 100%;
        padding: 14px 16px;
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        border: 1.5px solid #DDD;
        border-radius: 6px;
        transition: border-color 0.3s, box-shadow 0.3s;
        box-sizing: border-box;
    }
    .wpcf7 input:focus,
    .wpcf7 textarea:focus,
    .wpcf7 select:focus {
        border-color: #C9A84C;
        box-shadow: 0 0 0 3px rgba(201, 168, 76, 0.15);
        outline: none;
    }
    .wpcf7 label {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        font-weight: 600;
        color: #1B2A4A;
        display: block;
        margin-bottom: 6px;
    }
    .wpcf7 input[type="submit"] {
        background: #C9A84C;
        color: #fff;
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        font-weight: 700;
        padding: 16px 32px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background 0.3s;
        letter-spacing: 0.03em;
    }
    .wpcf7 input[type="submit"]:hover {
        background: #B8973E;
    }
    .wpcf7-response-output {
        border-radius: 6px !important;
        font-family: 'Inter', sans-serif !important;
    }
    .wpcf7 p {
        margin-bottom: 16px;
    }
    </style>
    <?php
}

// ============================================
// 7. SECURITY: REMOVE WP VERSION FROM HEAD
// ============================================
remove_action('wp_head', 'wp_generator');

// ============================================
// 8. DISABLE WORDPRESS EMOJI SCRIPTS (performance)
// ============================================
add_action('init', 'jc_disable_emojis');
function jc_disable_emojis() {
    remove_action('wp_head', 'print_emoji_detection_script', 7);
    remove_action('wp_print_styles', 'print_emoji_styles');
    remove_action('admin_print_scripts', 'print_emoji_detection_script');
    remove_action('admin_print_styles', 'print_emoji_styles');
}
