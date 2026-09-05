# Stopping an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-stop-instance.htm
- Fetched: 2026-09-05 01:52 CDT

# Stopping an Instance

You can stop an instance using OCI tools or from the operating system.

## Shutting Down or Restarting an Instance Using the Instance's OS

You can shut down and restart instances using the commands available in the OS when you're signed in to the instance. Shutting down an instance using the instance's OS doesn't[stop billing](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resource-billing-stopped-instances.htm)for that instance. If you shut down an instance this way, be sure to also stop it from the Console or API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-stop-instance.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-stop-instance.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-stop-instance.htm#)
- 

- Navigate to the Compute Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).
- From the Actions menu (three dots) for the instance, select Stop .

By default, the Console gracefully restarts the instance by sending a shutdown command to the OS. The system waits for up to 15 minutes for the OS to shut down. The instance is powered off and then powered back on.
Note  
  
If the applications that run on the instance take more than 15 minutes to shut down, improperly stopping them might result in data corruption. To avoid this,[shut down the instance using the commands available in the OS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-stop-instance.htm#operatingsystem)before you stop the instance using the Console.
Caution  
  
To stop the instance immediately, without waiting for the OS to respond, select the Force stop the instance by immediately powering off checkbox. Improperly stopping an instance might result in data corruption.
- Select Stop instance .
- 

Use the[instance action](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/action.html)command and required parameters to stop an instance:

```

```

To power off the instance immediately, use the`STOP`action.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[InstanceAction](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/InstanceAction)operation to stop an instance, passing the value`SOFTSTOP`as the action to perform.

To power off the instance immediately, use the`STOP`
