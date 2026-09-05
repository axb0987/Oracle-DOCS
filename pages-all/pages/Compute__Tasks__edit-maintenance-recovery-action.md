# Setting Instance Availability During Maintenance Events
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-maintenance-recovery-action.htm
- Fetched: 2026-09-05 01:51 CDT

# Setting Instance Availability During Maintenance Events

When the underlying infrastructure for a compute instance needs to[undergo planned maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/infrastructure-maintenance.htm#planned-maintenance__vm-planned-maintenance)or[recover from an unexpected failure](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/infrastructure-maintenance.htm#hardware-failure), Oracle Cloud Infrastructure automatically attempts to recover the instance by migrating it to healthy hardware.

For virtual machine (VM) instances, when applicable, Oracle Cloud Infrastructure live migrates[supported VM instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#live-migration__live-migration-support)from the physical VM host that needs maintenance to a healthy VM host with minimal disruption to running instances. If you do not want your instances live migrated, you can choose to receive a notification for the maintenance event. After you receive the notification, you have 14 days to[reboot migrate](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#reboot)your instance. The instance is only live migrated if you do not reboot the instance before the due date. If the instance can't be live migrated, reboot migration (for standard VM shapes) or rebuild in place (for dense I/O VM shapes) is used instead.

After a migration, by default the instance is recovered to the same lifecycle state as before the maintenance event. If you have an alternate process to recover the instance after a reboot migration, you can optionally configure the instance to remain stopped after the maintenance is complete. You can then restart the instance on your own schedule.

For permissions, see[Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instances.htm#instance-permissions).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-maintenance-recovery-action.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-maintenance-recovery-action.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-maintenance-recovery-action.htm#)
- 

You can use the Console to configure live migration options and the lifecycle state of instances after a migration.

## Configuring Live Migration

- Navigate to the Compute Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).
- Select an instance.
- Select the option you see:
- Select Actions then More actions then Edit .
- Select More actions then Edit .
- Select Advanced options then navigate to Availability configuration .
- In the Live migration section, select an option:
- Let Oracle Cloud Infrastructure select the best migration option : Select this option to let Oracle Cloud Infrastructure select the best option to[migrate the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm)to a healthy physical VM host if an underlying infrastructure component needs to undergo maintenance.
- Use live migration if possible : Select this option to have the instance[live migrated](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#live-migration)to a healthy physical VM host without any notification or disruption. If live migration isn't successful,[reboot migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#reboot)is used. Some shapes don't support live migration.
- Opt-out : Select this option to have a notification sent for the maintenance event. The instance is live migrated if you don't proactively reboot the instance before the due date.

For the Restore instance lifecycle state after infrastructure maintenance checkbox, select an option:
- To reboot a running instance after it's recovered, select the checkbox.
- To recover the instance in the stopped state, clear the checkbox.
- Select Save changes .
- 

Use the[instance update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/update.html)command and required parameters to update an instance:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute Service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use this API operation to edit the maintenance recovery action for an instance:
- [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)
