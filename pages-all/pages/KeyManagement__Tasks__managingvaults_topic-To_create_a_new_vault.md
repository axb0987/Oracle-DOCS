# Creating a Vault
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm
- Fetched: 2026-09-05 02:36 CDT

# Creating a Vault

Learn how to create a vault in OCI.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm#)
- 

- On the Vaults list page, select Create Vault . If you need help finding the list page, see[Listing Vaults](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/managingvaults-listing-vaults.htm).
- In the Create Vault dialog box, provide the following details:

- If needed, select a different compartment in which you want to create the vault.
- Enter a name for the vault.
- Select Make it virtual private vault if you want a dedicated partition in a hardware security module (HSM).
Note  
  
You cannot change the vault type after the vault is created.
- Select Tags to add tags to the vault. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option (you can apply tags later) or ask your administrator.
- Select one of the following options:

- Select Create Vault .
- Select Save as stack to save the resource definition as a Terraform configuration. For more information about saving stacks from resource definitions, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
- 

use the[oci kms management vault create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/create.html)command and required parameters to create a new vault.
Tip  
  
You can't change the vault type after the vault is created.
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Use the[CreateVault](https://docs.oracle.com/iaas/api/#/en/key/latest/Vault/CreateVault)operation with the KMSVAULT API endpoint to create a vault.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
