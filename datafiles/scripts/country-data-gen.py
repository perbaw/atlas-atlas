import csv
from itertools import islice

infile = 'raw-data/worldcountries.csv'
outfile = 'files/countries.csv'

with open(infile, encoding="latin1") as ip, open(outfile,"w") as out:
    reader = csv.reader(ip)
    out.write("Country, First letter, Last letter\n")

    for line in islice(ip, 1, 195):
        line = tuple(line.strip().split(","))
        name = line[1]
        first = name[0].lower()
        last = name[-1].lower()
        entry = f"{name}, {first}, {last}\n"
        out.write(entry)
