from flask import Flask

app = Flask(__name__)

from shakespearean_insult_generator import views
