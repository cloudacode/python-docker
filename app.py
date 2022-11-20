from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # welcome messages
    messages = ['Welcome Cloudacode.com',
                'Python Flask App',
                ]
    # return render_template('hello.html', messages=messages)
    return messages
