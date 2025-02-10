import csv
from itertools import islice
infile = 'raw-data/worldcities.csv'
outfile = 'files/cities-500.csv'

with open(infile) as ip, open(outfile,"w") as out:
    reader = csv.reader(ip)
    out.write("City, First letter, Last letter\n")

    for line in islice(ip,1, 501):
        line = tuple(line.strip().split(","))
        name = line[1][1:-1]
        first = name[0].lower()
        last = name[-1].lower()
        entry = name+', '+first+', '+last+'\n'
        out.write(entry)


with open(outfile) as ip:
    reader = csv.reader(ip)
    header = next(reader)
    rows = sorted(reader, key=lambda row: row[0].lower()) 
    
with open(outfile, "w", newline="", encoding="utf-8") as out:
    writer = csv.writer(out)
    writer.writerow(header)
    writer.writerows(rows)