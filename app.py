from flask import Flask
from flask import request, jsonify
from uuid import uuid4
import sqlite3
import utils

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/workbooks/add',methods=['POST'])
def upload_a_workbook():
    # accept sheet , access level
    #return file_id and access token
    #return 409 if the file already exists
    file = request.files['file']
    id =str(uuid4())
    access_token = str(uuid4())
    file_name = file.file_name
    file_name = file_name.replace(' ','_')
    if(utils.insertfile(id,file_name,access_token)):
        return jsonify({
            "id":id,
            "file_name":file_name,
            "access_token":access_token
        })
    return "error Occured",500
    

@app.route('/workbooks/<file_id>/<sheet>',methods=['GET'])
def get_sheet_data(file_id, sheet):
    # return jsonified sheet data
    # accept range as query params
    # accept authcode in header return 403 if authentication token incorrect

    pass



if __name__ == '__main__':
    app.run()