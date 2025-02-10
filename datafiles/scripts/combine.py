import csv

in1 = "files/cities-500.csv"
in2 = "files/countries.csv"
out = "files/combined.csv"

all = []

with open(in1) as ip1, open(in2) as ip2, open(out,"w") as op:
    rd1 = csv.reader(ip1)
    rd2 = csv.reader(ip2)
    wr = csv.writer(op)

    hd = next(rd1)
    hd = next(rd2)

    all.extend(rd1)
    all.extend(rd2)
    all = sorted(all, key = lambda row: row[0].lower())

    wr.writerow(["Country", "Code", "Population"])  
    wr.writerows(all)