# Managing Volumes
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/managing-volumes.htm
- Fetched: 2026-09-05 19:20 CDT

# Managing Volumes

Use the OCI Terraform provider to manage boot volumes.

This guide details the following scenarios:
- Preserving boot volumes when performing compute instance scaling
- Boot volume troubleshooting and repair
- Replicating volumes to another availability domain

To read more about boot volumes, see[Boot Volumes](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm).

## Preserving Boot Volumes

You might want to change compute instance shape while using the same boot volume. When you terminate your instance, you can keep the associated boot volume and use it to create a new instance using a different instance type or shape. This approach is useful for scenarios where instance shape can't be changed[while resizing instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm).

To achieve this, you need to detach the boot volume from the running instance. This can be performed by either terminating the instance while preserving the boot volume or by stopping the instance and detaching the boot volume,

All Terraform resources of type`oci_core_instance`have the parameter`preserve_boot_volume`set as`true`by default. This parameter ensures that upon termination of the instance, the attached boot volume isn't terminated.
```

```

After the boot volume is detached, the OCID of the boot volume can be referred as the source of the new instance, as the following example illustrates:
```

```

## Detaching Boot Volumes for Troubleshooting and Repair

If you think a boot volume issue is causing a compute instance problem, you can stop the instance and detach the boot volume. Then you can attach it to another instance as a data volume to troubleshoot it. After resolving the issue, you can then reattach it to the original instance or use it to launch a new instance.

After the boot volume has been detached, the OCID of the boot volume can be referred as the block volume parameter for another instance.
```

```

After you have resolved the issue, detach this volume from the second instance and attach it as a boot volume to the original instance.
```

```

## Replicate a Volume to an Availability Domain within the Region

You can use Terraform to replicate existing compute instance boot and block volumes to another availability domain within the same region.

To replicate a volume:
- Create a data source for the volume using`oci_core_boot_volume`or`oci_core_volume`.
- Use the`oci_core_boot_volume_backup`or`oci_core_volume_backup`resource to create a backup of the source volume.
- Define the target volume resource to be created from the backup.

The following example Terraform configuration replicates both a boot volume and a block volume:
```

```

You can use these steps to move an instance to the second availability domain or to create a disaster recovery deployment in the second availability domain.

If this method is used for a pure retargeting scenario where the source volumes (and the backups) are removed after the duplication, then the Terraform configuration must be refactored after the source volumes are removed to avoid destroying the target instances on the next apply.

If using this scenario for disaster recovery cold standby, you can regularly use the Terraform`taint`
