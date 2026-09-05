# Moving Block Volume Resources Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/moveblockresourcecompartments.htm
- Fetched: 2026-09-05 01:47 CDT

# Moving Block Volume Resources Between Compartments

Move resources to different compartments.

You can move Block Volume resources such as block volumes, boot volumes, volume backups, volume groups, and volume group backups from one compartment to another. When you move a Block Volume resource to a new compartment, associated resources are not moved. After you move the resource to the new compartment, inherent policies apply immediately and affect access to the resource through the Console. For more information, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).
Important  
  
When moving Block Volume resources between compartments you need to ensure that the resource users have sufficient access permissions on the compartment the resource is being moved to.

## Tasks

- [Moving a Block Volume to Another Compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changecompartmentblockvolume.htm)
- [Moving a Boot Volume to Another Compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-boot-volume-compartment-bv-boot-volume.htm)
- [Moving a Volume Group Backup to Another Compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-volume-group-backup-compartment-bv-volume-group-backup.htm)
- [Moving a Block Volume Backup to Another Compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-volume-backup-compartment-bv-volume-backup.htm)
- [Moving a Boot Volume Backup to Another Compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/change-boot-volume-backup-compartment-bv-boot-volume-backup.htm)
- [Moving a Volume Group to Another Compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Concepts/change-compartment-volume-group.htm)

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The following policies allow users to move Block Volume resources to a different compartment:

```

```

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

## Security Zones

[Security Zones](https://docs.oracle.com/iaas/Content/security-zone/home.htm)ensure that your cloud resources comply with Oracle security principles. If any operation on a resource in a security zone compartment violates a[policy for that security zone](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm), then the operation is denied.

The following security zone policies affect your ability to move Block Volume resources from one compartment to another:
- You can't move a block volume or boot volume from a security zone to a compartment that is not in the security zone.
-
