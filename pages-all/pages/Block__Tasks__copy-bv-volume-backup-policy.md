# Duplicating a Backup Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copy-bv-volume-backup-policy.htm
- Fetched: 2026-09-05 01:45 CDT

# Duplicating a Backup Policy

Make an editable copy of an existing backup policy. Both Oracle-defined and user-defined backup policies can be duplicated. Use the Console.

- On the Backup Policies list page, find the backup policy that you want to work with. If you need help finding the list page or the backup policies, see[Listing Backup Policies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/../Tasks/list-backup-policies.htm).
- From the Actions menu (three dots) , select Duplicate This Backup Policy .
- On the Duplicate backup policy page, enter the following information.

- Name : Specify a name for the policy. Avoid entering confidential information.
- Duplicate into Compartment : Select the compartment to create the backup policy in. It doesn't need to be the same compartment as the backup policy you're duplicating.
- Cross region copy target : (Optional) Select a region to enable cross region copy. This function automates the copying of the volume backup to a second region that you specify after each backup is created. For more information, see[Scheduling Volume Backup Copies Across Regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#CrossRegionCopy).

Select the checkbox to acknowledge the warning.

When you assign a backup policy with cross region copy enabled to a volume, you can optionally select Encrypt using customer-managed keys for Cross region backup copy encryption to encrypt the volume backup with a Vault key from the destination region. See[Cross-Region Backup Copies](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/assign-encryption-key.htm#xrr-backup)for more information.
- Tags : (Optional) Select Tags to add tags to the backup policy. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
-
