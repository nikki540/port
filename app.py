from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)
# CHANGE this in production (store in environment variable)
app.config['SECRET_KEY'] = 'replace-with-a-secure-random-value'

@app.route('/')
def home():
    # show success message if redirected after contact
    success = request.args.get('success')
    return render_template('index.html', success=success)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    message = request.form.get('message', '').strip()

    # Save messages to a local file (for demo). In production use DB / email.
    os.makedirs('data', exist_ok=True)
    with open('data/messages.txt', 'a', encoding='utf-8') as f:
        f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n---\n")

    # Redirect back to home with a success flag
    return redirect(url_for('home', success='true'))

@app.route('/resume')
def download_resume():
    # sends static/resume.pdf as a download
    return send_from_directory('static', 'Res.pdf', as_attachment=True)

if __name__ == '__main__':
    # debug=True for local development; turn off in production
    app.run(debug=True)
