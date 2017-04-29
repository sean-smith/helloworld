
# github.com/sean-smith/helloworld

from flask import Flask, render_template
app = Flask(__name__,static_url_path='', 
       	static_folder='static')

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
	code = """
def helloworld():
	print ' Hello World!'"""
	return render_template('index.html', code=code)

if __name__ == "__main__":
    app.run('0.0.0.0', port=80)