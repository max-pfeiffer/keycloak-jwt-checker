"""Tests for using command line options."""

from typing import Any

from click.testing import CliRunner, Result
from testcontainers.keycloak import KeycloakContainer

from keycloak_jwt_checker import cli


def test_cli(
    cli_runner: CliRunner,
    keycloak_container_and_client: tuple[KeycloakContainer, dict[str, Any]],
) -> None:
    """Test the command line interface with options."""
    keycloak_container = keycloak_container_and_client[0]
    keycloak_client = keycloak_container_and_client[1]

    result: Result = cli_runner.invoke(
        cli,
        args=[
            "--server-url",
            keycloak_container.get_url(),
            "--client-id",
            keycloak_client["clientId"],
            "--client-secret",
            keycloak_client["secret"],
            "--realm",
            "master",
            "--username",
            keycloak_container.username,
            "--password",
            keycloak_container.password,
            "--skip-tls-verification",
        ],
    )
    assert result.exit_code == 0
