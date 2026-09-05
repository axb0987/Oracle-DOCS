# Updating Refresh Token Expirations
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/refreshtokenexiry.htm
- Fetched: 2026-09-05 02:18 CDT

# Updating Refresh Token Expirations

Refresh tokens carry the information necessary to get a new access token. In other words, whenever an access token is required to access a specific resource, a client may use a refresh token to get a new access token issued by the authentication server.

A common use case is getting new access tokens after old ones have expired, such as an access token expiring on a mobile app. The mobile app sends the refresh token to obtain a new access token with no need for caching the user's password.

Refresh tokens do expire, but are typically long-lived.
Use the following steps when you want to see how long the refresh token is valid or when you need to update the refresh token value.
Note  
  
The default value for the`refreshTokenExpiry`attribute is seven days. The value is listed in seconds:`604800.`

## Get the Current Refresh Token Expiration Value

Make a GET request to the`/Apps`endpoint, requesting a specific App ID, and then specify the`refreshTokenExpiry`attribute.

Request Example
```

```

Response Example

The`refreshTokenExpiry`attribute is returned in the response (in bold in the example).
```

```

Alternatively, you can make a GET request to the`/Apps`endpoint, requesting a specific App ID to return all application-specific attributes, including the`refreshTokenExpiry`attribute.

Request Example
```

```

Response Example

The`refreshTokenExpiry`attribute is returned in the response (in bold in the example).
```

```

## Change the Refresh Token Value

To update the`refreshTokenExpiry`attribute value, make a PATCH request to the`/Apps`endpoint specifying the App ID, and then define the updated`refreshTokenExpiry`attribute value in the payload.

Request Example
```

```

Response Example

The response returned includes the updated`refreshTokenExpiry`attribute value (in bold in the example).
```

```
