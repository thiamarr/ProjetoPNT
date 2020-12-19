from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)
    

@app.route("/")
def index():
    return render_template("pnt.html")

@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        forms = request.forms["nm"]
        return redirect(url_for("forms", frm=forms))
    else:
        return render_template("tabela.html")

@app.route("/<frm>")
def forms(frm):
    return f"<h1>{frm}</h1>"

if __name__ == "__main__":
    app.run(debug=True)