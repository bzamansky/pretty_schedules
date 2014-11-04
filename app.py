from flask import Flask, render_template, request, session
from roster import getClasses

app = Flask(__name__)
app.secret_key="blah"


@app.route("/", methods = ["GET","POST"])
def home():
	varl = {}
	data = {}
	if request.method == "POST":
		term = request.form['term']
		varl['subj'] = request.form['subject']
		varl['level'] = request.form['level']
		data = getClasses(term,varl)
		print data[0].keys()




	return render_template("index.html",classes=data)

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port = 5000)
