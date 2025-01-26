"""Keycloak JWT Checker."""

# ruff: noqa: D301

import pprint

import click
from jwt import decode
from keycloak import KeycloakOpenID


@click.command()
@click.option(
    "--server-url",
    required=True,
    help="URL of the Keycloak server",
)
@click.option(
    "--client-id",
    required=True,
    help="Client ID",
)
@click.option(
    "--client-secret",
    required=True,
    help="Client secret",
)
@click.option(
    "--realm",
    required=True,
    help="Realm",
)
@click.option(
    "--username",
    required=True,
    help="Username",
)
@click.option(
    "--password",
    required=True,
    help="Password",
)
def cli(server_url, client_id, client_secret, realm, username, password) -> None:
    """Command line interface (CLI).

    CLI provides common operations for configuring and running the application.

    Run 'irrigation-pi COMMAND --help' for more information about commands and usage.
    \f

    :return:
    """
    keycloak_openid = KeycloakOpenID(
        server_url=server_url,
        client_id=client_id,
        client_secret_key=client_secret,
        realm_name=realm,
        verify=False,
    )
    token = keycloak_openid.token(username, password)
    access_token = token.get("access_token")
    id_token = token.get("id_token")
    refresh_token = token.get("refresh_token")
    if access_token:
        click.echo("ACCESS TOKEN:")
        click.echo(
            pprint.pprint(
                decode(access_token, client_secret, options={"verify_signature": False})
            )
        )
    if id_token:
        click.echo("ID TOKEN:")
        click.echo(
            pprint.pprint(
                decode(id_token, client_secret, options={"verify_signature": False})
            )
        )
    if refresh_token:
        click.echo("REFRESH TOKEN:")
        click.echo(
            pprint.pprint(
                decode(
                    refresh_token, client_secret, options={"verify_signature": False}
                )
            )
        )
