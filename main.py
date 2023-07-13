
import vote_count
import turnout
import utils
import vote_count_and_turnout
import general

if __name__ == '__main__':
    # fetch all the most recent data
    print("[INFO] Fetching most recent data...")
    utils.get_all_data()
    print("[INFO] Done fetching data")

    # ask the user if they want society or department data
    data_type = input("Do you want to get society (1), department data (2) or accommodation data(3)? ")

    # ask the user what type of data they want
    data = input("Do you want to get vote count (1) or turnout data (2)? ")

    if data_type == "0":
        if data == "0":
            # save everything to png
            print("[INFO] Plotting society vote count data...")
            vote_count.plot_society_vote_count()
            print("[INFO] Plotting society turnout data...")
            turnout.plot_society_turnout()
            print("[INFO] Plotting departmewnt vote count data...")
            vote_count.plot_department_vote_count()
            print("[INFO] Plotting department turnout data...")
            turnout.plot_department_turnout()
            print("[INFO] Plotting department vote count and turnout data...")
            vote_count_and_turnout.plot_department_vote_count_and_turnout()
            print("[INFO] Plotting society vote count and turnout data...")
            vote_count_and_turnout.plot_society_vote_count_and_turnout()
            print("[INFO] Plotting accommodation vote count and turnout data...")
            vote_count_and_turnout.plot_accommodation_vote_count_and_turnout()
            print("[INFO] Plotting student type vote count and turnout data...")
            vote_count_and_turnout.plot_student_type_vote_count_and_turnout()
            print("[INFO] Plotting study level vote count and turnout data...")
            vote_count_and_turnout.plot_study_level_vote_count_and_turnout()
            print("[INFO] Plotting society vote count by turnout data...")
            vote_count_and_turnout.plot_society_by_turnout_with_vote_count()   
            print("[INFO] Plotting society turnout by vote count data...")         
            vote_count_and_turnout.plot_society_by_vote_count_with_turnout()
        else:
            print("Invalid data type")
    elif data_type == "1":
        if data == "1":
            vote_count.plot_society_vote_count()
        elif data == "2":
            turnout.plot_society_turnout()
        elif data == "3":
            vote_count_and_turnout.plot_society_vote_count_and_turnout()
        else:
            print("Invalid data type")
    elif data_type == "2":
        if data == "1":
            vote_count.plot_department_vote_count()
        elif data == "2":
            turnout.plot_department_turnout()
        elif data == "3":
            vote_count_and_turnout.plot_department_vote_count_and_turnout()
        else:
            print("Invalid data type")
    elif data_type == "3":
        if data == "1":
            print("Not implemented yet")
            # vote_count.plot_accommodation_vote_count() # TODO
        elif data == "2":
            print("Not implemented yet")
            # turnout.plot_accommodation_turnout() # TODO
        elif data == "3":
            vote_count_and_turnout.plot_accommodation_vote_count_and_turnout()
        else:
            print("Invalid data type")
    elif data_type == "999":
        if data == "999":
            utils.get_all_data_in_one_file()
    elif data_type == "77":
        if data == "77":
            general.plot_pie_of_votes_out_of_eligible()
    else:
        print("Invalid data type")
