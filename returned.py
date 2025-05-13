from write import print_return_bill

def calculate_fine(rented_duration, returned_duration):
    fine_per_month = 5000
    months_overdue = max(0, returned_duration - rented_duration)
    total_fine = months_overdue * fine_per_month
    return total_fine

def return_land():
    return_land_id = input("Enter the ID of land you want to return: ")

    try:
        d = {}
        with open("land.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace("\n", "").replace(" ", "")
                l = line.split(",")

                k = l[0]
                value = l[1:]
                d[k] = value

        if return_land_id in d:
            if d[return_land_id][-1] == "NotAvailable":
                for i in range(len(lines)):
                    if lines[i].startswith(str(return_land_id) + ","):
                        customer_name = input("Please enter your name: ")
                        phone_number = input("Please enter your contact number: ")

                        while True:
                            try:
                                contract_duration = int(input("Please enter the duration of the contract in months: "))
                                returned_duration = int(input("Please enter the duration of the rent in months: "))
                                break
                            except ValueError:
                                print("Invalid input. Please enter a valid number for the duration.")


                        total_fine = calculate_fine(contract_duration, returned_duration)
                        details = d[return_land_id][:4] + [returned_duration, customer_name, phone_number]
                        cart = {return_land_id: details}
                        print_return_bill(cart, total_fine)

                        lines[i] = lines[i].replace("Not Available", "Available")

                        file = open("land.txt", "w")
                        file.writelines(lines)
                        file.close()

                        if(total_fine<=0):
                            print("Returned")
                        else:
                            print("Returned with Fine: "+str(total_fine))
                        return

            print("Land with such ID not rented")
        else:
            print("Invalid Land ID")

    except FileNotFoundError:
        print("File containing available lands not found.")
