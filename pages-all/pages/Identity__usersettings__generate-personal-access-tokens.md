# Generating an Access Token
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/generate-personal-access-tokens.htm
- Fetched: 2026-09-05 02:30 CDT

# Generating an Access Token

An access token is an authorization that's used by a client application to access an API or a resource application within a limited period.

The time-bound access tokens inform the resource application that the client is authorized to access the application and perform specific actions specified by the scope that's granted.

You can download access tokens only if an identity domain administrator assigns administrator roles or resource applications to your account.

- Go to your My Profile console page. If you need help finding the My Profile console page, see[Getting Your Profile Details](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/get-details-my-profile.htm).
- Select the Tokens and keys tab and find My access tokens on the page.
- You can download an access token in the following ways:
- Select Invokes identity domains APIs to specify the available administrator roles that are assigned to you. The APIs from the specified administrator roles are included in the token.
- Select Invokes other APIs to select confidential applications that are assigned to your account.
- Select Select an application to add a configured confidential resource application. On the Select an application window, the list of assigned confidential applications displays.
- Select applications, and then select Add . The My access tokens page lists the added applications.
- In the Token Expires in mins field, select or enter how long (in minutes) the access token you're generating can be used before it expires. You can choose to keep the default number or specify between 1 and 527,040 .
-
