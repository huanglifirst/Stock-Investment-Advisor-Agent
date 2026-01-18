# Stock Investment Advisor Agent

## Environment Variables

Set the following environment variables before running the Financial MCP agents:

### OpenAI Compatible API

- `OPENAI_COMPATIBLE_API_KEY`: API key for the OpenAI-compatible provider.
- `OPENAI_COMPATIBLE_BASE_URL`: Base URL for the OpenAI-compatible endpoint.
- `OPENAI_COMPATIBLE_MODEL`: Default model name for agents that do not specify a dedicated model.

### Per-Agent Model Overrides

Each agent can read its own model environment variable. If the variable is unset, it falls back to `OPENAI_COMPATIBLE_MODEL`.

- `FUNDAMENTAL_MODEL`: Model for the fundamental analysis agent.
- `TECHNICAL_MODEL`: Model for the technical analysis agent.
- `VALUE_MODEL`: Model for the valuation analysis agent.
- `NEWS_MODEL`: Model for the news analysis agent.
- `SUMMARY_MODEL`: Model for the summary agent (API mode only).

### Local Model Toggle

- `USE_LOCAL_MODEL`: Set to `local` to enable the local FinR1 model in the summary agent; otherwise it uses the API.
