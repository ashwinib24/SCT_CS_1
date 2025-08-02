from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift, mode):
    result = ""
    shift = int(shift)
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    if request.method == 'POST':
        text = request.form['message']
        shift = request.form['shift']
        mode = request.form['mode']
        output = caesar_cipher(text, shift, mode)
    return render_template('index.html', result=output)

if __name__ == '__main__':
    app.run(debug=True)
