import utils

url = "https://www.guildofstudents.com/svc/voting/stats/election/membershipstats/112?groupIds=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20&sortBy=itemname&sortDirection=ascending"

def get_election_stats_for_student_groups_election():
    data = utils.get_data(url)

    # save the data to a file
    utils.save_formatted_data(data, "data/student_groups_election.json")

    society_turnout_data = {}

    # JSON FORMAT: {"Groups" -> "All Societies" -> Items -> "Name" and "Turnout"}

    # Extract the "All Societies" data
    all_societies_data = data["Groups"][0]["Items"]

    # loop over the data and add the society name and turnout to a dictionary
    for society in all_societies_data:
        society_turnout_data[society["Name"]] = society["Turnout"]

    # sort the dictionary by the turnout percentage, highest to lowest
    sorted_dict = sorted(society_turnout_data.items(), key=lambda x: x[1], reverse=True)

    # get the top 10 societies
    top_10 = sorted_dict[:10]

    # plot the top 10 societies
    utils.plot_turnout_data(dict(top_10), "Top 10 Societies by Turnout (SGE)", "Society", "Turnout Percentage")

    all_societies_voting_numbers = {}

    # loop over the data and add the society name and voting numbers to a dictionary
    for society in all_societies_data:
        all_societies_voting_numbers[society["Name"]] = (society["Voters"], society["Turnout"])

    # sort the data to be highest to lowest by Voters numbers
    sorted_dict = sorted(all_societies_voting_numbers.items(), key=lambda x: x[1][0], reverse=True)
    
    # get the top 10 societies
    top_10 = sorted_dict[:10]

    # plot the top 10 societies
    utils.plot_count_with_turnout(dict(top_10), "Top 10 Societies by Voting Numbers (SGE)", "Society", "Voting Numbers")
    

if __name__ == '__main__':
    get_election_stats_for_student_groups_election()