# Passing Custom Parameters to a Social Identity Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/passCustomerParamsIdP.htm
- Fetched: 2026-09-05 02:18 CDT

# Passing Custom Parameters to a Social Identity Provider

Use the identity domains REST API to pass a custom parameter for social identity provider (IdP) configurations. For each social IdP, you can define both static and dynamic custom parameters, which are passed as-is to the IdP when sent in an authorization request.

## Custom Parameter Definition
You can define relay parameter mappings by using the social attribute`relayIdpParamMappings`. This parameter stores mapping key-value pairs for a social IdP. A dynamic parameter type maps to an empty or null value. A static parameter type contains a value.
- If a key is defined as a static parameter, but passed with a different value, at runtime, the static value defined in the IdP configuration is used.
- If a relay parameter variable is passed in authorization, and the URL is undefined in the IdP configuration, then this variable is ignored.
```

```

## Example of Relay Parameter Mappings Being Passed to an IdP

This authorization URL that's passed to the identity domains REST API:

```

```

The redirect from the identity provider becomes:

`<IDPProvider Authorize URI>?client_id=....redirect_uri=....&brand=abc¶m1=test¶m2=value2`.

The variable`newParam`is ignored because it wasn't defined in the original IdP configuration. The value for`param2`is static and doesn't get changed during runtime authorization. The dynamic parameter`brand`gets a value at runtime, because it was defined initially as a dynamic type during the IdP configuration.

## Create a Social IdP with Relay Parameter Mapping

`cURL: POST /admin/v1/SocialIdentityProviders`

Example Request Body
```

```

Example Response Body
```

```

## Add a Relay Parameter Mapping to an Existing IdP
```

```

Example Request Body
```

```

Example Response Body
```

```

## Fetch Relay Parameter Mappings for an Existing IdP

`cURL: GET /admin/v1/SocialIdentityProviders/{idpId}?attributes=relayIdpParamMappings`

Example Request Body : Not applicable.

Example Response Body
```

```

## Update a Relay Parameter Mapping for an IdP

`cURL: PATCH /admin/v1/SocialIdentityProviders/{idpId}`

Example Request Body
```

```

Example Response Body
```

```

## Delete a Relay Parameter Mapping from an IdP

`cURL: PATCH /admin/v1/SocialIdentityProviders/{idpId}`

Example Request Body
```

```

Example Response Body
```

```

## Delete All Relay Parameter Mappings from an IdP

`cURL: PATCH /admin/v1/SocialIdentityProviders/{idpId}`

Example Request Body
```

```

Example Response Body
```

```
