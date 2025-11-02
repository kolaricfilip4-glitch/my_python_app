from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-please-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///history_blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"Article('{self.title}', '{self.author}', '{self.date_posted}')"

# Routes
@app.route('/')
def index():
    articles = Article.query.order_by(Article.date_posted.desc()).all()
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article.html', article=article)

@app.route('/new', methods=['GET', 'POST'])
def new_article():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        
        if title and author and content:
            article = Article(title=title, author=author, content=content)
            db.session.add(article)
            db.session.commit()
            flash('Article successfully created!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Please fill in all fields!', 'error')
    
    return render_template('new_article.html')

@app.route('/edit/<int:article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    article = Article.query.get_or_404(article_id)
    
    if request.method == 'POST':
        article.title = request.form['title']
        article.author = request.form['author']
        article.content = request.form['content']
        
        if article.title and article.author and article.content:
            db.session.commit()
            flash('Article successfully updated!', 'success')
            return redirect(url_for('article', article_id=article.id))
        else:
            flash('Please fill in all fields!', 'error')
    
    return render_template('edit_article.html', article=article)

@app.route('/delete/<int:article_id>', methods=['POST'])
def delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    flash('Article successfully deleted!', 'success')
    return redirect(url_for('index'))

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Only enable debug mode if explicitly set in environment variable
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)
