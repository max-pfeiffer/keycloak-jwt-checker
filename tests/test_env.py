"""Tests for command line interface."""

from typing import Any

from click.testing import CliRunner, Result
from testcontainers.keycloak import KeycloakContainer

from keycloak_jwt_checker import cli


def test_env(
    cli_runner: CliRunner,
    keycloak_container_and_client: tuple[KeycloakContainer, dict[str, Any]],
) -> None:
    """Test the command line interface with environment variables."""
    keycloak_container = keycloak_container_and_client[0]
    keycloak_client = keycloak_container_and_client[1]

    result: Result = cli_runner.invoke(
        cli,
        env={
            "KEYCLOAK_JWT_CHECKER_SERVER_URL": keycloak_container.get_url(),
            "KEYCLOAK_JWT_CHECKER_CLIENT_ID": keycloak_client["clientId"],
            "KEYCLOAK_JWT_CHECKER_CLIENT_SECRET": keycloak_client["secret"],
            "KEYCLOAK_JWT_CHECKER_REALM": "master",
            "KEYCLOAK_JWT_CHECKER_USERNAME": keycloak_container.username,
            "KEYCLOAK_JWT_CHECKER_PASSWORD": keycloak_container.password,
            "KEYCLOAK_JWT_CHECKER_SKIP_TLS_VERIFICATION": "true",
        },
    )
    assert result.exit_code == 0
