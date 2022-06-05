
from typer.testing import CliRunner
import json
import pytest
#Typer testing integrates well with pytest
#CliRunner is a class that allows to create a runner for testing responses to real-worlds commands

from todo import __app_name__, __version__, cli, DB_READ_ERROR,SUCCESS,todo


runner = CliRunner()

#basic testing for production
def test_version():

    result = runner.invoke(cli.app, ["--version"])

    assert result.exit_code == 0

    assert f"{__app_name__} v{__version__}\n" in result.stdout

@pytest.fixture
def dummy_json(tmp_path):
    todo = [{"Description": "Write API.", "Priority": 1, "Done": False}]
    db_file = tmp_path / "todo.json"
    with db_file.open("w") as db_data:
        json.dump(todo,db_data,ident=4)
	
    return db_file




data_test1 = {
    "description": ["Build", "the", "API"],
    "priority": 1,
    "todo": {
        "Description": "Build the API.",
        "Priority": 1,
        "Done": False,
    },
}
data_test2 = {
    "description": ["Implement Test"],
    "priority": 2,
    "todo": {
        "Description": "Implement Test.",
        "Priority": 2,
        "Done": False,
    },
}
