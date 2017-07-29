from random import randint
from shakespearean_insult_generator import app


def read_insults(insults_path):
    insults_start, insults_middle, insults_end = [], [], []
    with open(insults_path) as csvfile:
        insults = csvfile.readlines()
        for row in insults:
            start, middle, end = row.strip().split(',')
            insults_start.append(start)
            insults_middle.append(middle)
            insults_end.append(end)

    return insults_start, insults_middle, insults_end


insults_start, insults_middle, insults_end = read_insults("insults.csv")


def generate_insult(insults_start, insults_middle, insults_end):
    return insults_start[randint(0, len(insults_start)-1)] + " "\
        + insults_middle[randint(0, len(insults_middle)-1)] + " "\
        + insults_end[randint(0, len(insults_end)-1)]


@app.route('/')
def insult():
    return "Thou {insult}".format(insult=generate_insult(insults_start,
                                                         insults_middle,
                                                         insults_end))


@app.route('/<name>')
def insult_name(name):
    return "{name}, thou {insult}".format(name=name,
                                          insult=generate_insult(insults_start,
                                                                 insults_middle,
                                                                 insults_end))
