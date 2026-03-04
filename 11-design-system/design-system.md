# Visual Design System: HomeByJingChen

## Design Philosophy

Modern luxury meets approachable warmth. The visual identity should convey professionalism and prestige while remaining inviting — never cold or intimidating. Every design choice serves the brand positioning: **strategic, trustworthy, and personal**.

---

## Color Palette

### Primary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Navy** | `#1B2A4A` | 27, 42, 74 | Primary brand color. Headers, footers, hero overlays, text |
| **Gold** | `#C9A84C` | 201, 168, 76 | Accent color. CTAs, highlights, icons, hover states |
| **White** | `#FFFFFF` | 255, 255, 255 | Primary background, text on dark backgrounds |

### Secondary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Light Navy** | `#2D4066` | 45, 64, 102 | Secondary headers, card backgrounds |
| **Dark Gold** | `#B8973E` | 184, 151, 62 | CTA hover state, gold text on light backgrounds |
| **Cream** | `#FDF8F0` | 253, 248, 240 | Warm background sections (testimonials, callouts) |
| **Light Gray** | `#F5F5F5` | 245, 245, 245 | Alternate section backgrounds |
| **Medium Gray** | `#888888` | 136, 136, 136 | Secondary text, captions, metadata |
| **Dark Text** | `#333333` | 51, 51, 51 | Body text on light backgrounds |

### Semantic Colors

| Name | Hex | Usage |
|------|-----|-------|
| **Success** | `#2D8B4E` | Form success states, positive indicators |
| **Error** | `#D44638` | Form errors, validation messages |
| **Link** | `#1B2A4A` | Text links (underlined on hover) |

