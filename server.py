from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# `read-form` endpoint 
@app.route('/handleSubmit', methods=['POST'])
def handleSubmit():

    # Get the form data as Python ImmutableDict datatype 
    data = request.form

    ## Return the extracted information 
    return {
        'name'     : data['name'],
        'why are you here' : data['address']
    }
