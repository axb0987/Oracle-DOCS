# Using allowSelfChange To Update Profile Attributes
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/change-your-own-profile-attributes.htm
- Fetched: 2026-09-05 02:17 CDT

# Using allowSelfChange To Update Profile Attributes

You can use the API to change your own profile attributes (for example, an email address or a password) in an identity domain by setting the`allowSelfChange`attribute to`true`in the request payload or URL query string parameter. By default, this attribute is set to`false`.

Use the`allowSelfChange`attribute in the request payload for the following operations:
- Users (PATCH, REPLACE)
- UserCapabilityChanger (REPLACE)
- UserLockedStateChanger (CREATE)
- UserPasswordChanger (REPLACE)
- UserPasswordResetter (REPLACE)
- UserStateChanger (PATCH)
- UserStatusChanger (REPLACE)
- UserDbCredentials (CREATE)
- ApiKeys (CREATE, UPDATE)
- AuthTokens (CREATE, UPDATE)
- CustomerSecretKeys (CREATE, UPDATE)
- OAuth2ClientCredentials (CREATE, UPDATE)
- SmtpCredentials (CREATE, UPDATE)
- SupportAccounts (CREATE)
Use the`allowSelfChange`attribute as a URL query string parameter for the DELETE operation on the following APIs.
Note  
  
You must set`allowSelfChange=true`as a URL query string parameter for DELETE operations.
- UserDbCredentials
- ApiKeys
- AuthTokens
- CustomerSecretKeys
- OAuth2ClientCredentials
- SmtpCredentials
- SupportAccounts

## Sample Request: /Users
Operation: PATCH`/admin/v1/Users/<id>`
```

```

## Sample Request: /UserCapabilitiesChanger
Operation: PUT`/admin/v1/UserCapabilitiesChanger/<id>`
```

```

## Sample Request: /UserLockedStateChanger
Operation: POST`/admin/v1/UserLockedStateChanger`
```

```

## Sample Request: /UserPasswordChanger
Operation: PUT`/admin/v1/UserPasswordChanger`
```

```

## Sample Request: /UserPasswordResetter
Operation: PUT`/admin/v1/UserPasswordResetter`
```

```

## Sample Request: /UserStatusChanger
Operation: PUT`/admin/v1/UserStatusChanger`
```

```

## Sample Requests: /ApiKeys
Operation: POST`/admin/v1/ApiKeys`
```

```

Operation: PATCH`/admin/v1/ApiKeys/<id>`
```

```

Operation: DELETE`/admin/v1/ApiKeys/e1eaf8a28e58485fb86f16f914fd08c7?allowSelfChange=true`
```

```

## Sample Requests: /SmtpCredentials
Operation: POST`/admin/v1/SmtpCredentials/<id>`
```

```

Operation: PATCH`/admin/v1/SmtpCredentials`
```

```

Operation: DELETE`/admin/v1/SmtpCredentials/e1eaf8a28e58485fb86f16f914fd08c7?allowSelfChange=true`

## Sample Requests: /AuthTokens
Operation: POST`/admin/v1/AuthTokens`
```

```

Operation: PATCH`/admin/v1/AuthTokens/<id>`
```

```

Operation: DELETE`/admin/v1/SmtpCredentials/e1eaf8a28e58485fb86f16f914fd08c7?allowSelfChange=true`

## Sample Requests: /CustomerSecretKeys
Operation: POST`/admin/v1/CustomerSecretKeys`
```

```

Operation: PATCH`/admin/v1/CustomerSecretKeys/<id>`
```

```

Operation: DELETE`/admin/v1/CustomerSecretKeys/e1eaf8a28e58485fb86f16f914fd08c7?allowSelfChange=true`

## Sample Requests: /OAuth2ClientCredentials
Operation: POST`/admin/v1/OAuth2ClientCredentials`
```

```

Operation: PATCH`/admin/v1/OAuth2ClientCredentials/<id>`
```

```

Operation: DELETE`/admin/v1/OAuth2ClientCredentials/e1eaf8a28e58485fb86f16f914fd08c7?allowSelfChange=true`

## Sample Request: /SupportAccounts
Operation: POST`/admin/v1/SupportAccounts`
```

```

Operation: DELETE`/admin/v1/ApiKeys/e1eaf8a28e58485fb86f16f914fd08c7?allowSelfChange=true`
