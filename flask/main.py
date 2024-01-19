
from flask import Flask, request, jsonify
from flask_cors import CORS 
from openai import OpenAI
from config import key

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/')
def home():
    return "Yes, Flask app is running on port 5050."


@app.route('/generate-image', methods=['POST'])
def generate_image():
    try:
        client = OpenAI(api_key=key)
        response = client.images.generate(
            prompt=request.json.get(
                'prompt', ''),
            size="1024x1024",
            quality="hd",
            n=1,)
        image_url = response.data[0].url
        return jsonify({'image_url': image_url})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(port=5050)
