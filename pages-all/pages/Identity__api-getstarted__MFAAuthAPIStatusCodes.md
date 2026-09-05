# Authentication and On-Demand MFA API HTTP Status Codes
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/MFAAuthAPIStatusCodes.htm
- Fetched: 2026-09-05 02:17 CDT

# Authentication and On-Demand MFA API HTTP Status Codes

The Authentication and On-Demand Multifactor Authentication (MFA) APIs for identity domains in IAM are REST compliant and use standard HTTP response status codes to indicate failure.

This table describes the different status codes and the use cases in which these status codes are sent.

See the[Status Code Definitions](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)section of the Hypertext Transfer Protocol -- HTTP/1.1.

HTTP Status Code Use Case

Sample JSON Response Body
`400 Bad Request`

This code indicates a bad request. This code is sent if any attribute is supplied with an invalid value in the payload, which signifies syntax issues.
```

```

`401 Unauthorized`

This code indicates unauthorized access. This is used when the`requestState`is invalid or expired, or the ID of the`otpCode`provided during authentication is invalid.
```

```

`422`

This code is used when the request is syntactically correct, but semantically wrong. 422 means that the request is an unprocessable entity. For example, when the request is missing the`op`attribute, which is mandatory for a given action.
```

```

`500 Internal Server Error`

This code indicates an internal server error. When this error occurs, the response contains the`ecId`
