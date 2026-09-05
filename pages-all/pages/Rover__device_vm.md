# Configuring Your Host to Run CLI commands on Device-Hosted Instances
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/device_vm.htm
- Fetched: 2026-09-05 03:02 CDT

# Configuring Your Host to Run CLI commands on Device-Hosted Instances

Configure your host computer to run the OCI command line interface (CLI) on its compute instances.

Follow these guidelines for running CLIs on compute instances hosted by Roving Edge Infrastructure devices.

Note  
  

The instructions in this topic are for Oracle Linux host computers.
- 

Have the instance go through the following local IP:

`169.254.169.254`

Have the instance refer to the Roving Edge device as`otec-console-local`.

For example, add the following entry to the instance's`/etc/hosts`file:
```

```

- 

Employ the following IP Tables rules:
```

```

See[Service Ports](https://docs.oracle.com/iaas/Content/Rover/device_specifications.htm#ServicePorts)for a list of available ports.

Save the iptable so that the rules persist after a reboot:
```

```

## Unsupported CLI Commands

The following CLI commands are currently not supported. Workarounds are provided where available.
- 

Object Storage CLIs :`oci os list`

You can only use the`oci os list`command when you include the`--fields`option. For example:
```

```

- 

Compute CLIs :`oci compute instance list-vnics`

The`oci compute instance list-vnics`command lists the VNICs that are attached to the specified instance and is often used to get the public IP for a compute node. This CLI is not currently supported in Roving Edge Infrastructure. You can get VNIC information, including IP address associated with a VNIC attached to a compute node, using any of the following methods:

- 

Device Console : Go to the following location:

Compute &gt; Instances &gt; Instance Details &gt; Attached VNICs

The IP addresses for the VNICs are listed in the dialog box that appears.
- 

CLI :`oci compute instance list-vnics`

First, run the following command to list all the VNIC's attachments:
```

```

Next, run the following command for the specific VNIC for which you want to get details:
```

```

The following example shows these two commands run together with their respective returns:
```

```

If only one VNIC is attached, you can combine these CLI commands with other Linux tools to limit the output to just the public IP address using the following command:
```

```

For example:
```

```
