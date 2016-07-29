import csv
with open ("MOCK_DATA.csv", "r") as csvfile:
    idnumber = raw_input("Please ente your ID: ")
    read_data = csv.reader(csvfile, delimiter=',')
    for row in read_data:
        if idnumber == row[0]:
            print row[1] + ' '+ row[2] + ' '+ row[3]
            break
        else:
            pass




