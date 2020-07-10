from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('upload.template.html',
                           CLOUD_NAME=os.environ.get('CLOUD_NAME'),
                           CLOUD_UPLOAD_PRESET=os.environ.get(
                               'CLOUD_UPLOAD_PRESET')
                           )


@app.route('/', methods=["POST"])
def process_upload():
    uploaded_url = request.form.get('uploaded_file_url')
    return render_template('show_image.template.html', url=uploaded_url)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
