# AI Research Agent (Work in Progress)

A beginner-friendly Python research assistant that uses an LLM and web search to generate structured reports about a topic. This project started while following Tech With Tim's [Build an AI Agent From Scratch in Python](https://www.youtube.com/watch?v=bTMPwUgLZf0) tutorial; I'm continuing to refine and extend it as I learn.

> **Status:** Learning project / early prototype. Reports are AI-generated and should be checked against original sources before use.

## Current features

- Accepts a research question from the terminal.
- Uses an OpenAI chat model via LangChain.
- Searches the web using DDGS.
- Returns a validated Pydantic research report with a summary, strengths, weaknesses, controversies, and source URLs.
- Reads API credentials from a local environment file.

## Tech stack

Python · LangChain · OpenAI API · Pydantic · DDGS · python-dotenv

## Get started

Requires Python 3.10+ and an OpenAI API key. Usage of the OpenAI API may incur charges.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Put your own key in `.env` (do **not** commit that file):

```dotenv
OPENAI_API_KEY=your_actual_key_here
```

Run the application:

```bash
python main.py
```

Sample question: `The impact of AI on software engineering`

## Project files

```text
ai-research-agent/
├── main.py           # Research schema and agent entry point
├── tools.py          # Web-search tool
├── requirements.txt  # Python dependencies
├── .env.example      # Safe configuration template
├── .gitignore        # Prevents local secrets and generated files from being committed
└── README.md
```

## Limitations

- This is a prototype, not a fact-checking system; search snippets do not guarantee accurate claims.
- Sources may be incomplete, unavailable, or insufficient for a research topic.
- The application currently runs only in the terminal.
- The project has not yet added automated tests, persistent history, or report export.

## Next steps

- [ ] Improve source validation and citations.
- [ ] Add Wikipedia as another research tool.
- [ ] Export reports to Markdown or PDF.
- [ ] Add basic automated tests.
- [ ] Build a simple frontend once the agent is stable.

## Tutorial credit

Initial learning was based on [Tech With Tim's YouTube tutorial](https://www.youtube.com/watch?v=bTMPwUgLZf0). This repository documents my own study and incremental development, including updates for the modern LangChain agent interface.
