from flask import Flask ,request

app = Flask(__name__)

@app.route('/')
def hello():
    q = request.args.get('q')
    print(q)
    return { "message": "Hello!"}, 201

@app.route('')

if __name__ == '__main__':
    app.run(debug=True)