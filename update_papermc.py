#!/usr/bin/env python3

import requests
import json
from os.path import realpath
import pathlib
from tqdm import tqdm
import sys

API_ENDPOINT = "https://papermc.io/api/v1/paper/"
WORKING_DIR = pathlib.Path(realpath(__file__)).parent
SERVER_INFO_PATH = WORKING_DIR / "papermc_info.json"
# defaults if not set otherwise just keep existing values from 'SERVER_INFO_PATH' file
SERVER_NAME = "PaperMC"
SERVER_JAR_PATH = WORKING_DIR / "server.jar"

def download_file(url, filepath):
    chunk_size = 1024  # 1 MB
    with requests.get(url, stream=True) as r:
        file_size = int(r.headers.get('content-length'))
        num_bars = file_size // chunk_size
        with open(filepath, 'wb') as f:
            for chunk in tqdm(r.iter_content(chunk_size=chunk_size),
                              total=num_bars,
                              unit='KB',
                              desc=str(filepath),
                              leave=True,
                              file=sys.stdout):
                f.write(chunk)

def papermc_update(server_info, version, build):
    # 'server_info' can be an empty dict
    download_endpoint = API_ENDPOINT + version + '/' + str(build) + '/download'
    print("Downloading from '{}'...".format(download_endpoint))
    download_file(download_endpoint, SERVER_JAR_PATH)
    print("Done '{}'".format(SERVER_JAR_PATH))
    if 'name' not in server_info:
        server_info['name'] = SERVER_NAME
    if 'path' not in server_info:
        server_info['path'] = str(SERVER_JAR_PATH)
    server_info['version'] = version
    server_info['build'] = build
    with open(SERVER_INFO_PATH, 'w') as f:
        f.write(json.dumps(server_info))
    print("Finished update.")


def papermc_check(version):
    # assume ordered latest to earliest
    r = requests.get(API_ENDPOINT)
    r = json.loads(r.text)
    if version in r['versions']:
        print("Using version '{}'".format(version))
        r = requests.get(API_ENDPOINT + version)
        r = json.loads(r.text)
        latest_build = int(r['builds']['latest'])
        if SERVER_INFO_PATH.is_file() and SERVER_INFO_PATH.stat().st_size != 0:
            try:
                with open(SERVER_INFO_PATH, 'r') as f:
                    server_info = json.loads(f.read())
            except json.JSONDecodeError as e:
                print("Could not decode json from '{}'".format(str(SERVER_INFO_PATH)))
                return
            if version != server_info['version']:
                print("Version change from '{}' to '{}'. Please update manually.".format(server_info['version'], version))
                return
            if latest_build > server_info['build']:
                print("Update required '{}-{}' -> '{}-{}'".format(
                    server_info['version'],
                    str(server_info['build']),
                    version,
                    str(latest_build)))
                papermc_update(server_info, version, latest_build)
            else:
                print("No action. Current: '{}-{}', Latest: '{}-{}'".format(
                    server_info['version'],
                    str(server_info['build']),
                    version,
                    str(latest_build)))
        else:
            print("'{}' does not exist.".format(SERVER_INFO_PATH))
            papermc_update(dict(), version, latest_build)
    else:
        print("Version '{}' not found. Options are:".format(version))
        print(r['versions'])

papermc_check("1.16.2")
