from flask import Flask, render_template, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/', methods=['GET', 'POST'])
def home():
    success = False
    if request.method =='POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        print(f"NEw Contact Message: {name} ({email}) - {message}")
        success = True
    return render_template('index.html', success=success)
if __name__ == '__main__':
    app.run(debug=True)