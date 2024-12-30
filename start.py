#!/usr/bin/env python

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_SECRET_KEY = os.getenv('OPENAI_SECRET_KEY')
MODEL = 'gpt-4o'

client = OpenAI(
    api_key=OPENAI_SECRET_KEY
)

with open("source-data/changes.diff", "r") as file:    
    diff = file.read()

prompt = f"""Analize following Git diff and generate meaningful title and description for pull request. 
Return the answer in valid json format. 
Git diff:
{diff}
Template:
{{
    "title": "*",
    "description": "*"
}}
"""

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model=MODEL
)

print(chat_completion.choices[0].message.content)

