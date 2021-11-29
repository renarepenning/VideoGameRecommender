# CITATION https://blr.design/blog/python-multiple-json-to-csv/

#!/usr/bin/env python3

# Place this Python script in your working directory when you have JSON files in a subdirectory.
# To run the script via command line: "python3 json-to-csv-exporter.py"

import json
import glob
from datetime import datetime
import csv

# Place your JSON data in a directory named 'data/'
src = '/Users/renarepenning/Desktop'

date = datetime.now()
data = []

# Change the glob if you want to only look through files with specific names
files = glob.glob(src+'/IGDB_Data/*', recursive=True)

print('\n# files read', len(files))
# Loop through files

for single_file in files:
    with open(single_file, 'r') as f:

        # for a in single_file.splitlines:
        #     print(a)
        # Use 'try-except' to skip files that may be missing data
        try:

            json_file = json.loads(f)  # [0]
            # print(type(json_file))

            data.append([
                json_file['id'],
                json_file['category'],

                # json_file['requestedUrl'],
                # json_file['fetchTime'],
                # json_file['categories']['performance']['score'],
                # json_file['audits']['largest-contentful-paint']['numericValue'],
                # json_file['audits']['speed-index']['numericValue'],
                # json_file['audits']['max-potential-fid']['numericValue'],
                # json_file['audits']['cumulative-layout-shift']['numericValue'],
                # json_file['audits']['first-cpu-idle']['numericValue'],
                # json_file['audits']['total-byte-weight']['numericValue']
            ])
        except KeyError:
            print(f'Skipping {single_file}')

# Sort the data
data.sort()

# Add headers
data.insert(0, ['id', 'category'])
# ['id', 'category', 'created_at', 'external_games',
# 'first_release_date', 'genres', 'name', 'platforms', 'release_dates', 'similar_games', 'slug', 'summary', 'tags', 'updated_at', 'url', 'checksum'])

# Export to CSV.
# Add the date to the file name to avoid overwriting it each time.
csv_filename = f'{str(date)}.csv'
with open(csv_filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Updated CSV")
