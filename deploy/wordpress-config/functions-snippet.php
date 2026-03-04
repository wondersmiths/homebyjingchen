<?php
/**
 * HomeByJingChen — Custom Functions
 *
 * HOW TO ADD: Install "Code Snippets" plugin, create a new snippet,
 * paste this code, and activate it. Do NOT edit functions.php directly.
 */

// ============================================
// 1. LOAD GOOGLE FONTS (Self-hosted is better, but this works to start)
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
// 2. LIMIT POST REVISIONS
// ============================================
if (!defined('WP_POST_REVISIONS')) {
    define('WP_POST_REVISIONS', 5);
}

// ============================================
// 3. WPFORMS: TRACK SUBMISSIONS WITH GA4
// ============================================
add_action('wpforms_frontend_output_after', 'jc_wpforms_ga4_tracking', 10, 2);
function jc_wpforms_ga4_tracking($form_data, $form) {
    $form_name = esc_js($form_data['settings']['form_title']);
    $form_id = esc_js($form_data['id']);
    ?>
    <script>
    (function() {
        var form = document.querySelector('#wpforms-form-<?php echo $form_id; ?>');
        if (!form) return;
        form.addEventListener('submit', function() {
            if (typeof gtag === 'function') {
                gtag('event', 'generate_lead', {
                    'form_name': '<?php echo $form_name; ?>',
                    'form_id': '<?php echo $form_id; ?>'
                });
            }
            if (typeof fbq === 'function') {
                fbq('track', 'Lead', {
                    content_name: '<?php echo $form_name; ?>',
                    content_category: 'Lead Generation'
                });
            }
        });
    })();
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
// 5. ADD SCHEMA MARKUP — RealEstateAgent
// ============================================
add_action('wp_head', 'jc_schema_markup');
function jc_schema_markup() {
    // Only output on homepage
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
// 6. SECURITY: REMOVE WP VERSION FROM HEAD
// ============================================
remove_action('wp_head', 'wp_generator');

// ============================================
// 7. DISABLE WORDPRESS EMOJI SCRIPTS (performance)
// ============================================
add_action('init', 'jc_disable_emojis');
function jc_disable_emojis() {
    remove_action('wp_head', 'print_emoji_detection_script', 7);
    remove_action('wp_print_styles', 'print_emoji_styles');
    remove_action('admin_print_scripts', 'print_emoji_detection_script');
    remove_action('admin_print_styles', 'print_emoji_styles');
}
