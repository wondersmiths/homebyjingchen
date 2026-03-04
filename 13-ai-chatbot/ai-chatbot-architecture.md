# Future AI Chat Assistant: Architecture Overview

## Vision

An AI-powered chat assistant embedded on HomeByJingChen.com that can answer listing questions, provide neighborhood information, schedule showings, and qualify leads — operating 24/7 as a virtual extension of Jing's service.

**Phase:** Future feature (Phase 2, post-launch)

---

## Core Capabilities

### 1. Listing Questions
- "What homes are available in Cupertino under $2M?"
- "Tell me about this listing at 123 Main St"
- "How many bedrooms does this home have?"
- "What's the price per square foot?"

### 2. Neighborhood Information
- "What are the best schools in Sunnyvale?"
- "How's the market in Palo Alto right now?"
- "What's the commute from Mountain View to San Francisco?"
- "Tell me about the Monta Vista neighborhood"

### 3. Showing Scheduling
- "I'd like to schedule a showing"
- "Can I see this home this weekend?"
- "Is there an open house coming up?"

### 4. Lead Qualification
- "I'm thinking about selling my home"
- "We're relocating from New York"
- "What's my home worth?"
- Qualify based on timeline, budget, motivation

### 5. General Real Estate Q&A
- "How does the buying process work?"
- "What do I need for pre-approval?"
- "What are closing costs?"

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    WEBSITE (Frontend)                        │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              Chat Widget (Bottom-Right)                │  │
│  │  ┌─────────────────────────────────────────────────┐  │  │
│  │  │  Hi! I'm Jing's assistant. How can I            │  │  │
│  │  │  help you today?                                 │  │  │
│  │  │                                                  │  │  │
│  │  │  ○ I want to buy a home                          │  │  │
│  │  │  ○ I want to sell my home                        │  │  │
│  │  │  ○ I have a question about a listing             │  │  │
│  │  │  ○ Just browsing                                 │  │  │
│  │  │                                                  │  │  │
│  │  │  ┌──────────────────────────┐ [Send]             │  │  │
│  │  │  │  Type your message...    │                    │  │  │
│  │  │  └──────────────────────────┘                    │  │  │
│  │  └─────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────┬───────────────────────────────────────┘
                      │ WebSocket / REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   BACKEND API (Node.js / Python)            │
│                                                             │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │ Conversation │  │    Intent    │  │   Response        │  │
│  │  Manager     │──│   Router     │──│   Generator       │  │
│  │             │  │              │  │  (Claude API)     │  │
│  └─────────────┘  └──────────────┘  └───────────────────┘  │
│         │                │                    │             │
│         ▼                ▼                    ▼             │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │  Session     │  │   Tool       │  │   Knowledge       │  │
│  │  Store       │  │   Functions  │  │   Base (RAG)      │  │
│  │ (Redis)      │  │              │  │                   │  │
│  └─────────────┘  └──────┬───────┘  └───────┬───────────┘  │
│                          │                   │              │
└──────────────────────────┼───────────────────┼──────────────┘
                           │                   │
              ┌────────────┼───────────────────┼────────┐
              │            ▼                   ▼        │
              │  ┌──────────────┐  ┌────────────────┐   │
              │  │  External     │  │  Vector DB     │   │
              │  │  Services     │  │  (Pinecone /   │   │
              │  │              │  │   Supabase)    │   │
              │  │  • IDX API   │  │                │   │
              │  │  • Calendar  │  │  Embedded:     │   │
              │  │  • CRM       │  │  • Listings    │   │
              │  │  • Email     │  │  • Community   │   │
              │  │              │  │    pages       │   │
              │  │              │  │  • FAQs        │   │
              │  │              │  │  • Market data │   │
              │  └──────────────┘  └────────────────┘   │
              │         INTEGRATIONS                     │
              └──────────────────────────────────────────┘
```

---

## Technical Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **LLM** | Claude API (Sonnet for speed, Opus for complex queries) | Natural language understanding and response generation |
| **Backend** | Node.js (Express) or Python (FastAPI) | API server, conversation management |
| **Vector DB** | Pinecone or Supabase pgvector | RAG retrieval for listings, community data, FAQs |
| **Session Store** | Redis | Conversation context persistence |
| **Chat Widget** | Custom React component or Botpress | Frontend chat interface |
| **Hosting** | Vercel / Railway / AWS Lambda | Serverless or lightweight server |
| **Calendar** | Calendly API or Cal.com | Showing/consultation scheduling |
| **CRM** | Follow Up Boss API or kvCORE | Lead creation and tracking |

---

## Conversation Flow Design

### Opening Flow
```
Bot: Hi! I'm Jing's assistant. I can help you find homes,
     get market info, or schedule a showing. What brings you
     here today?

     ○ I want to buy a home
     ○ I want to sell my home
     ○ I have a question about a listing
     ○ Just browsing

User: [selects or types]

