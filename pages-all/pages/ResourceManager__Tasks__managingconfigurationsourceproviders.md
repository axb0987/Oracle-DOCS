# Managing Configuration Source Providers
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm
- Fetched: 2026-09-05 02:56 CDT

# Managing Configuration Source Providers

Remotely store Terraform configurations using configuration source providers in Resource Manager.
Note  
  
For remote Terraform configurations in DevOps, see[Creating a Stack from DevOps](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-devops.htm).

You can perform the following management tasks with configuration source providers:
- [Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-csp.htm)
- [Creating a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-csp.htm)
- [Creating a Bitbucket Cloud Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-csp-bb-cloud.htm)
- [Creating a Bitbucket Server Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-csp-bb-server.htm)
- [Creating a GitHub Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-csp-github.htm)
- [Creating a GitLab Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-csp-gitlab.htm)
- [Creating a Stack from a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-stack-from-csp.htm)
- [Creating a Stack from Bitbucket Cloud](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-stack-from-csp-bitbucket-cloud.htm)
- [Creating a Stack from Bitbucket Server](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-stack-from-csp-bitbucket-server.htm)
- [Creating a Stack from Git](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-stack-from-csp-git.htm)
- [Getting a Configuration Source Provider's Details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/get-csp.htm)
- [Updating a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/update-csp.htm)
- [Updating a Configuration Source Provider (Any Type)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/update-csp-basic.htm)
- [Updating a Bitbucket Cloud Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/update-csp-bb-cloud.htm)
- [Updating a Bitbucket Server Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/update-csp-bb-server.htm)
- [Updating a GitHub Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/update-csp-github.htm)
- [Updating a GitLab Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/update-csp-gitlab.htm)
- [Validating the Connection for a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/validate-connection-csp.htm)
- [Moving a Configuration Source Provider to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/change-compartment-csp.htm)
- [Deleting a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/delete-csp.htm)

## Required IAM Policy

Use policies to grant access to configuration source providers in Resource Manager.

To manage configuration source providers, you must be given the required type of access in a policy written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. To create a configuration source provider, you need`manage orm-config-source-providers`. To create a stack with an existing configuration source provider, you need`manage orm-stacks`and`read orm-config-source-providers`. If you're new to policies, see[IAM Policies Overview](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm).

Administrators: For common policies that give groups access to configuration source providers in Resource Manager, see[Manage Configuration Source Providers (Securing Resource Manager)](https://docs.oracle.com/iaas/Content/Security/Reference/resourcemanager_security.htm#iam-policies__csp).

## Supported Products

Review the products supported for configuration source providers in Resource Manager.
Note  
  
For product-specific prerequisites, see the product-specific instructions for creating configuration source providers. For example, for GitHub, see[Creating a GitHub Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm).

[Submodules](https://git-scm.com/book/en/Git-Tools-Submodules)are supported. When accessing a Terraform configuration in a repository with submodules, as when running an apply job on a stack that uses a configuration source provider in Git, Resource Manager recursively clones the repository.

A configuration source provider can be one of the following types:
- Bitbucket
- GitHub
- GitLab

Following are the supported products for each type of configuration source provider.
- Bitbucket:
- Bitbucket Cloud
- Bitbucket Server
- GitHub:
- [GitHub Enterprise](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/githubs-products#github-enterprise)
- GitHub Enterprise Server
- GitHub Enterprise Cloud
- [GitHub Free for organizations](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/githubs-products#github-free-for-organizations)
- [GitHub Free for user accounts](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/githubs-products#github-free-for-user-accounts)
- [GitHub Team](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/githubs-products#github-team)
- GitLab:
- GitLab Community Edition
- GitLab Enterprise Edition
- GitLab.com

## Example Server URLs

[Bitbucket Cloud](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-cloud.htm):
- `https://bitbucket.org/`

[Bitbucket Server](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm):
- `my-private-bitbucket-server.example.com`

[GitHub](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm):
- GitHub Enterprise Cloud:`https://github.com/org-name`
- GitHub Enterprise Server:`https://hostname/api/v3`
- GitHub Free for Organization:`https://github.com/org-name`
- GitHub Free for User Accounts:`https://github.com`
- GitHub team:`https://github.com/team-name`

[GitLab](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-gitlab.htm):
- GitLab.com product:`https://gitlab.com/`
- GitLab installation (relative URL):`https://example.com/gitlab`
- GitLab installation (subdomain):`https://gitlab.example.com/`

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
