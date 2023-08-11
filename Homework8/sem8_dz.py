import os
import json
import pandas as pn
import pickle


def scan_dict(path: str) -> dict:
    data = {
        'name': os.path.basename(path),
        'size': os.path.getsize(path),
        'parent': os.path.relpath(os.path.join(path, os.pardir))
    }
    if os.path.isdir(path):
        data['type'] = "directory"
        data['children'] = [scan_dict(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        data['type'] = "file"
    return data


with open('file.json', 'w', encoding='utf-8') as f_write:
    json.dump(scan_dict('home_dir'), f_write, ensure_ascii=False, indent=2)

pn.DataFrame(scan_dict('home_dir')).to_csv('file.csv', index=False)

with open('file.pickle', 'wb') as f:
    pickle.dump(scan_dict('home_dir'), f)
