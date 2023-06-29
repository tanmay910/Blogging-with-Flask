from flask import Flask,render_template

app = Flask(__name__)

@app.route('/user/<name>')
def index(name):
    return render_template("index.html",username=name)


if __name__ == "__main__":
    app.run(debug=True)
    

    
    