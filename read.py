def available():
    try:
        d={}
        #the data stored in the file must be given to function the program
        file = open("land.txt","r")
        
        #text based UI element
        print(
            "\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│\t\t\t\t Available Lands \t\t\t\t\t    │\n"         
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│ Land ID\t\tLocation\tDirection\t\tAnna\t\tPrice\t    │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|")

        #accessing the file contents
        lines = file.readlines()
        for line in lines:
            line = (line.replace("\n", "")).replace(" ","")
            l = line.split(",")
            
            #appending the list elements to the dictionary
            #list's first element is the key
            k = l[0]

            #assgning values to the dictionary keys
            value = []
            for i in range(1,len(l)):
                value.append(l[i])
            d[k] = value
            
        #flag
        available = False
        
        #iterating through the dictionary to display available lands
        for key in d:
            if d[key][-1]=="Available":
                land_id = key
                location = d[key][0]
                direction = d[key][1]
                anna = d[key][2]
                price = d[key][3]
                        
                print("│  {:<20}{:<20}{:<20}{:<20}{:<9}│".format(land_id, location, direction, anna, price))
                available = True
                
        # if no land is available, print message
        if not available:
            print("│  No available lands\t\t\t\t\t\t\t\t\t    │")

        #text based UI element
        print("|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|")

        #file close
        file.close()

    #exception handler incase file is not found
    except FileNotFoundError:
        print("File containing available lands not found.")
