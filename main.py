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
    title= db.Column(db.String(120))
    body = db.Column(db.String)

    def __init__(self, title, body):
        self.title = title
        self.body = body

#blog_posts = []

@app.route('/', methods=['POST', 'GET'])
def index():


    return redirect('/blog')

@app.route('/blog', methods=['POST', 'GET'])
def dat_blog_doh():

    return render_template('blog_page.html',title="Dis Lil Blog O' Mine!", blog_posts=Blog.query.all())
    #return redirect('/')


    

# Need to do error messages displayed if the title or body are left blank, rerendering the form and the info submitted
@app.route('/newpost', methods=['POST', 'GET'])
def add_post():
    if request.method == 'POST':
        blog_title = request.form["blog_title"]
        blog = request.form['new_content']
        new_post = Blog(blog_title, blog)
        db.session.add(new_post)
        db.session.commit()

        blog_posts = Blog.query.all()

        return render_template('add_a_blog.html',title="Dis Lil Blog O' Mine!",  blog_posts=Blog.query.all())
    
        
       # return redirect('/blog')

#@app.route('/newpost', methods=['POST', 'GET'])
#def post():

#@app.route('/newpost', methods=['POST', 'GET'])

#def check_post():

        #Empty Error Displays

 #       blog_title = request.form['blog_title']
  #      blog = request.form['new_content']

   #     title_error = ''
    #    content_error = ''
    
        #if len(blog_title) <= -1:
          #  title_error= "Please provide a title for your blog."
         #   blog_title= ''
        #    new_content= new_content  

       # if len(new_content) <= -1:
           # content_error= "Please provide some content for your blog."
           # blog_title= blog_title
            #new_content= ''
        #if not title_error and not content_error:
            #return render_template('add_a_blog.html',title="Dis Lil Blog O' Mine!", blog_title = blog_title, 
                #new_content= new_content, title_error= title_error, content_error=content_error)



   
        

if __name__ == '__main__':
    app.run()

    