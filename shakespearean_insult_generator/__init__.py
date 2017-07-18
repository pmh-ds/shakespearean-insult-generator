from flask import Flask
from shakespearean_insult_generator.main.controllers import main

app = Flask(__name__)

app.register_blueprint(main)