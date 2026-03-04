# Seller Home Valuation Funnel: 3-Step Lead Capture

## Overview

A multi-step form funnel that converts seller traffic into qualified leads. The funnel uses progressive disclosure (asking for increasingly personal information across steps) and persuasive microcopy to maximize completion rates.

**Goal:** Capture seller contact info in exchange for a personalized home valuation.
**Implementation:** WPForms Pro multi-page form, embedded via Elementor on `/sell/home-valuation/`

---

## UX Flow Diagram

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌───────────────┐
│                 │    │                 │    │                 │    │               │
│  STEP 1         │───▶│  STEP 2         │───▶│  STEP 3         │───▶│  THANK YOU    │
│  Property       │    │  Property       │    │  Contact        │    │  Confirmation │
│  Address        │    │  Details        │    │  Information    │    │               │
│                 │    │                 │    │                 │    │               │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └───────────────┘
     Step 1 of 3           Step 2 of 3           Step 3 of 3          Redirect/Modal
```

---

## Step 1: Property Address

### Purpose
Low-friction entry. The user only needs to type their address — the easiest possible action to start.

### Layout
```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│          What's Your Silicon Valley Home Worth?                  │
│                                                                  │
│     Get a complimentary, expert-prepared home valuation —        │
│     not an algorithm. A real analysis from someone who           │
│     knows your neighborhood.                                    │
│                                                                  │
│     ┌──────────────────────────────────────────────────────┐     │
│     │  Enter your property address                         │     │
│     │  ┌──────────────────────────────────────────────┐    │     │
│     │  │  🔍  Start typing your address...            │    │     │
│     │  └──────────────────────────────────────────────┘    │     │
│     │                                                      │     │
│     │               [ Next Step → ]                        │     │
│     │                                                      │     │
│     │  🔒 Your information is private and never shared.   │     │
│     └──────────────────────────────────────────────────────┘     │
│                                                                  │
│  ● ○ ○  Step 1 of 3                                             │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Fields
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| Property Address | Google Places Autocomplete or text input | Yes | Autocomplete preferred for UX |

### Microcopy
- **Headline:** What's Your Silicon Valley Home Worth?
- **Subheadline:** Get a complimentary, expert-prepared home valuation — not an algorithm. A real analysis from someone who knows your neighborhood.
- **Placeholder:** Start typing your address...
- **Privacy note:** Your information is private and never shared.
- **Button:** Next Step →

---

## Step 2: Property Details

### Purpose
Gather property context to personalize the valuation. These questions also increase perceived investment (sunk cost) making it more likely the user completes Step 3.

### Layout
```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│          Tell Us About Your Property                             │
│                                                                  │
│     This helps us prepare an accurate valuation                  │
│     tailored to your home.                                       │
│                                                                  │
│     ┌──────────────────────────────────────────────────────┐     │
│     │                                                      │     │
│     │  Property Type                                       │     │
│     │  ┌──────────────────────────────────────────────┐    │     │
│     │  │  Single Family ▾                             │    │     │
│     │  └──────────────────────────────────────────────┘    │     │
│     │                                                      │     │
│     │  Bedrooms              Bathrooms                     │     │
│     │  ┌────────────┐        ┌────────────┐                │     │
│     │  │  3 ▾       │        │  2 ▾       │                │     │
│     │  └────────────┘        └────────────┘                │     │
│     │                                                      │     │
│     │  Approximate Square Footage                          │     │
│     │  ┌──────────────────────────────────────────────┐    │     │
│     │  │  e.g., 1,800                                 │    │     │
│     │  └──────────────────────────────────────────────┘    │     │
│     │                                                      │     │
│     │  Condition                                           │     │
│     │  ┌──────────────────────────────────────────────┐    │     │
│     │  │  Good — well maintained ▾                    │    │     │
│     │  └──────────────────────────────────────────────┘    │     │
│     │                                                      │     │
│     │  Timeline to Sell                                    │     │
│     │  ┌──────────────────────────────────────────────┐    │     │
│     │  │  Within 3 months ▾                           │    │     │
│     │  └──────────────────────────────────────────────┘    │     │
│     │                                                      │     │
│     │   [ ← Back ]              [ Almost Done → ]          │     │
│     │                                                      │     │
│     └──────────────────────────────────────────────────────┘     │
│                                                                  │
│  ● ● ○  Step 2 of 3                                             │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Fields
| Field | Type | Required | Options |
|-------|------|----------|---------|
| Property Type | Dropdown | Yes | Single Family, Townhome, Condo, Multi-Family |
| Bedrooms | Dropdown | Yes | 1, 2, 3, 4, 5, 6+ |
| Bathrooms | Dropdown | Yes | 1, 1.5, 2, 2.5, 3, 3.5, 4+ |
| Approximate Sq Ft | Number input | No | Placeholder: "e.g., 1,800" |
| Condition | Dropdown | Yes | Excellent — recently updated, Good — well maintained, Fair — needs some work, Needs major renovation |
| Timeline to Sell | Dropdown | Yes | Just exploring, Within 6 months, Within 3 months, ASAP |

### Microcopy
- **Headline:** Tell Us About Your Property
- **Subheadline:** This helps us prepare an accurate valuation tailored to your home.
- **Back button:** ← Back
- **Forward button:** Almost Done →

---

## Step 3: Contact Information

### Purpose
Capture lead contact information. By this point, the user has invested effort in Steps 1-2 and is highly likely to complete.

### Layout
```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│          Where Should We Send Your Valuation?                    │
│                                                                  │
│     Jing will personally review your property details            │
│     and send you a custom valuation within 24 hours.             │
│                                                                  │
│     ┌──────────────────────────────────────────────────────┐     │
│     │                                                      │     │
│     │  First Name                Last Name                 │     │
│     │  ┌────────────────┐        ┌────────────────┐        │     │
│     │  │                │        │                │        │     │
│     │  └────────────────┘        └────────────────┘        │     │
│     │                                                      │     │
│     │  Email Address                                       │     │
│     │  ┌──────────────────────────────────────────────┐    │     │
│     │  │                                              │    │     │
│     │  └──────────────────────────────────────────────┘    │     │
│     │                                                      │     │
│     │  Phone Number                                        │     │
│     │  ┌──────────────────────────────────────────────┐    │     │
│     │  │                                              │    │     │
│     │  └──────────────────────────────────────────────┘    │     │
│     │                                                      │     │
│     │  Preferred Language                                  │     │
│     │  ○ English   ○ 中文 (Mandarin)                       │     │
│     │                                                      │     │
│     │  Anything else you'd like us to know? (Optional)     │     │
│     │  ┌──────────────────────────────────────────────┐    │     │
│     │  │                                              │    │     │
│     │  └──────────────────────────────────────────────┘    │     │
│     │                                                      │     │
│     │   [ ← Back ]         [ Get My Valuation ]            │     │
│     │                                                      │     │
│     │  🔒 We respect your privacy. No spam, ever.         │     │
│     └──────────────────────────────────────────────────────┘     │
│                                                                  │
│  ● ● ●  Step 3 of 3                                             │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Fields
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| First Name | Text | Yes | |
| Last Name | Text | Yes | |
| Email | Email | Yes | |
| Phone | Tel | Yes | |
| Preferred Language | Radio | No | English (default), 中文 (Mandarin) |
| Additional Notes | Textarea | No | "Anything else you'd like us to know?" |

