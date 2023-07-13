import utils
import csv

fields = ['Department', 'Students']

def get_top_departments_by_number_of_students(x = None):
    print("Department data was last updated: " + utils.check_last_updated("data/department_data.json"))
    update = input("Would you like to update the data? (y/n): ")

    if update == "y":
        utils.get_department_data()

    data = utils.load_data_from_file("data/department_data.json")

    # format of the data is: [Groups] -> [Items] -> [Name, Eligible]

    # create a list of tuples containing the department name and the number of students
    department_list = []
    for department in data["Groups"][0]["Items"]:
        department_list.append((department["Name"], department["Eligible"]))

    # sort the list by the number of students
    department_list.sort(key=lambda x: x[1], reverse=True)

    # if x is specified, return the top x departments
    if x is not None:
        return department_list[:x]
    
    # otherwise return all departments
    else:
        return department_list
    

def get_total_number_of_students():
    print("Department data was last updated: " + utils.check_last_updated("data/department_data.json"))
    update = input("Would you like to update the data? (y/n): ")

    if update == "y":
        utils.get_department_data()

    data = utils.load_data_from_file("data/department_data.json")

    # format of the data is: [Groups] -> [Items] -> [Name, Eligible]
    # iterate over and sum all of of the [Eligible] values
    total = 0
    for department in data["Groups"][0]["Items"]:
        total += department["Eligible"]
    
    return total


if __name__ == '__main__':
    # get all departments by number of students
    department_list = get_top_departments_by_number_of_students()

    # write it to a csv file
    with open('csv/all_departments_by_number_of_students.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(fields)
        writer.writerows(department_list)
    
    # get the top 10 departments by number of students
    top_10_department_list = get_top_departments_by_number_of_students(10)

    # write to a csv file
    with open('csv/top_10_departments_by_number_of_students.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(fields)
        writer.writerows(top_10_department_list)

    # get the total number of students
    total = get_total_number_of_students()
    print("[INFO] Total number of students: " + str(total))







