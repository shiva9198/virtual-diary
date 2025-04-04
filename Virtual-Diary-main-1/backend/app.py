from flask import Flask, request, jsonify
from flask_cors import CORS
from diary_logic import initialize_diary_file, add_entry, get_entries, save_entry
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allows Flutter to access this API

initialize_diary_file("/Users/shiva/Documents/Virtual-Dairy/backend/diary_entries.xlsx")

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Virtual Diary Backend is Running!"}), 200

@app.route('/add_entry', methods=['POST'])
def api_add_entry():
    data = request.get_json()
    content = data.get("content", "")
    if not content:
        return jsonify({"status": "fail", "message": "Content required"}), 400

    add_entry(content)
    return jsonify({"status": "success", "message": "Entry added"}), 200

@app.route('/get_today', methods=['GET'])
def api_get_today():
    today = datetime.now().strftime("%Y-%m-%d")
    entries = get_entries(today)
    return jsonify({"status": "success", "date": today, "entries": entries}), 200

@app.route('/get_entries', methods=['GET'])
def api_get_entries():
    date = request.args.get("date")
    if not date:
        return jsonify({"status": "fail", "message": "Date is required"}), 400
    entries = get_entries(date)
    return jsonify({"status": "success", "date": date, "entries": entries}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)