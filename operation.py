from datetime import datetime
from read import available
from write import print_bill

def rent_lands():
    #displaying the available lands by invoking display_available_lands
    available()
    
    try:
        #accessing the file
        d={}
        file = open("land.txt","r")
        lines = file.readlines()
        for line in lines:
            line = (line.replace("\n", "")).replace(" ","")
            l = line.split(",")

            #appending the list elements to the dictionary
            #list's first element is the key
            k = l[0]

            #assigning values to the dictionary keys
            value = []
            for i in range(1,len(l)):
                value.append(l[i])
            d[k] = value

        #Customer Details
        customer_name = input("Please enter your name : ")
        phone_number=input("Please enter your contact number : ")
            
        #Renting the land
        land_id=input("\nPlease enter the Land ID you want to rent: ")
        print(
            "|!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│ Entered Land ID: "+ land_id +"    │ \n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!|\n")

        #Initializing flag
        land_found = False

        
        #Validating if the entered land is available or not.
        for key in d:
            if land_id==key: 

                land_found = True
                
                if d[key][-1]=="Available":
                    
                    #text based UI elements

                    print("Land Available!")

                    print(
                            "\n|!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
                             f"│  Land Details : {land_id} \t    │\n"
                              "|!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
                            f"│ Location: {d[land_id][0]}       │\n"
                            f"│ Direction: {d[land_id][1]}\t    │\n"
                            f"│ Price: {d[land_id][3]}  \t    │\n"
                            f"│ Anna: {d[land_id][2]}  \t\t    │\n"
                             "|!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n")

                    # Check anna
                    while True:
                        anna = input("Enter the number of anna you want to rent: ")
                        try:
                            int_anna = int(anna)
                            if anna == d[land_id][2]:
                                print("Valid anna quantity!")
                                break
                            else:
                                print("Invalid input. Please enter valid anna quantity.")
                        except ValueError:
                            print("Invalid input. Please enter a valid integer for the anna quantity.")

                    # Land renting duration
                    while True:
                        duration = input("Enter the duration (in months) to rent the land: ")
                        try:
                            duration_int = int(duration)
                            if duration_int > 0:
                                print("Entered duration is valid")
                                break
                            else:
                                print("Invalid input. Please enter a positive integer for the duration.")
                        except ValueError:
                            print("Invalid input. Please enter a valid integer for the duration.")

                    #To update the land.txt file
                    for i in range(len(lines)):
                        if lines[i].startswith(str(land_id) + ","):
                            lines[i] = lines[i].replace("Available", "Not Available")
                            break
                    else:
                        print("Land ID not found.")
                        return

                    file = open("land.txt", "w")
                    file.writelines(lines)
                    #list to store details of purchased land
                    details=[]

                    #dictionary to store land ID's of lands rented.
                    cart={}

                    for i in range(0,4):
                        details.append(d[land_id][i])
                    details.append(duration)
                    details.append(customer_name)
                    details.append(phone_number)
                    
                    cart[land_id]=details
                     #updating dictionary

                    #printing the bill by invoking print_bill function
                    print_bill(cart) 

                #else block for invalid land ID requests    
                else:
                    print("\nLand not available")
                    break

        if not land_found:
            print("\nInvalid land ID")
    #exception handler incase file is not found
    except FileNotFoundError:
        print("File containing available lands not found.")
