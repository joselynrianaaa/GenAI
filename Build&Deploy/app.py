from flask import Flask, request, render_template
import requests
import base64

app = Flask(__name__)

# Replace with your Krutrim secret key
API_KEY = 'yswq-q_rcpHFQZzPdTeI//qWoP_Sd'
API_URL = 'https://cloud.olakrutrim.com/v1/multimodal/generations/idefics'

def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

def query_idefics(image_bytes, prompt):
    payload = {
        "modelName": "idefics",
        "prompts": [
            "<image>",  # Placeholder for the image
            prompt
        ],
        "images": [
            image_bytes  # Base64 encoded image
        ],
        "maxTokens": 50
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    response = requests.post(url=API_URL, json=payload, headers=headers)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        image = request.files.get('image')
        prompt = request.form.get('prompt')

        if image and prompt:
            image_bytes = encode_image(image)
            result = query_idefics(image_bytes, prompt)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
