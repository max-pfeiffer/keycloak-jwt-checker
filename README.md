# Keycloak JWT Checker
A little tool for debugging claims contained in JSON Web Tokens issued by Keycloak confidential clients.
Keycloak configuration can be quite complex. So I found it useful to have a tool to look at the claims contained
in JWTs if they contain the values you need for your use cases.

The CLI tool takes credentials of the client you configured in Keycloak and uses some users credentials to issue
tokes for that user using OIDC enpoints. It then decodes the JWT and displays it's claim content on stdout.
