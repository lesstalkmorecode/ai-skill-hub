FROM node:22-bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends python3 git ca-certificates \
    && rm -rf /var/lib/apt/lists/*
RUN npm install -g @openai/codex@0.144.5
LABEL ai-skill-hub.evals="1"
ENV AI_SKILL_HUB_EVAL_CONTAINER=1 CODEX_HOME=/state/codex PYTHONDONTWRITEBYTECODE=1
WORKDIR /opt/hub
COPY plugin.json README.md AGENTS.md ./
COPY skills ./skills
COPY agents ./agents
COPY adapters ./adapters
COPY docs ./docs
COPY evals/*.py ./evals/
USER node
WORKDIR /workspace
