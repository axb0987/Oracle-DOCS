# Inserting a Masked Object
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_key_util_inject_masked.htm
- Fetched: 2026-09-05 02:32 CDT

# Inserting a Masked Object

Get details for the Key Management Utility command for inserting a masked object.

The insertMaskedObject command inserts a masked object from a file into an HSM partition. This is similar to the restore functionality in a "backup and restore" operation.

In the[Key Management Utility](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_key_mgmt_operations.htm), open a command prompt and run the`insertMaskedObject`command to insert a masked object.

Syntax

```

```

Parameters

Parameter Description
-h Displays this information
-f Name of the file that contains the masked object. By default, the object is a key or data (include`-user`argument if it's user information).
-min_srv Specifies the minimum number of servers on which the inserted masked object is synchronized before the timeout parameter expires. The default value is 2.
-timeout Indicates the wait time (in seconds) for the key to sync across servers.

Example
```

```
