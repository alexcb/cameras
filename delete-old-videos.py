#!/usr/bin/env python3
import os
import re
import datetime
import shutil
import time

max_age = datetime.timedelta(days=60)
video_dir = '/media/securitycam/videos/front-yard/'

video_re = re.compile('^front-([0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}-[0-9]{2}-[0-9]{2})\\.mkv$')
timestamp_re = re.compile('^([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2})-([0-9]{2})-([0-9]{2})$')

program_start_datetime = datetime.datetime.now()

# parses a time like "2023-11-18T06-30-00"
def parse_timestamp(s):
    return datetime.datetime.strptime(s, '%Y-%m-%dT%H-%M-%S')

# parses a date like "2023-03-11"
def parse_date(s):
    return datetime.datetime.strptime(s, '%Y-%m-%d')
    
def get_dirs_to_delete(video_dir):
    to_delete = []
    files = os.listdir(video_dir)
    for f in files:
        path = os.path.join(video_dir, f)
        if not os.path.isdir(path):
            continue
        try:
            dir_date = parse_date(f)
        except ValueError:
            continue
        dir_age = program_start_datetime - dir_date
        if dir_age > max_age:
            to_delete.append(path)
    return to_delete

dirs_to_delete = get_dirs_to_delete(video_dir)
dirs_to_delete.sort()
for path in dirs_to_delete:
    print(f'rm {path}')
    shutil.rmtree(path)

with open('/tmp/delete-old-videos', 'w') as fp:
    fp.write(f'last run at {time.time()}\n')
