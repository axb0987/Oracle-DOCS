# Synchronizing a key
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_user_mgmt_sync_key.htm
- Fetched: 2026-09-05 02:33 CDT

# Synchronizing a key

Command to synchronize a key.

The`synckey`command enables you to synchronize a key from one node to another by extracting a key from the current partition and inserting it into another partition

In the User Management utility, open a command prompt and run`storeFixedKey`command to store the partition fixed, preshared key (PKBK).

Syntax
```

```

Parameter Description
`KeyHandle`Handle of the key to sync.
`ServerID`server ID mapped to target HSM.

Example
```

```
