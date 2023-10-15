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

@app.route('/paste/<text>')
def put_data():
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
	win32clipboard.CloseClipboard()

if __name__ == "__main__":
    app.run()