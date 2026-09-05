# Creating a Bitbucket Cloud Configuration Source Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-cloud.htm
- Fetched: 2026-09-05 02:54 CDT

# Creating a Bitbucket Cloud Configuration Source Provider

Create a configuration source provider in Resource Manager from Bitbucket Cloud .

## Before You Begin

To connect Oracle Cloud Infrastructure Resource Manager to a Bitbucket Cloud repository, you must first create a Bitbucket Cloud API token with read scope (limited permissions).

See[API token permissions](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/).

When creating the API token:
- Use your Atlassian account email for Bitbucket API authentication.
- Store the API token in an OCI Vault secret.
- Recommended scope:`read:repository:bitbucket`.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-cloud.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-cloud.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-cloud.htm#)
- 

After completing all the prerequisites, follow these steps in the Console to create a configuration source provider from Bitbucket Cloud .

- On the Configuration source providers list page, select Create configuration source provider . If you need help finding the list page or the configuration source provider, see[Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-csp.htm).
- In the Create configuration source provider panel, enter a name and optional description for the configuration source provider. Avoid entering confidential information.
- Select the compartment that you want to store the configuration source provider in.
- (Optional) To use a[private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/private-endpoints.htm), follow these steps:
- Select Private endpoint .
- Select or create a private endpoint. To select a private endpoint or certificate in a different compartment, select Change Compartment .
- Select an SSL certificate.
For more information about private endpoints for private servers, see[Private Git Server](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/private-endpoints.htm#private-git).
- For Type , select Bitbucket Cloud .
- Enter the following values:

- Server URL : The Bitbucket Cloud service endpoint. Example:[https://bitbucket.org/](https://bitbucket.org/)
- Email : Atlassian account email used with the Bitbucket Cloud API token.
- Vault :[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/home.htm)where the secret is stored.
- Secret :[Secret](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm)for authorization.
Note  
  
The secret contains the Bitbucket Cloud API token, not an app password.
- (Optional) Add one or more tags to the configuration source provider: Select Show advanced options to show tagging options.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .
- To confirm that Resource Manager can access the server URL using the provided authentication information, select the configuration source provider to open its details page, and then select Validate connection .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/configuration-source-provider/create-bitbucket-cloud-email-api-token-provider.html)oci resource-manager configuration-source-provider create-bitbucket-cloud-email-api-token-provider`command and required parameters to create a configuration source provider from Bitbucket Cloud .

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Run the[CreateConfigurationSourceProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider/CreateConfigurationSourceProvider)operation to create a configuration source provider from Bitbucket Cloud .

For an example of the`configSourceProviderType`part of the request, see[CreateBitbucketCloudEmailApiTokenConfigurationSourceProviderDetails Reference](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateBitbucketCloudEmailApiTokenConfigurationSourceProviderDetails).

## What's Next

[Validating the Connection for a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/validate-connection-csp.htm)
