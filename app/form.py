from flask import Flask, render_template, flash, session, redirect, url_for
from wtforms import TextAreaField, TextField, SubmitField
from wtforms.validators import Required,Email
from flask_wtf import FlaskForm


class ContactForm(FlaskForm):
    Name = TextField("Name", validators=[Required("Please enter your name properly.")])
    Email= TextField("E-Mail", validators=[Required("Please enter a Email address."),Email("Please enter a valid Email.")])
    Subject= TextField("Subject", validators=[Required("Please enter a Subject matter.")])
    Message= TextAreaField("Message", validators=[Required("Please enter a Message.")])
    Submit = SubmitField("Send")