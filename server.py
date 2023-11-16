from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/engagements')
def engagements():
    return render_template('engagements.html', title="Engagements")


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == "__main__":
    app.run(debug=True)
