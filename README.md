# WhatsApp-Chatbot

## Introduction

This project aims to integrate a bot into WhatsApp using Twilio, Ngrok, and OpenAI API keys. Instead of accessing ChatGPT through a browser, we opted to make it available on WhatsApp for easier access and enhanced security.

## Prerequisites

<div align="left">
  <img alt="OpenAi API" src="https://img.shields.io/badge/ChatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white"/>
  <img alt="Twilio API" src="https://img.shields.io/badge/Twilio-F22F46?style=for-the-badge&logo=Twilio&logoColor=white"/> 
  <img alt="Ngrok" src="https://img.shields.io/badge/ngrok-140648?style=for-the-badge&logo=Ngrok&logoColor=white"/>
  <img alt="WhatsApp" src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/>
</div>
## Process

1. **Write `app.py`**:
   - Paste your OpenAI API keys in the code.
2. **Run the code**:
   - Obtain the server URL (e.g., `https://127.0.0.1`, copy `127.0.0.1`).
3. **Configure Ngrok**:
   - Paste the server URL in the command: `ngrok http 127.0.0.1`.
   - Copy the forwarding URL provided by Ngrok.
4. **Set up Twilio**:
   - Paste the Ngrok forwarding URL into Twilio's Sandbox configuration.
5. **Connect to WhatsApp**:
   - Your bot is now connected and can answer queries on WhatsApp.

## Workflow

1. The user sends a query on WhatsApp.
2. Twilio receives the query and forwards it to the Ngrok URL.
3. Ngrok forwards the query to your server.
4. Your server, using the OpenAI API, processes the query and fetches the relevant answer.
5. The answer is sent back through Ngrok to Twilio, and then to WhatsApp.

### Visual Representation:

```
API keys -> Code -> Ngrok -> Twilio -> WhatsApp
```

## Benefits

- **Easy Access**: Interact with ChatGPT directly from WhatsApp.
- **Secure**: Ensures a secure connection and data handling.
- **Time Efficient**: Provides quick responses to user queries.

---
