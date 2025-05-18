import selector
import inserter
import history

def get_hymn_list():
    num_hymns = int(input("How many hymns do you need? (2-4) "))

    opening = selector.get_opening_hymn()
    sacrament = selector.get_sacrament_hymn()
    intermediate = selector.get_intermediate_hymn()
    closing = selector.get_closing_hymn() 

    if num_hymns < 4:
        intermediate = None
    
    if num_hymns < 3:
        closing = None

    hymns = [opening, sacrament, intermediate, closing]

    # TODO: =============================================!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    inserter.insert_hymns(opening[0], sacrament[0], 
                          intermediate[0] if intermediate else None, 
                          closing[0] if closing else None) 
    
    for hymn in hymns:
        if hymn is not None:
            print(f"{hymn[0]} {hymn[1]}")


def get_hymn_history():
    number_shown = 5
    results = history.get_history(number_shown)

    print("Previous hymns:")
    print("Date", "Opening", "Sacrament", "Intermediate", "Closing")
    for row in results:
        for column in row:
            print(column, end=" ")
        print()

    # See more hymns
    q = input("Do you want to see more? (y/n) ")
    while q != "n":
        number_shown += 5
        results = history.get_history(number_shown)
        print("Previous hymns:")
        print("Date", "Opening", "Sacrament", "Intermediate", "Closing")
        for row in results:
            for column in row:
                print(column, end=" ")
            print()
        q = input("Do you want to see more? (y/n) ")

    # TODO: Yet to be tested 
    # Make changes if necessary
    g = input("Do you want to make changes? (y/n) ")
    if g == "y":
        date = input("Enter the date of the hymn you want to change: ")
        position = input("Enter the position (opening, sacrament, intermediate, closing): ")
        hymn_number = int(input("Enter the correct hymn number: "))

        history.make_changes(date, position, hymn_number)
        
# =========================== Main Function =================================== # 

def main():
    print("Welcome")
    print("Type 1 to select hymns")
    user_input = int(input("Type 2 to see previous hymns: "))
    print()
    
    if user_input == 1:
        get_hymn_list()

    elif user_input == 2:
        get_hymn_history()

    print("\nGoodbye :)")
    
if __name__ == "__main__":
    main()   