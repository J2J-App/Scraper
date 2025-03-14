import csv
import os


clg = ["dtu","nsut","nsut-west","nsut-east","iiit-delhi","igdtuw"]
yr = ["2022","2023","2024"]

c=0
for cl in clg:
    for y in yr:
        l=[]
        with open(f"Data/{cl}-data/{y}/{cl}-{y}-cutoff.csv","r",newline="") as f:
            r=csv.reader(f)
            for i in r:
                if cl == "iiit-delhi":
                    z = i[2].split()
                    if i[4]=="U1" or i[4]=="U2":
                        continue
                    try:
                        i[2] = z[1][1:].rstrip(")")
                    except IndexError:
                        i[2] = "-"
                else:
                    i[2] = i[2].split()[0]
                if i[1] == "SingleGirlChild":
                    continue
                if i[1] == "SpotRound-2" or i[1] == "SpotRound-1":
                    continue
                if cl == "nsut" or cl == "nsut-west" or cl == "nsut-east":
                    i[1] =i[1].replace("GirlCandidate","-SGC")
                if i[4] == "Upgradation 2":
                    i[4] = "U2"
                if i[4] == "Upgradation 1":
                    i[4] = "U1"
                if i[2] != "-":
                    l.append(i)
                #record number 1106 of NSUT 2022 has to be updated manually to remove the rogue "(Priority"
                if cl == "nsut" and y == "2022":
                    i[2]=i[2].replace("(Priority","")
        print(f"{cl} - {y} - {len(l)}")
        c+=len(l)
        os.makedirs(f"filtered-data/{cl}-data/{y}", exist_ok=True)
        with open(f"filtered-data/{cl}-data/{y}/{cl}-{y}-cutoff.csv","w",newline="") as f:
            w=csv.writer(f)
            w.writerows(l)
print(f"Total records: {c}")