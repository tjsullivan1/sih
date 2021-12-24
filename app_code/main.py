from pathlib import Path
from typing import Optional

import fastapi
import json
import uvicorn
from fastapi.staticfiles import StaticFiles


api = fastapi.FastAPI()


def configure():
    configure_routing()
    configure_api_keys()


def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')


def configure_api_keys():
    file = Path('settings.json').absolute()
    if not file.exists():
        print(f"WARNING: {file} file not found. You cannot continue -- please see settings_Template.json")
        raise Exception("settings.json file not found. You cannot continue -- please see settings_Template.json")
    
    with open('settings.json') as fin:
        settings = json.load(fin)
    

if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    configure()