from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/download')
def download_file(filename):
    path = filename
    return send_file(path, as_attachment=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/introduction')
def introduction():
    return render_template('introduction.html')


@app.route('/analysis')
def analysis():
    return render_template('analysis.html')


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/dataset')
def dataset():
    return render_template('dataset.html')


@app.route('/implementation')
def implementation():
    return render_template('implementation.html')


if __name__ == '__main__':
    app.run(debug=True)
