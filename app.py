import os
import json
from datetime import date
import flask
from flask import request, jsonify, render_template
from google import genai

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest-tasks', methods=['POST'])
def suggest_tasks():
    data = request.get_json()
    braindump = data.get('braindump')

    if not braindump:
        return jsonify({"error": "Missing 'braindump' text in request body"}), 400

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return jsonify({"error": "GEMINI_API_KEY environment variable not set"}), 500

    # Configure Gemini
    client = genai.Client(api_key=api_key)

    prompt = (
        f"Parse this ADHD brain dump into EXACTLY 3 work tasks and 3 private tasks. "
        f"Return a JSON object with keys 'work' and 'private', each containing a list of 3 strings.\n\n"
        f"{braindump}"
    )

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config={'response_mime_type': 'application/json'}
        )
        return jsonify(json.loads(response.text))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/select-tasks', methods=['POST'])
def select_tasks():
    data = request.get_json()
    tasks = data.get('tasks', [])
    today = date.today().isoformat()
    
    filename = 'tasks.json'
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                saved_data = json.load(f)
            except json.JSONDecodeError:
                saved_data = {}
    else:
        saved_data = {}

    saved_data[today] = tasks
    
    with open(filename, 'w') as f:
        json.dump(saved_data, f, indent=2)

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, port=45000)
