from flask import Flask, render_template, send_from_directory
import glob, os, inflect

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'files'

@app.route("/")
def home():
    filesPaths = glob.glob("files/*")
    pathsIters = [inflect.engine().number_to_words(int(i[0])) for i in enumerate(filesPaths)]
    filesPathsDict = dict(zip(pathsIters, filesPaths))
    return render_template('home.html', filesPaths=filesPathsDict)

@app.route('/files/<filename>', methods=['GET', 'POST'])
def download(filename):
    filepath = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(filepath, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)