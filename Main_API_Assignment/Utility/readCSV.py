import csv

def read_test_data_from_csv():
    test_data = []
    with open("/Users/vbalasubramaniyam/Documents/GitHub/HuTraining/Main_API_Assignment/Utility/readData.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        next(data)  # skip header row
        for row in data:
            test_data.append(row)
    return test_data