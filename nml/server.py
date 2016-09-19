from flask import Flask, render_template, request, url_for
from flask_cors import CORS
import os, sys, base64
import MoleAnalyzer


app = Flask(__name__)
CORS(app)


@app.route('/')
def form():
    return 'Gotcha'


@app.route('/image/', methods=['POST'])
def image():
    data = request.form['file'].split(',', 1)[1]
    pic = base64.b64decode(data)
    with open(r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\analyze\testing1.jpg", 'wb') as file:
        file.write(pic)

    result = MoleAnalyzer.analyze_mole(r"C:\Users\ofir arzi\Desktop\NoMole\NoMole\nml\images\analyze\testing1.jpg")
    return str(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7891))
    app.run(host='192.168.0.52', port=port, debug=True)
