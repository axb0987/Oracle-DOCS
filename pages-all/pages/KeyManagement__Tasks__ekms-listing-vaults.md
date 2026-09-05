# Listing External Key Management Vaults
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms-listing-vaults.htm
- Fetched: 2026-09-05 02:34 CDT

# Listing External Key Management Vaults

Learn how to navigate to the list view for External Key Management vaults in the OCI Console.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms-listing-vaults.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms-listing-vaults.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms-listing-vaults.htm#)
- 

- Open the navigation menu , select Identity &amp; Security , and then select External Key Management .

The Vaults list page opens. All vaults in the selected compartment are displayed in a table.
- To view the vaults in a different compartment, use the Compartment filter to switch compartments.

You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see[Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).

## Filtering List Results

Use filters to limit the vaults in the list. Perform one of the following actions depending on the options that you see:

- From the Search and Filter box above the list table, select one or more filters and specify the values that you want to use to narrow the list. In general, the filters correspond to the columns shown in the list table, although some filters represent attributes that aren't shown in the table. The Compartment filter is always displayed next to Applied filters .
- On the left side of the list page, select a value from one of the available filters, such as compartment, state, or tags.

Change the order of the items in the list table by using the sort icons next to the column names.

For information about searching for resources and managing the columns in the list table, if those features are available, see[Listing Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/new-console.htm#new_console_list).

## Actions

In the list table, select the name of a vault to open its details page, where you can view its status and perform other tasks.

To perform an action on a &lt;resourceType&gt; directly from the list table, select any of the following options from the Actions menu (three dots) in the row for that &lt;resourceType&gt;:
- View details : Open the details page for the vault.
- Copy OCID : Copy the OCID of the vault to the clipboard.
- Move resource : Move the vault to another compartment.
- Manage tags : Add one or more tags to the vault. See[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
- Delete : .

To create a vault, select Create Vault . See[Creating an External Key Management Vault](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_create_vault.htm)for more information.
- 

Use the[oci kms management vault list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/kms/management/vault/list.html)command and required parameters to list the vaults in the specified compartment:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[ListVaults](https://docs.oracle.com/iaas/api/#/en/key/latest/VaultSummary/ListVaults)operation with the Management Endpoint to list the vaults in the specified compartment.

Note  
  

The Management Endpoint is used for management operations including Create, Update, List, Get, and Delete. The Management Endpoint is also called the control plane URL or the KMSMANAGEMENT endpoint.

The Cryptographic Endpoint is used for cryptographic operations including Encrypt, Decrypt, Generate Data Encryption Key, Sign, and Verify. The Cryptographic Endpoint is also called the data plane URL or the KMSCRYPTO endpoint.

You can find the management and cryptographic endpoints in a vault's details metadata. See[Getting a Vault's Details](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/../Tasks/tasks_managingvaults_topic_get_vault_details.htm)for instructions.

For regional endpoints for the Key Management, Secret Management, and Secret Retrieval APIs, see[API Reference and Endpoints](https://docs.oracle.com/iaas/api/). For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
