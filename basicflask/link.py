from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    a = "Devesh"
    
    return render_template("welcome.html")+ a

if __name__=="__main__":
    app.run(debug=True)
