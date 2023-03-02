# program to pull election voting data from the guild website and do some different stuff
# department api url: https://www.guildofstudents.com/svc/voting/stats/election/paramstats/107?groupIds=9&sortBy=itemname&sortDirection=ascending
# society api url: https://www.guildofstudents.com/svc/voting/stats/election/membershipstats/107?groupIds=1&sortBy=itemname&sortDirection=ascending
# json format is the same for both, just different groupIds
# groupIds: 1 = societies, 9 = departments
# see the existing json files for examples of the data structure

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap

# get the data from the guild website
def get_data(url):
    r = requests.get(url)
    return r.json()

# save the data to a file
def save_formatted_data(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)

# Get the most recent department data from the guild website
def get_department_data():
    url = "https://www.guildofstudents.com/svc/voting/stats/election/paramstats/107?groupIds=9&sortBy=itemname&sortDirection=ascending"
    data = get_data(url)
    save_formatted_data(data, "department_data.json")

# Get the most recent society data from the guild website
def get_society_data():
    url = "https://www.guildofstudents.com/svc/voting/stats/election/membershipstats/107?groupIds=1&sortBy=itemname&sortDirection=ascending"
    data = get_data(url)
    save_formatted_data(data, "society_data.json")

# Save json data to a csv file
def save_data_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# load json data from file
def load_data_from_file(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

# create a plot with provided data
def plot_turnout_data(data, title, x_label, y_label):
    plt.bar(list(data.keys()), list(data.values()), align='center')
    plt.title(title)
    plt.xticks(rotation=90)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # add values to the bars
    for i, v in enumerate(list(data.values())):
        plt.text(i, v, str(round(v)) + "%", color='blue', fontweight='bold', horizontalalignment='center')

    plt.savefig("graphs/" + title + ".png", dpi = 1200)
    plt.show()


# create a plot with provided data, non-percentage data
def plot_data(data, title, x_label, y_label):
    plt.bar(list(data.keys()), list(data.values()), align='center')
    plt.title(title)
    plt.xticks(rotation=90)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # add values to the bars
    for i, v in enumerate(list(data.values())):
        plt.text(i, v, str(round(v)), color='blue', fontweight='bold', horizontalalignment='center')

    plt.savefig("graphs/" + title + ".png", dpi = 1200)
    plt.show()


# create a plot with provided data, vote count with turnout in brackets
def plot_count_with_turnout(data, title, x_label, y_label):
    # separate the data into two lists, one for the vote count and one for the turnout
    vote_count = []
    turnout = []
    labels = []

    for key, value in data.items():
        vote_count.append(value[0])
        turnout.append(value[1])
        labels.append(key)
    
    labels = ["\n".join(wrap(l, 11)) for l in labels]

    # create the plot
    plt.bar(labels, vote_count, align='center')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # add values to the bars
    for i, v in enumerate(vote_count):
        # separate the strings first
        label = str(round(v)) + " (" + str(round(turnout[i])) + "%)"

        plt.text(i, v, label, color='black', fontweight='bold', horizontalalignment='center')

    plt.savefig("graphs/" + title + ".png", dpi = 1200)
    plt.show()
        






