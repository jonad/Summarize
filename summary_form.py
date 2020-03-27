from flask import Flask, render_template, jsonify, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField

class SummaryForm(FlaskForm):
    summarization = TextAreaField('Enter the sentence to summarize')
    summarize = SubmitField('Summarize')
    
    

