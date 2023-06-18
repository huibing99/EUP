import json
from flask import Flask, request

app = Flask(__name__)

with open('./posts.json', 'r') as f:
    data = json.load(f)

newslist = []

for post in data:
    newslist.append({
        "id": post["id"],
        "date": post["date"],
        "content": post["content"],
        "source": post["source"],
        "label": post["label"],
        "label_2": post["label_2"]
    })


@app.route('/getList')
def getList():
    try:
        pageSize = int(request.args.get('pageSize'))
        pageNum = int(request.args.get('pageNum'))
        start = (pageNum-1)*pageSize
        return {
            'code': 200,
            'data': newslist[start: start+pageSize],
            'total': len(newslist)
        }
    except:
        return {
            'code': 400,
            'data': ''
        }


@app.route('/getDetail')
def getDetail():
    try:
        id = int(request.args.get('id'))
        return {
            'code': 200,
            'data': data[id-1]
        }
    except:
        return {
            'code': 400,
            'data': ''
        }


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)