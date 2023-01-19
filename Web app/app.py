from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import generate_mask

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'uploads'

#home page
@app.route('/')
def index():
    return render_template('index.html')

#to upload MRI file
@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            generate_mask.mask_generator(uploaded_file)
        return redirect(url_for('display_layers'))
    return render_template('index.html')

#go to second webpage to show prediction
@app.route('/predict')
def display_layers():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('view_layers.html', files=files)


@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


if __name__ == "__main__":
    app.run(debug=True)
