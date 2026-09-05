# Instance Creation Fails with the "IP address... has already been allocated for the subnet" Error
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/instance-creation-ip-allocated.htm
- Fetched: 2026-09-05 02:06 CDT

# Instance Creation Fails with the "IP address... has already been allocated for the subnet" Error

When creating an instance, the operation can fail with a "The IP address X.X.X.X has already been allocated for the subnet..." error.

When you search for the IP address in the Console, it shows that the IP address is being used by a File Storage mount target.

Cause : Each mount target requires three internal IP addresses in the subnet to function. In this case, the IP address of the instance to be created was already taken by a mount target, so the instance creation failed.

You can use the CLI to search for used IP addresses. Use the following command to find all used IP addresses in a subnet:

```

```

To find all internal IP addresses in a subnet that are used by mount targets, use the following command:

```

```

For more information, see[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/managingmounttargets.htm#limitations).

Solution : Keep mount targets and Compute instances in different subnets to avoid this situation. For more information, see[File Storage Security Rule Scenarios](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm#File_Storage_Security_Rule_Scenarios)
