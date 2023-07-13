import utils
import csv

fields = ['Name', 'Members']

# functions to pull the most recent society data from the website and sort it in a variety of ways

# function to get the top x societies by number of members
# if no x is specified, it will return all societies
# ask if the user would like to update the data in the file
def get_top_societies_by_member_count(x = None):
    print("Society data was last updated: " + utils.check_last_updated("data/student_groups_election.json"))
    update = input("Would you like to update the data? (y/n): ")
    if update == "y":
        utils.get_society_data()
    
    data = utils.load_data_from_file("data/student_groups_election.json")
    # format of the data is: [Groups] -> [Items] -> [Name, Eligible]

    # create a list of tuples containing the society name and the number of members
    society_list = []
    for society in data["Groups"][0]["Items"]:
        society_list.append((society["Name"], society["Eligible"]))

    # sort the list by the number of members
    society_list.sort(key=lambda x: x[1], reverse=True)

    # if x is specified, return the top x societies
    if x is not None:
        return society_list[:x]
    # otherwise return all societies
    else:
        return society_list

if __name__ == '__main__':
    # get all societies by member count
    society_list = get_top_societies_by_member_count()

    # write it to a csv file
    with open('csv/all_societies_by_member_count.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(fields)
        writer.writerows(society_list)

        print("Successfully wrote all societies by member count to csv file.")
    
    # get the top 10 societies by member count
    top_10_society_list = get_top_societies_by_member_count(10)

    # write to a csv file
    with open('csv/top_10_societies_by_member_count.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(fields)
        writer.writerows(top_10_society_list)

        print("Successfully wrote top 10 societies by member count to csv file.")








