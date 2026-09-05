# Editing an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-instance.htm
- Fetched: 2026-09-05 01:51 CDT

# Editing an Instance

You can edit the properties of a compute instance without having to rebuild the instance or redeploy your applications. When you edit an instance, the instance's OCID remains the same.

On supported instances, the following edits can be made:
- [Renaming an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/renaminginstance.htm)
- [Changing the Capacity Reservation for an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/editingcapacityreservation.htm)
- [Changing the Shape of an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resizinginstances.htm)
- [Changing the Windows License Type of an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/changewinlicense.htm)
- [Editing the Fault Domain for an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-fault-domain.htm)
- [Editing the Launch Options for an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-launch-options.htm)
- [Enabling In-Transit Encryption Between an Instance and Boot Volumes or Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enable-intransit-encryption.htm)
- [Setting Instance Availability During Maintenance Events](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-maintenance-recovery-action.htm)

## Required IAM Policy

To use OCI resources, you must be granted security access in a policy (IAM) by an administrator. This access is required whether you're using the Console, the CLI, or the REST API. If you get a message that you don't have permission or are unauthorized, verify with your administrator you have the correct security access for your compartment .

The simplest policy to let users[create](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/launchinginstance.htm),[edit](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/edit-instance.htm), and[terminate (delete)](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/terminatinginstance.htm)instances is[Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances). The policies give the specified group general access to manage instances and images and access to attach existing block volumes to instances.
If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see[Details for Core Services](https://docs.oracle.com/iaas/Content/Identity/Reference/corepolicyreference.htm).

## Applying Tags

Apply tags to resources to help organize them according to your business needs. You can apply tags when you create a resource, and you can update a resource later to add, revise, or remove tags. For general information about applying tags, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
