# OAuth 2.0 Client Credentials for Roving Edge Infrastructure Devices
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/OAuth_2.0/oauth2-credential_management.htm
- Fetched: 2026-09-05 03:00 CDT

# OAuth 2.0 Client Credentials for Roving Edge Infrastructure Devices

Describes how to manage OAuth 2.0 client credential tasks for users on your Roving Edge Infrastructure devices.

You can perform the following OAuth 2.0 client credentials management tasks:
- 

[Listing OAuth 2.0 Client Credentials for a Roving Edge Infrastructure Device](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/OAuth_2.0/list_oauth2-credential.htm#ListOAuthCredential)
- 

[Getting an OAuth 2.0 Client Credential's Details for a Roving Edge Infrastructure Device](https://docs.oracle.com/en-us/iaas/Content/Rover/IAM/User_Credentials/OAuth_2.0/get_oauth2-credential.htm#ListOAuthCredential)

The single default OAuth 2.0 client credential "UI-console-oauth-credential" is generated when a user is added. This client credential is required for the user to login to a Device Console.

You can view this entry in the list of OAuth 2.0 client credentials under the within the Details page of a user resource and view its details. You cannot update or delete this credential, nor can you create additional ones for the user.

You need the following information from the OAuth 2.0 client credential for the token request:
- The generated secret
- The OCID of the OAuth 2.0 client credential
- The scope and audience (fully-qualified scope)

See[Working with OAuth 2.0 Client Credentials](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm#oauth)
