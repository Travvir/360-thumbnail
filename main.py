from flask import send_file, Flask, request, render_template
from werkzeug.utils import secure_filename
from equi2pers.lib.Equirec2Perspec import Equirectangular
import cv2
import os
import json
import base64

app = Flask(__name__)

@app.route("/")
def render():
    return render_template('index.html')


@app.route("/thumbnail", methods=['POST'])
def thumbnail():
    print(request)
    height = 300
    width = 300
    if 'img' not in request.files:
        return 'No file part', 400
    file = request.files['img']

    if file.filename == '':
        return 'No selected file', 400

    if 'fov' not in request.form or 'theta' not in request.form or 'phi' not in request.form:
        return 'Missing parameters', 400

    if 'height' in request.form and request.form.get('height').strip():
        height = int(request.form.get('height'))
    if 'width' in request.form and request.form.get('width').strip():
        width = int(request.form.get('width'))

    filename = secure_filename(file.filename)
    filepath = os.path.join('/tmp', filename)
    file.save(filepath)


    fov = float(request.form.get('fov'))
    theta = float(request.form.get('theta'))
    phi = float(request.form.get('phi'))

    equ = Equirectangular(filepath)
    img = equ.GetPerspective(fov, theta, phi, height, width)
    output1 = '/tmp/output.png'
    cv2.imwrite(output1, img) 
    with open(output1, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('ascii')

    return json.dumps({"image": encoded_string})
    # return send_file(output1, mimetype='image/png')