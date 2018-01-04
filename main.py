from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:bloggingmyfeelings@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
app.secret_key = 'y337kGcys&zP3B'

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self, name):
        self.name = name



blog_posts = []

@app.route('/', methods=['POST', 'GET'])
def index():


    return render_template('add_a_blog.html',title="Dis Lil Blog O' Mine!", blog_posts=blog_posts)

@app.route('/blog', methods=['POST'])
def dat_blog_doh():

    return render_template('blog_page.html',title="Dis Lil Blog O' Mine!", blog_posts=blog_posts)
    #return redirect('/')

@app.route('/newpost', methods=['POST'])
def add_post():

    if request.method == 'POST':
        blog = request.form['blog']
        new_post = Blog(blog)
        db.session.add(new_post)
        db.session.commit()


    return render_template('add_a_blog.html',title="Dis Lil Blog O' Mine!",  blog_posts=blog_posts)


if __name__ == '__main__':
    app.run()







if __name__ == '__main__':
    app.run()


    