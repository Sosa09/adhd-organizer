import os
import json
import flask
from flask import request, jsonify
from google import genai

app = flask.Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, port=45000)
