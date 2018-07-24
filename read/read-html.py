from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    f = open('/data/user_inputs.txt','r')
    msg = f.read()
    f.close()
    arr = msg.split(" ")
    msg = ""
    for i in range(len(arr)):
    	msg += arr[i]+"<br>"
    return msg

if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0', port = 4000)
