import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    hostname=os.environ.get('DATABASE_HOSTNAME')
    port=os.environ.get('DATABASE_PORT')
    password=os.environ.get('DATABASE_PASSWORD')
    db_name=os.environ.get('DATABASE_NAME')
    username=os.environ.get('DATABASE_USERNAME')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{username}:{password}@{hostname}:{port}/{db_name}'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
 