from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

KNOWLEDGE_BASE = {
    'admission': 'Apply online → Document verification → Entrance test → Merit list → Fee payment',
    'library': 'Central Library - Block A, Ground Floor',
    'cafeteria': 'Main Cafeteria - Block B, 1st Floor',
    'results': 'Check results at college.edu/results with roll number',
    'attendance': 'Minimum 75% attendance required for exam eligibility'
}

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    
    # Simple keyword-based responses
    response = 'I can help with admissions, campus locations, and student services.'
    message_lower = message.lower()
    
    if 'admission' in message_lower:
        response = KNOWLEDGE_BASE['admission']
    elif 'library' in message_lower:
        response = KNOWLEDGE_BASE['library']
    elif 'cafeteria' in message_lower:
        response = KNOWLEDGE_BASE['cafeteria']
    elif 'result' in message_lower:
        response = KNOWLEDGE_BASE['results']
    elif 'attendance' in message_lower:
        response = KNOWLEDGE_BASE['attendance']
    
    return jsonify({'response': response})

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '')
    from_lang = data.get('from', 'en')
    to_lang = data.get('to', 'en')
    
    if from_lang == to_lang:
        return jsonify({'translated_text': text})
    
    try:
        translated = translator.translate(text, src=from_lang, dest=to_lang)
        return jsonify({'translated_text': translated.text})
    except:
        return jsonify({'translated_text': text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)