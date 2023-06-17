import json
from flask import Flask, request

app = Flask(__name__)

with open('./newslist.json', 'r') as f:
    data = json.load(f)

@app.route('/getList')
def getList():
    pageSize = int(request.args.get('pageSize'))
    pageNum = int(request.args.get('pageNum'))
    start = (pageSize-1)*pageNum
    return {
        'code': 200,
        'data': data[start: start+pageSize],
        'total': len(data)
    }


# @app.route('/getDetail')
# def getDetail():
#     id = int(request.args.get('id'))
#     a[id-1]


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)