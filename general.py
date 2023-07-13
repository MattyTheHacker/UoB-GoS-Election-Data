import utils

# plot a pie chart of the number of votes cast out of the number of eligible voters
def plot_pie_of_votes_out_of_eligible():
    labels = "Didn't vote", "Voted"

    # update general data in the file
    utils.get_all_data_in_one_file()

    # load the data from the file
    data = utils.load_data_from_file("data/all_data.json")

    # get the number of eligible voters
    # the json format is "Voters"
    total_possible_voters = int(data["Eligible"]) 

    # get the number of votes cast
    # the json format is: "Eligible"
    actual_number_of_voters = int(data["Voters"])

    non_voters = total_possible_voters - actual_number_of_voters

    # plot the pie chart
    utils.plot_pie_chart([non_voters, actual_number_of_voters], "Number of votes cast out of the number of eligible voters", labels)

