from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/',methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    else:
        abort(400)

@app.route('/', methods=['GET'])
def index():
        return 'success', 200
   

if __name__ == '__main__':
    app.run()


