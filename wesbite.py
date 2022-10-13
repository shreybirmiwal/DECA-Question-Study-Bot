from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/business")
def business():
	return "<h1>business<h1>"

@app.route("/hospitality")
def hospitality():
	return "<h1>hospitality<h1>"

@app.route("/entrepreneurship")
def entrepreneurship():
	return "<h1>entrepreneurship<h1>"

@app.route("/finance")
def finance():
	return "<h1>finance<h1>"

@app.route("/marketing")
def marketing():
	return "<h1>marketing<h1>"

@app.route("/pfl")
def pfl():
	return "<h1>personal financial literacy<h1>"

@app.route("/", methods=["POST", "GET"])
def home():
	if(request.method == "POST"):
		if request.form.get('business') == "BUSINESS MANAGEMENT + ADMINISTRATION":
			return redirect(url_for("business"))

		if request.form.get('hospitality') == "HOSPITALITY + TOURISM":
			return redirect(url_for("hospitality"))

		if request.form.get('entrepreneurship') == "ENTREPRENEURSHIP":
			return redirect(url_for("entrepreneurship"))

		if request.form.get('finance') == "FINANCE":
			return redirect(url_for("finance"))

		if request.form.get('marketing') == "MARKETING":
			return redirect(url_for("marketing"))

		if request.form.get('personal financial literacy') == "PERSONAL FINANCIAL LITERACY":
			return redirect(url_for("pfl"))

	return render_template("home.html")

if __name__ == "__main__":
    app.run()


