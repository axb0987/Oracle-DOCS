# Live, Reboot, and Manual Migration: Moving a Compute Instance to a New Host
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm
- Fetched: 2026-09-05 01:52 CDT

# Live, Reboot, and Manual Migration: Moving a Compute Instance to a New Host

This topic provides information about maintenance actions that involve relocating virtual machine (VM) and bare metal instances during[infrastructure maintenance events](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/infrastructure-maintenance.htm). Available actions include:
- [Live Migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#live-migration)
- [Reboot Migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#reboot)
- [Moving an Instance with Manual Migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#manual)
Important  
  
For information about when a virtual machine needs to be migrated, see[Instance Maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/infrastructure-maintenance.htm).
Tip  
  
Dedicated virtual machine host migration: For information about how to relocate dedicated virtual machine hosts during infrastructure maintenance events, see[Managing Maintenance Reboot Migration for Dedicated Virtual Machine Hosts](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/dedicatedvmhosts_topic-infrastructure-maintenance.htm).
Note  
  
Oracle Platform Services: For instances that were created with[Oracle Platform Services](https://docs.oracle.com/iaas/Content/General/Reference/PaaSprereqs.htm)and located in the compartment`ManagedCompartmentForPaaS`, you must use the interface for the specific Platform Service to reboot the instances.

## Live Migration

Live Migration is a mechanism for moving a VM from one physical server to another while the VM is still running. During a live migration, the source VM instance continues to run as the Compute service copies memory and all virtual components to the new target VM instance. When the copy is complete, there is only a slight pause, typically measured in tens of milliseconds, when the system switches to the new VM.

During an[infrastructure maintenance event](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/infrastructure-maintenance.htm#planned-maintenance__recovering-an-instance), Oracle Cloud Infrastructure live migrates supported VM instances from a healthy physical VM host that needs maintenance to a healthy VM host with minimal disruption to running instances.

If an instance cannot be live migrated, Oracle Cloud Infrastructure schedules a due date for reboot migration within 14 to 16 days and sends you a notification. If you do not proactively reboot the instance before the due date, the instance is reboot migrated for you.

By default, Oracle Cloud Infrastructure live migrates the instance without sending any notification about the upcoming maintenance. When a live migration begins and ends, an[infrastructure maintenance event](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm#computeevents__compute_instance)is emitted. You can[use automation to track infrastructure maintenance events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm).

### Live Migration Support

When you[create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm), select settings that are compatible with live migration. For an existing instance, where supported, you can enable live migration by editing the instance to use settings that are compatible with live migration. Some settings that are incompatible with live migration cannot be edited after you create an instance.

The following table shows the criteria that make an instance compatible with live migration. All criteria must be met for an instance to support live migration.

Category Criteria that support live migration Can setting be edited after creating the instance?
Realm Tenancy is in the[commercial realm](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). No.
Shape

Instance uses one of the following[shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm):
- VM.Standard1 series
- VM.Standard.B1 series
- VM.Standard2 series
- VM.Standard3.Flex
- VM.Standard4.Ax.Flex
- VM.Standard.E2 series
- VM.Standard.E2.1.Micro
- VM.Standard.E3.Flex
- VM.Standard.E4.Flex
- VM.Standard.E5.Flex
- VM.Standard.E6.Flex
- VM.Standard.E6.Ax.Flex
- VM.Optimized3.Flex
- VM.Standard.A1.Flex
- VM.Standard.A4.Flex
- VM.Standard.A4.Ax.Flex

Other VM shapes, bare metal instances, and instances on dedicated virtual machine hosts do not support live migration.

Yes, for some shapes.[Change the shape of the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm)to a supported shape.

Alternatively,[terminate (delete) the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm), but do not delete the associated boot volume. Then, use the boot volume to[create a new instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm)using a shape that supports live migration.
Image

Instances that use Linux or Windows[platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/images.htm)support live migration.

For instances that use[custom images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm)or Oracle Cloud Infrastructure Marketplace images, Oracle Cloud Infrastructure attempts to live migrate the instance. No.
Networking launch type Instance uses[paravirtualized networking](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#instance-network-launch-types). Yes,[edit the networking launch type](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-launch-options.htm).
Shielded instances Not supported. No.
Windows Defender Credential Guard is enabled Not supported. No.
Virtual network interface cards (VNICs) Maximum total number of attached VNICs is six. Yes,[detach and delete secondary VNICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm#To3)until six or fewer VNICs total are attached.

To determine whether an instance supports live migration:
- Open the navigation menu and select Compute . Under Compute , select Instances .
- Select the instance that you're interested in.
- Check the Live migration field for the instance. If the field displays View incompatibilities , the instance doesn't support live migration.
- (Optional) To see which settings are not compatible with live migration, click View incompatibilities .

## Reboot Migration

With reboot migration, the instance is stopped, migrated to a healthy host, and restarted. A short downtime occurs during the migration. You can control when the downtime occurs by proactively reboot migrating the instance before the maintenance due date.

Reboot migration is supported for VM instances that use standard, GPU, and dense I/O shapes, and for bare metal instances that use standard shapes. The default maintenance action depends on the instance[shape](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm).
- 

VM instances:
- 

Standard/GPU shapes (including Flex): Within 24 hours after the maintenance due date, the VM instance is stopped, migrated to a healthy host, and restarted. A short downtime occurs during the migration.

You can control when the downtime occurs by proactively reboot migrating the instance before the maintenance due date.
- 

DenseIO shapes (including Flex): On the maintenance due date, the VM instance is stopped, rebuilt, and restarted. A downtime of several hours occurs during the maintenance process.

If you want to minimize downtime and can delete the locally-attached NVMe-based SSD, you can proactively reboot the instance before the scheduled maintenance time. The instance will be reboot migrated to a healthy host and the SSD will be permanently deleted. A short downtime occurs during the migration.
- 

Bare metal instances:
- 

Standard shapes: Within 24 hours after the maintenance due date, the bare metal instance is stopped, migrated to a healthy host, and restarted. A short downtime occurs during the migration.

You can control when the downtime occurs by proactively reboot migrating the instance before the maintenance due date.

If reboot migration is unsuccessful, Oracle Cloud Infrastructure sends a notification. You must manually migrate the instance to a healthy host.

After the instance is reboot migrated, the Maintenance reboot field is cleared. This change indicates that the instance was moved successfully.
Important  
  
Use the Console, CLI, or SDK to reboot migrate a VM instance. Rebooting the instance from the operating system does not migrate the instance to new hardware.

After a migration, by default the instance is recovered to the same lifecycle state as before the maintenance event. If you have an alternate process to recover the instance after a reboot migration, you can configure the instance to remain stopped after it is migrated to healthy hardware. For more information about configuring migration options, including the lifecycle state of instances after a migration, see[Setting Instance Availability During Maintenance Events](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-maintenance-recovery-action.htm).
Tip  
  
You can extend the due date for reboot migration, see[Extending Maintenance Deadline](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/infrastructure-maintenance.htm#planned-maintenance__extending-deadline)

### Prerequisites for Reboot Migration

Prepare the instance for reboot migration:
- Ensure that any block volumes defined in`/etc/fstab`use the[recommended options](https://docs.oracle.com/iaas/Content/Block/References/fstaboptions.htm).
- Ensure that any File Storage service (NFS) mounts use the`nofail`option.
- If you use the[Oracle-provided script](https://github.com/oracle/terraform-examples/blob/master/examples/oci/connect_vcns_using_multiple_vnics/scripts/secondary_vnic_all_configure.sh)to configure secondary VNICs, ensure it runs automatically at startup.
- 

If the instance uses a dense I/O shape, back up the locally-attached NVMe-based SSD:
- [Create](https://docs.oracle.com/iaas/Content/Block/Tasks/creatingavolume.htm)and[attach](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm)one or more block volumes to the instance.
- Copy the data from the NVMe devices to the block volumes.

### Moving a VM Instance with Reboot Migration

After you complete the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#prerequisites-reboot):
- Stop any running applications.
- 

Use the Console, CLI, or SDK to[reboot the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm). Reboot migration is not performed when you restart the instance from the operating system.

If the instance uses a dense I/O[shape](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm):
- Using the Console: In the Reboot instance dialog box, select the Delete the local NVMe-based SSD and reboot migrate to a healthy host option.
- Using the CLI or SDK: In the[InstanceAction](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/InstanceAction)operation, set the`allowDenseRebootMigration`attribute to`true`.
Caution  
  
For dense I/O instances, the NVMe-based SSD is permanently deleted. We recommend that you create a backup of the SSD before proceeding.
- Confirm that the maintenance event in the Maintenance tab is in the`Succeeded`state. (There are three possible final states:`Succeeded`,`Canceled`,`Failed`).
- Start and test any applications on the instance.
- 

For dense I/O instances, if you want to restore the NVMe-based SSD:
- [Attach the block volumes](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm)used to back up local NVMe devices.
- Copy the data onto the NVMe storage on the new instance.
- [Detach](https://docs.oracle.com/iaas/Content/Block/Tasks/detachingavolume.htm)and optionally[delete](https://docs.oracle.com/iaas/Content/Block/Tasks/deletingavolume.htm)the block volumes.

### Moving a Bare Metal Instance with Reboot Migration

After you complete the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#prerequisites-reboot):
- Stop any running applications.
- 

Use the Console, CLI, or SDK to[reboot the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm). Reboot migration is not performed when you restart the instance from the operating system.
- Using the Console: In the Reboot instance dialog box, select the Reboot migrate the instance to a healthy host option.
- Using the CLI or SDK: In the[InstanceAction](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/InstanceAction)operation, pass the value`REBOOTMIGRATE`as the action to perform. To reboot migrate the instance immediately, leave the`timeScheduled`attribute empty.
- Confirm that the maintenance event in the Maintenance tab is in the`Succeeded`state. (There are three possible final states:`Succeeded`,`Canceled`,`Failed`).
- Start and test any applications on the instance.

## Moving an Instance with Manual Migration

For instances without a date in the Maintenance reboot field (available in the Console, CLI, and SDKs), you must move the instance manually. This method requires that you delete (terminate) the instance, and then launch a new instance from the retained boot volume. Instances that have additional VNICs, secondary IP addresses, remote attached block volumes, the Trusted Platform Module (TPM) enabled, or that belong to a backend set of a load balancer require additional steps.

### Limitations and Warnings for Manual Migration

Be aware of the following limitations and warnings when performing a manual migration:
- Any public IP addresses assigned to your instance from a[reserved public pool](https://docs.oracle.com/iaas/Content/Network/Tasks/assign-public-ip-instance-launch.htm)are retained. Any that were not assigned from a reserved public IP address pool will change. Private IP addresses do not change.
- MAC addresses, CPUIDs, and other unique hardware identifiers do change during the move. If any applications running on the instance use these identifiers for licensing or other purposes, be sure to take note of this information before moving the instance to help you manage the change.
- Shielded instances have additional limitations. See[Migrating Shielded Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/shielded-instances.htm#shielded-instances-migrate).

### Prerequisites for Manual Migration

- 

Before moving the instance, document all critical details:
- The instance's region, availability domain, and fault domain.
- The instance's display name.
- All private IP addresses, names, and subnets. Note that the instance can have multiple VNICs, and each VNIC can have multiple secondary IP addresses.
- All private DNS names. The instance can have multiple VNICs, and each VNIC can have multiple secondary IP addresses. Each private IP address can have a DNS name.
- Any[public IP addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm)assigned from a reserved public pool. Note that the instance can have multiple VNICs, and each VNIC can have multiple secondary private IP addresses. Each VNIC and secondary private IP address can have an attached public IP address.
- Any block volumes attached to the instance.
- Any tags on the instance or attached resources.
- 

Prepare the instance for manual migration:
- Ensure that any block volumes defined in`/etc/fstab`use the[recommended options](https://docs.oracle.com/iaas/Content/Block/References/fstaboptions.htm).
- Ensure that any File Storage service (NFS) mounts use the`nofail`option.
- If you have statically defined any network interfaces belonging to secondary VNICs using their MAC addresses, such as those defined in`/etc/sysconfig/network-scripts/ifcfg*`, those interfaces will not start due to the change in the MAC address. Remove the static mapping.
- If you use the[Oracle-provided script](https://github.com/oracle/terraform-examples/blob/master/examples/oci/connect_vcns_using_multiple_vnics/scripts/secondary_vnic_all_configure.sh)to configure secondary VNICs, ensure it runs automatically at startup.

### Moving an Instance Manually

After you complete the prerequisites, perform the following steps.

- Stop any running applications.
- 

Ensure that those applications will not start automatically.
Caution  
  
When the relocated instance starts for the first time, any block volumes, secondary VNICs, or any resource that relies on them, will not be attached. The absence of these resources can cause application issues.
- 

If the instance uses a dense I/O[shape](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm), back up the locally-attached NVMe-based SSD:
- [Create](https://docs.oracle.com/iaas/Content/Block/Tasks/creatingavolume.htm)and[attach](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm)one or more block volumes to the instance.
- Copy the data from the NVMe devices to the block volumes.
- Unmount any[block volumes](https://docs.oracle.com/iaas/Content/Block/Tasks/disconnectingfromavolume.htm)or File Storage[service (NFS) mounts](https://docs.oracle.com/iaas/Content/File/Tasks/mountingfilesystems.htm).
- [Back up all block volumes](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumebackups.htm).
- 

[Create a backup of the boot volume](https://docs.oracle.com/iaas/Content/Block/Concepts/bootvolumebackups.htm).
Important  
  
Do not generalize or specialize Windows instances.
- 

Terminate (delete) the instance, preserving the attached boot volume:

Using the Console

Follow the steps in[Terminating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/terminatinginstance.htm), ensuring that the Permanently delete the attached boot volume check box is cleared. This preserves the boot volume that is associated with the instance.

Using the CLI

Use the[instance terminate](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/terminate.html)operation and set the`preserve-boot-volume`option to`true`.

Using the API

Use the[TerminateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/TerminateInstance)operation and pass the`preserveBootVolume`parameter set to`true`in the request.
- 

[Create a new instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/launchinginstance.htm)using the boot volume from the terminated instance.

(Optional) If the instance is on a new dedicated virtual machine host:
- In the Placement section, select Show advanced options .
- For Capacity type , select Dedicated host .
- Select the dedicated virtual machine host that you want to place the instance on.

In the create instance flow, specify the private IP address that was attached to the primary VNIC. If the public IP address was assigned from a reserved IP address pool, be sure to assign the same IP address.
- When the instance state changes to Running ,[stop the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/restartinginstance.htm).
- Recreate any[secondary VNICs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm)and[secondary IP addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipaddressesanddns.htm).
- 

[Attach any block volumes](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm).
Note  
  
This step includes any volumes used to back up local NVMe devices. Copy the data onto the NVMe storage on the new instance, and then detach the volumes.
- [Start the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/restartinginstance.htm).
- Start and test any applications on the instance.
- Configure the applications to start automatically, as required.
- [Recreate the required tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
-
