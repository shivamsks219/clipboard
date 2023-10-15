#flask app for clipboard
import win32clipboard
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def fetch_data():
    win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	return data
