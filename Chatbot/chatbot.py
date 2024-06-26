import os
import markdown

import mesop as me
import mesop.labs as mel

import gevent.monkey
gevent.monkey.patch_all()

import openai

@me.page(
    security_policy=me.SecurityPolicy(
        allowed_iframe_parents=["https://google.github.io"]
    ),
    path="/post/chatbot",
    title="Chat w Diary",
)
def page():
    header()
    with me.box(style=me.Style(height="91%", overflow_y="auto")): 
        mel.chat(transform, title="Chat w Diary", bot_user="Diary Bot")

def header():
    with me.box(style=me.Style(
        background="#1C2541",
        border=me.Border(bottom=me.BorderSide(style="solid", width=1, color="#dcdcdc")),
        overflow_x="clip",
    )):
        with me.box(style=me.Style(
            padding=me.Padding(top=12, right=12, left=12, bottom=12),
            display="flex",
            align_items="end",
            justify_content="space-between",
            # margin=me.Margin(left=12, right=12, bottom=12, top=12),
            font_size=24,
            color="#BFACC8",
        )):
            with me.box(style=me.Style(display="flex")):
                with me.box(style=me.Style(display="flex", cursor="pointer"), on_click=navigate_home):
                    me.text("Internship", style=me.Style(font_weight=700, margin=me.Margin(right=8)))
                    me.text("Diary - ChatBot")
def navigate_home(e: me.ClickEvent):
    me.navigate("/")

def transform(input: str, history: list[mel.ChatMessage]):
    blog_data = read_all_files()
    context = " ".join(blog_data)
    # print("Chat History:", history) 
    messages = [
        {"role": "system", "content": "You are a helpful assistant that knows everything about the blog content of this website, i.e. all the data from daily and weekly posts."},
    ]
    messages.extend([{"role": msg.role, "content": msg.content} for msg in history])
    messages.append({"role": "user", "content": input})
    response = get_gpt_response(messages,context)
    yield response

def read_all_files():
    blog_data = []
    blog_data.extend(read_files_from_folder("./", ".md"))
    blog_data.extend(read_files_from_folder("./Daily/", ".py"))
    blog_data.extend(read_files_from_folder("./Weekly/", ".py"))
    blog_data.extend(read_files_from_folder("./Projects/", ".py"))
    return blog_data

def read_files_from_folder(folder, extension):
    data = []
    for filename in os.listdir(folder):
        if filename.endswith(extension):
            filepath = os.path.join(folder, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()
                data.append(text)
    return data

# OpenAI Chatbot Integration
from flask import Flask, request, jsonify, session, render_template
import openai

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
OPENAI_MODEL_NAME = os.getenv('OPENAI_MODEL_NAME', 'gpt-4o')

openai.api_key = OPENAI_API_KEY

client = openai.OpenAI()
model = "gpt-4o"

def get_gpt_response(messages, context):

    messages.insert(1, {"role": "system", "content": context})
    
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=messages
        # messages=[
        #     {"role": "system", "content": "You are a helpful assistant that knows everything about the blog content of this website, i.e. all the data from daily and weekly posts."},
        #     {"role": "user", "content": messages[-1]['content']},
        #     {"role": "system", "content": context}
        # ]
    )
    return response.choices[0].message.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_prompt = request.form['prompt']

    messages = session.get('messages', [
        {"role": "system", "content": "You are an expert assistant. Your responses are based on the blog content and should be able to explain and answer concisely."}
    ])
    
    messages.append({"role": "user", "content": user_prompt})

    blog_data = read_all_files()
    context = " ".join(blog_data)
    
    completion = get_gpt_response(messages, context)
    
    model_response = completion
    messages.append({"role": "assistant", "content": model_response})
    session['messages'] = messages 
    
    return {"response": model_response}

if __name__ == '__main__':
    app.run(debug=True)
