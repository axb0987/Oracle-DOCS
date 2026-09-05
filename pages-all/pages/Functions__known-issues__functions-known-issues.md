# Known Issues for OCI Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/known-issues/functions-known-issues.htm
- Fetched: 2026-09-05 02:09 CDT

# Known Issues for OCI Functions

Known issues have been identified in OCI Functions.

## A function fails to connect to a VM in a subnet assigned a CIDR block of 172.17.0.0/16
Details

When a function attempts to connect to a virtual machine (VM) instance that resides in a subnet that has been assigned an IPv4 CIDR block of 172.17.0.0/16, the function fails to establish the connection to the VM instance. Background

OCI Functions uses a bridge network, which is a virtual network that enables containers connected to the same bridge network to communicate with each other. The default bridge network typically uses a subnet that has been assigned an IPv4 CIDR block of 172.17.0.0/16.

If a function attempts to connect to a VM instance residing in a subnet that has also been assigned an IPv4 CIDR block of 172.17.0.0/16, an IP address conflict occurs that prevents the function connecting to the VM. Workaround

Assign an IPv4 CIDR block to the subnet in which the VM resides that is something other than 172.17.0.0/16. For example, 10.0.1.0/24 , 172.18.20.64/28.

## A Go or dotnet function fails to deploy in a Cloud Shell session based on ARM (aarch64)
Details

If you have built a function using the Go FDK or the dotnet FDK in a Cloud Shell session, and the Cloud Shell session is based on the ARM (aarch64) architecture, when you attempt to deploy the function using the Fn Project CLI, the command fails with the following message:
```

```
Background

At the time of writing, Cloud Shell uses Oracle Linux 7 as its base image. However, when Oracle Linux 7 runs on the ARM architecture, Oracle Linux 7 fails to map the shared libraries for the Go and dotnet FDKs. As a result, the Fn Project CLI command fails with the`Failed to map segment from shared object`message. Workarounds

The failure to map the shared libraries is addressed in Oracle Linux 8. When Cloud Shell migrates from Oracle Linux 7 to Oracle Linux 8 (currently planned for the end of 2024), the issue with functions built using Go and dotnet FDKs will be resolved. In the meantime, consider the following workarounds:
- Option 1: Change Cloud Shell architecture to X86_64

If you have the flexibility to switch the architecture of your Cloud Shell session from ARM (aarch64) to X86_64, then do so.
- Option 2: Use an ARM-based VM that uses an Oracle Linux 8 image

If you do not have the flexibility to change the architecture of your Cloud Shell session from ARM (aarch64) to X86_64, then consider using an ARM-based VM that uses an Oracle Linux 8 image. Here are some high-level instructions:
- Create an ARM-based VM that uses an Oracle Linux 8 image (see[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm)).
- Set up the VM to run OCI Functions (see[Functions QuickStart on an OCI Compute Instance](https://docs.oracle.com/en-us/iaas/Content/Functions/known-issues/../Tasks/functionsquickstartocicomputeinstance.htm)).
- Build and deploy the function on the VM (see[Functions QuickStart on an OCI Compute Instance](https://docs.oracle.com/en-us/iaas/Content/Functions/known-issues/../Tasks/functionsquickstartocicomputeinstance.htm)).