### Microcopy
- **Headline:** Where Should We Send Your Valuation?
- **Subheadline:** Jing will personally review your property details and send you a custom valuation within 24 hours.
- **Submit button:** Get My Valuation
- **Privacy note:** We respect your privacy. No spam, ever.

---

## Thank You / Confirmation

### Layout
```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│                      ✓                                           │
│                                                                  │
│          Your Valuation Request Has Been Received!               │
│                                                                  │
│     Jing will personally review your property and send you       │
│     a detailed home valuation within 24 hours.                   │
│                                                                  │
│     In the meantime:                                             │
│                                                                  │
│     → Explore homes in your neighborhood                         │
│     → Read the latest Silicon Valley market report               │
│     → Learn about Jing's selling process                         │
│                                                                  │
│     Questions? Call Jing directly: (408) XXX-XXXX                │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Microcopy
- **Headline:** Your Valuation Request Has Been Received!
- **Body:** Jing will personally review your property and send you a detailed home valuation within 24 hours.
- **Next steps:** Links to community pages, market report, and selling process

---

## Implementation Notes

### WPForms Pro Configuration
1. Create a multi-page form with 3 pages (page breaks between steps)
2. Enable AJAX submission for seamless experience
3. Connect to email notification (Jing receives lead details)
4. Connect to CRM if available (e.g., Follow Up Boss, kvCORE)
5. Set up Google Analytics event tracking on each step and final submission

### Conversion Optimization
- **Progress indicator** — Visual dots/bar showing 3 steps (reduces abandonment)
- **Low-friction start** — Step 1 only requires address (single field)
- **Sunk cost progression** — By Step 3, users have invested effort and are likely to complete
- **Privacy reassurance** — Lock icon + privacy text on Steps 1 and 3
- **Personal touch** — "Jing will personally review" builds trust over automated tools
- **24-hour promise** — Specific timeline creates urgency and expectation
- **No generic lead pages** — This funnel is branded to Jing, not a generic "find your home's value" template

### Analytics Events to Track
| Event | Trigger | GA4 Event Name |
|-------|---------|---------------|
| Funnel Start | Step 1 loads | `valuation_funnel_start` |
| Step 1 Complete | "Next Step" clicked | `valuation_step1_complete` |
| Step 2 Complete | "Almost Done" clicked | `valuation_step2_complete` |
| Form Submitted | "Get My Valuation" clicked | `valuation_submitted` |
| Abandonment | User leaves before completing | Track via exit rate per step |

### A/B Testing Opportunities
- **Headline variants:** "What's Your Home Worth?" vs. "Your Free Silicon Valley Home Valuation"
- **Step 2 field count:** Full details vs. minimal (just type + timeline)
- **CTA copy:** "Get My Valuation" vs. "See My Home's Value" vs. "Request My Free Report"
- **Social proof addition:** Add "150+ valuations completed this year" near the form
