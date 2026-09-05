# Updating an Object Storage Bucket's Vault Key
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_update_the_Vault_key_assigned_to_a_bucket.htm
- Fetched: 2026-09-05 02:51 CDT

# Updating an Object Storage Bucket's Vault Key

Update the Vault key assigned to an Object Storage bucket.

## Using the Console

- On the Buckets list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the bucket, see[Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
- On the details page, find Encryption key .
- From the Actions menu (three dots) , select Edit key .
The Edit master encryption key panel opens.
- Update the encryption key settings as needed. For descriptions of the settings, see[Assigning a Key to a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_assign_a_Vault_master_encryption_key_to_a_bucket.htm).
- Select Update .

## Using the CLI

```

```

kms_key_id is the OCID of the key versions that contain the cryptographic material used to encrypt and decrypt data, protecting the data where the data is stored.

For example:
```

```

### Adding Custom Key Value to a Bucket

Use the[oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html)command and required parameters to add a custom key value to a bucket.

```

```

JSON-formatted_key-value_pair is a key-value pair input as valid formatted JSON. See[Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output)and[Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON)for information about JSON formatting.

For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/)
