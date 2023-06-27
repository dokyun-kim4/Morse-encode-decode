from flask import Flask,redirect,render_template,request
import morse as ms

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/encode', methods=['POST'])
def morse_encode():
    text = request.form['text']
    encoded_text = ms.encode_morse(text)
    return encoded_text


@app.route('/decode', methods=['POST'])
def morse_decode():
    text = request.form['text']
    decoded_text = ms.decode_morse(text)
    return decoded_text


if __name__ == "__main__":
    app.run(debug=True)