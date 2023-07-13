# using utils provided, get the turnout data for the departments and societies and plot it

import utils


def plot_society_turnout():
    # update the data in the file
    utils.get_society_data()

    # load the data from the file
    data = utils.load_data_from_file("data/society_data.json")

    # initialise data dictionary for society name and turnout percentage
    data_dict = {}

    # format of the data is: [Groups] -> [Items] -> [Name, Turnout]
    for group in data["Groups"]:
        for society in group["Items"]:
            # add the society name and turnout to a dictionary
            data_dict[society["Name"]] = society["Turnout"]

    # sort the dictionary by the turnout percentage, highest to lowest
    sorted_dict = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)

    # get the top 10 societies
    top_10 = sorted_dict[2:12]

    # plot the top 10 societies
    utils.plot_turnout_data(dict(top_10), "Top 10 Societies by Turnout", "Society", "Turnout Percentage")


def plot_department_turnout():
    # update the data in the file
    utils.get_department_data()

    # load the data from the file
    data = utils.load_data_from_file("data/department_data.json")

    # initialise data dictionary for department name and turnout percentage
    data_dict = {}

    # format of the data is: [Groups] -> [Items] -> [Name, Turnout]
    for group in data["Groups"]:
        for department in group["Items"]:
            # add the department name and turnout to a dictionary
            data_dict[department["Name"]] = department["Turnout"]

    # sort the dictionary by the turnout percentage, highest to lowest
    sorted_dict = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)

    # get the top 10 departments
    top_10 = sorted_dict[1:11]

    # plot the top 10 departments
    utils.plot_turnout_data(dict(top_10), "Top 10 Departments by Turnout", "Department", "Turnout Percentage")
