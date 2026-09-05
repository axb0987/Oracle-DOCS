# Updating a GitLab Configuration Source Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-gitlab.htm
- Fetched: 2026-09-05 02:56 CDT

# Updating a GitLab Configuration Source Provider

Update a GitLab configuration source provider in Resource Manager.
When you update a configuration source provider, you can also update its tags. For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm). For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-gitlab.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-gitlab.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-gitlab.htm#)
- 

- On the Configuration source providers list page, select the configuration source provider that you want to work with. If you need help finding the list page or the configuration source provider, see[Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-csp.htm).
- On the configuration source provider's details page, select Edit .
- To change the connection details, in the Edit configuration source provider panel, edit one or more of the following values:

- To use a different[private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/private-endpoints.htm#private-git), select the endpoint and then select an SSL certificate. This option is available when the configuration source provider was created with a private endpoint.
- Server URL : The service endpoint.

Examples:
- GitLab.com product:`https://gitlab.com/`
- GitLab installation (relative URL):`https://example.com/gitlab`
- GitLab installation (subdomain):`https://gitlab.example.com/`
- Personal access token : Enter the personal access token (PAT).
- Optionally change the compartment, name, or description.
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/configuration-source-provider/update-gitlab-access-token-provider.html)oci resource-manager configuration-source-provider update-gitlab-access-token-provider`command and required parameters to update a configuration source provider from GitLab.

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Run the[UpdateConfigurationSourceProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider/UpdateConfigurationSourceProvider)operation to update a configuration source provider that uses GitLab.

For an example of the`configSourceProviderType`part of the request, see[UpdateGitlabAccessTokenConfigurationSourceProviderDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/UpdateGitlabAccessTokenConfigurationSourceProviderDetails)
