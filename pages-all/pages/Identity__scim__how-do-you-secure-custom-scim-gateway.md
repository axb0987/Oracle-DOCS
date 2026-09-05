# Securing the Custom SCIM Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/scim/how-do-you-secure-custom-scim-gateway.htm
- Fetched: 2026-09-05 02:28 CDT

# Securing the Custom SCIM Gateway

Secure the custom SCIM gateway in an OCI IAM identity domain.

Because you don't want unauthorized users or clients to access your custom SCIM gateway, you must secure it. To secure it, use an authorization token to protect the HTTP(S) endpoints of your gateway. This token validates the user or client to allow them to make appropriate HTTP calls to the gateway endpoints. If the token isn't present or is invalid, then the endpoints return a`401 HTTP`response code because IAM isn't authorized to access the endpoints.
