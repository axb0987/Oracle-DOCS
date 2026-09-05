# Creating a Mount Target
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-mount-target.htm
- Fetched: 2026-09-05 02:03 CDT

# Creating a Mount Target

Create a File Storage mount target.

When you[create a new file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-file-system.htm), you can create a mount target and export for the file system. You can also create a mount target later for file systems in a specified compartment and subnet. If you need a[high performance mount target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#performance), create a standard mount target, then[upgrade its performance level](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-mt-performance.htm). A file system can only be associated with a mount target in the same availability domain.

## Choosing the Subnet for a Mount Target

Each mount target, during creation, requires three IP addresses in the subnet. We recommend using a subnet that's dedicated to mount targets so that instances or other resources don't use the IP addresses that mount targets need.
Caution  
  
Don't use /30 or smaller subnets for mount target creation because they don't have enough available IP addresses. A /28 subnet with 13 available IP addresses could support four mount targets if dedicated for that purpose.

For more information, see[Mount Target Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#limitations)and[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm).

[Searching a subnet for used IP addresses](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-mount-target.htm#)

You can use the CLI to search for used IP addresses, including those used by mount targets. To find the IP addresses in a subnet that are used by mount targets, use the following command:

```

```

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-mount-target.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-mount-target.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-mount-target.htm#)
- 

- On the Mount Targets list page, select Create mount target . If you need help finding the list page or the mount target, see[Listing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-mount-targets.htm).
- 

In the Create mount target panel, provide the following details:
- New mount target name : Replace the default with a friendly name for the mount target. It doesn't have to be unique - an Oracle Cloud Identifier (OCID) uniquely identifies the mount target. Avoid entering confidential information.
Note  
  
The mount target name is different than the DNS hostname, which is specified in the advanced options.
- Compartment : Specify the compartment in which you want to create the file system.
- Availability domain : The AD in which to create the mount target.
Note  
  
While it's possible to access mount targets from any AD in a region, for best performance, the mount targets should be in the same availability domain as the Compute instances that access them. For more information, see[Regions and Availability Domains](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/filestorageoverview.htm#Regions).
- Virtual cloud network compartment : The compartment containing the cloud network (VCN) in which to create the mount target.
- Virtual cloud network : Select the cloud network (VCN) where you want to create the new mount target.
- Subnet compartment : Specify the compartment containing a subnet within the VCN to attach the mount target to.
- 

Subnet : Select a subnet to attach the mount target to. Subnets can be either AD-specific or regional (regional ones have " regional" after the name). Subnets can support IPv4 or IPv6. For more information, see[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)
Note  
  
We recommend using a subnet that's dedicated to mount targets so that instances or other resources don't use the IP addresses that mount targets need. For more information, see[Choosing the Subnet for a Mount Target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-mount-target.htm#subnet-selection).
- 

Use network security groups to control traffic: Select this option to add this mount target to an existing NSG. Select an NSG from the list.
Note  
  
Rules for the NSG you select must be configured to allow traffic to the mount target's VNIC using specific protocols and ports. For more information, see[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm).
- 

(Optional) IP details : Configure the mount target's IP details:
- IP address : You can specify an unused IP address in the subnet you selected for the mount target. If the subnet uses dual-stack IPv4/IPv6 addressing, or single-stack IPv6 addressing, you can specify an IPv6 address. For more information, see[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/managingmounttargets.htm#limitations)for Mount Targets and[IPv6 Addresses](https://docs.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).
- 

Hostname : Specify a hostname you want to assign to the mount target.
Note  
  

The File Storage service constructs a fully qualified domain name (FQDN) by combining the hostname with the FQDN of the subnet the mount target is located in.

For example,`myhostname.subnet123.dnslabel.oraclevcn.com`.

After the mount target is created, the hostname may be changed in the mount target's details page. For more information, see[Managing Mount Targets](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm).
Note  
  
If enabling[Kerberos authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm)for a mount target in a VCN that uses the default Internet and VCN Resolver for DNS, you must specify a hostname.
- (Optional) Tags : To add tags to the mount target, select Tagging .

If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- (Optional) Show security attributes : Add up to three security attributes to restrict access to the mount target, select . If you have permissions to create a resource, then you might also have permissions to add security attributes to that resource. To add a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.
- In the Resource locks section, select a lock level for the resource:
- No Lock : No restrictions.
- Delete : Prevents the resource from being deleted.
- Full : Prevents all modifications except reading the resource.
- To create the mount target, select Create .
- (Optional) To save the configuration as a Resource Manager stack, select Save as stack . For more information, see[Managing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/stacks.htm).
- 

Use the[`fs mount-target create`](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/create.html)command and required parameters to create a mount target:

```

```

Avoid entering confidential information.

Use the`--nsg-ids`parameter to add the mount target to a NSG. For example:`--nsg-ids '["<nsg_OCID_1>","<nsg_OCID_2"]'`.
Note  
  
The only accepted value for the`--requested-throughput`parameter when creating a mount target is 1. To change a mount target's performance level, see[Updating Mount Target Performance](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-mt-performance.htm).
Use the`--ip-address`parameter to assign an IP address to the mount target. If the subnet uses dual- stack IPv4/IPv6 addressing, or single-stack IPv6 addressing, you can specify an IPv6 address, such as`2001:db8:0123:7811:abcd:ef01:2345:6789`. For example:
```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[CreateMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/CreateMountTarget)operation to create a mount target.
Note  
  
The only accepted value for the`requestedThroughput`attribute when creating a mount target is 1. To change a mount target's performance level, see[Updating Mount Target Performance](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/change-mt-performance.htm).

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
