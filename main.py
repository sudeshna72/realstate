from operation import available, rent_lands
from returned import return_land


def mainloop():
    while True:
        print(
            "\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│\t\t\t Welcome to Techno Property Nepal \t\t\t\t│\n"         
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                                                                       │\n"
            "│ 1. Available lands                                                                    │\n"
            "│ 2. Rent land                                                                          │\n"
            "│ 3. Return land                                                                        │\n"
            "│ 4. Exit                                                                               │\n"
            "│                                                                                       │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|"
        )
        choice = input("\nEnter your choice : ")

        #display lands
        if choice == "1":
            available()

        #rent lands
        elif choice == "2":
            rent_lands()

        #return Land
        elif choice == "3":
            return_land()

        
        #Exit the program
        elif choice == "4":

            print("\nThank you for using TechnoProperty Nepal!")
            break

        else:

            #Invalid Choice
            print("Invalid choice. Please try again.")


mainloop()
