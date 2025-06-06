from datetime import datetime

def print_bill(details):

    #printing the invoice in command line 
    for key in details:
        print(

            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                         Invoice                                           │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                                                                           │\n"
            "│ Invoice NO :  999                                  Date/time : "+str(datetime.now())+" │\n"
            "│                                                                                           │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│ Customer Name : "+ details[key][5] +"                                                                    │\n"
            "│ Contact number : "+ details[key][6] +"                                                                 │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                                                                           │\n"
            "│ Land ID\t Location\t Direction \tQty \t Price \t      Duration             │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│ "+key+"\t\t"+details[key][0]+"\t"+details[key][1]+"\t\t"+details[key][2]+"\t"+details[key][3]+"\t\t"+details[key][4]+" \t\t      │\n"
            "│                                                                                           │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            
        )
    #thank you message
    print("Thank you for using our services")

    #generating the invoice in a text file

    #generating a file name
    file_name = str(details[key][5]) + "_" + str(details[key][6]) + "_" + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".txt"

    #accessing the file with encoding Unicode character encoding utf-8
    invoice_file = open(file_name, "w", encoding="utf-8")

    #writing to the file
    invoice_file.write(
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                Techno Property Nepal                                          │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                         Invoice                                               │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                                                                            │\n"
            "│ Invoice NO :  999                                  Date/time : "+str(datetime.now())+"  │\n"
            "│                                                                                            │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│ Customer Name : "+ details[key][5] +"                                                            │\n"
            "│ Contact number : "+ details[key][6] +"                                                          │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                                                                            │\n"
            "│ Land ID\t Location\t Direction \tQty \t Price \t Duration                                 │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│"+key+"\t\t"+details[key][0]+"\t"+details[key][1]+"\t"+details[key][2]+"\t"+details[key][3]+"\t"+details[key][4]+"│\n"
            "│                                                                                              │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "└───────────────────────────────────────────────────────────────────────────────────────────┘\n")

def print_return_bill(details,total_fine):
    for key in details:
        print(
            "<!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                Techno Property Nepal                                       │\n"
            "<!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                      Return Invoice                                        │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                                                                            │\n"
            "│ Invoice NO :  999                                  Date/time : " + str(datetime.now()) + "  │\n"
            "│                                                                                            │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│ Customer Name : " + str(details[key][5]) + "                                                      │\n"
            "│ Contact number : " + str(details[key][6]) + "                                                     │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                                                                            │\n"
            "│ Land ID\t Location\t Direction \tQty \t Price \t Duration                                 │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│" + str(key) + "\t\t" + str(details[key][0]) + "\t" + str(details[key][1]) + "\t" + str(details[key][2]) + "\t" + str(details[key][3]) + "\t" + str(details[key][4]) + "│\n"
            "│ Fine: Nrs " + str(total_fine) + "                                                        │\n"
            "│                                                                                            │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "└───────────────────────────────────────────────────────────────────────────────────────────┘\n"
        )
    print("Thank you for using our services")

    file_name = "Return_" + str(details[key][5]) + "_" + str(details[key][6]) + "_" + datetime.now().strftime(
        '%Y-%m-%d_%H-%M-%S') + ".txt"

    invoice_file = open(file_name, "w", encoding="utf-8")

    invoice_file.write(
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                Techno Property Nepal                                       │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                      Return Invoice                                        │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                                                                            │\n"
            "│ Invoice NO :  999                                  Date/time : " + str(datetime.now()) + "  │\n"
            "│                                                                                            │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│ Customer Name : " + str(details[key][5]) + "                                                      │\n"
            "│ Contact number : " + str(details[key][6]) + "                                                     │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│                                                                                            │\n"
            "│ Land ID\t Location\t Direction \tQty \t Price \t Duration                                 │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "│" + str(key) + "\t\t" + str(details[key][0]) + "\t" + str(details[key][1]) + "\t" + str(details[key][2]) + "\t" + str(details[key][3]) + "\t" + str(details[key][4]) + "│\n"
            "│ Fine: Nrs " + str(total_fine) + "                                                        │\n"
            "│                                                                                            │\n"
            "|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|\n"
            "└───────────────────────────────────────────────────────────────────────────────────────────┘\n"
        )
    invoice_file.close()