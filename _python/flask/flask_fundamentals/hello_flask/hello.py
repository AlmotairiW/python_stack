from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')                           
def hello_world():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html',  phrase="hello", times=5)


@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>') 
def say(name):
    return "Hi," + name

@app.route('/repeat/<n>/<word>') 
def repeat(n, word):
    return (word+'\n') * int(n)

@app.route('/*')
def any():
    return 'Sorry! No response. Try again."'
if __name__=="__main__":   
    app.run(debug=True)    

