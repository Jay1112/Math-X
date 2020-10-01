from flask import Flask, render_template, redirect, url_for, request
import random
from config import Config
import requests

temp1 = None
temp2 = None

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/addition",methods=["POST","GET"])
def addition():
	num1 = random.randint(1,100)
	num2 = random.randint(1,100)

	answer = request.form.get("answer")
	temp1 = request.form.get("hidden1")
	temp2 = request.form.get("hidden2")
	type_answer = str(type(answer))

	if type_answer != "<class 'NoneType'>":
		if answer.isdigit() == True:
			temp1 = int(temp1)
			temp2 = int(temp2)
			temp_ans = temp1 + temp2
			correct_ans = str(temp1) + " + " + str(temp2) + " = " + str(temp1+temp2)

			if temp_ans == int(answer):
				return render_template("addition.html",num1=num1,num2=num2,message="Your answer was Correct. | " + correct_ans,right="right")
			else:
				return render_template("addition.html",num1=num1,num2=num2,message="Your answer wasn't Correct. | " + correct_ans,wrong="wrong")
		else:
			return render_template("addition.html",num1=num1,num2=num2,message="Only Digits are allowed.",warn="warning")		

	return render_template("addition.html",num1=num1,num2=num2)

@app.route("/subtraction",methods=["POST","GET"])
def subtraction():
	num1 = random.randint(1,100)
	num2 = random.randint(1,100)

	if num2>num1:
		temp = num1
		num1 = num2
		num2 = temp

	answer = request.form.get("answer")
	temp1 = request.form.get("hidden1")
	temp2 = request.form.get("hidden2")
	type_answer = str(type(answer))

	if type_answer != "<class 'NoneType'>":
		if answer.isdigit() == True:
			temp1 = int(temp1)
			temp2 = int(temp2)
			temp_ans = temp1 - temp2
			correct_ans = str(temp1) + " - " + str(temp2) + " = " + str(temp1-temp2)

			if temp_ans == int(answer):
				return render_template("subtraction.html",num1=num1,num2=num2,message="Your answer was Correct. | " + correct_ans,right="right")
			else:
				return render_template("subtraction.html",num1=num1,num2=num2,message="Your answer wasn't Correct. | " + correct_ans,wrong="wrong")
		else:
			return render_template("subtraction.html",num1=num1,num2=num2,message="Only Digits are allowed.",warn="warning")		

	return render_template("subtraction.html",num1=num1,num2=num2)

@app.route("/multiplication",methods=["POST","GET"])
def multiplication():
	num1 = random.randint(1,100)
	num2 = random.randint(1,100)

	answer = request.form.get("answer")
	temp1 = request.form.get("hidden1")
	temp2 = request.form.get("hidden2")
	type_answer = str(type(answer))

	if type_answer != "<class 'NoneType'>":
		if answer.isdigit() == True:
			temp1 = int(temp1)
			temp2 = int(temp2)
			temp_ans = temp1 * temp2
			correct_ans = str(temp1) + " x " + str(temp2) + " = " + str(temp1*temp2)

			if temp_ans == int(answer):
				return render_template("multiplication.html",num1=num1,num2=num2,message="Your answer was Correct. | " + correct_ans,right="right")
			else:
				return render_template("multiplication.html",num1=num1,num2=num2,message="Your answer wasn't Correct. | " + correct_ans,wrong="wrong")
		else:
			return render_template("multiplication.html",num1=num1,num2=num2,message="Only Digits are allowed.",warn="warning")		

	return render_template("multiplication.html",num1=num1,num2=num2)

@app.route("/division",methods=["POST","GET"])
def division():
	num2 = random.randint(1,100)
	k = random.randint(1,100)
	num1 = k*num2

	answer = request.form.get("answer")
	temp1 = request.form.get("hidden1")
	temp2 = request.form.get("hidden2")
	type_answer = str(type(answer))

	if type_answer != "<class 'NoneType'>":
		if answer.isdigit() == True:
			temp1 = int(temp1)
			temp2 = int(temp2)
			temp_ans = temp1 // temp2
			correct_ans = str(temp1) + " / " + str(temp2) + " = " + str(temp1//temp2)

			if temp_ans == int(answer):
				return render_template("division.html",num1=num1,num2=num2,message="Your answer was Correct. | " + correct_ans,right="right")
			else:
				return render_template("division.html",num1=num1,num2=num2,message="Your answer wasn't Correct. | " + correct_ans,wrong="wrong")
		else:
			return render_template("division.html",num1=num1,num2=num2,message="Only Digits are allowed.",warn="warning")		

	return render_template("division.html",num1=num1,num2=num2)

if __name__=="__main__":
	app.run(debug=True)