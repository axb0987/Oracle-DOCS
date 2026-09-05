# GET, POST, PUT, PATCH Request and Response Examples
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OCISRequestBody.htm
- Fetched: 2026-09-05 02:17 CDT

# GET, POST, PUT, PATCH Request and Response Examples

`GET`,`POST`,`PUT`, and`PATCH`requests and responses require a JSON request body.

## GET Request and Response Example

The following is an example of a JSON request body used with a`GET`method to list a user, and the response.

Request:
```

```

Response:
```

```

## POST Request and Response Example

The following is an example of a JSON request body used with a`POST`method to create a new user, and the response.

Request:

```

```
Response:
```

```

## PUT Request and Response Example

The following is an example of a JSON request body used with a`PUT`method to replace user information, and the response.

Request:
```

```

Response:
```

```

## PATCH Request and Response Example

The following is an example of a JSON request body used with a`PATCH`method to amend user information, and the response.

Request:

```

```
Response:
```

```

Note  
  

- 

The`schemas`attribute is set to the schema collection that corresponds with the resource. For example,`urn:ietf:params:scim:schemas:core:2.0:User`, corresponds with`/Users`. See[SCIM Schema Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OCISSchema.htm).
-
