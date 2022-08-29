from flask import Flask
 
app = Flask(__name__)
 
@app.route('/hello')
def hello():
    return 'Hello World up'
 
app.run(host='localhost', port=5000)
