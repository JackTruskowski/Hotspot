import csv
import argparse
from website.models import RestaurantNaive

MAX_COUNT = 100

with open("data/restaurants3.csv") as f:
    reader = csv.reader(f)
    count = 0
    
    for row in reader:
        if count == 0:
            count+=1
            continue
        
        if count >= MAX_COUNT:
            break
        try:
            new_entry = RestaurantNaive(
                rest_id = int(row[0]),
                name = row[1],
                address = row[2],
            )
            new_entry.save()
        except:
            print("failed to commit an entry to the db")
        count += 1
            
