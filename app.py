from app_files import create_app, db
from app_files.index.routes import home
from os import path

app = create_app()

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return home()


'''
This is just an entry point into the application.
 
'''
