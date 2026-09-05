# Client/User JWT Assertion
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/ClientAssertion.htm
- Fetched: 2026-09-05 02:17 CDT

# Client/User JWT Assertion

An assertion is a package of information that facilitates the sharing of identity and security information across security domains. An assertion typically contains information about a subject or principal, information about the party that issued the assertion and when it was issued. It also contains information about the conditions under which the assertion is to be considered valid, such as when and where it can be used. The intent is to provide an alternative client authentication mechanism. Clients can build client assertions and use them as credentials rather than using the client ID and client secret in an OAuth token request.

Identity domains support the use of client and user assertions for authentication. The following information defines the format of the client assertion and the user assertion, including standard and custom claims. Names with (*) are proprietary to Oracle.

## Client/User Assertion Headers

Name Value
`kid`Key identifier. Used to identify the trusted third-party certificate to validate the assertion signature. The`x5t`or`kid`claim must be present in the JWT assertion header.
`type`Type. Identifies the type of assertion, which is always`JWT`.
`alg`Algorithm. Identifies the specific type of JWT signing algorithm. This is a required header for the JWT assertion. Identity domains support RS256.
`x5t`Base64 URL encoded X.509 certificate sha1 thumbprint. This is used to identify specific certificates. The`x5t`or`kid`claim must be present in the JWT assertion header.

## JWT Body/Claims

Name Value
`sub`Subject. The principal that's the subject of the JWT: For client assertions, the client ID value must be the identity domain App`name`attribute. For user assertions, the claim value must be the username.
`iss`Issuer. The Client that's generating the assertions (identity domain App`name`attribute). This is a required claim for the assertion.
`aud`Audience. Identifies the recipients for which the JWT is intended. The identity domain URL (`https://<domainURL>`) must be one of the`aud`claim values.
`exp`Expiration. The time (UNIX epoch time) when the JWT assertion expires. This is a required claim for the assertion.
`iat`Issued at. The date when the assertion was issued.

Sample JWT Client Assertion
```

```

Sample JWT User Assertion
```

```

## Generating User and Client Assertions Using a Signing Key

Before You Begin
Ensure that you have the following installed.
- GlassFish javax.json-1.0.4 library
- JDK 8 to perform the base64 encoding/decoding.

Note: It's not necessary to generate a signed client assertion if the client can authenticate using client ID &amp; client secret. You need to decide how to authenticate the client by using the client ID/client secret or by using PKI.

Assertion Generator Lightweight JDK8

```

```

## Sample Output and Decoding from Assertion Java Code
Trusted Client Signed User Assertion
```

```

Trusted Client Signed Client Assertion
```

```

Decoding User Assertion

Header
```

```

Payload
```

```

Decoding Client Assertion

Header
```

```

Payload
```

```

## Example Token Requests Using User Assertions
Example Request Using Authorization Header and User Assertion
```

```

Example Request Using User Assertion and Client Assertion
```

```
