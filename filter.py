import csv
import os

clg = ["dtu","nsut","nsut-west","nsut-east","iiit-delhi","igdtuw"]
yr = ["2022","2023","2024"]
for cl in clg:
    for y in yr:
        l=[]
        with open(f"Data/{cl}-data/{y}/{cl}-{y}-cutoff.csv","r",newline="") as f:
            r=csv.reader(f)
            for i in r:
                if cl == "iiit-delhi":
                    z = i[2].split()
                    try:
                        i[2] = z[1][1:].rstrip(")")
                    except IndexError:
                        i[2] = "-"
                if i[4]=="Upgradation 2":
                    i[4]="U2"
                if i[4]=="Upgradation 1":
                    i[4]="U1"
                if i[2]!="-":
                    l.append(i)
        print(f"{cl} - {y} - {len(l)}")
        os.makedirs(f"filtered-data/{cl}-data/{y}", exist_ok=True)
        with open(f"filtered-data/{cl}-data/{y}/{cl}-{y}-cutoff.csv","w",newline="") as f:
            w=csv.writer(f)
            w.writerows(l)
