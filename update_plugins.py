#!/usr/bin/env python3


import requests
import json
import pathlib
from os.path import realpath
#import cloudscraper

plugins_dir = pathlib.Path(realpath(__file__)).parent / pathlib.Path("plugins/")
plugins_dir.mkdir(parents=True, exist_ok=True)

# EssentialsX
exclude = ["EssentialsXXMPP", "EssentialsXGeoIP", "EssentialsXProtect", "EssentialsXAntiBuild", ]
p = plugins_dir / pathlib.Path("EssentialsX/")
p.mkdir(parents=True, exist_ok=True)
response = requests.get('https://api.github.com/repos/EssentialsX/Essentials/releases/latest')
# add check for version if match no action
asset_urls = [a['browser_download_url'] for a in json.loads(response.text)['assets']]
for url in asset_urls:
    filename = url.split('/')[-1].split('-')[0]
    if filename not in exclude:
        r = requests.get(url)
        with open(p / (filename + ".jar"), 'wb') as f:
            f.write(r.content)

# Vault
# behind cloudflare does not like "bots"
# if this fails just start building from source
#scraper = cloudscraper.create_scraper()
#r = scraper.get("https://dev.bukkit.org/projects/vault/files/latest")
#with open(plugins_dir / "Vault.jar", 'wb') as f:
#    f.write(r.content)
