# CRUD Operations for an Apple IdP
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/crud-operations-aple-idp.htm
- Fetched: 2026-09-05 02:22 CDT

# CRUD Operations for an Apple IdP

Learn how to create, read, update, and delete an Apple IdP.

## 1. Getting an Admin Access Token

- 

Sign in with an administrator account.
- 

Select Profile and choose a user profile.
- 

Select Tokens and keys .
- 

Go to My access tokens .
- 

Choose Identity Domain Administrator role and enter desired token expiry.
- 

Select Download token .

## 2. Creating an Apple IdP

### POST /admin/v1/SocialIdentityProviders Example
```

```

### Response Example
```

```

## 3. Getting an Apple IdP

### GET /admin/v1/SocialIdentityProviders Request Example
```

```

### Response Example
```

```

## 4. Updating an Apple IdP

### PATCH /admin/v1/SocialIdentityProviders/&lt;id&gt; Request Example

Send a GET request first and record the ID of Apple IdP in the response.
```

```

### Response Example
```

```

## 5. Deleting an Apple IdP

### DELETE /admin/v1/SocialIdentityProviders/&lt;id&gt; Request Example
- Send a GET request first and then record the ID of Apple IdP in the response.
- Remove any social users associated with this IdP and remove this IdP from IdP policies.
- Disable this IdP with a PATCH call. The following is an example of a PATCH call.
```

```

### Response Example
```

```

## 6. Adding and Removing an IdP from an IdP Policy

See:
- [Adding Identity Providers to the Policy](https://docs.oracle.com/iaas/Content/Identity/idppolicies/add-identity-providers-policy.htm)
- [Removing Identity Providers from the Policy](https://docs.oracle.com/iaas/Content/Identity/idppolicies/remove-identity-providers-policy.htm)
