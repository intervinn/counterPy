
import os

from enum import Enum

class Methods(Enum):
    RETURN = "return"
    PRINT = "print"

class Counter:

    formats: list = [
        "java",
        "py",
        "js",
        "jsx",
        "ts",
        "tsx",
        "html",
        "css",
        "cpp",
        "cs",
        "c",
        "h",
        "rb",
        "rs",
        "go",
        "vue",
        "dart",
        "php",
        "scala",
        "kt",
        "json",
    ]

    def __init__(self, dir: str) -> None:
        self.dir = dir

    def count(self, method: Enum):

        files: list = []

        for filename in os.listdir(self.dir):
            for format in self.formats:
                if filename.endswith(f".{format}"):
                    files.append(format)
        
        res: dict = {
            "total": len(files)
        }

        for i in files:
            res[i] = files.count(i)

        if method.value == "print":
            for k in res:
                print(f"{k} - {res[k]}")
        if method.value == "return":
            return res