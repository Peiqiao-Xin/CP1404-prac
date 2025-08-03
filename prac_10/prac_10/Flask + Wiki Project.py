from flask import Flask, request, render_template, redirect, url_for
import markdown
import os

app = Flask(__name__)
DATA_DIR = 'pages'

@app.route('/')
def home():
    files = os.listdir(DATA_DIR)
    return render_template('home.html', pages=files)

@app.route('/<page>')
def view_page(page):
    path = os.path.join(DATA_DIR, f"{page}.md")
    if not os.path.exists(path):
        return redirect(url_for('edit_page', page=page))
    text = open(path).read()
    html = markdown.markdown(text)
    return render_template('view.html', content=html, page=page)

@app.route('/<page>/edit', methods=['GET', 'POST'])
def edit_page(page):
    path = os.path.join(DATA_DIR, f"{page}.md")
    if request.method == 'POST':
        with open(path, 'w') as f:
            f.write(request.form['content'])
        return redirect(url_for('view_page', page=page))
    content = ''
    if os.path.exists(path):
        content = open(path).read()
    return render_template('edit.html', content=content, page=page)