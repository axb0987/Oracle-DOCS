# Updating a Bitbucket Cloud Configuration Source Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-bb-cloud.htm
- Fetched: 2026-09-05 02:56 CDT

# Updating a Bitbucket Cloud Configuration Source Provider

Update a Bitbucket Cloud configuration source provider in Resource Manager.

Important  
  
In 2025, Atlassian announced the deprecation of app passwords in favor of API tokens for REST API authentication. If any existing Bitbucket Cloud configuration source providers still use app passwords, you must update them to instead use an Atlassian account email address together with an API token. See[API tokens](https://support.atlassian.com/bitbucket-cloud/docs/api-tokens/).

When you update a configuration source provider, you can also update its tags. For instructions, see[Updating a Tag for a Single Resource](https://docs.oracle.com/iaas/Content/General/Tasks/resourcetags-updating-tags-single-resource.htm). For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-bb-cloud.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-bb-cloud.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-bb-cloud.htm#)
- 

- On the Configuration source providers list page, select the configuration source provider that you want to work with. If you need help finding the list page or the configuration source provider, see[Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-csp.htm).
- On the configuration source provider's details page, select Edit .
- To change the connection details, in the Edit configuration source provider panel, edit one or more of the following values:

- To use a different[private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/private-endpoints.htm#private-git), select the endpoint and then select an SSL certificate. This option is available when the configuration source provider was created with a private endpoint.
- Server URL : The Bitbucket Cloud service endpoint. Example:[https://bitbucket.org/](https://bitbucket.org/)
- Email : Atlassian account email used with the Bitbucket Cloud API token.
- Vault :[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/home.htm)where the secret is stored.
- Secret :[Secret](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm)for authorization.
Note  
  
The secret contains the Bitbucket Cloud API token, not an app password.
- Optionally change the compartment, name, or description.
- Select Save changes .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/configuration-source-provider/update-bitbucket-cloud-email-api-token-provider.html)oci resource-manager configuration-source-provider update-bitbucket-cloud-email-api-token-provider`command and required parameters to update a configuration source provider from Bitbucket Cloud .

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Run the[UpdateConfigurationSourceProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider/UpdateConfigurationSourceProvider)operation to update a configuration source provider that uses Bitbucket Cloud .

For an example of the`configSourceProviderType`part of the request, see[UpdateBitbucketCloudEmailApiTokenConfigurationSourceProviderDetails Reference](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/UpdateBitbucketCloudEmailApiTokenConfigurationSourceProviderDetails)
