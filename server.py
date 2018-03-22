"""
This bot listens to port 5002 for incoming connections from Facebook. It takes
in any messages that the bot receives and echos it back.
"""
from flask import Flask, request

app = Flask(__name__, static_url_path="/",
            static_folder="/home/ubuntu/roshan/xbot-agent")



@app.route("/bot2", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        
        return 'Invalid verification token'

    if request.method == 'POST':
        
        return "Success"

if __name__ == "__main__":
    app.run(host="0.0.0.0" port=9002, debug=True, threaded = True)

