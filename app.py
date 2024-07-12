from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
from config import OPENAI_API_KEY, OPENAI_BASE_URL

app = Flask(__name__)
# openai.api_key = OPENAI_API_KEY
# openai.base_url = OPENAI_BASE_URL
draw_syn=["draw","paint","image","picture","photo","painting","drawing"]


def generate_image(text_prompt):
    generation_response=openai.Image.create(
        prompt=text_prompt,
        n=1,
        size="1024x1024",
        response_format="url",
    )
    print(generation_response)
    generated_image_url=generation_response["date"][0]["url"]
    return generated_image_url

def generate_answer(question):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=question,
        max_tokens=1000,
        n=1,
        stop=None,
    )
    return response.choices[0].text


@app.route("/whatsapp",methods=['POST'])
def wa_reply():
    query=request.form.get('Body').lower()
    print("User Query:",query)
    twilio_response=MessagingResponse()
    reply=twilio_response.message()
    if query.split(" ")[0].lower() in draw_syn:
        image_url=generate_image(query)
        reply.media(image_url,caption=query)
    else:
        answer=generate_answer(query)
        reply.body(answer)
    return str(twilio_response)


