[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![codecov](https://codecov.io/gh/max-pfeiffer/keycloak-jwt-checker/graph/badge.svg?token=Cqp6pn58fB)](https://codecov.io/gh/max-pfeiffer/keycloak-jwt-checker)
![pipeline workflow](https://github.com/max-pfeiffer/keycloak-jwt-checker/actions/workflows/pipeline.yml/badge.svg)

# Keycloak JWT Checker
A little CLI tool for debugging claims contained in JSON Web Tokens (JWT) issued by Keycloak confidential clients.

Keycloak configuration can be quite complex. So I found it useful to have a tool to look at the claims contained
in JWTs. You can see quickly if they contain the values you need for your use case.

The CLI tool takes the credentials of the client you configured in Keycloak and uses some user's credentials to issue
tokens for that user using OIDC endpoints. It then decodes the JWTs and prints its claim contents on stdout:
* access token
* id token
* refresh token

## Install
```shell
pip install keycloak-jwt-checker
```

## Usage
```shell
$ keycloak-jwt-checker --help
Usage: keycloak-jwt-checker [OPTIONS]

  Keycloak JWT Checker.

  A little tool for debugging claims contained in JSON Web Tokens (JWT) issued
  by Keycloak confidential clients.

Options:
  --server-url TEXT        URL of the Keycloak server  [required]
  --client-id TEXT         Client ID  [required]
  --client-secret TEXT     Client secret  [required]
  --realm TEXT             Realm  [required]
  --username TEXT          Username of a Keycloak user you configured for this
                           client  [required]
  --password TEXT          Password of a Keycloak user you configured for this
                           client  [required]
  --skip-tls-verification  Set this flag if the TLS verification should be
                           skipped on OIDC endpoints
  --help                   Show this message and exit.
```

## Environment Variables
If you are concerned about security or just don't want to use the CLI options for secrets or passwords, you can also use
the following environment variables to provide these values to Keycloak JWT Checker.
```shell
KEYCLOAK_JWT_CHECKER_SERVER_URL=http:localhost:8080
KEYCLOAK_JWT_CHECKER_CLIENT_ID=test
KEYCLOAK_JWT_CHECKER_CLIENT_SECRET=verysecretsecret
KEYCLOAK_JWT_CHECKER_REALM=myrealm
KEYCLOAK_JWT_CHECKER_USERNAME=testuser
KEYCLOAK_JWT_CHECKER_PASSWORD=testpassword
KEYCLOAK_JWT_CHECKER_SKIP_TLS_VERIFICATION=true
```
