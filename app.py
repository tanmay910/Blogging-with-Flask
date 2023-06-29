from flask import Flask,render_template

app = Flask(__name__)

@app.route('/user/<name>')
def index(name):
    return render_template("index.html",username=name)

@app.errorhandler(404)
def error404(e):
    return render_template('404.html')
    



if __name__ == "__main__":
    app.run(debug=True)
    

    
    