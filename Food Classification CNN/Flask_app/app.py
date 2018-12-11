from flask import Flask, render_template
import requests
from requests.auth import HTTPBasicAuth
from predict import predict

app = Flask(__name__)

@app.route('/')
def index():
  # result = predict('idli (003).JPEG')
  
  return render_template('index.html', predict=predict)

@app.route('/predict/<image_name>')
def prediction(image_name):
  result = predict(image_name)
  
  return result

if __name__ == '__main__':
  app.run(debug=True, port=8002)