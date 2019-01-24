from flask import Flask, render_template
app = Flask(__name__)

@app.route("/result")
def dict():

    result = {"Maths":80,"C":70,"Java":80}

    return render_template("table.html",result=result)

if __name__=="__main__":
    app.run(debug=True)
