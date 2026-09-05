# Creating and Activating an OAuth Client App
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/CreateActivateOAuthClientApp.htm
- Fetched: 2026-09-05 02:17 CDT

# Creating and Activating an OAuth Client App

This section provides example requests to create and activate an OAuth Client App using the identity domains REST API.

## Create an OAuth Client App

An OAuth client application is an HTTP client that can acquire, and then use an access token. There are three types of OAuth client applications that you can create: Confidential, Trusted, and Public. Both the confidential and trusted client apps are specified by using`CustomWebAppTemplateId`as the value for the`basedOnTemplate`attribute. The public client app is specified by using`CustomBrowserMobileTemplateId`as the value for the`basedOnTemplate`attribute. The following examples show how to craft a request to create each of the client application types.

If you're building an OAuth Client App that supports self-service operations, the client app must be granted the "Me" role. Granting the client this role ensures that the generated access token contains the scope`"urn:opc:idm:t.user.me"`. This scope allows the client to access endpoints to perform self-service operations such as`/Me,``/MyApps`, and so on. Use the`/Grants`endpoint to grant an AppRole to an app.
Note  
  
If you're using the optional`name`attribute in your request, be sure to use only alphanumeric characters and the underscore ( _ ) character in the value.

Confidential
```

```

Trusted
```

```

Public
Note  
  
See[onBehalfOf Allowed Operation](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OnBehalfOf.htm)for more information on using this allowed operation when you create a public OAuth Client application.
```

```

Required App Attributes for an OAuth Client App

Required App Attribute Description
`displayName`Identifies the display name of the application. Display name is intended to be user-friendly, and an administrator can change the value at any time.
`basedOnTemplate`Indicates the application template on which the application is based.
`isOAuthClient`If set to`true`, indicates that this application acts as an OAuth Client.
`clientType`Specifies the type of access that this App has when it acts as an OAuth Client. The possible values are`confidential,``trusted`, and`public.`

## Activate an OAuth Client App

Use the following example to create a request to activate an OAuth Resource Server application.
```

```
