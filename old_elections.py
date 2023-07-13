import os
import utils

current_election_id = 168
lowest_possible_value = 1

historical_ids = list(range(lowest_possible_value, current_election_id))

def get_all_historic_data():
    print("[INFO] Fetching all historic data...")
    for id in historical_ids:
        print("[INFO] Fetching data for election " + str(id) + "...")
        utils.get_all_specific_election_data(id)
    print("[INFO] Fetching all historic data... done!")

def plot_turnout_of_all_historic_elections():
    # extract the total turnout for each election and add it to the list
    # each item in the list should be a touple of election name and turnout
    turnout_list = []
    file_list = utils.list_json_files("historic_data")

    # sort the list by the election ID
    # format: election_ID_name.json
    file_list.sort(key=lambda x: int(x.split("_")[1]))

    # use data already saved in the files
    for file in file_list:
        data = utils.load_data_from_file("historic_data" + os.sep + file)

        # check the turnout isn't 0
        if (data["Turnout"] != 0):
            turnout_list.append((data["Title"], data["Turnout"]))
    
    utils.plot_historic_election_turnout(turnout_list)


if __name__ == "__main__":
    get_all_historic_data()
    plot_turnout_of_all_historic_elections()



