# Getting Key Diff Map
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_user_mgmt_retriving_key_diff_map.htm
- Fetched: 2026-09-05 02:33 CDT

# Getting Key Diff Map

Command to get key diff map.

The`getKeyDiffMap`command gets information about the keys that are synchronized on all HSMs.

In the User Management utility, open a command prompt and run`getKeyDiffMap`command to get information about the keys that are synchronized on all HSMs.

Syntax
```

```

Parameter Description
`ServerID`(Global mode only) ID of the server for which to get the map.
`UserID`The user ID whose keys you want to find. Use 0 to include the keys of all users (the default is 0).
`KeyHandle`Key handle for which to get information.Use 0 for all keys (default value is 0).
`Output File`(Optional) File path to dump the output.

Example
```

```
