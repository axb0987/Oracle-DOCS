# Can't Connect to Bitbucket Server
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/bitbucket-cant-connect.htm
- Fetched: 2026-09-05 02:57 CDT

# Can't Connect to Bitbucket Server

Troubleshoot connection issues to Bitbucket servers while working with Resource Manager.

Can't connect to Bitbucket Server .

This issue can occur in the following situations:
- Creating a[Bitbucket Server configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-csp-bb-server.htm).
- [Creating a stack from a Bitbucket Server configuration source provider.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-stack-bitbucket-server.htm)
- [Running a job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-job.htm)on a stack that uses a Terraform configuration stored in Bitbucket Server .
- Receiving an error message when[confirming accessibility to a configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/validate-connection-csp.htm).

## Cause: The access token was revoked

## Remedy: Re-create the access token

Re-create the access token, ensuring that the token scope includes required permissions. See the relevant Bitbucket documentation:[https://confluence.atlassian.com/bitbucketserver/http-access-tokens-939515499.html](https://confluence.atlassian.com/bitbucketserver/http-access-tokens-939515499.html)

## Cause: The required permission scopes changed and are insufficient

## Remedy: Re-create the access token

Re-create the access token, ensuring that the token scope includes required permissions. See the relevant Bitbucket documentation:[https://confluence.atlassian.com/bitbucketserver/http-access-tokens-939515499.html](https://confluence.atlassian.com/bitbucketserver/http-access-tokens-939515499.html)

## Cause: The Bitbucket Server repository permissions changed or are insufficient

## Remedy: Use admin or owner
Ensure that the Bitbucket Server repository permissions meet requirements (admin or owner).

## Cause: The Bitbucket server isn't accessible over the internet

## Remedy: Use port 443
Ensure that the server runs on port 443. Resource Manager only allows HTTPS traffic through port 443.
Note  
  
By default, Bitbucket Server uses port 7990 for HTTP traffic and port 8443 for HTTPS traffic.

## Remedy: Confirm that you can view the access token

- Ensure that the access token is stored as a secret in a[vault](https://docs.oracle.com/iaas/Content/KeyManagement/home.htm).
- Ensure that you have the correct[policies](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm#permissions)to view the secret from the specified vault.

## Remedy: For a public server, use a public IP address
Ensure that the Bitbucket server uses a[public IP address](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).

## Remedy: For a private server, use a certificate and private endpoint

Note  
  
Ensure that the certificate in the Certificates service matches the certificate on the Bitbucket server.
- 

For certificate instructions, see[Creating a Certificate](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-csp-bb-server.htm#create-cert)and[Importing an Existing Certificate](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-csp-bb-server.htm#import-cert).
- For private endpoint instructions, see[Creating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-private-endpoints.htm).
- For high-level instructions on private servers, see[Private Git Server](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/private-endpoints.htm#private-git).

## Remedy: Ensure that the Bitbucket server meets all prerequisites
See[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-csp-bb-server.htm#prereqs)
