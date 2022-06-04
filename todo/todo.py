from typing import Any, Dict, NamedTuple

from pathlib import Path

from todo.db import DatabaseHandler

class ThisTODO(NamedTuple):

    todo: Dict[str, Any]

    error: int

#kinda like a controller class 
#Composition's notion by including the DatabaseHandler class
class Doer():
    def __init__(self,db_path:Path) -> None:
        self._db_handler = DatabaseHandler(db_path)
