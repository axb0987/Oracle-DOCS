# Adding mTLS support to API Deployments
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingmtlssupport.htm
- Fetched: 2026-09-05 01:37 CDT

# Adding mTLS support to API Deployments

Find out how to use a request policy to add mTLS support to API deployments with API Gateway.

The API gateways you create with the API Gateway service are secured through TLS encryption and verification. An API gateway presents a server certificate to an API client during a TLS handshake, enabling the API client to validate the authenticity of the API gateway. The process of the API client authenticating the API gateway is known as one-way TLS.

In many situations, you only want to allow authenticated API clients to access an API. In these situations, you want the API gateway to validate the authenticity of an API client, by verifying the TLS certificate presented by the API client. The process of the API gateway authenticating the API client is known as mutual TLS (mTLS).

With mTLS, both the API gateway and the API client exchange and verify certificates during the TLS handshake. The API gateway verifies the TLS certificate presented by the API client using custom Certificate Authority (CA) root certificates, and custom CA bundles of root and intermediate certificates. The custom CAs and CA bundles are stored in the API gateway's trust store, along with a default CA bundle that contains certificates of well-known public CAs. Note that in an mTLS handshake, the API gateway only uses custom CAs and custom CA bundles to verify API client certificates. The API gateway does not use the default CA bundle to verify API client certificates. So if you want an API gateway to support mTLS, you must add custom CAs and CA bundles to the API gateway's trust store (see[Customizing Trust Stores for TLS Certificate Verification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaysettingupcustomcertificateauthorities.htm)).

For extra control, you can also specify that certificates presented by API clients to an API gateway must contain particular values in the certificate's Email Address, URL, or Domain Name fields. If you specify values for these fields when setting up mTLS for an API gateway, the API gateway will reject requests from API clients presenting certificates that do not contain them. If you don't specify values for these fields when setting up mTLS, the API gateway will accept all requests from API clients providing the certificate is valid. You can specify up to 10 values for each API deployment by default (you can change this internal limit).

After a successful mTLS handshake between the API gateway and an API client, a Base64-encoded version of the certificate presented by the API client is saved in the`request.cert`context table as a context variable named`request.cert[client_base64]`. When defining an API deployment, you can reference the certificate using the format`${request.cert[client_base64]}`(see[Adding Context Variables to Policies and HTTP Back End Definitions](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycontextvariables.htm)). Note that if an API client presents a TLS certificate that is greater than 8 KB in size (after it has been Base64-encoded), the certificate is not saved as a context variable.

You use a request policy in the API deployment specification to add mTLS support to an API (see[Adding Request Policies and Response Policies to API Deployment Specifications](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingrequestpolicies.htm)). The mTLS request policy applies globally to all routes in an API deployment specification.
Note the following:
- If an API client presents a TLS certificate to an API gateway and the API deployment is not mTLS-enabled, the API gateway simply ignores the TLS certificate that has been presented. The`request.cert[client_base64]`context variable is not set in this situation.
- If an API gateway is unable to validate the TLS certificate presented by an API client, the API gateway rejects the request with an HTTP 401 error status response code.
- If an API gateway uses a custom CA bundle to validate the TLS certificate presented by an API client, no more than three CA certificates can be traversed at any point in the certificate chain during validation. In other words, to be valid, a CA certificate in the chain must either itself be signed directly by a custom CA present in the API gateway's trust store, or be no more than two intermediate certificates away from a certificate that has been signed by such a custom CA.[Contact us](https://support.oracle.com/)if you want to allow more intermediate certificates.

You can add an mTLS request policy to an API deployment specification by:
- using the Console
- editing a JSON file

## Using the Console to Add mTLS Request Policies

To add an mTLS request policy to an API deployment specification using the Console:
- 

Create or update an API deployment using the Console, select the Create deployment option, and enter details on the Basic information page.

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- 

In the API request policies section of the Basic information page, under Mutual-TLS, select the Enable mTLs option and optionally specify:
- Subject alternative name (SAN) / Common name (CN): Values that must appear in one or more of the following fields of the certificate presented by the API client for the API gateway to accept requests from the client:
- Email Address
- URL
- Domain Name

For example,`example.com`. You can specify up to 10 values by default (you can change this internal limit). Validation is case-insensitive.

You can include an asterisk (*) wildcard at the start and/or at the end of each value, to represent zero, one, or more characters. You cannot include an asterisk wildcard in the middle of the value. For example:
- `*.example.com`matches`server.example.com`
- `server.example.*`matches`server.example.com`
- `*.example.*`matches`server.example.com`
- `server.*.com`does not match`server.example.com`because the wildcard cannot be in the middle of the value

If you specify values when setting up mTLS for an API deployment, the API gateway will reject requests from API clients presenting certificates that do not contain them. If you don't specify values when setting up mTLS, the API gateway will accept all requests from API clients providing the certificate is valid.
- Select Next and enter or change additional details for the API deployment, as required.
- Select Create or Update to create or update the API deployment.
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)).

## Editing a JSON File to Add mTLS Request Policies

To add an mTLS request policy to an API deployment specification in a JSON file:
- 

Using your preferred JSON editor, edit the existing API deployment specification to which you want to add mTLS support, or create a new API deployment specification (see[Creating an API Deployment Specification](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingspecification.htm)).

For example, the following basic API deployment specification defines a simple Hello World serverless function in OCI Functions as a single back end:

```

```

- 

To specify an mTLS request policy that applies globally to all the routes in an API deployment:
- 

Insert a`requestPolicies`section before the`routes`section, if one doesn't exist already. For example:

```

```

- 

Add the following`mutualTLS`policy to the new`requestPolicies`section to apply globally to all the routes in an API deployment:

```

```

where:
- `"isVerifiedCertificateRequired": true|false`, is either`true`or`false`, indicating whether mTLS is enabled for the API deployment. If not specified, the default is`false`.
- `"allowedSans": [<list-of-values>]`is an optional comma-separated list of values that must appear in one or more of the following fields of the certificate presented by the API client for the API gateway to accept requests from the client:
- Email Address
- URL
- Domain Name

For example,`example.com`. You can specify up to 10 values by default (you can change this internal limit). Validation is case-insensitive.

You can include an asterisk (*) wildcard at the start and/or at the end of each value, to represent zero, one, or more characters. You cannot include an asterisk wildcard in the middle of the value. For example:
- `*.example.com`matches`server.example.com`
- `server.example.*`matches`server.example.com`
- `*.example.*`matches`server.example.com`
- `server.*.com`does not match`server.example.com`because the wildcard cannot be in the middle of the value

If you specify values when setting up mTLS for an API deployment, the API gateway will reject requests from API clients presenting certificates that do not contain them. If you don't specify values when setting up mTLS, the API gateway will accept all requests from API clients providing the certificate is valid.

For example:

```

```

- Save the JSON file containing the API deployment specification.
- 

Use the API deployment specification when you create or update an API deployment in the following ways:
- by specifying the JSON file in the Console when you select the Upload an existing deployment API option
- by specifying the JSON file in a request to the API Gateway REST API

For more information, see[Deploying an API on an API Gateway by Creating an API Deployment](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm)and[Updating an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayupdating.htm).
- (Optional) Confirm the API has been deployed successfully by calling it (see[Calling an API Deployed on an API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayinvokingdeployedapi.htm)
