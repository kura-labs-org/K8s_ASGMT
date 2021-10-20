from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify
import json
import os.path
from werkzeug.utils import secure_filename

# change to just application = Flask(__name__)
application = app = Flask(__name__)
app.secret_key = 'hfsdfhghergjhfg'


@app.route("/")
def home():
    return render_template('home.html', code=session.keys())

@app.route('/url_page', methods=['GET','POST'])
def page():
    if request.method == 'POST':
        urls = {}

        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)

        if request.form['code'] in urls.keys():
            flash('This code has been taken!!')
            return redirect(url_for('home'))


        urls[request.form['code']] = {'url':request.form['url']}
        with open('urls.json','w') as url_file:
            json.dump(urls, url_file)
            session[request.form['code']] = True
        return render_template('url.html', code=request.form['code'])
    else:
        return redirect(url_for('home'))

@app.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
    return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
@app.route('/api')
def session_api():
    return jsonify(list(session.keys()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)