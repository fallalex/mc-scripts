#!/usr/bin/env python3


import requests
import json
import pathlib
import sys
from os.path import realpath

def check_essentials(response, p):
    print("Latest 'EssentialsX' Version -", response['tag_name'])
    if (p / "version.txt").exists():
        with open(p / "version.txt", 'r') as f:
            cur_version = f.read().strip()
    else:
        print("No previous version known")
        update_essentials(response, p)
        return
    if cur_version == response['tag_name']:
        print("up-to-date")
    else:
        print("Updating 'EssentialsX' Version -", cur_version)
        update_essentials(response, p)

def update_essentials(response, p ):
    exclude = ["EssentialsXXMPP", "EssentialsXGeoIP", "EssentialsXProtect", "EssentialsXAntiBuild", ]
    asset_urls = [a['browser_download_url'] for a in response['assets']]
    for url in asset_urls:
        filename = url.split('/')[-1].split('-')[0]
        if filename not in exclude:
            print("Download '" + filename + "'")
            r = requests.get(url)
            with open(p / (filename + ".jar"), 'wb') as f:
                f.write(r.content)
            print("  Done   '" + filename + "'")
    with open(p / "version.txt", 'w') as f:
        f.write(response['tag_name'])

plugins_dir = pathlib.Path(realpath(__file__)).parent / pathlib.Path("plugins/")
plugins_dir.mkdir(parents=True, exist_ok=True)

# EssentialsX
p = plugins_dir / pathlib.Path("EssentialsX/")
p.mkdir(parents=True, exist_ok=True)
response = requests.get('https://api.github.com/repos/EssentialsX/Essentials/releases/latest')
response = json.loads(response.text)
check_essentials(response, p)

