# Rebooting an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-reboot-instance.htm
- Fetched: 2026-09-05 01:52 CDT

# Rebooting an Instance

If the instance is scheduled for infrastructure maintenance, when the instance is rebooted, the instance reboots on a healthy physical host.

For steps to manage the lifecycle state of instances in an instance pool, see[Stopping and Starting the Instances in an Instance Pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-reboot-instance.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-reboot-instance.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-reboot-instance.htm#)
- 

- Navigate to the Compute Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).
- From the Actions menu (three dots) for the instance, select Reboot .

By default, the Console gracefully restarts the instance by sending a shutdown command to the OS. The system waits for up to 15 minutes for the OS to shut down. The instance is powered off and then powered back on.
Important  
  
If the applications that run on the instance take more than 15 minutes to shut down, improperly stopping them might result in data corruption. To avoid this,[shut down the instance using the commands available in the OS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-stop-instance.htm#operatingsystem)before you restart the instance using the Console.
Caution  
  
Force reboot: To reboot the instance immediately, without waiting for the OS to respond, select the Force reboot the instance by immediately powering off, then powering back on option. Improperly stopping an instance might result in data corruption.
- Select Reboot instance .

## Infrastructure maintenance

If the instance is scheduled for[infrastructure maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/infrastructure-maintenance.htm), for supported shapes, you can control when the maintenance downtime occurs by[proactively reboot migrating](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#moving-reboot)the instance to a healthy physical host before the maintenance due date. Depending on the shape, do one of the following:
- Standard VM shapes: The instance is migrated when you reboot it. You don't need to select any additional options.
- 

Dense I/O VM shapes: To reboot migrate the instance now, select the Delete the local NVMe-based SSD and reboot migrate to a healthy host option. For information about other maintenance options for dense I/O instances, see[Instance Maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/infrastructure-maintenance.htm).
Caution  
  
The NVMe-based SSD is permanently deleted. We recommend that you create a backup of the SSD before proceeding.
- Standard bare metal shapes: Select the Reboot migrate the instance to a healthy host option.
- 

Use the[instance action](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/action.html)command and required parameters to reboot an instance:

```

```

To reboot the instance immediately, use the`RESET`action.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[InstanceAction](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/InstanceAction)operation to reboot an instance, passing the value`SOFTRESET`as the action to perform.

To reboot the instance immediately, use the`RESET`