### Color Application Rules
- Navy backgrounds use white text + gold accents
- White/light backgrounds use navy headings + dark text body
- Gold is reserved for CTAs, icons, and highlights — never used as a background for large sections
- Cream (#FDF8F0) used sparingly for warmth — testimonials, special callout sections
- Maintain minimum 4.5:1 contrast ratio for all text (WCAG AA)

---

## Typography

### Font Stack

| Role | Font | Fallback | Source |
|------|------|----------|--------|
| **Headings** | Playfair Display | Georgia, serif | Google Fonts |
| **Body** | Inter | -apple-system, sans-serif | Google Fonts |
| **Accent/Labels** | Inter | -apple-system, sans-serif | Google Fonts |

### Type Scale

| Element | Size (Desktop) | Size (Mobile) | Weight | Line Height | Letter Spacing |
|---------|---------------|---------------|--------|-------------|---------------|
| H1 | 48px | 32px | 700 | 1.2 | -0.02em |
| H2 | 36px | 28px | 700 | 1.3 | -0.01em |
| H3 | 28px | 22px | 600 | 1.4 | 0 |
| H4 | 22px | 18px | 600 | 1.4 | 0 |
| H5 | 18px | 16px | 600 | 1.5 | 0 |
| Body Large | 18px | 16px | 400 | 1.8 | 0 |
| Body | 16px | 15px | 400 | 1.7 | 0 |
| Body Small | 14px | 13px | 400 | 1.6 | 0 |
| Caption | 12px | 12px | 500 | 1.5 | 0.05em |
| Button | 16px | 14px | 700 | 1 | 0.03em |

### Typography Rules
- Headings (H1-H2): Playfair Display — adds luxury feel
- Headings (H3-H5): Inter Semi-Bold — clean and modern
- Body text: Inter Regular — excellent readability
- Maximum line length: 720px for body text
- Paragraph spacing: 24px between paragraphs
- Use sentence case for headings (not Title Case for all words)

---

## Spacing System

Based on an 8px grid.

| Token | Value | Usage |
|-------|-------|-------|
| `xs` | 4px | Tight spacing between related elements |
| `sm` | 8px | Inner padding for compact elements |
| `md` | 16px | Standard element padding |
| `lg` | 24px | Card padding, section element gaps |
| `xl` | 32px | Between content groups |
| `2xl` | 48px | Between page sections (mobile) |
| `3xl` | 64px | Between page sections (tablet) |
| `4xl` | 80px | Between page sections (desktop) |
| `5xl` | 120px | Hero section padding |

### Section Spacing
- Desktop section padding: 80px top/bottom
- Tablet section padding: 64px top/bottom
- Mobile section padding: 48px top/bottom
- Content max-width: 1200px (centered)
- Text content max-width: 720px (centered, for readability)

---

## Button Styles

### Primary Button (Gold)
```css
.btn-primary {
  background-color: #C9A84C;
  color: #FFFFFF;
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: 0.03em;
  padding: 16px 32px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.btn-primary:hover {
  background-color: #B8973E;
  transform: translateY(-1px);
}
```

### Secondary Button (Outline)
```css
.btn-secondary {
  background-color: transparent;
  color: #FFFFFF;
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: 0.03em;
  padding: 14px 30px;
  border: 2px solid #FFFFFF;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  background-color: #FFFFFF;
  color: #1B2A4A;
}
```

### Text Link Button
```css
.btn-text {
  background: none;
  color: #C9A84C;
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  font-weight: 600;
  padding: 0;
  border: none;
  cursor: pointer;
  text-decoration: none;
  border-bottom: 2px solid transparent;
  transition: border-color 0.3s ease;
}

.btn-text:hover {
  border-bottom-color: #C9A84C;
}
```

### Button Sizes
| Size | Padding | Font Size |
|------|---------|-----------|
| Small | 10px 20px | 14px |
| Default | 16px 32px | 16px |
| Large | 20px 40px | 18px |

---

## Card Styles

### Listing Card
```css
.listing-card {
  background: #FFFFFF;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.listing-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.listing-card__image {
  width: 100%;
  height: 240px;
  object-fit: cover;
}

.listing-card__content {
  padding: 24px;
}

.listing-card__price {
  font-family: 'Inter', sans-serif;
  font-size: 24px;
  font-weight: 700;
  color: #1B2A4A;
}

.listing-card__details {
  font-size: 14px;
  color: #888;
  margin-top: 8px;
}
```

### Testimonial Card
```css
.testimonial-card {
  background: #FFFFFF;
  border-radius: 12px;
  padding: 32px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
}

.testimonial-card__stars {
  color: #C9A84C;
  font-size: 18px;
  letter-spacing: 2px;
  margin-bottom: 16px;
}

.testimonial-card__quote {
  font-size: 16px;
  font-style: italic;
  line-height: 1.7;
  color: #333;
}

.testimonial-card__author {
  font-size: 14px;
  font-weight: 700;
  color: #1B2A4A;
  margin-top: 16px;
}
```

### Community Card
```css
.community-card {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  height: 300px;
}

.community-card__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.community-card:hover .community-card__image {
  transform: scale(1.05);
}

.community-card__overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 24px;
  background: linear-gradient(transparent, rgba(27, 42, 74, 0.85));
  color: #FFFFFF;
}

.community-card__name {
  font-family: 'Playfair Display', serif;
  font-size: 24px;
  font-weight: 700;
}
```

---

## Form Styles

```css
.form-input {
  width: 100%;
  padding: 14px 16px;
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  color: #333;
  background: #FFFFFF;
  border: 1.5px solid #DDD;
  border-radius: 6px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.form-input:focus {
  border-color: #C9A84C;
  box-shadow: 0 0 0 3px rgba(201, 168, 76, 0.15);
  outline: none;
}

.form-input::placeholder {
  color: #AAA;
}

.form-label {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  font-weight: 600;
  color: #1B2A4A;
  margin-bottom: 6px;
  display: block;
}

.form-error {
  font-size: 13px;
  color: #D44638;
  margin-top: 4px;
}
```

---

## Icon Style

- **Style:** Line icons (not filled), consistent 1.5px stroke
- **Color:** Gold (#C9A84C) on light backgrounds, White on dark backgrounds
- **Size:** 48px for feature icons, 24px for inline icons, 16px for UI icons
- **Library:** Lucide Icons or Phosphor Icons (both open source, consistent line style)

---

## Shadow System

| Level | Value | Usage |
|-------|-------|-------|
| None | none | Flat elements |
| Subtle | `0 2px 8px rgba(0,0,0,0.04)` | Resting cards |
| Default | `0 4px 20px rgba(0,0,0,0.06)` | Cards, dropdowns |
| Elevated | `0 8px 30px rgba(0,0,0,0.12)` | Hover states, modals |
| Overlay | `0 16px 48px rgba(0,0,0,0.16)` | Floating elements, dialogs |

---

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| Small | 4px | Tags, badges |
| Default | 6px | Buttons, inputs |
| Medium | 12px | Cards, images |
| Large | 20px | Feature cards |
| Full | 9999px | Pills, avatars |

---

## Responsive Breakpoints

| Breakpoint | Width | Columns |
|-----------|-------|---------|
| Mobile | < 768px | 1 column |
| Tablet | 768px – 1024px | 2 columns |
| Desktop | > 1024px | 3-4 columns |
| Wide | > 1440px | Content max-width 1200px, centered |

---

## Elementor Global Settings

Apply these in **Elementor → Site Settings → Global**:

### Global Colors
- Primary: #1B2A4A (Navy)
- Secondary: #C9A84C (Gold)
- Text: #333333
- Accent: #C9A84C

### Global Fonts
- Primary: Playfair Display
- Secondary: Inter
- Text: Inter
- Accent: Inter

### Default Container Width
- Max width: 1200px
- Padding: 20px (mobile), 40px (tablet), 0 (desktop with max-width)

### Button Defaults
- Typography: Inter, 16px, 700
- Border radius: 6px
- Padding: 16px 32px
