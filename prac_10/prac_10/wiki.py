from flask import Flask, request, render_template, redirect, url_for
import markdown, os

app = Flask(__name__)
DATA_DIR = 'pages'

@app.route('/')
def home():
    pages = os.listdir(DATA_DIR)
    return render_template('home.html', pages=pages)

@app.route('/<title>')
def view(title):
    path = os.path.join(DATA_DIR, f"{title}.md")
    if not os.path.exists(path):
        return redirect(url_for('edit', title=title))
    text = open(path).read()
    html = markdown.markdown(text)
    return render_template('view.html', content=html, title=title)

@app.route('/<title>/edit', methods=['GET', 'POST'])
def edit(title):
    path = os.path.join(DATA_DIR, f"{title}.md")
    if request.method == 'POST':
        with open(path, 'w') as f:
            f.write(request.form['content'])
        return redirect(url_for('view', title=title))
    content = ''
    if os.path.exists(path):
        content = open(path).read()
    return render_template('edit.html', content=content, title=title)