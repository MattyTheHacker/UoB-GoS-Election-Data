import vote_count
import turnout

if __name__ == '__main__':
    # ask the user if they want society or department data
    data_type = input("Do you want to get society (1) or department data (2)? ")

    # ask the user what type of data they want
    data = input("Do you want to get vote count (1) or turnout data (2)? ")

    if data_type == "1":
        if data == "1":
            vote_count.plot_society_vote_count()
        elif data == "2":
            turnout.plot_society_turnout()
        else:
            print("Invalid data type")
    elif data_type == "2":
        if data == "1":
            vote_count.plot_department_vote_count()
        elif data == "2":
            turnout.plot_department_turnout()
        else:
            print("Invalid data type")
    elif data_type == "3":
        # plot the vote count for departments combined with their turnout
        
