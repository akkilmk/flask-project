
from flask import Flask,url_for,request,escape
from account import account

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


app.register_blueprint(account,url_prefix ="")



if __name__ == '__main__':
    app.run(debug=True)