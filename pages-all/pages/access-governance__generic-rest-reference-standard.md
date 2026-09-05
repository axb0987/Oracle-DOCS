# Generic REST Reference (Standard UI Driven)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/generic-rest-reference-standard.htm
- Fetched: 2026-09-05 03:14 CDT

# Generic REST Reference (Standard UI Driven)

Let's see a few REST API examples to configure for the orchestrated system.

## Create Account API Request Response

To configure Create Account API, use the following example:

### Create Account API Details

- Name: Create User
- Method: POST
- URL:`<target-system>/admin/v1/Users`
- Headers
- `Content-Type`:`application/json`
- `Authorization`:`<<CREDENTIALS>>`. The value`<<CREDENTIALS>>`is resolved at runtime using OCI Vault or User entered credentials configured in[Integration Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#oracle-grest-integrationsettings).
- Request Body for REST API

The`schemas`attribute shown in the example:
```

```

- Response
```

```
This API creates a target account and maps the returned identifier to the`uid`attribute.

## Group Search API

### Group Search Account API Details

- Name: Group Search (Permission)
- Method: POST
- URL:`<target-system>/admin/v1/Groups/.search`
- Headers
- `Content-Type`:`application/json`
- `Authorization`:`<<CREDENTIALS>>`. The value`<<CREDENTIALS>>`is resolved at runtime using OCI Vault or User entered credentials configured in Integration Settings.
- Request Body for REST API

Include the`schemas`attribute shown in the example:
```

```

- Response

Using the JSON Editor, use the following response:
```

```

## Country Lookup API

- Name: Search Countries
- Method: GET
- URL:`<target-system>/admin/v1/AllowedValues/countries`
- Headers
- `Content-Type`:`application/json`
- `Authorization`:`<<CREDENTIALS>>`. The value`<<CREDENTIALS>>`is resolved at runtime using OCI Vault or User entered credentials configured in Integration Settings.
- Response

Using the JSON Editor, use the following response:
```

```

## Add Group Membership API

- Name: Add Group Membership
- Method: PATCH
- URL:`<target-system>/admin/v1/Groups/<EL>attributes.get('groups').get('uid').get(0)</EL>`
- Headers
- `Content-Type`:`application/json`
- `Authorization`:`<<CREDENTIALS>>`. The value`<<CREDENTIALS>>`is resolved at runtime using OCI Vault or User entered credentials configured in Integration Settings.
- Request

Use the following request:
```

```

- Response
Using the JSON Editor, use the following response:
```

```

Or, use the JSON Editor
```

```

## Delete Account API

- Name: Delete Account API
- Method: DELETE
- URL:`<target-system>/admin/v1/Users/<EL>attributes.get('uid').get(0)</EL>`
- Headers
- `Content-Type`:`application/json`
- `Authorization`:`<<CREDENTIALS>>`. The value`<<CREDENTIALS>>`is resolved at runtime using OCI Vault or User entered credentials configured in Integration Settings.
- Parameter : forceDelete: true
- Response

Use the following response:
```

```

Or, use the JSON Editor
```

```

## Change Password API Request Response

The following example shows how to configure a Change Password API for an account. The Change Password API option is available when the`__PASSWORD__`system attribute is configured for the account.

- Name: Change Password
- Method: PUT
- URL:`<target-host>/admin/v1/UserPasswordChanger/<EL>attributes.get('uid').get(0)</EL>`
- Headers
- `Content-Type`:`application/json`
- `Authorization`:`<<CREDENTIALS>>`. The value`<<CREDENTIALS>>`is resolved at runtime using OCI Vault or User entered credentials configured in Integration Settings.
- Request

Use the following JSON request:
```

```
Or, use the JSON editor to configure the Change Password API
```

```
The URL and request body depend on the Change Password API exposed by the target application.

## Response Validation

You can define a response validation expression for APIs to validate the business use cases and decide whether a`2xx`response represents a successful operation.

Response validation checks the response body in addition to the HTTP status code

For example, consider a Create Account API that returns the following response:
```

```

To verify that the username returned by the target application matches the account name in the request, specify the following in Response validation expression:
```

```
After the execution of the operation, response validation expression is evaluated. If the expression returns`success`
