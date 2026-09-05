# Assigning a Key to an Object Storage Bucket
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_Object_Storage_bucket.htm
- Fetched: 2026-09-05 02:31 CDT

# Assigning a Key to an Object Storage Bucket

Assigning a key to a new Object Storage bucket using the OCI Console, CLI, and API interfaces.

- [Console](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_Object_Storage_bucket.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_Object_Storage_bucket.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_a_new_Object_Storage_bucket.htm#)
- 

- Open the navigation menu and select Storage . Under Object Storage &amp; Archive Storage , select Buckets .
- Under List Scope , in the Compartment list, choose the compartment where you want to create a bucket that's encrypted with a Vault service master encryption key.
- 

Select Create Bucket , and then follow the instructions in[Creating an Object Storage Bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm).
- 

Open a command prompt and run`oci os bucket create`to create a bucket that is encrypted with a Vault service master encryption key:

```

```

For example:
```

```

For a complete list of parameters and values for CLI commands, see[KMS CLI Command Reference.](https://docs.oracle.com/iaas/tools/oci-cli/3.37.4/oci_cli_docs/cmdref/kms.html)
- 

Run the[CreateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/CreateBucket)and[UpdateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/UpdateBucket)operations to create and assign a vault key to an Object Storage bucket.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
