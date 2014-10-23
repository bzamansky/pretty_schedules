from flask import Flask, render_template, request, session
from roster import getClasses

app = Flask(__name__)
app.secret_key="blah"


@app.route("/", methods = ["GET","POST"])
def home():
	url = ""
	varl = {}
	if request.method == "POST":
		varl['subj'] = request.form['subject']
		varl['level'] = request.form['level']
		url = getClasses("SP15",varl)


	return render_template("index.html",url=url)

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port = 7999)