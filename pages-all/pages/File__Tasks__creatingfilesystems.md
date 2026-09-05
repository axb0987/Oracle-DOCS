# Creating File Systems
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/creatingfilesystems.htm
- Fetched: 2026-09-05 02:03 CDT

# Creating File Systems

You can create a shared file system in the cloud using the File Storage service. Network access to your file system is provided through a[mount target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm). Exports control how NFS clients access file systems when they connect to a mount target. File systems must have at least one export in one mount target for any instance to[mount](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/mountingfilesystems.htm)and use the file system. When you[use the Console to create your first file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-file-system.htm), the workflow also creates a mount target and export for it.

## Prerequisites

Before you create a file system, you need:
- At least one Virtual Cloud Network (VCN) in a compartment. For more information, see[VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm).
- We recommend that the VCN contains a subnet dedicated to file system mount targets so that other resources don't use the IP addresses that might be needed by mount targets. For more information, see[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managingmounttargets.htm#limitations)for mount targets.
- Correctly configured security rules for the file system mount target. Security rules can be created in the security list for the mount target subnet, or in a Network Security Group (NSG) that you add the mount target to. See[Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm)for information about how security rules work in Oracle Cloud Infrastructure. Use the instructions in[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm)to set up security rules correctly for file systems.

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users create, manage, and delete file systems](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#general-file-system-management)allows users to create file systems. Since mount targets are network endpoints, users must also have "use" permissions for VNICs, private IPs, private DNS zones, and subnets to create or delete a mount target. See the[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference.htm)for more information.

If you're planning to encrypt file systems using your own keys, see the policies in[Encrypting a File System](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/encrypt-file-system.htm).

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Details for the File Storage Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/filestoragepolicyreference.htm)
