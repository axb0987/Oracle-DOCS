# Regenerating OAuth 2.0 Client Credential Secrets for Password Resetting for a Roving Edge Infrastructure Device
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/OAuth_2.0/regenerate_secret.htm
- Fetched: 2026-09-05 03:00 CDT

# Regenerating OAuth 2.0 Client Credential Secrets for Password Resetting for a Roving Edge Infrastructure Device

Describes how to regenerate the secret of an OAuth 2.0 Client Credential resource associated with a user on your Roving Edge Infrastructure device.

Note  
  

Regenerating the secret and forwarded to the user in need is a requirement for resetting a user's password.

## Using the Device Console

- Open the navigation menu and select Identity Management &gt; Users . The Users page appears. All users are listed in tabular form.
- Select the user whose secret you want to regenerate. The user's Details page appears.
- Select OAuth 2.0 Client Credentials under Resources . The OAuth 2.0 client credential's page appears. All OAuth 2.0 client credentials are listed in tabular form.
- Select Regenerate Secret under UI-console-oauth-credential . The Regenerate OAuth 2.0 Client Credential dialog box appears.
- Select Regenerate Secret .

Note  
  

If you generate a new secret for this OAuth 2.0 client credential, the previously generated secret becomes invalid and requests made with the previous secret are denied access to target scopes.
-