Bot: [Routes to appropriate flow]
```

### Buyer Flow
```
Bot: Great! Let's find your perfect home. What city or
     neighborhood are you most interested in?

User: Cupertino

Bot: Cupertino is a fantastic choice — especially for families
     with school-age children. Here are some quick questions
     to help narrow things down:

     What's your approximate budget?
     ○ Under $1.5M
     ○ $1.5M - $2.5M
     ○ $2.5M - $3.5M
     ○ $3.5M+

User: $2M-$3M

Bot: And how many bedrooms are you looking for?

User: 4

Bot: I found 12 active listings in Cupertino with 4+ bedrooms
     between $2M-$3M. Here are the top 3:

     [Listing card 1]
     [Listing card 2]
     [Listing card 3]

     Would you like to schedule a showing for any of these?
     Or would you like to connect with Jing directly?
```

### Seller Flow
```
Bot: Thinking about selling? I can help you get started.
     What's your property address?

User: 123 Main St, Sunnyvale

Bot: Thanks! Based on recent sales in your area, Sunnyvale
     homes similar to yours have been selling between
     $1.8M - $2.2M. For a precise, personalized valuation,
     Jing would love to do a deeper analysis.

     Would you like to:
     ○ Get a free home valuation from Jing
     ○ Learn about our selling process
     ○ Ask more questions about the market
```

### Handoff to Human
```
Bot: This is a great question that Jing can answer in detail.
     Would you like me to:

     ○ Schedule a call with Jing (takes 30 seconds)
     ○ Have Jing email you
     ○ Continue chatting with me

     [If schedule]: Opens Calendly widget
     [If email]: Captures email, sends to CRM
```

---

## Knowledge Base (RAG)

### What to Embed

| Content Type | Source | Update Frequency |
|-------------|--------|-----------------|
| Active listings | IDX API / MLS feed | Daily auto-sync |
| Community pages | Website content | On content update |
| FAQ content | Curated Q&A document | Monthly |
| Market reports | Jing's market analysis | Monthly |
| School data | GreatSchools / CUSD data | Annually |
| Process guides | Buyer/Seller page content | On content update |
| Testimonials | Website content | On new additions |

### Embedding Strategy
1. Chunk content into 500-token segments with overlap
2. Generate embeddings using Anthropic's embedding model or OpenAI text-embedding-3-small
3. Store in vector database with metadata (source, city, content_type, date)
4. On query: retrieve top 5 relevant chunks, inject into Claude prompt as context

---

## Lead Qualification Logic

### Scoring Matrix
| Signal | Score | Action |
|--------|-------|--------|
| Has budget + timeline + area | Hot (+30) | Immediate CRM lead + Jing notification |
| Asks about specific listing | Warm (+20) | CRM lead, follow-up within 24h |
| Asks about selling | Warm (+20) | Trigger valuation funnel |
| Browsing neighborhoods | Cool (+10) | Nurture with content |
| Asks general questions | Informational (+5) | Provide value, offer to connect |

### Lead Capture Triggers
- When the user expresses clear buying/selling intent
- When the user asks about a specific property
- When the user requests a showing or valuation
- After 3+ substantive exchanges (relationship built)

---

## Safety & Brand Guardrails

### System Prompt Guidelines
```
You are Jing Chen's AI assistant on her real estate website.

Rules:
- Always be helpful, warm, and professional
- Never provide legal, financial, or tax advice — recommend consulting a professional
- Never guarantee home values or investment returns
- Never disparage other agents or brokerages
- If asked about Jing's commission, say "Jing would be happy to discuss that directly"
- If you don't know something, say so and offer to connect with Jing
- Always offer a path to connect with Jing for complex questions
- Comply with Fair Housing Act — never discriminate based on protected classes
- Don't discuss neighborhood demographics, crime, or religion
- Represent Jing's brand: strategic, trustworthy, and personal
```

---

## Implementation Phases

### Phase 2a: MVP (Month 1-2 post-launch)
- Basic chat widget with Claude API
- FAQ responses from embedded knowledge base
- Lead capture form within chat
- Email notification to Jing on new leads

### Phase 2b: Listing Integration (Month 3-4)
- IDX API integration for live listing search within chat
- Specific listing Q&A
- Showing request flow with Calendly

### Phase 2c: Full Intelligence (Month 5-6)
- CRM integration (auto-create leads, track conversations)
- Market data integration (live stats in responses)
- Multi-language support (English + Mandarin)
- Conversation analytics dashboard

---

## Estimated Costs

| Component | Monthly Cost |
|-----------|-------------|
| Claude API (Sonnet, ~1000 conversations/month) | $50-150 |
| Vector DB (Pinecone starter) | $0-70 |
| Redis (Upstash) | $0-10 |
| Hosting (Vercel/Railway) | $0-20 |
| Chat widget | Custom (free) or Botpress ($0-50) |
| **Total estimate** | **$50-300/month** |
