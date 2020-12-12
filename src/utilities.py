from pathlib import Path
from typing import Union

import yaml
from yaml import Loader


def read_yaml(file: Union[str, Path], key: str = None) -> dict:
    with open(file, "r") as fp:
        params = yaml.load(fp, Loader)
    return params[key] if key else params


def dump_yaml(obj: dict, file_path: Union[str, Path], key: str = None, norm: bool = False) -> Path:
    obj = obj[key] if key else obj
    if norm:
        obj = normalize(obj)
    with open(file_path, "w+") as file:
        yaml.dump(obj, file)
    return Path(file_path)
    
def normalize(obj:dict,ndigits:int = 4) ->dict:
    for key,value in obj.items():
        if isinstance(value,dict):
            value=normalize(value,dict)
        if isinstance(value,(float,)):
            obj[key]=round(value,ndigits)
    return obj