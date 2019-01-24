from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/admin")
def hadmin():
    return "Admin area"

@app.route("/guest/<guest>")
def hguest(guest):
    return "Guest User %s not having admin rights" % guest

@app.route("/user/<name>")
def huser(name):


    if name == "admin":
        return redirect(url_for("hadmin"))
    else:
        return redirect(url_for("hguest", guest=name))

if __name__=="__main__":
    app.run(debug=True)

    
    
