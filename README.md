# Status Rephraser

A simple Python script to rewrite messy status updates using OpenAI’s GPT.

---

## Setup

1. Get an OpenAI API key from https://platform.openai.com/signup  
2. Create a `.env` file with your API key in this format:  
   `OPENAI_API_KEY=your-api-key`  
3. Install the required Python packages by running:  
   `pip install openai python-dotenv pyperclip`

---

## Usage

Run the script with:  
`python status_rephraser.py`

Paste your raw bullet points. Press Enter twice when done. The script will print the polished status update and copy it automatically to your clipboard.

---

## Notes

- Keep your `.env` file private and do not commit it to version control.  
- You can customize the prompt in the script if you want to change the tone or style of the rewriting.

---

## License

MIT License — use it freely, but no warranty.

---

## About

This project is a minimal tool to help automate the boring and repetitive task of rewriting status updates or notes using OpenAI’s GPT model. It’s designed to be easy to use and lightweight, requiring minimal setup.
