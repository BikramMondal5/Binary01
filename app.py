from flask import Flask, render_template

app = Flask(__name__, template_folder='frontend/templates')

@app.route('/')
def landing_page():
    return render_template('index.html')  # Just mention the file name

@app.route('/creators')
def creators_page():
    return render_template('creators.html')

@app.route('/learners')
def learners_page():
    return render_template('learners.html')

if __name__ == '__main__':
    app.run(debug=True)
