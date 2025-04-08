from flask import Flask, render_template, request
from datetime import datetime
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
    return render_template('index.html', current_year=datetime.now().year, success=success)
# test page
@app.route('/tes')
def tes():
    return render_template('tes.html')
if __name__ == '__main__':
    app.run(debug=True)