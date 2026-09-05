# Getting User Diff Map
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_user_mgmt_retriving_user_diff.htm
- Fetched: 2026-09-05 02:33 CDT

# Getting User Diff Map

Command to getting user diff map.

The`getUserDiffMap`command to find all the keys that a user owns in the partition.

In the User Management utility, open a command prompt and run`getUserDiffMap`command to get information whether the user is synchronized on all partitions. This command is currently supported only on Server mode.

Syntax
```

```

Parameter Description
`UserID`User ID for which to check the (use 0 to check all users) synchronization.
`OutputFile`Path to the file in which to dump the data.(Optional).

Example
```

```
