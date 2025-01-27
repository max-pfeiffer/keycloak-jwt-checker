"""Test fixtures."""

from typing import Any

import pytest
from click.testing import CliRunner
from testcontainers.keycloak import KeycloakContainer


@pytest.fixture(scope="session")
def keycloak_container_and_client() -> tuple[KeycloakContainer, dict[str, Any]]:
    """Keycloak container and confidential client.

    :return:
    """
    with KeycloakContainer("quay.io/keycloak/keycloak:24.0.5") as keycloak_container:
        # Create a confidential client
        admin_client_master_realm = keycloak_container.get_client()
        client_id = admin_client_master_realm.create_client(
            {
                "clientId": "test",
                "secret": "supersecret",
                "publicClient": False,
                "standardFlowEnabled": True,
                "implicitFlowEnabled": False,
                "directAccessGrantsEnabled": True,
                "enabled": True,
            }
        )
        client = admin_client_master_realm.get_client(client_id)
        yield keycloak_container, client


@pytest.fixture(scope="session")
def cli_runner() -> CliRunner:
    """CLI runner for testing click CLI.

    :return:
    """
    runner = CliRunner()
    return runner
