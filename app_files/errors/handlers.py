from flask import Blueprint, render_template


errors = Blueprint('errors', __name__)

'''
@errors.errorhandler 
I would have used this but this will work for only this blueprint which is not what I want.
I want this error handler to to work across the entire application.
That's why I used @errors.app_errorhandler instead.
'''


@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500
