# Adding Security Attributes to a Mount Target
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/zpr-mount-target.htm
- Fetched: 2026-09-05 02:05 CDT

# Adding Security Attributes to a Mount Target

Use Zero Trust Packet Routing with a mount target.
You can use Zero Trust Packet Routing (ZPR) along with or in place of network security groups to manage network access to OCI resources . To do this, define ZPR policies that govern how resources communicate with each other, and then add security attributes to those resources. For more information, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
Caution  
  
If an endpoint has a Zero Trust Packet Routing (ZPR) security attribute, traffic to the endpoint must satisfy ZPR policies and also all NSG and security list rules. For example, if you're already using NSGs and you add a security attribute to an endpoint, all traffic to the endpoint is blocked. From then onward, a ZPR policy must explicitly allow traffic to the endpoint.

## Required IAM Policy

To use ZPR with File Storage mount targets, create an IAM policy that grants the File Storage service permission to inspect and use the security attribute namespace required by ZPR.

For example, you can use the following policy:

```

```

The name of the File Storage service user depends on your realm . For realms with realm key numbers of 10 or less, the pattern for the File Storage service user is`FssOc <n> Prod`, where n is the realm key number. Realms with a realm key number greater than 10 have a service user of`fssocprod`. For more information about realms, see[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About).

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/zpr-mount-target.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/zpr-mount-target.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/zpr-mount-target.htm#)
- 

- On the File Storage mount targets list page, select the File Storage mount target that you want to work with. If you need help finding the list page or the File Storage mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-mount-targets.htm).
- On the details page, select Security tab and then select Add security attribute .
- In the Add security attribute panel, enter the following information:

- Security attribute namespace : A security attribute namespace is a container for a set of security attributes in Zero Trust Packet Routing (ZPR).
- Security attribute key : The name for a specific security attribute.
- Security attribute value : The value for a specific security attribute.

These values must match an existing ZPR policy. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm).
- When finished, select Add security attributes .
- 

Use the[`fs mount-target update`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/update.html)command and required parameters to add security associations to a mount target:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/UpdateMountTarget)operation to add security associations to a mount target.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
