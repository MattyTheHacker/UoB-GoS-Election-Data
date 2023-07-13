import utils
import csv

# the website seems to think this is something to do with RON? no idea

url = "https://www.guildofstudents.com/svc/voting/stats/election/membershipstats/110?groupIds=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20&sortBy=itemname&sortDirection=ascending"
url2 = "https://www.guildofstudents.com/svc/voting/stats/election/membershipstats/107?groupIds=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20&sortBy=itemname&sortDirection=ascending"

data = utils.get_data(url)

all_groups = []

# json format: [Groups] -> [Name], [Items] 

# iterate over the data and separate out into lists based on [Items]
for group in data["Groups"]:
    # open a csv file for each group
    rows = []
    with open("data/test/" + group["Name"] + ".csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        
        # write the name of the group to the file
        group_name = group["Name"]
        headers = [group_name, 'Members']
        writer.writerow(headers)
        
        # iterate over the items in the group
        for item in group["Items"]:
            row = [item["Name"], item["Eligible"]]
            rows.append(row)

            # add the group to the list of groups with it's category
            if group["Name"] != "All Societies":
                all_groups.append([item["Name"], group["Name"], item["Eligible"]])
    
        # sort rows by number of members
        rows.sort(key=lambda x: x[1], reverse=True)

        # write the rows to the file
        writer.writerows(rows)

# sort by number of members
all_groups.sort(key=lambda x: x[2], reverse=True)

# write the groups to a file
with open("data/test/all_groups.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    headers = ["Name", "Category", "Members"]
    writer.writerow(headers)
    writer.writerows(all_groups)

utils.save_formatted_data(data, "data/test/test.json")