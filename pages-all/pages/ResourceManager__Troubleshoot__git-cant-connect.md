# Can't Connect to Git
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/git-cant-connect.htm
- Fetched: 2026-09-05 02:57 CDT

# Can't Connect to Git

Troubleshoot connection issues to Git servers while working with Resource Manager.

Can't connect to GitHub or GitLab.

This issue can occur in the following situations:
- Creating a[GitHub](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-csp-github.htm)or[GitLab configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-csp-gitlab.htm).
- [Creating a stack from a Git configuration source provider.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-stack-git.htm)
- [Running a job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-job.htm)on a stack that uses a Terraform configuration stored in Git.
- Receiving an error message when[confirming accessibility to a configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/validate-connection-csp.htm).

## Cause: The Personal Access Token (PAT) was revoked

## Remedy: Re-create the PAT

Re-create the Personal Access Token (PAT), ensuring that the token scope includes required permissions.
See the relevant Git documentation.
- GitHub:[https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token)
- GitLab:[https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)

## Cause: The required permission scopes changed and are insufficient

## Remedy: Re-create the PAT

Re-create the Personal Access Token (PAT), ensuring that the token scope includes required permissions.
See the relevant Git documentation.
- GitHub:[https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token)
- GitLab:[https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)

## Cause: The Git repository permissions changed or are insufficient

## Remedy: Use admin or owner
Ensure that the GitHub or GitLab repository permissions meet requirements (admin or owner).

## Cause: The Git server isn't accessible over the internet

## Remedy: For a public server, use a public IP address
Ensure that the Git server uses a[public IP address](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).

## Remedy: For a private server, use a certificate and private endpoint

Note  
  
Ensure that the certificate in the Certificates service matches the certificate on the Git server.
- 

For certificate instructions, see[GitHub](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-csp-github.htm#import-cert)and[GitLab](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-csp-gitlab.htm#import-cert).
- For private endpoint instructions, see[Creating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-private-endpoints.htm).
- For high-level instructions on private servers, see[Private Git Server](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/private-endpoints.htm#private-git).

## Remedy: Ensure that the Git server meets all prerequisites
See[GitHub](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-csp-github.htm#prereqs)and[GitLab prerequisites](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/../Tasks/create-csp-gitlab.htm#prereqs)
