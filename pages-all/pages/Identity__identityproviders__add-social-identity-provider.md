# Adding a Social Identity Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/add-social-identity-provider.htm
- Fetched: 2026-09-05 02:22 CDT

# Adding a Social Identity Provider

Add a social identity provider (IdP) so that users can sign in to an identity domain in IAM with their social credentials.
Configure the IdP to redirect to IAM.
- 

Create an application for the social IdP.

For example, go to the Google developer site to create a Google application. Store the Client ID and the Client secret values in a safe place. Make sure the Client ID and the Client secret values from the application that you created at the social IdP. You use this ID and this secret when configuring the social IdP in the identity domain.
- 

Configure the value of`redirectUrl`in the application.

The value of`redirectUrl`must have the following format:

```

```

Note  
  

Ensure the value of redirectUrl doesn't contain the port number`:443`. If it does, either update the existing URL to remove the port number or add a new URL without the port number to the IdP application using the external provider's developer website.
Each social IdP calls these redirect URLs by a different name:
- 

Apple ID: Return URLs
- 

Facebook: Valid OAuth redirect URIs
- 

Google and LinkedIn: Authorized redirect URL
- 

Microsoft: Redirect URLs
- 

OpenID Connect: redirect_uri
- 

X (formerly Twitter): Callback URL

To add a social identity provider

- On the Identity providers list page, add a social identity provider. If you need help finding the list page, see[Listing Identity Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/list-identity-providers.htm#console).
- Select the Actions menu and then select Add Social IdP .
- Select the social identity Type .
Make sure you have the Client ID and the Client secret values from the application that you created at the social IdP. You use this ID and secret when configuring the social IdP in the identity domain.

The following lists the available social providers:
- 

Apple
Note  
  
For information about adding an Apple identity provider, see[Adding an Apple Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/integrating-apple-idp.htm).
- 

Facebook
- 

Google
- 

LinkedIn
- 

Microsoft
- 

OpenID Connect
- 

X (formerly Twitter)
- In the Name and Description fields, enter a name and description for the social identity provider.

Note  
  
The social identity provider name can contain spaces. However, it can't contain special characters. Avoid entering confidential information.
- Enter the client ID and the client secret for the social login type.
- In general you enter the Client ID and the Client secret for the social login type.
- For Apple, enter the Apple developer ID and the Apple private key ID .
- For OpenID Connect, enter the Discovery service URL .
- (Optional) To allow users to link their social accounts, select the Enable account linking checkbox. To prevent users from linking their social accounts, clear the checkbox.

Note  
  
You can prevent users from linking to their social accounts for security or organizational purposes. For example, if a hacker accesses the user's social account, the hacker can't sign in to the identity domain to access resources and applications.
- (Optional) Enable social autoRedirect.
- (Optional) Enable registration.
- (Optional) Enable Just-In-Time (JIT) provisioning.
- (Optional) Add custom attributes.
- Select Add .
- From the Actions menu (three dots) , select Activate IdP .
- Log in with the social IdP.

Note  
  

You might encounter this error message: "Not Logged In: You are not logged in. Please log in and try again."

The most likely cause is that the application you created on the social IdP side has the wrong client ID or redirect URL in the configuration. Check the client ID and the redirect URL configuration, and try to log in again.
- (Optional) Activate the IdP before adding it to any policies. For more information, see[Activating or Deactivating an Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/activate-identity-provider.htm)
