from flask import Flask,render_template,request
from flask import Flask,request
from . import app
from flask_restful import Api
import nltk
import nltk.corpus
# nltk.download('stopwords')
import nltk.tokenize.punkt
import nltk.stem.snowball
import time
import collections
from nltk.tokenize import WordPunctTokenizer
import string

import pyodbc
app = Flask(__name__)