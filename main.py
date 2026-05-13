
import random
from flask import Flask, request
 
app = Flask(__name__)
 
secret_number = random.randint(1, 100)
 
 
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Number Guessing Game</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f4f8;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                background: white;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                max-width: 400px;
                width: 100%;
            }
            h1 { color: #333; }
            p { color: #666; }
            input[type=number] {
                padding: 10px 16px;
                font-size: 18px;
                border: 2px solid #ddd;
                border-radius: 8px;
                width: 120px;
                text-align: center;
                margin: 10px 0;
            }
            button {
                display: block;
                width: 100%;
                padding: 12px;
                margin-top: 12px;
                font-size: 18px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: background 0.2s;
            }
            button:hover { background-color: #45a049; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>ðŸŽ¯ Number Guessing Game</h1>
            <p>I'm thinking of a number between <strong>1</strong> and <strong>100</strong>. Can you guess it?</p>
            <form action="/guess" method="get">
                <input type="number" name="guess" min="1" max="100" placeholder="?" required autofocus>
                <button type="submit">Guess!</button>
            </form>
        </div>
    </body>
    </html>
    """
 
 
@app.route("/guess")
def guess_number():
    guess = int(request.args.get("guess"))
 
    if guess < secret_number:
        return """
        <h1 style="color: red; text-align: center;">Too low, try again!</h1>
        <p style="text-align: center;">
            <img src="https://media.giphy.com/media/3o7abKh0pu0NwenHMS/giphy.gif" width="400">
        </p>
        <p style="text-align: center;"><a href="/">Go back</a></p>
        """
 
    elif guess > secret_number:
        return """
        <h1 style="color: blue; text-align: center;">Too high, try again!</h1>
        <p style="text-align: center;">
            <img src="https://media.giphy.com/media/3o7aDgf8J4s7l7f9b2/giphy.gif" width="400">
        </p>
        <p style="text-align: center;"><a href="/">Go back</a></p>
        """
 
    else:
        return f"""
        <h1 style="color: green; text-align: center;">You found me! ðŸŽ‰</h1>
        <p style="text-align: center; font-size: 80px;">The number was {secret_number}</p>
        <p style="text-align: center;">
            <img src="https://media.giphy.com/media/26ufnwz3wDUli7GU0/giphy.gif" width="400">
        </p>
        <p style="text-align: center;"><a href="/">Play again</a></p>
        """
 
 
if __name__ == "__main__":
    app.run(debug=True)
 
