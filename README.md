# WhatsApp-Chatbot

## Introduction

This project aims to integrate a bot into WhatsApp using Twilio, Ngrok, and OpenAI API keys. Instead of accessing ChatGPT through a browser, we opted to make it available on WhatsApp for easier access and enhanced security.

## Prerequisites

<div align="left">
  <img alt="OpenAi API" src="img/ai.png" height="70" width="70"/>
  <img alt="Twilio API" src="img/twilio.png" height="70" width="70"/> 
  <img alt="Ngrok" src="img/ngrok.png" height="70" width="70"/>
  <img alt="WhatsApp" src="img/whatsapp.png" height="70" width="70"/>
</div>

## Working

1. **Write `app.py`**:
   - Paste your OpenAI API keys in the code.
2. **Run the code**:
   - Obtain the server URL (e.g., `https://127.0.0.1`).
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

## Advantages

- **Easy Access**: Interact with ChatGPT directly from WhatsApp.
- **Security**: Ensures a secure connection and data handling.
- **Time Efficient**: Provides quick responses to user queries.

---
