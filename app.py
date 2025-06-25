from flask import Flask, redirect, render_template, request, jsonify, send_from_directory, session
from flask_cors import CORS
from groq import Groq
import requests
import json
import os
import sqlite3

app = Flask(__name__)
app.secret_key = 'GnUB9NVLy3'  # Flask session key
CORS(app)

# Initialize Groq API client
client = Groq(api_key="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")

# Memory storage
MEMORY_FILE = 'memory.json'
chat_history = []

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_memory(memory):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f)

def get_weather():
    try:
        url = "http://api.weatherapi.com/v1/current.json"
        params = {
            "key": "bce9a00258654cec9e9173833250506",
            "q": "Tunis",
            "aqi": "no"
        }
        response = requests.get(url, params=params)
        data = response.json()
        city = data['location']['name']
        country = data['location']['country']
        temp = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return f"The current weather in {city}, {country} is {temp}°C and {condition.lower()}."
    except Exception as e:
        print("Weather error:", e)
        return "Sorry, I couldn't fetch the weather."



@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    memory = load_memory()

    if not user_input:
        return jsonify({'response': "Message is empty.", 'history': chat_history}), 400

    # Handle weather question
    if "weather" in user_input.lower():
        weather = get_weather()
        chat_history.append({"role": "assistant", "content": weather})
        return jsonify({'response': weather, 'history': chat_history})

    # Handle memory instruction
    if "remember:" in user_input.lower():
        try:
            key_value = user_input.lower().split("remember:")[1].strip().split("=")
            if len(key_value) == 2:
                key, value = key_value[0].strip(), key_value[1].strip()
                memory[key] = value
                save_memory(memory)
                reply = f"✅ Got it! I will remember that {key} is {value}."
                chat_history.append({"role": "assistant", "content": reply})
                return jsonify({'response': reply, 'history': chat_history})
        except:
            reply = "⚠️ I couldn't understand the memory format. Use: remember: key = value"
            chat_history.append({"role": "assistant", "content": reply})
            return jsonify({'response': reply, 'history': chat_history})

    memory_string = "\n".join(f"{k}: {v}" for k, v in memory.items())
    system_prompt = {
        "role": "system",
        "content": f"You are a helpful assistant. Here's what you remember:\n{memory_string}"
    }

    chat_history.append({"role": "user", "content": user_input})
    messages = [system_prompt] + chat_history

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages
        )
        reply = response.choices[0].message.content
    except Exception as e:
        print("Groq error:", e)
        reply = "Sorry, I couldn't process your request."

    chat_history.append({"role": "assistant", "content": reply})
    return jsonify({'response': reply, 'history': chat_history})

@app.route('/clear', methods=['POST'])
def clear():
    global chat_history
    chat_history = []
    return jsonify({"status": "cleared"})

@app.route('/save', methods=['POST'])
def save():
    with open("chat_history.txt", "w", encoding="utf-8") as f:
        for msg in chat_history:
            f.write(f"{msg['role'].upper()}: {msg['content']}\n")
    return jsonify({"status": "saved"})

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        return jsonify({"message": "User registered successfully!"})
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 400
    finally:
        conn.close()

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row  # Allow access by column name
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        session['user'] = {
            'username': user['username'],
            'email': user['email']
        }
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Invalid credentials"}), 401


def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()
@app.route('/home')
def home():
    if 'user' not in session:
        return redirect('/login')  # or '/'
    return render_template(
        'home.html',
        username=session['user']['username'],
        email=session['user']['email']
    )
@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/login')
def login_page():
    return render_template('login.html')
@app.route('/chat')
def AI_Helper():
    return render_template('AI Helper.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/')
def index():
    return render_template('home.html')  # or 'AI Helper.html' or whatever page you want as your homepage


   



if __name__ == '__main__':
    app.run(debug=True, port=5500)
