#Resources:
#https://www.youtube.com/watch?v=7LNl2JlZKHA (tutorial to set up simple API in React using Flask)
#https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/ (Tutorial to install Python environment in Windows)
#https://www.geeksforgeeks.org/how-to-install-flask-in-windows/ (tutorial to install Flask in Windows)
#Before running React app, test API at localhost:5000/members. 
#How to run this server:
# run "cd .ven\" AND "Scripts\activate" (Windows) or "source ven/bin/activate" (Mac)
# run "pip install flask" (Windows) or "pip3 install flask" (Mac)
# run "python server.py" (Windows) or "python3 server.py" (Mac)
#
#to stop server, run "deactivate"

from flask import Flask, render_template, request, send_file
from flask_cors import CORS 
import subprocess
import os

app = Flask(__name__)
CORS(app)

SCRIPT_PATH = "TTI_AI/stable_diffusion.openvino/demo.py"  # Path to your Stable Diffusion script
OUTPUT_PATH = "output.png"  # Path where the image is saved
PORT = 5000

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    
    try:
        # Run the Stable Diffusion script with the user's prompt
        subprocess.run(
            ["/usr/bin/python3", SCRIPT_PATH, "--prompt", prompt],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Verify the image was created
        if not os.path.exists(OUTPUT_PATH):
            raise FileNotFoundError("Output image not generated")
            
        return send_file(OUTPUT_PATH, mimetype='image/png')
    
    except Exception as e:
        return f"Error generating image: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)

#from flask import Flask, request, jsonify
#import requests
#from flask_cors import CORS



#app = Flask(__name__)
#CORS(app)

#Members API Route
#@app.route("/members")

#def members():
    #return {"members": ["Member1", "Member2", "Member3"]} #dictionary (key-value pair) with array as value

#if __name__ == "__main__":
    #app.run(debug=True, host='0.0.0.0', port=5000)