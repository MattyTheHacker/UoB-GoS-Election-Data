# program to pull election voting data from the guild website and do some different stuff
# department api url: https://www.guildofstudents.com/svc/voting/stats/election/paramstats/107?groupIds=9&sortBy=itemname&sortDirection=ascending
# society api url: https://www.guildofstudents.com/svc/voting/stats/election/membershipstats/107?groupIds=1&sortBy=itemname&sortDirection=ascending
# json format is the same for both, just different groupIds
# groupIds: 1 = societies, 9 = departments
# see the existing json files for examples of the data structure

import requests
import os
import json
import csv
import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap
from sanitize_filename import sanitize

# list all json files in a directory
def list_json_files(directory):
    return [pos_json for pos_json in os.listdir(directory) if pos_json.endswith('.json')]

# get the data from the guild website
def get_data(url):
    r = requests.get(url)
    return r.json()

# save the data to a file
def save_formatted_data(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)

# check when the specified data was last updated
def check_last_updated(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data["DateGenerated"]

# Get the most recent department data from the guild website
def get_department_data():
    url = "https://www.guildofstudents.com/svc/voting/stats/election/paramstats/107?groupIds=9&sortBy=itemname&sortDirection=ascending"
    data = get_data(url)
    save_formatted_data(data, "data/department_data.json")

# Get the most recent society data from the guild website
def get_society_data():
    url = "https://www.guildofstudents.com/svc/voting/stats/election/membershipstats/107?groupIds=1&sortBy=itemname&sortDirection=ascending"
    data = get_data(url)
    save_formatted_data(data, "data/society_data.json")

# get the most recent accommodation data from the guild website
def get_accommodation_data():
    url = "https://www.guildofstudents.com/svc/voting/stats/election/paramstats/107?groupIds=5&sortBy=itemname&sortDirection=ascending"
    data = get_data(url)
    save_formatted_data(data, "data/accommodation_data.json")

def get_student_type_data():
    url = "https://www.guildofstudents.com/svc/voting/stats/election/paramstats/107?groupIds=4&sortBy=itemname&sortDirection=ascending"
    data = get_data(url)
    save_formatted_data(data, "data/student_type_data.json")

def get_study_level_data():
    url = "https://www.guildofstudents.com/svc/voting/stats/election/paramstats/107?groupIds=7&sortBy=itemname&sortDirection=ascending"
    data = get_data(url)
    save_formatted_data(data, "data/study_level_data.json")

def get_all_data_in_one_file():
    url = "https://www.guildofstudents.com/svc/voting/stats/election/paramstats/107?groupIds=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20&sortBy=itemname&sortDirection=ascending"
    data = get_data(url)
    save_formatted_data(data, "data/all_data.json")

def get_all_specific_election_data(election_id):
    url = "https://www.guildofstudents.com/svc/voting/stats/election/paramstats/" + str(election_id) + "?groupIds=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20&sortBy=itemname&sortDirection=ascending"
    data = get_data(url)

    # extract title from the json
    title = data["Title"]

    # remove any invalid characters from the title
    title = sanitize(title)

    save_formatted_data(data, str("historic_data/election_" + str(election_id) + "_" + title + ".json"))
    print("[INFO] Fetching data for election " + title + "... done!")

# get all the most recent data from the guild website
def get_all_data():
    print("[INFO] Fetching department data...")
    get_department_data()
    print("[INFO] Fetching society data...")
    get_society_data()
    print("[INFO] Fetching accommodation data...")
    get_accommodation_data()
    print("[INFO] Fetching student type data...")
    get_student_type_data()
    print("[INFO] Fetching study level data...")
    get_study_level_data()
    print("[INFO] Fetching all data... done!")

# Save json data to a csv file
def save_data_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# save a dictionary to csv file
def save_dictionary_to_csv(dictionary, filename):
    with open (filename, 'w') as f:
        w = csv.DictWriter(f, dictionary.keys())
        w.writeheader()
        w.writerow(dictionary)


# load json data from file
def load_data_from_file(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

# create a plot with provided data
def plot_turnout_data(data, title, x_label, y_label):
    # wrap labels
    labels = ["\n".join(wrap(l, 11)) for l in list(data.keys())]

    plt.figure(figsize = (12, 8), dpi = 100)
    plt.bar(labels, list(data.values()), align='center')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # add values to the bars
    for i, v in enumerate(list(data.values())):
        plt.text(i, v, str(round(v)) + "%", color='blue', fontweight='bold', horizontalalignment='center')

    plt.savefig("graphs/" + title + ".png")
    # plt.show()


# create a plot with provided data, non-percentage data
def plot_data(data, title, x_label, y_label):
    # wrap labels
    labels = ["\n".join(wrap(l, 11)) for l in list(data.keys())]

    plt.figure(figsize = (12, 8), dpi = 100)
    plt.bar(labels, list(data.values()), align='center')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # add values to the bars
    for i, v in enumerate(list(data.values())):
        plt.text(i, v, str(round(v)), color='blue', fontweight='bold', horizontalalignment='center')

    plt.savefig("graphs/" + title + ".png")
    # plt.show()


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
        # print(key, value[0], value[1])
    
    labels = ["\n".join(wrap(l, 11)) for l in labels]

    # create the plot
    plt.figure(figsize = (16, 12), dpi = 200)
    plt.bar(labels, vote_count, align='center')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # add values to the bars
    for i, v in enumerate(vote_count):
        # separate the strings first
        label = str(round(v)) + " (" + str(round(turnout[i])) + "%)"

        plt.text(i, v, label, color='black', fontweight='bold', horizontalalignment='center')

    plt.savefig("graphs/" + title + ".png")
    # plt.show()
        

def plot_turnout_with_vote_count(data, title, x_label, y_label):
    # separate the data into lists
    vote_count = []
    turnout = []
    labels = []

    for key, value in data.items():
        vote_count.append(value[0])
        turnout.append(value[1])
        labels.append(key)
        # print(key, value[0], value[1])

    labels = ["\n".join(wrap(l, 11)) for l in labels]

    # create the plot
    plt.figure(figsize = (16, 12), dpi = 200)
    plt.bar(labels, turnout, align='center')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # add values to the bars
    for i, v in enumerate(turnout):
        # separate the strings first
        label = str(round(v)) + "% (" + str(round(vote_count[i])) + ")"

        plt.text(i, v, label, color='black', fontweight='bold', horizontalalignment='center')

    plt.savefig("graphs/" + title + ".png")
    


# plot a pie chart with the provided data
def plot_pie_chart(data, title, labels):

    # generate the plot
    fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

    # configure the plot to be a pie chart with the data and labels we have
    ax.pie(data, labels=labels, autopct='%1.1f%%')

    # save the plot to the folder
    plt.savefig("graphs/" + title + ".png")


def plot_historic_election_turnout(data):
    title = "Historic Election Turnout"
    x_label = "Election"
    y_label = "Turnout"

    labels = []
    turnout = []

    # the data is in the format: (title, turnout)
    # title should be plotted on the x axis
    # turnout should be plotted on the y axis

    # iterate over the list and put the items into their respective list
    for item in data:
        labels.append(item[0])
        turnout.append(item[1])

    # wrap the labels
    labels = ["\n".join(wrap(l, 9)) for l in labels]

    # create the plot
    plt.figure(figsize = (20, 12), dpi = 200)
    plt.bar(labels, turnout, align='edge', width=0.5)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # add values to the bars
    for i, v in enumerate(turnout):
        plt.text(i, v, str(round(v)) + "%", color='black', fontweight='bold', horizontalalignment='center')
    
    # show the plot
    # plt.show()

    # save the plot to the folder
    plt.savefig("graphs/" + title + ".png")
