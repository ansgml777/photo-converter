from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

@app.route('/remove_bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    file = request.files['image']
    input_image = Image.open(file.stream).convert('RGBA')
    output_image = remove(input_image)
    buf = io.BytesIO()
    output_image.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
