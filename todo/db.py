import configparser

from pathlib import Path
import json
from typing import Any,Dict,List,NamedTuple


from todo import DB_WRITE_ERROR,DB_READ_ERROR,JSON_ERROR, SUCCESS


DEFAULT_DB_FILE_PATH = Path.home().joinpath(

    "." + Path.home().stem + "_todo.json"

)


def get_database_path(config_file: Path) -> Path:

    """Return the current path to the to-do database."""

    config_parser = configparser.ConfigParser()

    config_parser.read(config_file)

    return Path(config_parser["General"]["database"])


def init_database(db_path: Path) -> int:

    """Create the to-do database."""

    try:

        db_path.write_text("[]")  # Empty to-do list

        return SUCCESS

    except OSError:

        return DB_WRITE_ERROR


#Responding
class DBResponse(NamedTuple):
    todo:List[Dict[str,Any]]
    error: int

#Database handler stuff
class DatabaseHandler:
    def __init__(self,db_path:Path) -> None:
        self._db_path = db_path
    def read_todos(self) -> DBResponse:
        try:
            with self._db_path.open("r") as db:
                try:
                    return DBResponse(json.load(db),SUCCESS)
                except json.JSONDecodeError:
                    return DBResponse([],JSON_ERROR)
        except OSError:
            #IO Problem
            return DBResponse([],DB_READ_ERROR)
    def write_todos(self,todo:List[Dict[str,Any]]) -> DBResponse:
        try:
            with self._db_path.open("w") as db_file:
                json.dump(todo,db_file,ident=4)
            return DBResponse(todo,SUCCESS)
        except OSError:
            return DBResponse(todo,DB_WRITE_ERROR)

