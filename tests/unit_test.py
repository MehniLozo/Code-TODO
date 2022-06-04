
from typer.testing import CliRunner

#Typer testing integrates well with pytest
#CliRunner is a class that allows to create a runner for testing responses to real-worlds commands

from todo import __app_name__, __version__, cli


runner = CliRunner()

#basic testing for production
def test_version():

    result = runner.invoke(cli.app, ["--version"])

    assert result.exit_code == 0

    assert f"{__app_name__} v{__version__}\n" in result.stdout
