from flask import *

app = Flask(__name__)

@app.route("/")
def upload():
    return render_template("upload_file.html")

if __name__ == "__main__":
    app.run(debug=True)
