from flask import Flask, jsonify

app = Flask(__name__)

quizzes = {
    "1": {
        "title": "שאלון ראשון שלי",
        "questions": [
            {"text": "כמה זה 2+2?", "options": ["3", "4", "5"], "answer": "4"},
            {"text": "מה הצבע של השמיים?", "options": ["ירוק", "כחול", "אדום"], "answer": "כחול"}
        ]
    }
}

@app.route('/get_quiz/<quiz_id>')
def get_quiz(quiz_id):
    if quiz_id in quizzes:
        return jsonify(quizzes[quiz_id])
    return jsonify({"error": "לא נמצא שאלון"}), 404

if __name__ == '__main__':
    app.run()
