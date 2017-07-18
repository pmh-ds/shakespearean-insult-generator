import csv
from flask import Flask
app = Flask(__name__)

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
    
print(insults_start)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)