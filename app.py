from flask import Flask, render_template, send_from_directory
import os

# Importing your parser function
from gazparser import parse

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/download')
def download():
     parse()  # Calling the parse function you imported
     return send_from_directory(directory=os.getcwd(), filename="result.xlsx", as_attachment=True)

if __name__ == '__main__':
     app.run(debug=True)

