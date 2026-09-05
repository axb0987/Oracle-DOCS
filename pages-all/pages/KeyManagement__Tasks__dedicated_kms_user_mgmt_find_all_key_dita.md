# Finding All Keys
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_user_mgmt_find_all_key_dita.htm
- Fetched: 2026-09-05 02:33 CDT

# Finding All Keys

Command to find all keys.

The`findAllKeys`command enables you to find all the keys that a user owns in the partition.

In the User Management utility, open a command prompt and run`findAllKeys`command to find all the keys that a user owns in the partition.

Syntax

```

```

Parameter Description
`UserID`Identification of the user whose keys you want to find. 0 for all users.
`GetkeyHash ID`

Whether or not to include the key hash.

0 - no key hash

1 - with key hash
`Output File`(Optional) Path to the file in which to dump the data.

Example
```

```
