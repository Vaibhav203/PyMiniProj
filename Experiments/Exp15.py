# from flask import Flask
# #Vaibhav Bhaliya   68   SEITB-3
# app=Flask(__name__)
# @app.route("/")
# def home():
#     return "SEITB_B3"
# if __name__=="__main__":
#     app.run(debug=True)


# from flask import Flask
# #Vaibhav BHaliya   68   SEITB-B3
# app=Flask(__name__)
# @app.route('/home1')
# def home():
#     return "Welcome to flask API"
# if __name__=="__main__":
#     app.run(debug=True)



# from flask import Flask
# # Vaibhav Bhaliya   68   SEITB-B3
# app=Flask(__name__)
# @app.route('/home1/<int:age>')
# def home(age):
#     return "my age is:%d"%age
# if __name__=="__main__":
#     app.run( debug=True)



# from flask import Flask
# # Vaibahv Bhaliya   68   SEITB-B3
# app=Flask(__name__)
# @app.route('/home1/<name>')
# def home(name):
#     return "Hello "+name+ " You like Flask"
# if __name__=="__main__":
#     app.run(debug=True)


from flask import *
# Vaibhav Bhaliya   68   SEITB-B3
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})

@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num ** 2})

if __name__ == '__main__':
    app.run(debug=True)

