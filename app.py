from cynergy import container
from flask import Flask, render_template, request, send_file

import container_initialization
from hat_service import HatService

app = Flask(__name__, static_url_path='')
container_initialization.init({"SKYRIM_HELMET_LOCATION": "skyrim.png", "DOG_MODEL_LOCATION": "dogHeadDetector.dat"})
hat_service = container.get(HatService)


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template("pages/upload.html")
    else:
        if 'file' not in request.files:
            return "Missing file", 400
        image = request.files['file']
        if not image:
            return "Empty file", 400
        result = hat_service.put_hat_on_it(image)
        return send_file(result, "image/png", attachment_filename=f"{image.filename}_WithHat.png", as_attachment=True)


if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0")
