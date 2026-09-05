# Token Exchange Grant Type Two-Legged Authorization Flow Example
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/token_exchange_grant_type_two_legged.htm
- Fetched: 2026-09-05 02:18 CDT

# Token Exchange Grant Type Two-Legged Authorization Flow Example

Use the following examples to create your Token Exchange grant type requests.

Each of these examples requires a signed request. To learn how to create signature header requests, see[Request Signatures](https://docs.oracle.com/iaas/Content/API/Concepts/signingrequests.htm).

## Request Example: Exchange an API Key for an Identity Domain Access Token
Use the API Key of a User to make a signed request to obtain an access token for the user who owns that API Key.
```

```

## Request Example: Exchange a User Principal for an Identity Domain Access Token
Use a User Principal to make a signed request to obtain an access token for that user.
```

```

The following additional scopes can also be used:
- `offline_access`
- `urn:opc:resource:consumer:tokengenerator:appid::<appId>`
- `urn:opc:resource:consumer:<scopeExtension>::<scopeQualifier>`
The following is request example using the`offline_access`scope.
```

```

When this scope is included, both an access token and a refresh token are produced. The refresh token format is listed in the response example below.
```

```

## Request Example: Exchange an Instance Principal (IPST) for an Identity Domain Access Token
Use an Instance Principal to make a signed request to obtain an access token for that instance.
```

```

## Request Example: Exchanging Resource Principal (RPST) for an Identity Domain Access Token
Use a Resource Principal to make a signed request to obtain an access token for that resource.
```

```

## Response Example
The following example shows the contents of the response body in JSON format when you use the Token Exchange grant type to obtain an access token for all 2-legged flow requests.
```

```
