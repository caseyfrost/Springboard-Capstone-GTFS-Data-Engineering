import urllib.request
import json
import time
import os
from google.transit import gtfs_realtime_pb2
from protobuf_to_dict import protobuf_to_dict


def crt_outfile(out_dir):
    """Creates output path for file with filename unique to every second"""

    date = time.strftime('%Y_%m_%d-%H_%M_%S_%p')
    filename = f'BART_{date}.json'
    out_file_path = os.path.join(out_dir, filename)
    return out_file_path


def crt_trip_update_json(url):
    gtfs_feed = gtfs_realtime_pb2.FeedMessage()
    gtfs_feed.ParseFromString(urllib.request.urlopen(url).read())
    gtfs_dict = protobuf_to_dict(gtfs_feed)
    return json.dumps(gtfs_dict, indent=4, sort_keys=True)


def write_json(path, js):
    with open(path, 'w') as outfile:
        outfile.write(js)


if __name__ == '__main__':
    trip_update_dir = r'/Users/caseyfrost/Desktop/Springboard/GTFS_Capstone_Project/json_files/bart/trip_update'
    bart_trip_updt_url = r'http://api.bart.gov/gtfsrt/tripupdate.aspx'
    out_file = crt_outfile(trip_update_dir)
    json_obj = crt_trip_update_json(bart_trip_updt_url)
    write_json(out_file, json_obj)
