from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def pagehome():
    return render_template("HTML.html")
if __name__=="__main__":
    app.run(port=8081)