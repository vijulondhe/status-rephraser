import openai
import os
import pyperclip
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def rephrase(text):
    messages = [
        {"role": "system", "content": "Rewrite this as a clear, polite status update."},
        {"role": "user", "content": text}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
    )
    return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    print("Paste your raw updates (hit Enter twice when done):")
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)

    raw_text = "\n".join(lines)
    polished = rephrase(raw_text)
    print("\nHere’s your polished update:\n")
    print(polished)
    pyperclip.copy(polished)
    print("\nCopied to clipboard. Done.")
