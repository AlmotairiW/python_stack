from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/') 
def hello_world():
    return 'Hello World!' 

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>') 
def say(name):
    return "Hi," + name

@app.route('/repeat/<n>/<word>') 
def repeat(n, word):
    return (word+'\n') * int(n)

if __name__=="__main__":   
    app.run(debug=True)    

