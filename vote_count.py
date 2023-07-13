# using utils provided, get the total vote counts for the top 10 departments and societies and plot it

import utils


def plot_society_vote_count():
    # update the data in the file
    utils.get_society_data()

    # load the data from the file
    data = utils.load_data_from_file("data/society_data.json")

    # initialise data dictionary for society name and vote count
    data_dict = {}

    # format of the data is: [Groups] -> [Items] -> [Name, Voters]
    for group in data["Groups"]:
        for society in group["Items"]:
            # add the society name and vote count to a dictionary
            data_dict[society["Name"]] = society["Voters"]

    # sort the dictionary by the vote count, highest to lowest
    sorted_dict = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)

    # get the top 10 societies
    top_10 = sorted_dict[:10]

    # plot the top 10 societies
    utils.plot_data(dict(top_10), "Top 10 Societies by Vote Count", "Society", "Vote Count")


def plot_department_vote_count():
    # update the data in the file
    utils.get_department_data()

    # load the data from the file
    data = utils.load_data_from_file("data/department_data.json")

    # initialise data dictionary for department name and vote count
    data_dict = {}

    # format of the data is: [Groups] -> [Items] -> [Name, Voters]
    for group in data["Groups"]:
        for department in group["Items"]:
            # add the department name and vote count to a dictionary
            data_dict[department["Name"]] = department["Voters"]

    # sort the dictionary by the vote count, highest to lowest
    sorted_dict = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)

    # get the top 10 departments
    top_10 = sorted_dict[:10]

    # plot the top 10 departments
    utils.plot_data(dict(top_10), "Top 10 Departments by Vote Count", "Department", "Vote Count")

