# Stopping and Starting the Instances in an Instance Pool
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm
- Fetched: 2026-09-05 01:52 CDT

# Stopping and Starting the Instances in an Instance Pool

You can start, stop and restart all the instances in an instance pool as needed to update software or resolve error conditions.

To automatically stop and start instances in an instance pool based on a schedule, you can[enable autoscaling](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm)for the pool.
Tip  
  
To stop all instances in an instance pool, stop the pool itself, rather than the individual instances. If you stop all of the instances in a pool without stopping the pool, the pool tries to relaunch the instances.

## Shutting Down or Restarting an Instance Using the Instance's OS

You can shut down and restart instances using the commands available in the operating system when you are logged in to the instance. Shutting down an instance using the instance's OS does not stop billing for that instance. If you shut down the instances in an instance pool this way, be sure to also stop the instance pool from the Console or API.

## Resource Billing for Stopped Instances

For both VM and bare metal instances, billing depends on the[shape](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/computeshapes.htm)that you use to create the instance:
- Standard shapes: Stopping an instance pool pauses billing. However, stopped instances continue to count toward your service limits.
- Dense I/O shapes: Billing continues for stopped instance pools because the NVMe storage resources are preserved. Related resources continue to count toward your service limits. To halt billing and remove related resources from your service limits, you must[delete the instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm).
- GPU shapes: For VM instances that use shapes in the VM.GPU.A10 series, stopping an instance pool pauses billing. However, stopped instances continue to count toward your service limits. For all other GPU shapes, billing continues for stopped instance pools because GPU resources are preserved. Related resources continue to count toward your service limits. To halt billing and remove related resources from your service limits, you must[delete the instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm).
- HPC shapes: Billing continues for stopped instance pools because the NVMe storage resources are preserved. Related resources continue to count toward your service limits. To halt billing and remove related resources from your service limits, you must[delete the instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm).
- Optimized shapes: For VM instances, stopping an instance pool pauses billing. However, stopped instances continue to count toward your service limits. For bare metal instances, billing continues for stopped instance pools because the NVMe storage resources are preserved. Related resources continue to count toward your service limits. To halt billing and remove related resources from your service limits, you must[delete the instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm).

Shutting down an instance using the instance's OS does not stop billing for that instance. If you shut down the instances in an instance pool this way, be sure to also stop the instance pool from the Console or API.

For more information about Compute pricing, see[Compute Pricing](https://www.oracle.com/cloud/compute/pricing.html). For more information about how instances running Microsoft Windows Server are billed when they are stopped, see[How am I charged for Windows Server on Oracle Cloud Infrastructure?](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/microsoftlicensing.htm#generalquestions)

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm#)
- 

[To start all instances in a pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm#)

- Navigate to the Instance pools list page. If you need help finding the list page, see[Listing Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instance-pools-list.htm).
- From the Actions menu (three dots) for the instance pool which contains the instances you want to start.
- Select Start , and then confirm when prompted.

[To stop all instances in a pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm#)

- Navigate to the Instance pools list page. If you need help finding the list page, see[Listing Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instance-pools-list.htm).
- From the Actions menu (three dots) for the instance pool which contains the instances you want to stop.
- Select Stop .

By default, the Console gracefully stops the instances by sending a shutdown command to the operating system. After waiting 15 minutes for the OS to shut down, the instances are powered off.
Note  
  
If the applications that run on the instances take more than 15 minutes to shut down, then they could be improperly stopped, resulting in data corruption. To avoid this,[shut down the instances using the commands available in the OS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm#Stopping_and_Starting_the_Instances_in_an_Instance_Pool)before you stop the instances using the Console.

Stop Immediately

If you want to stop the instances immediately, without waiting for the OS to respond, select the Force stop the instance pool by immediately powering off every instance in the pool check box.

Select Stop instance pool .

[To reboot all instances in a pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm#)

- Navigate to the Instance pools list page. If you need help finding the list page, see[Listing Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/instance-pools-list.htm).
- From the Actions menu (three dots) for the instance pool which contains the instances you want to reboot.
- Select Reboot .
- 

By default, the Console gracefully restarts the instances by sending a shutdown command to the operating system. After waiting 15 minutes for the OS to shut down, the instances are powered off and then powered back on.
Note  
  
If the applications that run on the instances take more than 15 minutes to shut down, they could be improperly stopped, resulting in data corruption. To avoid this,[shut down the instances using the commands available in the OS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstancepool.htm#Stopping_and_Starting_the_Instances_in_an_Instance_Pool)before you restart the instance using the Console.

Reboot Immediately

If you want to reboot the instances immediately, then without waiting for the OS to respond, select the Force reboot the instance pool by immediately powering off every instance in the pool, then powering them back on check box.

Select Reboot instance pool .
- 

To manage the lifecycle state of the instances in an instance pool using the CLI, open a command prompt and run any of the following commands.

To start (power on) the instances in the specified instance pool, use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/start.html)instance-pool start`command:

```

```

To stop (immediate power off) the instances in the specified instance pool, use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/stop.html)instance-pool stop`command:

```

```

To softstop (ACPI shutdown) the instances in the specified instance pool, use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/softstop.html)instance-pool softstop`command:

```

```

To reset (immediate power off and power on) the instances in the specified instance pool, use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/reset.html)instance-pool reset`command:

```

```

To softreset (ACPI shutdown and power on) the instances in the specified instance pool, use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/softreset.html)instance-pool softreset`command:

```

```

To specify your CLI options using JSON:

```

```

&lt;file://path/to/file.json&gt; is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see[Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).

For a complete list of flags and variable options for the Compute service CLI commands, see the[command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To manage the lifecycle state of the instances in an instance pool with the API, use the following operations:
- [StartInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/StartInstancePool)
- [StopInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/StopInstancePool)
- [SoftstopInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/SoftstopInstancePool)
- [ResetInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/ResetInstancePool)
- [SoftresetInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/SoftresetInstancePool)
