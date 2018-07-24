from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('helloworld.html')

@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    f = open('/data/user_inputs.txt','a')
    f.write(first_name+" ")
    f.close()
    return render_template('helloworld.html')

if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0', port = 3000)
