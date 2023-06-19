import os, requests, json, time
from shutil import copy
from os import path, listdir, getenv, path, makedirs
from os.path import isfile, join, exists

def run():
    DOWNLOAD_STRING: str = "https://roblox-client-optimizer.simulhost.com/ClientAppSettings.json"

    req = requests.get(DOWNLOAD_STRING)

    json_file = path.abspath('ClientAppSettings.json')

    if exists(json_file):
        os.remove(json_file)

    new_path = getenv('LOCALAPPDATA')
    files = [join(new_path, f) for f in listdir(new_path) if not isfile(join(new_path, f)) if 'Roblox' in f]
    new_path = getenv('programfiles')
    files = files + [join(new_path, f) for f in listdir(new_path) if not isfile(join(new_path, f)) if 'Roblox' in f]
    new_path = getenv('programfiles(x86)')
    files = files + [join(new_path, f) for f in listdir(new_path) if not isfile(join(new_path, f)) if 'Roblox' in f]

    for folder in files:
        if exists(join(folder, "Versions")):
            for f in listdir(join(folder, "Versions")):
                if not isfile(join(folder, "Versions", f)):
                    makedirs(join(folder, "Versions", f, "ClientSettings"), exist_ok=True)
                    new_path_name = join(folder, "Versions", f, "ClientSettings", "ClientAppSettings.json")
                    if exists(new_path_name):
                        os.remove(new_path_name)
                    
                    with open(new_path_name, "w") as my_file:
                        json.dump(req.json(), my_file, indent=6)
                        my_file.close()

while True:
    run()
    time.sleep(120)