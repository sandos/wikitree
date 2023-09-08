from urllib import request
import csv
import io

profiles = []

PAGE_SIZE = 50000

def get_all_query(query):
    page = 0
    global profiles
    while True:
        response = request.urlopen(f"https://plus.wikitree.com/function/WTWebProfileSearch/Profiles.csv?Query={query}&MaxProfiles=1700000&Format=CSV&PageSize={PAGE_SIZE}&pageIdx={page}")
        csv_bytes = response.read()

        csv_string = csv_bytes.decode("utf-8")
        # print(csv_string)

        csv_file = io.StringIO(csv_string)

        reader = csv.reader(csv_file, delimiter=';')

        _ = next(reader)
        # print(first_row)

        cur_list = list(reader)

        profiles += cur_list

        page += 1

        print(f"Got {len(cur_list)} items, {len(profiles)} total")
        if len(cur_list) < PAGE_SIZE:
            print("Got non-full page, aborting")

            break


#get_all_query("Sweden")
get_all_query("Sverige")

user_ids = set()

for x in profiles:
    user_ids.add(x[0])

print(len(user_ids))
