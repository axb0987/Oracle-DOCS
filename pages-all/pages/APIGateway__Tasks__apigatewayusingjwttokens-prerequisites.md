# Prerequisites for Token Authentication
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-prerequisites.htm
- Fetched: 2026-09-05 01:39 CDT

# Prerequisites for Token Authentication

You must perform these tasks before you can enable authentication and authorization for API deployments using JSON Web Tokens (JWTs).
- An OAuth2-compliant identity provider (for example, OCI IAM with Identity Domains, Oracle Identity Cloud Service (IDCS), Auth0) must have already been set up to issue JWTs for users allowed to access the API deployment.
- If you want to use custom claims in authorization policies, the identity provider must be set up to add the custom claims to the JWTs it issues.

See the identity provider documentation for more information (for example, the[OCI IAM with Identity Domains documentation](https://docs.oracle.com/iaas/Content/Identity/applications/overview.htm), the[Oracle Identity Cloud Service (IDCS) documentation](https://docs.oracle.com/en/cloud/paas/identity-cloud/index.html), the[Auth0 documentation](https://auth0.com/docs/get-started)).

To validate a JWT using a corresponding public verification key provided by the issuing identity provider:
- the signing algorithm used to generate the JWT's signature must be one of RS256, RS384, or RS512
- the public verification key must have a minimum length of 2048 bits and must not exceed 4096 bits

To validate tokens using an authorization server's introspection endpoint:
- You must have already created and registered a client application with the authorization server to obtain client credentials (a client ID and a client secret). See the authorization server documentation for more information (for example, the[OCI IAM with Identity Domains documentation](https://docs.oracle.com/iaas/Content/Identity/applications/overview.htm), the[Oracle Identity Cloud Service (IDCS) documentation](https://docs.oracle.com/en/cloud/paas/identity-cloud/index.html), the[Auth0 documentation](https://auth0.com/docs/get-started)).
- You must have already stored the client secret you obtained from the authorization server as a secret in a vault in the Vault service (see[Creating a Secret in a Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets_topic-To_create_a_new_secret.htm)), and you must know the OCID and version number of the secret.
- You must have already set up a policy to give API gateways in a dynamic group permission to access the vault secret containing the client secret (see[Create a Policy to Give API Gateways Access to Credentials Stored as Secrets in the Vault Service](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingpolicies.htm#dynamicgrouppolicy-5)
