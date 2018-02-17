from flask import Flask, render_template, flash, session, redirect, url_for
from wtforms import TextAreaField, TextField, SubmitField
from wtforms.validators import Required,Email
from flask_wtf import FlaskForm


class ContactForm(FlaskForm):
    name = TextField("Name", validators=[Required("Please enter your name.")])
    Email= TextField("E-Mail", validators=[Required("Please enter your Email."),Email("Please enter your Email.")])
    Subject= TextField("Subject", validators=[Required("Please enter a Subject.")])
    Message= TextAreaField("Message", validators=[Required("Please enter a Message.")])
    Submit = SubmitField("Send")