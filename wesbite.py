from flask import Flask, render_template, request, redirect, url_for
import PyPDF2
import re
import pandas as pd

app = Flask(__name__)

def GetQuestion(test):
	print(ActualTest)

@app.route("/<typeOfTest>", methods=["POST", "GET"])
def test(typeOfTest):
	if(request.method == "POST"):
		if request.form.get('home') == "Back to Home":
			return redirect(url_for("home"))

	ActualTest = pd.read_csv('Tests/'+typeOfTest+'.csv')
	return render_template("test.html", testTitle=typeOfTest, question=GetQuestion(ActualTest))
	


@app.route("/", methods=["POST", "GET"])
def home():
	if(request.method == "POST"):
		if request.form.get('business') == "BUSINESS MANAGEMENT + ADMINISTRATION":
			return redirect(url_for("test", typeOfTest="Business Management + Administration"))

		if request.form.get('hospitality') == "HOSPITALITY + TOURISM":
			return redirect(url_for("test", typeOfTest="Hospitality + Tourism"))

		if request.form.get('entrepreneurship') == "ENTREPRENEURSHIP":
			return redirect(url_for("test",typeOfTest="Entrepreneurship"))

		if request.form.get('finance') == "FINANCE":
			return redirect(url_for("test", typeOfTest="Finance"))

		if request.form.get('marketing') == "MARKETING":
			return redirect(url_for("test", typeOfTest="Marketing"))

		if request.form.get('personal financial literacy') == "PERSONAL FINANCIAL LITERACY":
			return redirect(url_for("test", typeOfTest="Personal Finance Literacy"))

	return render_template("home.html")

if __name__ == "__main__":
    app.run()


