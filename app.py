
from datetime import datetime
import pytz
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/api/v1/hora', methods=['POST'])
def hora():
  content = request.json
  try:
    data = datetime.strptime(
      "%s %s" % (content['hora'], content['timezone']),
      '%H:%M:%S %z',
    )
    result = data.astimezone(pytz.utc).strftime("%H:%M:%S")

    return jsonify({
      "response": {
        "time": result,
        "timezone": "utc",
      },
    })
  except Exception as e:
    return jsonify({
      "error": str(e),
    })

@app.route('/', methods=['GET'])
def home():
  return render_template('home.html')


if __name__ == '__main__':
  app.run(host= '0.0.0.0', debug=True)