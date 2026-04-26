<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>השאלון המעוצב שלי</title>
    <style>
    
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .quiz-card {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            width: 400px;
            text-align: center;
        }
        h1 { color: #1a73e8; margin-bottom: 20px; }
        .question-text {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 15px;
            color: #333;
        }
        .option-button {
            display: block;
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            background: none;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 16px;
        }
        .option-button:hover {
            background-color: #e8f0fe;
            border-color: #1a73e8;
        }
        #loading { color: #666; }
    </style>
</head>
<body>

    <div class="quiz-card">
        <h1 id="quiz-title">טוען שאלון...</h1>
        <div id="quiz-container">
            <p id="loading">מתחבר לשרת הפייתון...</p>
        </div>
    </div>

    <script>
        
        // אנחנו מבקשים מהשרת את שאלון מספר 1
        fetch('/get_quiz/1')
            .then(response => response.json())
            .then(data => {
                // ברגע שהנתונים הגיעו מהפייתון:
                document.getElementById('quiz-title').innerText = data.title;
                const container = document.getElementById('quiz-container');
                container.innerHTML = ''; // מנקים את הודעת הטעינה

                // עוברים שאלה שאלה ומציגים אותה
                data.questions.forEach((q, index) => {
                    const qElement = document.createElement('div');
                    qElement.innerHTML = `<p class="question-text">${q.text}</p>`;
            
                    q.options.forEach(opt => {
                        const btn = document.createElement('button');
                        btn.className = 'option-button';
                        btn.innerText = opt;
                        btn.onclick = () => alert('בחרת בתשובה: ' + opt);
                        qElement.appendChild(btn);
                    });
                    
                    container.appendChild(qElement);
                });
            })
            .catch(error => {
                document.getElementById('quiz-title').innerText = "שגיאה!";
                document.getElementById('quiz-container').innerText = "לא הצלחתי להתחבר לשרת הפייתון.";
            });
    </script>

</body>
</html>
