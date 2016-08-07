import csv
store = []
with open("MOCK_DATA.csv", "r") as csvfile:
    read = csv.reader(csvfile, delimiter=",")
    for x in read:
        store.append(x[1])




placeholder = 0


def sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                placeholder = a[j + 1]
                a[j + 1] = a[j]
                a[j] = placeholder
    a.reverse()
    return a

print sort(store)


