# Use Case: Adding Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/use-case-adding-applications.htm
- Fetched: 2026-09-05 02:19 CDT

# Use Case: Adding Applications

To understand how to add custom applications in an identity domain, read this use case.

[

For this use case, a user accesses the Customer Quotes trusted application. This trusted application is a client application that makes REST API calls to the`abccorp.com`resource server application. A resource server application is a third-party application that provides services that a trusted application can consume on behalf of the user.

For this example, the`abccorp.com`resource server application is a financial application that contains REST APIs that can be used to make a quote (`/quote`), request for a quote (`/rfq`), or get information about the user (`/user`).

When the user accesses the Customer Quotes trusted application, the application makes REST API calls to the`abccorp.com`resource server application on behalf of the user. In this example, the user doesn't communicate directly with the`abccorp.com`application.

Because the Customer Quotes application performs actions on behalf of the user, the application needs access to the`/quote`,`/rfq`, and`/user`REST APIs available with the`abccorp.com`application. To make these REST API calls, the Customer Quotes application might ask for the user's consent. This consent can come at any time that the Customer Quotes application calls for these REST APIs in the`abccorp.com`application.

The user logs in to IAM and accesses the Custom Quotes application, through single sign-on, by using OAuth 2.0 and OpenID Connect, as this is a way of federating identities in the cloud. Because the Customer Quotes application is authorized on behalf of the user to make the`/quote`,`/rfq`, and`/user`REST API calls to the`abccorp.com`application, the user can use the Customer Quotes application to make a quote, request for a quote, and get information about the user. Any additional actions that the user wants to perform through the Customer Quotes application isn't allowed.
To build this workflow, you create and activate two custom applications in IAM:
- 

The`abccorp.com`resource server application. This application has REST APIs (resources) that other applications, such as the Customer Quotes application, can access. In this example, the user doesn't access the resource server application directly, but indirectly through the Customer Quotes application.

You register resources of the`abccorp.com`resource server application. Application resources are API calls that are authorized by IAM. For this example, the application resources are the`/quote`,`/rfq`, and`/user`REST APIs. For security and auditing purposes, you can specify whether the user must give consent to access these resources.
- 

The Customer Quotes trusted application. The user uses this application to access the REST APIs of the`abccorp.com`application.

When you create this custom application, you want to generate an authorization code for the user when the user logs in to IAM. The authorization code is then sent to the Customer Quotes application to retrieve an access token. The access token contains all the rights that the user has to access the resource server application. For this example, these rights include making a quote, requesting a quote, and retrieving information about the user.

Because the access token's lifetime is short, you might want to generate a refresh token. A refresh token is a secure mechanism to obtain a new access token when the current access token expires. This way, the Customer Quotes application can access the APIs of the`abccorp.com`application without asking for user consent again.

See[Add Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-applications.htm),[Activate Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/activate-applications.htm), and[Deactivate Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/deactivate-applications.htm)
