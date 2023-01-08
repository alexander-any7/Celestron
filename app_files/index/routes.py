from flask import render_template, request, Blueprint
from app_files.db_models import Post


index = Blueprint('index', __name__)


@index.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('home.html', posts=posts)


@index.route('/about')
def about():
    return render_template('about.html', title='About')


@index.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')