# Managing Custom Claims
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/custom-claims-token.htm
- Fetched: 2026-09-05 02:17 CDT

# Managing Custom Claims

You can use the identity domains REST API to add custom claims to an access token, an identity token, or both the tokens.

Custom claims are rules that you can add to a token for the identity domain. There's no limit for the number of custom claims in a token. Token size is limited and the allowed values are "8000", "16000","32000", "128000".
The cURL command examples use the URL structure:
```

```

- Specify the headers on the cURL command line:

```

```

To obtain an access token, see[Working with OAuth 2 to Access the REST API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OATOAuthClientWebApp.htm).
- Create the custom claim name`MyATCustomClaim`and value`MyATValue`for the access token by running the following command:

```

```

Example
```

```

The following is an example of a JSON request body to create the custom claim:
```

```

Attribute

Description

`name`

The custom claim name.

Note: Maximum length is 100 characters.

`value`

The custom claim value.

Note: Maximum length is 100 characters. If the value comes from the evaluation of a user expression, then there's no limit.

`expression`

Specify if the custom claim value is a user expression. You can determine the user expression by using the Users endpoints.

Value:`true`or`false`

Example User Expression
- `$user.name.formatted expression`with value`admin opc`.
- `$user.emails.0.type`expression with value`recovery`.
- `$user.emails.1.type`expression with value`work`.
- `$user.urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User.myCustomAttribute`expression with value`customValue`.
Based on user expressions, a claim returns either a single value attribute or all the attributes associated with the expression. For example, the following expressions return a single value within an array:
- `$user.emails.0.value`
- `$(user.emails[0].value)`
While the following expressions return an array:
- `$user.emails.*.value`
- `$(user.emails[*].value)`

`allScopes`

Specify whether associate the custom claim with a set of scopes or all the scopes.

Value:`true`or`false`

`mode`Specify how you want to attach the custom claim to a token.
- `always`: The custom claim will be attached to the token.
- `request`: The custom claim will be attached to the token only if it's requested or overridden.
- `never`: The custom claim will not be attached to the token.

`tokenType`
Specify the token type.
- `AT`: To add custom claim for an access token.
- `IT`: To add custom claim for an identity token.
- `BOTH`: To add custom claim for the access and identity token.

scopes

Optional. The Custom Claim will be embedded to tokens if any scope in the scopes array is requested in the token request. You can either specify`allScopes`equals to`true`with no associated scopes array or has`allScopes`equals to`false`with associated scopes array.

The following shows an example of the response body:
```

```

You can derive the user expression from the`/admin/v1/Users`endpoint. This is the JSON returned for an admin user.

The values are parsed as String, and the bold in the sample shows how the values are derived for the following expressions.

Expression

Value

`$user.name.formatted`

"admin opc"

`$user.emails.0.type`

This expression and the next are an unlabeled array, with a number that starts from 0 to indicate the index of the element in the array.

"recovery"

`$user.emails.1.type`

"work"

`$user.urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User.myCustomAttribute`

"customValue"
```

```

- Replace all the attributes for the custom claim id`ddc7f88bea2a46258c593bddccaf2b86`by running the following command:

```

```

Example
```

```

The following shows an example of the request body.
```

```

The following shows an example of the response indicating the request succeeded.
```

```

- Set the`allScopes`to`false`for the id`ddc7f88bea2a46258c593bddccaf2b86`by running the following command:

```

```

Example
```

```

The following shows an example of the request body.
```

```

The following shows an example of the response indicating the request succeeded.
```

```

- View all the custom claims in the tenant by running the following command:

```

```

Example
```

```

The following shows an example of the response body.
```

```

- View the custom claims in a tenant by providing the query parameter.

```

```

Example
```

```

The following shows an example of the response body after providing the query parameter`?attributes=name,value`:
```

```

- Optionally, delete the custom claim from the tenant by running the following command:

```

```

Example
```

```
