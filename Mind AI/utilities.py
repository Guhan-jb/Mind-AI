from pathlib import Path
from typing import Any, Dict, List
import json
from urllib.request import urlretrieve


def download_file(url: str) -> Path:
    example_dirpath = Path(__file__).parent
    data_dirpath = example_dirpath / "data"
    data_dirpath.mkdir(exist_ok=True)
    filepath = data_dirpath / Path(url).name

    urlretrieve(url, filepath)
    return filepath


def print_emotions(emotions: List[Dict[str, Any]]) -> None:
    #emotion_map = {e["name"]: e["score"] for e in emotions}
    # for emotion in ["Joy", "Sadness", "Anger"]:
    #     return(f"- {emotion}: {emotion_map[emotion]:4f}")\
    print(emotions)
    json_data = json.dumps(emotions)
    file_path = 'data.json'
    with open(file_path, 'w') as json_file:
        json_file.write(json_data)
    return emotions[5]

