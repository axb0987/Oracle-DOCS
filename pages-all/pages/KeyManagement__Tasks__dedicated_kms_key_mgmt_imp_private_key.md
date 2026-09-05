# Importing a Private Key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_key_mgmt_imp_private_key.htm
- Fetched: 2026-09-05 02:32 CDT

# Importing a Private Key

Configure command for Importing a Private Key.

The importPrivKey command inserts a masked object from a file into a HSM partition. Similar to the restore functionality in a "Backup and restore" operation.

In the Key Management utility, open a command prompt and run`importPrivKey`command to inject a masked object. Syntax
```

```

Where,

Parameter Description
-h Displays this information
-f Name of the file that contains the masked object. By default, the object is a key or data (include -user argument if it is user information).
-o Request object/user handle (Optional)
-min_srv Specifies the minimum number of servers on which the inserted masked object is synchronized before the timeout parameter expires. The default value is 2.
