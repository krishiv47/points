while True:
    import os
    import csv

    f = open("points.csv", "r", newline='')
    f2 = open("points1.csv", "a", newline='')
    r = csv.reader(f)
    w2 = csv.writer(f2)
    roll = input("enter last four digit for roll no.:")
    for i in r:
        if str(i[0])[-4:] == roll:
            a = int(i[1])
            a = a + 1
            i[1] = str(a)
            w2.writerow(i)
        else:
            w2.writerow(i)
    f.close()
    f2.close()
    if os.path.isfile("points.csv"):
        os.remove("points.csv")
    if os.path.isfile("points1.csv"):
        os.rename("points1.csv",
                  "points.csv")
