# Updating the Master Encryption Key Assigned to a Stream Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/update-the-encryption-key-assigned-to-a-stream-pool.htm
- Fetched: 2026-09-05 03:06 CDT

# Updating the Master Encryption Key Assigned to a Stream Pool

Change a stream pool's master encryption key.

To review requirements for creating and managing streams, see[Getting Started with Streaming](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Concepts/streaminggettingstarted.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/update-the-encryption-key-assigned-to-a-stream-pool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/update-the-encryption-key-assigned-to-a-stream-pool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/update-the-encryption-key-assigned-to-a-stream-pool.htm#)
- 

- On the Stream pool list page, select the stream pool that you want to work with. If you need help finding the list page or the stream pool, see[Listing Stream Pools](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/../Tasks/list-stream-pools.htm).
- On the details page, select Edit settings .
- To encrypt the data in the streams in this stream pool by using your own Vault encryption key, select Encrypt using customer-managed keys . To use the Vault service for your encryption needs, you need access to a vault and key, and you must allow the service to use the key.

- Vault : Select the compartment that contains the vault with the master encryption key that you want to use, and then select the vault.
- Master encryption key : Select the compartment that contains the master encryption key that you want to use, and then select the key.

For more information about encryption with a Vault key that you manage, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)and[Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).
Note  
  

You can also update encryption settings from the details page.
- To stop using an Oracle-managed key in favor of a Vault master encryption key that you manage, select Assign , select a vault and encryption key you have access to, and then select Assign .
- To select a different Vault master encryption key that you manage, select Update , select a vault and encryption key you have access to, and then select Update .
- To remove the assigned Vault master encryption key and let Oracle manage the encryption key, select Unassign and then select Unassign again to confirm the removal of the existing key assignment.
- Select Edit settings to save changes.
- 

Use the[oci streaming admin stream-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/streaming/admin/stream-pool/update.html)command and required parameters to update a stream pool's master encryption key:

```

```

Tip  
  
Provide input for`--custom-encryption-key-details`,`--private-endpoint-details`, and`--kafka-settings`as valid formatted JSON. See[Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output)and[Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON)for information about JSON formatting.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateStreamPool](https://docs.oracle.com/iaas/api/#/en/streaming/latest/StreamPool/UpdateStreamPool)
