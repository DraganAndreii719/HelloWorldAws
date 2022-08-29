from flask import Flask
 
app = Flask(__name__)
 
@app.route('/hello')
def hello():
    return 'Hello World! te rog eu sa mergi'
 
app.run(host='localhost', port=5000)
