import csv
from random import randint
from flask import Flask
app = Flask(__name__)

# read insults
insults_start = []
insults_middle = []
insults_end = []
with open("insults.csv") as csvfile:
    insult_reader = csv.reader(csvfile, delimiter=",")
    for row in insult_reader:
        start, middle, end = row
        insults_start.append(start)
        insults_middle.append(middle)
        insults_end.append(end)

def generate_insult():
    return insults_start[randint(0, len(insults_start)-1)] + " "\
        + insults_middle[randint(0, len(insults_middle)-1)] + " "\
        + insults_end[randint(0, len(insults_end)-1)] + " "
    
@app.route('/')
def insult():
    return "Thou {insult}".format(insult=generate_insult())
    
@app.route('/<name>')
def insult_name(name):
    return "{name}, thou {insult}".format(name=name, insult=generate_insult())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)