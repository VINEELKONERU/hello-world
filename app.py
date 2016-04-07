from flask import Flask, request, jsonify 
from mongo import mongoFront

handle = mongoFront()
app = Flask(__name__)

@app.route("/")
def hello():
    return "I help you to find the articles"


@app.route('/api/titles', methods=['POST'])
def titles():
    req_json = request.get_json()
    if req_json:
        matched_records = handle.find_title(req_json["title"])
        return jsonify(matched_records)
    else:
        return jsonify({"status": "failed", "reason": "improper inputs"})
    # content = request.get_json(force=True)
    # print content

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=80) 
