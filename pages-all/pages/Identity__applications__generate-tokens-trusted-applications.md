# Generating Tokens for Confidential Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/generate-tokens-trusted-applications.htm
- Fetched: 2026-09-05 02:19 CDT

# Generating Tokens for Confidential Applications

When you create a confidential application and you configure the client to use the JWT assertion grant type, you can generate access tokens at any time using the identity domain Console.

Before You Begin:

Create an confidential application with the client configured to use the JWT assertion grant type and activate it. See[Adding a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-confidential-application.htm).

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/../domains/to-view-identity-domains.htm).
- On the details page, select Integrated applications . A list of applications in the domain is displayed.
- Select the confidential application that's configured to use the JWT Assertion grant type.
- Select either the Access token .
- Use the following table to configure which scopes are included in the access token:

Option Description
Available scopes

Select Available scopes to get the access token to access any resources configured for the application.

If the scopes are defined from multiples resource servers, the token can't be generated. Use the Customized scopes option and ensure that the selected scopes are from the same resource server.
Customized scopes using Invokes identity domain APIs

- 

Select Customized scopes and Invokes identity domain APIs .
- 

From the list of roles that are assigned to the client application, select those roles that you want to include or remove to limit the scopes to be populated in the resulting token.
Customized scopes using Invokes other APIs

- 

Select Customized scopes and Invokes other APIs .
- 

The UI displays a list of all the scopes assigned to the application. You can select any scopes as long as those scopes are from the same resource server.
Include refresh token

The Include refresh token checkbox is enabled if the Refresh token grant type is configured for your client application and the resource server to which the scopes belong to allows refresh token generation. The refresh token is used to obtain a new access token without requiring the user to reauthenticate.
- Select Download token .

Note  
  
The downloaded token gets saved as a`tokens<n>.tok`
