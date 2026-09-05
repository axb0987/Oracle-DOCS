# Updating Mount Target Performance
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-mt-performance.htm
- Fetched: 2026-09-05 02:02 CDT

# Updating Mount Target Performance

The performance of a File Storage mount target is partially dependent upon the maximum throughput available to the mount target. A mount target can have a Standard performance level or a specific High Performance level.

Important  
  

High performance mount targets require a 30-day commitment and are billed in 30-day cycles. When you change the performance of an existing mount target to a high performance shape, that 30-day billing cycle begins. For specific pricing details, see[Oracle Storage Cloud Pricing](https://www.oracle.com/cloud/storage/pricing.html).

You can upgrade a mount target to a high performance mount target at any time. If requirements change, and you don't need the same performance, you can downgrade the performance level at the end of the billing cycle.

Each availability domain is limited to two Standard mount targets, two 20 Gbps High Performance mount targets, one 40 Gbps High Performance mount target, and zero 80 Gbps High Performance mount targets by default.

See[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)for a list of applicable limits and instructions for requesting a limit increase.

For more information, see[Mount Target Performance](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#performance)and[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#limitations)for mount targets.

## Required IAM Policy

[Permissions to manage mount targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#Required_IAM_Policy)include the ability to update mount target performance. Consider more restrictive permissions if you don't want managers to change performance levels. A more specific policy for mount target performance management follows:
```

```

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Details for the File Storage Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/filestoragepolicyreference.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-mt-performance.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-mt-performance.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-mt-performance.htm#)
- 

- On the Mount Targets list page, select the mount target that you want to work with. If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-mount-targets.htm).
- 

From the Actions tab, select Update mount target performance .
- 

Select a Current mount target throughput :
- 1 Gbps of throughput (Standard)
- 20 Gbps of throughput (High performance)
- 40 Gbps of throughput (High performance)
- 80 Gbps of throughput (High performance)
- If you see a Warning about billing updates (this happens when you select a larger throughput) carefully review it. If you're okay with the update, accept it.
- To update mount target performance, select Update .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/upgrade-shape.html)oci fs mount-target upgrade-shape`command and required parameters to immediately upgrade a mount target's performance level:

```

```

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/schedule-downgrade-shape.html)oci fs mount-target schedule-downgrade-shape`command and required parameters to downgrade a mount target's performance level at the end of its billing cycle:
```

```

To cancel the scheduled downgrade of a mount target's performance level, use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/cancel-downgrade-shape.html)oci fs mount-target cancel-downgrade-shape`command:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

To immediately upgrade the performance level of a mount target and start the billing cycle, run the[UpgradeShapeMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/UpgradeShapeMountTarget)operation.

To downgrade the performance level of a mount target at the end of its billing cycle, run the[ScheduleDowngradeShapeMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/ScheduleDowngradeShapeMountTarget)operation. To cancel a scheduled performance level downgrade, run the[CancelDowngradeShapeMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/CancelDowngradeShapeMountTarget)operation.

To immediately release a mount target's resources, with the understanding that you'll still be billed for those resources until the cycle's end date, you can[delete the mount target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-mount-target.htm).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
