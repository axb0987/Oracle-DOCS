# Modifying Key Owner
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_user_mgmt_modify_key_owner.htm
- Fetched: 2026-09-05 02:33 CDT

# Modifying Key Owner

Command to modify key owner.

The`modifyKeyOwner`command enables you to change the key owner. This command can only be run in server mode.

In the User Management utility, open a command prompt and run`modifyKeyOwner`command to modify a key.

Syntax
```

```

Parameter Description
`KeyHandle`Key handle for which to change the owner.
`UserID`User ID of the new key owner.
`KCV`

Key check value for the key in hex

Optional for GENERIC_SECRET keys required for all other key types. Use`getAttribute <keyHandle>`to get KCV of the key.

Example
```

```
