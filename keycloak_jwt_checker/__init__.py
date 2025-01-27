"""Keycloak JWT Checker."""

# ruff: noqa: D301

import json

import click
from jwt import decode
from keycloak import KeycloakOpenID


@click.command()
@click.option(
    "--server-url",
    envvar="KEYCLOAK_JWT_CHECKER_SERVER_URL",
    required=True,
    help="URL of the Keycloak server",
)
@click.option(
    "--client-id",
    envvar="KEYCLOAK_JWT_CHECKER_CLIENT_ID",
    required=True,
    help="Client ID",
)
@click.option(
    "--client-secret",
    envvar="KEYCLOAK_JWT_CHECKER_CLIENT_SECRET",
    required=True,
    help="Client secret",
)
@click.option(
    "--realm",
    envvar="KEYCLOAK_JWT_CHECKER_REALM",
    required=True,
    help="Realm",
)
@click.option(
    "--username",
    envvar="KEYCLOAK_JWT_CHECKER_USERNAME",
    required=True,
    help="Username of a Keycloak user you configured for this client",
)
@click.option(
    "--password",
    envvar="KEYCLOAK_JWT_CHECKER_PASSWORD",
    required=True,
    help="Password of a Keycloak user you configured for this client",
)
@click.option(
    "--skip-tls-verification",
    envvar="KEYCLOAK_JWT_CHECKER_SKIP_TLS_VERIFICATION",
    flag_value=True,
    help="Set this flag if the TLS verification should be skipped on OIDC endpoints",
)
def cli(
    server_url: str,
    client_id: str,
    client_secret: str,
    realm: str,
    username: str,
    password: str,
    skip_tls_verification: bool,
) -> None:
    """Keycloak JWT Checker.

    A little tool for debugging claims contained in JSON Web Tokens (JWT) issued by
    Keycloak confidential clients.

    \f

    :return:
    """
    keycloak_openid = KeycloakOpenID(
        server_url=server_url,
        client_id=client_id,
        client_secret_key=client_secret,
        realm_name=realm,
        verify=not skip_tls_verification,
    )

    # Get tokens
    token = keycloak_openid.token(username, password)
    access_token = token.get("access_token")
    id_token = token.get("id_token")
    refresh_token = token.get("refresh_token")

    # Decode JWT and print results
    if access_token:
        click.echo("ACCESS TOKEN:")
        click.echo(
            json.dumps(
                decode(
                    access_token, client_secret, options={"verify_signature": False}
                ),
                indent=4,
            )
        )
    if id_token:
        click.echo("ID TOKEN:")
        click.echo(
            json.dumps(
                decode(id_token, client_secret, options={"verify_signature": False}),
                indent=4,
            )
        )
    if refresh_token:
        click.echo("REFRESH TOKEN:")
        click.echo(
            json.dumps(
                decode(
                    refresh_token, client_secret, options={"verify_signature": False}
                ),
                indent=4,
            )
        )
