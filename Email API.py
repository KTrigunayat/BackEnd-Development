from flask import Flask, request, jsonify, redirect

app = Flask(__name__)
import requests
def send_simple_message():
  	return requests.post(
  		"https://api.mailgun.net/v3/sandboxe9b60374c1894860bc6712b591c93f04.mailgun.org/messages",
  		auth=("api", "beaace59abd0620a4f8a86813da2fc48-c02fd0ba-21ebadf2"),
  		data={"from": "Kshitiz Trigunayat <mailgun@sandboxe9b60374c1894860bc6712b591c93f04.mailgun.org>",
  			"to": ["kshitiz52.525@gmail.com","rayyan.p@atriauniversity.edu.in","sunny.s@atriauniversity.edu.in"],
  			"subject": "Hello",
  			"text": "Kya chal raha hai Batao bhai please!"})
@app.route("/", methods=["POST"])
def index():
	send_simple_message()
	return "Email sent successfully"

@app.route("/webhook", methods=["POST"])
def webhook():
	print("Webhook recieved")
	data = request.get_json()
	print(data)
	return jsonify({"mesage":"OK"})
if __name__ == "__main__":
	app.run(debug=True)
