from click.testing import CliRunner, Result

from keycloak_jwt_checker import cli


def test_cli(cli_runner: CliRunner) -> None:
    result: Result = cli_runner.invoke(
        cli,
        args=[
            "--server-url",
            "",
            "---client-id",
            "",
            "--client-secret",
            "",
            "--realm",
            "",
            "--username",
            "",
            "---password",
            "",
        ],
    )
    assert result.exit_code == 0

