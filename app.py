from flask import Flask, render_template
from const import *
from functions import *
import random
import math as m

app = Flask(__name__)


@app.route('/', defaults={'category': 'all'})
@app.route('/<category>')
def home(category):
    match category:
        case 'moon':
            fileNames = images.MOON_FILES
        case 'landscape':
            fileNames = images.LANDSCAPE_FILES
        case 'other':
            fileNames = images.OTHER_FILES
        case _:
            fileNames = images.ALL

    random.shuffle(fileNames)
    return render_template('home.html',
                           category=category,
                           fileNames=fileNames,
                           range=range,
                           len=len,
                           extract_image_title_from_path=extract_image_title_from_path,
                           ceil=m.ceil)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')
