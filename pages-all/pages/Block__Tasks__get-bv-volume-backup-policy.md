# Getting Details for a Backup Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume-backup-policy.htm
- Fetched: 2026-09-05 01:46 CDT

# Getting Details for a Backup Policy

Retrieve details for a backup policy in Block Volume. You can get details for both Oracle-defined and user-defined backup policies.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume-backup-policy.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume-backup-policy.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume-backup-policy.htm#)
- 

On the Backup Policies list page, find the backup policy that you want to work with. If you need help finding the list page or the backup policies, see[Listing Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-backup-policies.htm).
- 

Use the[`oci bv volume-backup-policy get`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-backup-policy/get.html)command and specify the`--policy-id`parameter to retrieve details for a policy:

```

```

For example:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the`[](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackupPolicy/GetVolumeBackupPolicy)GetVolumeBackupPolicy`operation and specify the`policyId`
