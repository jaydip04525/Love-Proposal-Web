from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>💖 Love Proposal 💖</title>
    <style>
        body {
            text-align: center;
            background-color: #ffe6f0;
            font-family: Arial, sans-serif;
        }
        h1 {
            margin-top: 80px;
            font-size: 40px;
        }
        button {
            padding: 15px 30px;
            font-size: 20px;
            font-weight: bold;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }
        #yes {
            background-color: #ff4d6d;
            color: white;
        }
        #no {
            background-color: #4d79ff;
            color: white;
            position: absolute;
            left: 60%;
            top: 60%;
        }
    </style>
</head>

<body>
    <h1>Will you be mine? 💘</h1>

    <button id="yes" onclick="yesClicked()">YES</button>
    <button id="no" onmouseover="moveNo()">NO</button>

    <script>
        function yesClicked() {
            alert("My heart is officially smiling! 😍");
        }

        function moveNo() {
            let btn = document.getElementById("no");
            let x = Math.random() * 80 + "%";
            let y = Math.random() * 80 + "%";
            btn.style.left = x;
            btn.style.top = y;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
