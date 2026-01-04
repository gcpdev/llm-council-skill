# LLM Council Skill

A Claude skill that enables collaborative brainstorming with multiple AI models (ChatGPT and Gemini) before presenting implementation plans.

## What It Does

When you ask Claude to consult with other AI models, Claude will:
1. Query both ChatGPT and Gemini for their perspectives
2. Analyze their responses and identify valuable insights
3. Synthesize a comprehensive implementation plan incorporating ideas from all three models
4. Present the final plan with attribution to each model's contributions

## How to Use

Simply ask Claude to consult with other AI models using phrases like:

- "**Consult the council:** How should I architect a microservices system?"
- "**Ask ChatGPT and Gemini** what they think about my database design"
- "**Get perspectives from other AI models** on this technical decision"
- "**Consult with other LLMs:** What's the best approach for..."

**Example:**
```
User: Consult the council: How should I structure my React app for scalability?

Claude will then:
- Query ChatGPT and Gemini about React architecture
- Analyze their suggestions on components, state management, and organization
- Present a synthesized plan incorporating insights from all three models
```

## Installation

1. **Install the skill** in Claude by uploading the `llm-council.skill` file
2. **Set up API keys and model preferences**:
   - Copy `.env.template` to create a `.env` file in your working directory
   - Add your OpenAI API key (get it at https://platform.openai.com/api-keys)
   - Add your Gemini API key (get it at https://aistudio.google.com/app/apikey)
   - Optionally customize which models to use (see Model Options below)

## Model Options

**Default Models (Fast & Cost-Effective):**
- ChatGPT: `gpt-5-nano-2025-08-07` (highly cost-effective)
- Gemini: `gemini-3-flash-preview` (balanced speed and intelligence)

**Upgrade Options for Better Collaboration:**

**OpenAI models (ordered by capability):**
- `gpt-5-nano` - Fastest, cheapest version of GPT-5. It's great for summarization and classification tasks. (Default)
- `gpt-5-mini` - Balanced cost and quality
- `gpt-5.2` - Smart model, capable of most tasks
- `gpt-5.2-pro` - State-of-the-art for professional knowledge work

**Gemini models (ordered by capability):**
- `gemini-2.5-flash-lite` - Ultra-fast, optimized for throughput
- `gemini-2.5-flash` - Best price-performance
- `gemini-3-flash-preview` - Balanced (default)
- `gemini-3-pro-preview` - Most intelligent, best reasoning

**How to Configure:**
Add these lines to your `.env` file:
```
OPENAI_MODEL=gpt-5-nano
GEMINI_MODEL=gemini-3-flash-preview
```

**Recommended Configurations:**
- **Balanced**: Defaults (`gpt-5-nano` + `gemini-3-flash-preview`)
- **Budget**: `gpt-5-nano` + `gemini-2.5-flash`
- **High Quality**: `gpt-5` + `gemini-3-flash-preview`
- **Premium Reasoning**: `gpt-5.2` + `gemini-3-pro-preview`
- **Professional Work**: `gpt-5.2-pro` + `gemini-3-pro-preview`

## Benefits

- **Diverse perspectives**: Get insights from three different AI models with different training and capabilities
- **Better decisions**: Identify potential issues or alternatives you might have missed with a single model
- **Comprehensive planning**: Combine strengths of multiple models for more robust implementation plans

## API Costs

Both OpenAI and Gemini APIs have usage costs that vary significantly by model:

**OpenAI Cost Tiers (approximate, check current pricing):**

*Budget Tier:*
- `gpt-5-nano`: Very low cost per token
- 
*Standard Tier:*
- `gpt-5-mini`: Moderate cost

*Premium Tier:*
- `gpt-5.2`: Higher cost per token
- `gpt-5.2-pro`: Highest cost for professional work

**Gemini Cost Tiers (approximate, check current pricing):**

*Budget Tier:*
- `gemini-2.5-flash-lite`: Very low cost, optimized for throughput
- `gemini-2.5-flash`: Low cost, best price-performance

*Standard Tier:*
- `gemini-3-flash-preview`: Moderate cost (default)

*Premium Tier:*
- `gemini-3-pro-preview`: Higher cost for advanced reasoning

**Cost Management Tips:**
- Start with default models for routine brainstorming (very cost-effective)
- Use mid-tier models (`gpt-5-mini` + `gemini-3-flash-preview`) for balanced quality/cost
- Upgrade to premium models only for critical architectural decisions or complex reasoning tasks
- Set usage limits in your API dashboards (OpenAI Platform and Google AI Studio)
- Consider setting monthly budgets to avoid surprises
- Monitor your usage patterns and adjust model choices accordingly

**Note:** Each `/council` command makes 2 API calls (one to ChatGPT, one to Gemini), so total cost is the sum of both models' pricing.

## Skill Structure

```
llm-council/
├── SKILL.md                    # Main skill instructions
├── scripts/
│   └── query_llms.py          # Python script that queries both APIs
└── references/
    └── setup.md               # Detailed setup instructions
```

## Troubleshooting

**"API key not found" error**: Make sure your `.env` file is in the current working directory with the correct keys.

**API timeout**: The script has a 30-second timeout per API. If an API is slow or down, it will show an error but continue with the other model's response.

**One API fails**: Claude will note which model's perspective is unavailable and proceed with the available responses.
