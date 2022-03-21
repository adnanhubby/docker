from flask import Flask 
import os
import sys
app = Flask(__name__) 
 
@app.route('/') 
def hello_world(): 
    return 'Flask Dockerized'
 
if __name__ == '__main__':
    username = os.getenv("USERNAME")
    if username == None or username == "":
        print("please specify the username SECRET")
        sys.exit(1)
    app.run(debug=True, host='0.0.0.0') 
