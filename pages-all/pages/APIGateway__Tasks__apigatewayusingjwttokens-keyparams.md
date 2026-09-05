# Key Parameters Required to Verify JWT Signatures
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayusingjwttokens-keyparams.htm
- Fetched: 2026-09-05 01:39 CDT

# Key Parameters Required to Verify JWT Signatures

To verify the signature on a JSON Web Token (JWT), API gateways require the following key parameters are present in either the JWKS returned from a URI or the static JSON Web Key you specify.

Key Parameter Notes
`kid`The identifier of the key used to sign the JWT. The value must match the`kid`claim in the JWT header. For example,`master_key`.
`kty`The type of the key used to sign the JWT. Note that RSA is currently the only supported key type.
`use`or`key_ops`

If the`use`parameter is present, then it must be set to`sig`. If the`key-ops`parameter is present, then`verify`must be one of the valid values.
`n`The public key modulus.
`e`The public key exponent.
`alg`
