import utils

# plot the vote count for departments combined with their turnout in brackets
def plot_department_vote_count_and_turnout():
    # update department data in the file 
    utils.get_department_data()

    # load the data from the file
    data = utils.load_data_from_file("department_data.json")

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
    data = utils.load_data_from_file("society_data.json")

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

