# Auto-Deploy Setup — One-Time Steps in WordPress Admin

Before running the deploy script, do these 3 things in wp-admin:

## Step 1: Create an Application Password

1. Go to **Users → Your Profile**
2. Scroll to **Application Passwords** section
3. Enter name: `deploy-script`
4. Click **Add New Application Password**
5. Copy the generated password (you won't see it again)
6. Save it — you'll use it in the `.env` file

## Step 2: Install Required Free Plugins

Go to **Plugins → Add New** and install + activate:

- Elementor
- Kadence Blocks
- Contact Form 7
- Flamingo
- WP Super Cache
- ShortPixel (or Smush)
- Code Snippets
- Yoast SEO (already installed)

## Step 3: Create .env File

In the `deploy/auto-deploy/` folder, create a file named `.env`:

```
WP_URL=https://homesbyjingchen.com
WP_USER=your_admin_username
WP_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx xxxx
```

Replace with your actual credentials. This file is gitignored.
