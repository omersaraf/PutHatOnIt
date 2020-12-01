from flask import Flask, render_template, send_from_directory, jsonify, request, send_file

from hat_service import put_hat_on_it

app = Flask(__name__, static_url_path='')


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('templates/static', path)


@app.route('/')
def hello():
    return render_template("pages/upload.html")


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if 'file' not in request.files:
        return "Missing file", 400
    file = request.files['file']
    if not file:
        return "Empty file", 400
    result = put_hat_on_it(file)
    return send_file(result, "image/png", attachment_filename="with_hat.png", as_attachment=True)
    # return jsonify({"success": True})


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
