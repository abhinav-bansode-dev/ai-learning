[README_Version4.md](https://github.com/user-attachments/files/31210102/README_Version4.md)
# ai-learning

A personal collection of Python learning projects, mini-projects, and AI/LLM experiments — weather API clients, OpenAI/Gemini experiments, LangChain/semantic-kernel examples, simple analyzers, and small OOP practice projects.

---

## Table of Contents
- [About](#about)
- [Features](#features)
- [Repository structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration (.env)](#configuration-env)
- [Usage examples](#usage-examples)
  - [Weather scripts](#weather-scripts)
  - [LLM / OpenAI example](#llm--openai-example)
  - [Gemini / LangChain examples](#gemini--langchain-examples)
  - [Mini-projects & utilities](#mini-projects--utilities)
  - [Data analysis](#data-analysis)
- [Tests](#tests)
- [Data & persistence](#data--persistence)
- [Contributing](#contributing)
- [Authors](#authors)
- [Security & Notes](#security--notes)
- [Contact](#contact)

---

## About
This repository is a learning workspace for Python and AI-related experiments. It contains multiple standalone scripts demonstrating:
- API clients (weather, jokes, crypto)
- LLM calls (OpenAI, Gemini) and LangChain/semantic-kernel integrations
- Mini-projects (task manager, log analyzer, banking example)
- Simple data analysis (crypto price analyzer)
- Unit tests and small persistence examples

---

## Features
- Weather API clients and logging (weather_client.py, APIWeatherProject*.py)
- Direct LLM usage (DirectOpenAiCall.py) and Gemini experiments (Gemini_LangChain.py, Gemini_LangGraphChatBot.py)
- Mini-projects showing file-based JSON persistence and simple CLI usage
- Data collectors and analyzers (CryptoPriceAnalyzer.py)
- Example unit tests (test_weather_client.py)

---

## Repository structure (selected)
- Root: many standalone Python scripts (weather, LLM experiments, mini-projects)
- requirements.txt — Python dependencies
- Data files: *.csv, *.json, *.txt, weather_history.db
- Tests: test_example.py, test_weather_client.py
- Notable scripts:
  - weather_client.py — fetch_weather(city) -> dict, requires OPENWEATHER_API_KEY
  - APIWeatherProject.py / APIWeatherProject_Simple.py — example CLI/usage wrappers
  - DirectOpenAiCall.py — OpenAI Responses usage (OPENAI_API_KEY)
  - Gemini_LangChain.py / Gemini_LangGraphChatBot.py — Gemini + LangChain / LangGraph examples (GEMINI_API_KEY)
  - CryptoPriceAnalyzer.py — fetches BTC/ETH via CoinGecko and appends to crypto_prices.csv
  - MiniProject_TaskManagerWithJSONstorage.py — tasks.json-based manager

---

## Prerequisites
- Python 3.10+ recommended
- pip
- (Optional) virtualenv or venv
- API keys for OpenWeather, OpenAI, Gemini as needed

---

## Installation

Clone and install dependencies:

```bash
git clone https://github.com/abhinav-bansode-dev/ai-learning.git
cd ai-learning

python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
