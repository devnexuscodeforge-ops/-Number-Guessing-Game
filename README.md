# -Number-Guessing-Game
🎯 Number Guessing Game
A fun, interactive number guessing game built with Python and Flask. The server picks a random secret number between 0 and 9 — can you find it?
🎮 How It Works
Visit the home page, enter a number from 0–9, and the app tells you instantly:

Result	Response
📉 Too Low	Red page + GIF
📈 Too High	Blue page + GIF
🎉 Correct!	Green celebration page + GIF
Guessing works via URL routing — e.g. visiting /5 guesses the number 5.

✨ Features
Secret number randomly generated on server start
Clean, modern UI with a purple gradient home page
Color-coded feedback pages (red / blue / green)
Fun reaction GIFs for every outcome
Keyboard + button support for guessing
Pure Flask — no frontend framework required
🛠️ Tech Stack
Python 3.8+
Flask — lightweight web framework
HTML + CSS — embedded styling, no external CSS files
📦 Setup & Installation
1. Clone the repository
bash
git clone https://github.com/YOUR_USERNAME/number-guessing-game.git
cd number-guessing-game
2. Create a virtual environment
bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
3. Install dependencies
bash
pip install -r requirements.txt
4. Run the app
bash
python app.py
5. Open in your browser
http://127.0.0.1:5000
📁 Project Structure
number-guessing-game/
├── app.py              # Main Flask application (routes + HTML)
├── requirements.txt    # Python dependencies
├── .gitignore          # Files excluded from Git
├── LICENSE             # MIT License
└── README.md           # You're reading it!
🔍 How the Routing Works
GET /        → Home page with input form
GET /<guess> → Evaluates the guess and returns a result page
Example: typing 3 and clicking Go navigates to /3.

🚀 Deployment Ideas
Render — free Flask hosting: render.com
Railway — simple deploy from GitHub: railway.app
Heroku — classic PaaS: heroku.com
🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to change.

📄 License
This project is licensed under the MIT License.
