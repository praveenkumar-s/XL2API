from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/workbooks/add',methods=['POST'])
def upload_a_workbook():
    # accept sheet , access level
    #return file_id and access token
    #return 409 if the file already exists
    pass

@app.route('/workbooks/<file_id>/<sheet>',methods=['GET'])
def get_sheet_data(file_id, sheet):
    # return jsonified sheet data
    # accept range as query params
    # accept authcode in header return 403 if authentication token incorrect

    pass



if __name__ == '__main__':
    app.run()