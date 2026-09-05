# Using Access Token Authorization with My Services API
- Source: https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/usingoauth.htm
- Fetched: 2026-09-05 02:11 CDT

# Using Access Token Authorization with My Services API

Important  
  
The My Services dashboard and APIs are deprecated.

This topic explains how to set up and use access token authorization with the Oracle Cloud My Services API. Access token authorization allows a developer to access programmatic endpoints (APIs) to obtain some information (for example, entitlements, instances, or metering data) for your cloud account.

## About Access Tokens

An access token contains the information required to allow a developer to access information on your cloud account. A developer presents the token when making API calls. The allowed actions and endpoints depend on the scopes (permissions) that you select when you generate the token. An access token is valid for about an hour.

A refresh token allows the developer to generate a new access token without having to contact an administrator. A refresh token is valid for about one year.

## Process Overview

Setup steps for the Administrator:
- Create an Identity Cloud Service client application with the specific privileges you want to grant to developers.
- Generate an access token that contains the required privileges for the intended developer.
- Provide the access token and required information to the developer.
- Configure Identity Cloud Service for access token validation.

Steps for developer to use the token:
- Issue requests against My Services API endpoints. Include the access token for the authorization parameter.
- When the access token expires, refresh the access token without administrator intervention until the privilege is terminated.

## Administrator Tasks to Set Up Token Validation

Perform the following tasks to enable developer access with an access token:

[Create the IDCS client application](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/usingoauth.htm#)

- Sign in to Identity Cloud Services as an Administrator and go to the administration console. See[How to Access Oracle Identity Cloud Service](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/how-access-oracle-identity-cloud-service.html)if you need help signing in.
- Click the Applications tile. A list of the applications is displayed.
- Click + Add to create a new application.
- Click Confidential Application as the type of application.
- In the App Details section, enter a Name and Description . Avoid entering confidential information.
- Click Next .
- 

In the Client section:
- Select Configure this application as a client now .
- Under Authorization , for Allowed Grant Types , select the following options:
- JWT Assertion
- Refresh Token
- 

Under Token Issuance Policy , under Resources , click Add Scope .
- 

In the Select Scope dialog, select CloudPortalResourceApp and click the arrow to select scopes for the resource.
- 

Select the box next to each authorization that you might want to give the developers to whom you will provide an Access Token. (The permissions are assigned in another step.)
- 

Click Add to close the dialog. Your selections are displayed.
- 

Click Next .
- In the Resources section, accept the default and click Next .
- In the Web Tier Policy section, accept the default and click Next .
- 

In the Authorization section, click Finish .

The Application Added notification displays the new Client ID and Client Secret for the application.
Important  
  
Copy and store the Client ID and Client Secret in a safe place and then click Close . The Client ID and Client Secret are credentials that are specific to the application that you just created. You will need these credentials later.
- To complete the creation process, click Activate at the top of the page.

[Generate an access token](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/usingoauth.htm#)

- 

Navigate to the IDCS application that you created in the preceding task and select the Details tab.
- 

Click Generate Access Token .
- 

On the Generate Token dialog, select Customized Scopes , then select Invokes Other APIs .
- 

Select the scopes that you want to give to the developer who will receive this access token.
Note  
  
Oracle recommends that you provide only the minimum required privileges.
- 

Select Include Refresh Token .
- 

Click Download Token . Your browser will prompt you to download a token file (.tok). The token file contains an access token and a refresh token.
- Provide this file to the developer.

[Send the access information to a developer](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/usingoauth.htm#)

To call API endpoints, the developer needs:
- 

A token file that you generated.
- 

The Client ID and Client Secret for the IDCS application used to generate the token file. The Client ID and Secret are required for the developer to generate a new access token from the refresh token.
- 

The endpoints for the APIs.
- End points related to the itas:myservices scopes are:`https://itra.oraclecloud.com/itas/ <tenant-IDCS-ID> /myservices/api/v1`
- End points related to the itas:metering scopes are:`https://itra.oraclecloud.com/metering/api/v1`

Make sure that you send the above information in a secure way. If you think that this information has been compromised, see[Revoking a Developer's Ability to Refresh Access Tokens](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/usingoauth.htm#revoke).

[Configure Identity Cloud Service for access token validation](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/usingoauth.htm#)

To allow clients to access the tenant signing certificate without logging in to Oracle Identity Cloud Service:
- Sign in to the Oracle Identity Cloud Services admin console. See[How to Access Oracle Identity Cloud Service](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/how-access-oracle-identity-cloud-service.html)if you need help signing in.
- Open the navigation menu. Under Settings select Default Settings .
- Set the Access Signing Certificate toggle button to on.

## Using the Access Token

The token file has a .tok extension. The file contains the access token and the refresh token. The content looks like:
```

```

To use the token with the My Services API:
- Open the token file.
- 

Issue a request to a valid endpoint, inserting the access token for the`Authorization`parameter.

For example:

```

```

### Requesting a New Access Token from a Refresh Token

An access token is valid for about one hour. When the token is no longer valid you will get a 401 response code and an Error Message ("errorMessage") value containing "Expired."

You can generate a new short-lived access token from the refresh token. You'll need the Client ID and Client Secret to generate the new token. You can only generate tokens with the same or lower access (scopes) as your original token.

Example using the curl command:

```

```

Using the sample token file from the previous section, the value for &lt;refresh-token&gt; would be`AQID...9NCA=`.

Sample response:

```

```

Note  
  
When a developer generates a new access token and refresh token, the previous refresh token becomes invalid.

## Revoking a Developer's Ability to Refresh Access Tokens

If you need to revoke a developer's ability to refresh access tokens, you can either invalidate the existing refresh token by generating a new Client Secret for the token; or, you can temporarily revoke access by deactivating the application.
Important  
  
Taking either of these actions will terminate or suspend the ability of all developers using the current Client Secret or application. When generating tokens for multiple developers, consider creating more than one IDCS application to isolate developers from each other.

To terminate a developer's ability to refresh their access token
- Sign in to Identity Cloud Services as an Administrator and go to the administration console. See[How to Access Oracle Identity Cloud Service](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/how-access-oracle-identity-cloud-service.html)if you need help signing in.
- Click the Applications tile. A list of the applications is displayed.
- Click the application used to generate the token to view its details.
- Click Configuration .
- Under General Information , next to Client Secret , click Regenerate to generate a new Client Secret.

To restore the ability for the developer to generate an access token from a refresh token,[generate a new access token](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/usingoauth.htm#Generate). Then[provide the token](https://docs.oracle.com/en-us/iaas/Content/General/MyServices/Tasks/usingoauth.htm#Send)along with the new Client Secret to the developer.

To temporarily suspend a developer's ability to refresh their access token
- Sign in to Identity Cloud Services as an Administrator and go to the administration console. See[How to Access Oracle Identity Cloud Service](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/how-access-oracle-identity-cloud-service.html)if you need help signing in.
- Click the Applications tile. A list of the applications is displayed.
- Click the application used to generate the token to view its details.
- In the upper right corner of the page, click Deactivate .
- At the prompt, click Deactivate Application .
