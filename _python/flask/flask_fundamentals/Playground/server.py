from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return 'Playground - go to ../play to play' 


@app.route('/play')
def play():
    return render_template('play.html', x = 3, col = 'lightblue') #defualt is 3 boxes

@app.route('/play/<times>')
def playx(times):
    return render_template('play.html',   x = int(times), col = 'lightblue')

@app.route('/play/<times>/<color>')
def playxColor(times, color ):
    return render_template('play.html',   x = int(times), col = color)


if __name__=="__main__":   
    app.run(debug=True)