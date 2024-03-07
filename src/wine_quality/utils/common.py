import os
import yaml
import json
import joblib

from pathlib import Path
from typing import Any
from wine_quality import logger


def read_yaml(path_to_yaml: Path):
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully!")
   
    except ValueError:
        raise ValueError("yaml file is empty!")
       
    except Exception as e:
        raise e


def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


def save_josn(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at: {path}")


def load_json(path: Path):
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json loaded successfully from: {path}")


def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


def load_bin(path: Path):
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")


def get_size(path: Path):
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"