
import os

from enum import Enum

class Methods(Enum):
    RETURN = "return"
    PRINT = "print"

class Counter:

    exclude = [
        "gitignore",
        "git"
    ]

    def __init__(self, dir: str, debug: bool) -> None:
        self.dir = dir
        self.debug = debug

    def count(self, method: Enum):

        files: list = []

        for filename in os.listdir(self.dir):
            try:
                file = filename.split(".")[1]
                if file in self.exclude:
                    pass
                else:
                    files.append(file)

            except IndexError:
                if self.debug:
                    print("indexerror meeted skipping file")
            


        
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
