import utils

# plot the vote count for departments combined with their turnout in brackets
def plot_department_vote_count_and_turnout():
    # update department data in the file 
    utils.get_department_data()

    # load the data from the file
    data = utils.load_data_from_file("data/department_data.json")

    # create a dictionary to store the department name and a touple of the vote count and turnout
    department_data = {}

    # loop through the data and add the department name and vote count to the dictionary
    # format of the data is: [Groups] -> [Items] -> [Name, Turnout]
    for group in data["Groups"]:
        for item in group["Items"]:
            department_data[item["Name"]] = (item["Voters"], item["Turnout"])

    # sort the dictionary by the vote count, highest to lowest
    sorted_dict = sorted(department_data.items(), key=lambda x: x[1][0], reverse=True)

    # get the top 10 departments
    top_10 = sorted_dict[:10]

    # plot the top 10 departments
    utils.plot_count_with_turnout(dict(top_10), "Top 10 Departments by Vote Count With Turnout", "Department", "Vote Count")

def plot_society_vote_count_and_turnout():
    # update society data in the file
    utils.get_society_data()

    # load the data from the file
    data = utils.load_data_from_file("data/society_data.json")

    # create a dictionary to store the society name and a touple of the vote count and turnout
    society_data = {}

    # loop through the data and add the society name and vote count to the dictionary
    # format of the data is: [Groups] -> [Items] -> [Name, Turnout]
    for group in data["Groups"]:
        for item in group["Items"]:
            society_data[item["Name"]] = (item["Voters"], item["Turnout"])

    # sort the dictionary by the vote count, highest to lowest
    sorted_dict = sorted(society_data.items(), key=lambda x: x[1][0], reverse=True)

    # get the top 10 societies
    top_10 = sorted_dict[:10]

    # plot the top 10 societies
    utils.plot_count_with_turnout(dict(top_10), "Top 10 Societies by Vote Count With Turnout", "Society", "Vote Count")

def plot_accommodation_vote_count_and_turnout():
    # update accommodation data in the file
    utils.get_accommodation_data()

    # load the data from the file
    data = utils.load_data_from_file("data/accommodation_data.json")

    # create a dictionary to store the accommodation name and a touple of the vote count and turnout
    accommodation_data = {}

    # loop through the data and add the accommodation name and vote count to the dictionary
    # format of the data is: [Groups] -> [Items] -> [Name, Turnout]
    for group in data["Groups"]:
        for item in group["Items"]:
            accommodation_data[item["Name"]] = (item["Voters"], item["Turnout"])

    # sort the dictionary by the vote count, highest to lowest
    sorted_dict = sorted(accommodation_data.items(), key=lambda x: x[1][0], reverse=True)
    
    # take off the first value cos it's scuffed
    sorted_dict = sorted_dict[1:]

    # plot the top 10 accommodations
    utils.plot_count_with_turnout(dict(sorted_dict), "Top 10 Accommodations by Vote Count With Turnout", "Accommodation", "Vote Count")

def plot_student_type_vote_count_and_turnout():
    # update student type data in the file
    utils.get_student_type_data()

    # load the data from the file
    data = utils.load_data_from_file("data/student_type_data.json")

    # create a dictionary to store the student type name and a touple of the vote count and turnout
    student_type_data = {}

    # loop through the data and add the student type name and vote count to the dictionary
    # format of the data is: [Groups] -> [Items] -> [Name, Turnout]
    for group in data["Groups"]:
        for item in group["Items"]:
            student_type_data[item["Name"]] = (item["Voters"], item["Turnout"])

    # sort the dictionary by the vote count, highest to lowest
    sorted_dict = sorted(student_type_data.items(), key=lambda x: x[1][0], reverse=True)

    # plot the top 10 student types
    utils.plot_count_with_turnout(dict(sorted_dict), "Top 10 Student Types by Vote Count With Turnout", "Student Type", "Vote Count")

def plot_study_level_vote_count_and_turnout():
    # update study level data in the file
    utils.get_study_level_data()

    # load the data from the file
    data = utils.load_data_from_file("data/study_level_data.json")

    # create a dictionary to store the study level name and a touple of the vote count and turnout
    study_level_data = {}

    # loop through the data and add the study level name and vote count to the dictionary
    # format of the data is: [Groups] -> [Items] -> [Name, Turnout]
    for group in data["Groups"]:
        for item in group["Items"]:
            study_level_data[item["Name"]] = (item["Voters"], item["Turnout"])

    # sort the dictionary by the vote count, highest to lowest
    sorted_dict = sorted(study_level_data.items(), key=lambda x: x[1][0], reverse=True)

    # plot the top 10 study levels
    utils.plot_count_with_turnout(dict(sorted_dict), "Top 10 Study Levels by Vote Count With Turnout", "Study Level", "Vote Count")


def plot_society_by_vote_count_with_turnout():
    # update society data in the file
    utils.get_society_data()

    # load the data from the file
    data = utils.load_data_from_file("data/society_data.json")

    # create a dictionary to store the society name and a touple of the vote count and turnout
    society_data = {}

    # loop through the data and add the society name and vote count to the dictionary
    # format of the data is: [Groups] -> [Items] -> [Name, Turnout]
    for group in data["Groups"]:
        for item in group["Items"]:
            society_data[item["Name"]] = (item["Voters"], item["Turnout"])

    # sort the dictionary by the voter count, highest to lowest
    # format of the dictionary is: {society_name: (vote_count, turnout)}
    sorted_dict = sorted(society_data.items(), key=lambda x: x[1][0], reverse=True)

    # get the top 10 societies
    top_10 = sorted_dict[:10]

    # plot the top 10 societies
    utils.plot_count_with_turnout(dict(top_10), "Top 10 Societies by Vote Count With Turnout", "Society", "Turnout")

    # plot the 11 - 20 societies
    utils.plot_count_with_turnout(dict(sorted_dict[10:20]), "11 - 20 Societies by Vote Count With Turnout", "Society", "Turnout")


def plot_society_by_turnout_with_vote_count():
    # pull new data ordered by turnout
    url = "https://www.guildofstudents.com/svc/voting/stats/election/membershipstats/107?groupIds=1&sortBy=Turnout&sortDirection=descending"

    # get the data from the url
    dw = utils.get_data(url)

    # save data to file
    utils.save_formatted_data(dw, "data/society_data_by_turnout.json")

    # load data from file
    data = utils.load_data_from_file("data/society_data_by_turnout.json")

    # create a dictionary to store the society name and a touple of the vote count and turnout
    society_data = {}

    # loop through the data and add the society name and vote count to the dictionary
    # format of the data is: [Groups] -> [Items] -> [Name, Turnout]
    for group in data["Groups"]:
        for item in group["Items"]:
            society_data[item["Name"]] = (item["Voters"], item["Turnout"])

    # sort the dictionary by turnout, highest to lowest
    # data format is [Name, (Voters, Turnout)]
    sorted_dict = sorted(society_data.items(), key=lambda x: x[1][1], reverse=True) 

    # get the top 10 societies
    top_10 = sorted_dict[:10]

    # plot the top 10 societies
    utils.plot_turnout_with_vote_count(dict(top_10), "Top 10 Societies by Vote Count With Turnout", "Society", "Vote Count")

    # plot the 11 to 20 societies
    utils.plot_turnout_with_vote_count(dict(sorted_dict[10:20]), "11 to 20 Societies by Vote Count With Turnout", "Society", "Vote Count")


plot_society_by_vote_count_with_turnout()