#!/usr/bin/env python3
"""
Query multiple LLMs (Gemini and ChatGPT) for their perspectives on a given prompt.
Uses environment variables for API keys.
"""

import os
import sys
import json
from typing import Dict, Optional
import requests


def load_env_file(env_path: str = ".env") -> Dict[str, str]:
    """Load environment variables from .env file."""
    env_vars = {}
    if not os.path.exists(env_path):
        return env_vars

    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                env_vars[key.strip()] = value.strip().strip('"').strip("'")

    return env_vars


def query_openai(prompt: str, api_key: str, model: str = "gpt-5-nano") -> Optional[str]:
    """Query OpenAI's ChatGPT API."""
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 2000,
                "temperature": 0.7,
            },
            timeout=30,
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error querying ChatGPT ({model}): {str(e)}"


def query_gemini(
    prompt: str, api_key: str, model: str = "gemini-3-flash-preview"
) -> Optional[str]:
    """Query Google's Gemini API."""
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            json={
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"temperature": 0.7, "maxOutputTokens": 2000},
            },
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Error querying Gemini ({model}): {str(e)}"


def main():
    if len(sys.argv) < 2:
        print(
            json.dumps(
                {
                    "error": "Usage: query_llms.py <prompt>",
                    "chatgpt": None,
                    "gemini": None,
                }
            )
        )
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])

    # Load environment variables
    env_vars = load_env_file()
    openai_key = env_vars.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
    gemini_key = env_vars.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

    # Get model configuration (with defaults)
    openai_model = (
        env_vars.get("OPENAI_MODEL") or os.environ.get("OPENAI_MODEL") or "gpt-5-nano"
    )
    gemini_model = (
        env_vars.get("GEMINI_MODEL")
        or os.environ.get("GEMINI_MODEL")
        or "gemini-3-flash-preview"
    )

    # Query both APIs
    chatgpt_response = None
    gemini_response = None

    if openai_key:
        chatgpt_response = query_openai(prompt, openai_key, openai_model)
    else:
        chatgpt_response = "Error: OPENAI_API_KEY not found in .env file or environment"

    if gemini_key:
        gemini_response = query_gemini(prompt, gemini_key, gemini_model)
    else:
        gemini_response = "Error: GEMINI_API_KEY not found in .env file or environment"

    # Output as JSON
    result = {
        "prompt": prompt,
        "chatgpt": {"model": openai_model, "response": chatgpt_response},
        "gemini": {"model": gemini_model, "response": gemini_response},
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
