from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/c")
def c():
	code = """
main() {
	printf("Hello World!")
}"""
	return render_template('index.html', code=code)

@app.route("/python")
def python():
	code = """print "Hello World!"
	"""
	return render_template('index.html', code=code)

if __name__ == "__main__":
    app.run(debug=True)