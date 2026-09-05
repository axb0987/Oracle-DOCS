# Creating a Bitbucket Server Configuration Source Provider
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm
- Fetched: 2026-09-05 02:54 CDT

# Creating a Bitbucket Server Configuration Source Provider

Create a configuration source provider in Resource Manager from Bitbucket Server .

## Before You Begin

Following are the prerequisites to connect Oracle Cloud Infrastructure Resource Manager to Bitbucket Server . Private server
- Private instance
- Private IP address connected to a private domain name through a private DNS zone, using[a private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#private-git)
- Certificate. See[Creating a Certificate](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm#create-cert)and[Importing an Existing Certificate](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm#import-cert)
- Server must run over HTTPS on port 443 (certificate authority not required)

Port 443 is required for communication with Resource Manager. Port 8443 is the Bitbucket Server default. For more information on server setup, see Bitbucket Server documentation, such as the following page:[https://confluence.atlassian.com/bitbucketserver/secure-bitbucket-behind-nginx-using-ssl-776640112.html](https://confluence.atlassian.com/bitbucketserver/secure-bitbucket-behind-nginx-using-ssl-776640112.html). Public server
- Public IP address
- Server must run over HTTPS with a certificate authority; self-signed certificates aren't allowed

For more information on server setup, see Bitbucket Server documentation, such as the following page:[https://confluence.atlassian.com/bitbucketserver/secure-bitbucket-behind-nginx-using-ssl-776640112.html](https://confluence.atlassian.com/bitbucketserver/secure-bitbucket-behind-nginx-using-ssl-776640112.html). Access token
- Permissions to clone the repository and read the server information
- Stored as a[secret](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm)in a[vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults.htm)that you can access (through[policies](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm#permissions)) when creating the configuration source provider

### Creating a Certificate

Create a server certificate, certificate chain, and private key for a private Bitbucket server.

- Note the passphrase to use for creating the certificate.
- [Connect to your private compute instance.](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm)
- Create the server certificate.

For example, use the OpenSSL command line application.
- For Linux, run:`sudo yum install openssl`
- For MacOS, run:`brew install openssl`
- For Windows, download the`openssl`binary from[Win32/Win64 OpenSSL](https://slproweb.com/products/Win32OpenSSL.html)and configure the environment.

Example commands, using`vi`for file creation (you can alternatively use`touch`):
```

```

- Create the certificate chain (`cert_chain.crt`):
- Copy the contents of &lt;key-name&gt; .crt to the top of`cert_chain.crt`.
- Underneath, copy the contents of`myCA.pem`.
The root certificate (`.pem`contents) must follow the individual certificate (`.crt`contents).
- Save the file.
- Create the private key (`<key-name> .npass.key`) by running the following OpenSSL command:

```

```

### Importing an Existing Certificate

To access a private Bitbucket server, make its associated SSL certificate available in the Oracle Cloud Infrastructure Certificates service.

For more information about the Certificates service, see[Certificates](https://docs.oracle.com/iaas/Content/certificates/home.htm).

- Note the passphrase and the locations of the certificate chain, server certificate, and private key.
See[Creating a Certificate](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm#create-cert).
- Import the certificate.

See[Importing a Certificate](https://docs.oracle.com/iaas/Content/certificates/importing-certificate.htm).

After the certificate is in the Certificates service, you can select it along with a private endpoint when you[create the configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/create-csp.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm#)
- 

After completing all the prerequisites, follow these steps in the Console to create a configuration source provider from Bitbucket Server .

- On the Configuration source providers list page, select Create configuration source provider . If you need help finding the list page or the configuration source provider, see[Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-csp.htm).
- In the Create configuration source provider panel, enter a name and optional description for the configuration source provider. Avoid entering confidential information.
- Select the compartment that you want to store the configuration source provider in.
- (Optional) To use a[private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/private-endpoints.htm), follow these steps:
- Select Private endpoint .
- Select or create a private endpoint. To select a private endpoint or certificate in a different compartment, select Change Compartment .
- Select an SSL certificate.
For more information about private endpoints for private servers, see[Private Git Server](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/private-endpoints.htm#private-git).
- For Type , select Bitbucket Server .
- Enter the following values:

- Server URL : The Bitbucket Server service endpoint. Example:`my-private-bitbucket-server.example.com`
- Vault :[Vault](https://docs.oracle.com/iaas/Content/KeyManagement/home.htm)where the secret is stored.
- Secret :[Secret](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm)for authorization.
- (Optional) Add one or more tags to the configuration source provider: Select Show advanced options to show tagging options.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .
- To confirm that Resource Manager can access the server URL using the provided authentication information, select the configuration source provider to open its details page, and then select Validate connection .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/configuration-source-provider/create-bitbucket-server-access-token-provider.html)oci resource-manager configuration-source-provider create-bitbucket-server-access-token-provider`command and required parameters to create a configuration source provider from Bitbucket Server .

```

```

For a complete list of parameters and values for CLI commands, see the[Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
- 

Run the[CreateConfigurationSourceProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider/CreateConfigurationSourceProvider)operation to create a configuration source provider from Bitbucket Server .

For an example of the`configSourceProviderType`part of the request, see[CreateBitbucketServerAccessTokenConfigurationSourceProviderDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateBitbucketServerAccessTokenConfigurationSourceProviderDetails).

## What's Next

[Validating the Connection for a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/validate-connection-csp.htm)
