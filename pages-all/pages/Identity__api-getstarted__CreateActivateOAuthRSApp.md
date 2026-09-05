# Creating and Activating an OAuth Resource Server
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/CreateActivateOAuthRSApp.htm
- Fetched: 2026-09-05 02:17 CDT

# Creating and Activating an OAuth Resource Server

This section provides example requests to create and activate an OAuth Resource Server using the identity domains REST API.

## Create an OAuth Resource Server App

A resource server application is a third-party application that provides services that a web application can consume on behalf of the user. The example below shows how to craft a request to create an OAuth Resource application.
Note  
  
If you're using the optional`name`attribute in your request, be sure to use only alphanumeric characters and the underscore ( _ ) character in the value.
```

```

Required App Attributes for an OAuth Resource Server App

Required App Attribute Description
`displayName`Identifies the display name of the application. Display name is intended to be user-friendly, and an administrator can change the value at any time.
`basedOnTemplate`Indicates the application template on which the application is based.
`isOAuthResource`If set to`true`, indicates that this application acts as an OAuth Resource.
`audience`Identifies the base URI for all the scopes defined in this App. The value of`audience`is combined with the`value`of each scope to form an`fqs`(fully-qualified scope).

## Activate an OAuth Resource App

Use the following example to create a request to activate an OAuth Resource Server application.
```

```
