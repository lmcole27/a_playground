from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    var = request.cookies.get('theme')
    if var is None:
        return cookie()
    else:
        return f"<H1>Hello World! {var} </H1>"

@app.route('/cookie')
def cookie():
    response = make_response("<H1>Cookie is set</H1>")
    response.set_cookie('theme', 'dark')
    return response

#RUN THE WEBAPP
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)