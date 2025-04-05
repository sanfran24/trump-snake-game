from flask import Flask, send_file, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Trump Stock Snake</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f0f0f0;
                color: #333;
            }
            h1 {
                color: #d00;
                text-align: center;
            }
            .game-container {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                margin: 20px 0;
                text-align: center;
            }
            .download-btn {
                display: inline-block;
                background-color: #d00;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                margin-top: 20px;
            }
            .download-btn:hover {
                background-color: #b00;
            }
            .game-info {
                margin: 20px 0;
                line-height: 1.6;
            }
            img {
                max-width: 100%;
                border-radius: 5px;
                margin: 10px 0;
            }
        </style>
    </head>
    <body>
        <h1>Trump Stock Snake Game</h1>
        
        <div class="game-container">
            <h2>Play the Trump Stock Snake Game!</h2>
            <p>Control the Trump snake and eat stock logos to grow longer!</p>
            
            <div class="game-info">
                <h3>Game Features:</h3>
                <ul style="text-align: left;">
                    <li>Control Trump as he gobbles up the stock market</li>
                    <li>Collect famous company logos to grow your snake</li>
                    <li>American flag background</li>
                    <li>Sound effects when eating logos</li>
                    <li>Special sound clip at 10 logos eaten</li>
                </ul>
            </div>
            
            <p>This game is a Python application and must be downloaded to play.</p>
            <a href="/download" class="download-btn">Download Game</a>
        </div>
        
        <div class="game-container">
            <h3>How to Play:</h3>
            <p>1. Download the game using the button above</p>
            <p>2. Extract the ZIP file</p>
            <p>3. Run main.py to start playing</p>
            <p>4. Use arrow keys to control the snake</p>
        </div>

        <div class="game-container">
            <p>Created with Python and Pygame</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/download')
def download():
    # This would typically be a path to your packaged game
    # For now, we'll just return a simple text file
    return "Download feature will be implemented soon!"

if __name__ == '__main__':
    app.run(debug=True)
