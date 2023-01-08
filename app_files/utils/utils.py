import os
import secrets
from PIL import Image
from flask import url_for, current_app
from email.message import EmailMessage
import ssl
import smtplib


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token(user)
    em_sender = 'noreply@celestron.com'
    em_receiver = user.email
    subject = 'Password Reset Request'
    body = f'To reset your password, visit the following link: {url_for("users.reset_token", token=token, _external=True)}. If you did not make this request, then simply ignore this email and no changes will be made.'
    email = EmailMessage()
    email['Subject'] = subject
    email['From'] = em_sender
    email['To'] = em_receiver
    email.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.att.yahoo.com', context=context) as smtp:
        smtp.login(os.environ.get('MAIL_USERNAME'), os.environ.get('MAIL_PASSWORD'))
        smtp.sendmail(from_addr=em_sender, to_addrs=em_receiver, msg=email.as_string())

