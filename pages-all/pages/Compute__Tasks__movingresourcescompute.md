# Moving Compute Resources to a Different Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movingresourcescompute.htm
- Fetched: 2026-09-05 01:52 CDT

# Moving Compute Resources to a Different Compartment

You can move Compute resources such as instances, instance pools, and custom images from one compartment to another.

When you move a Compute resource to a new compartment, associated resources such as boot volumes and VNICs are not moved.

After you move the resource to the new compartment, inherent policies apply immediately and affect access to the resource through the Console. For more information, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The following policies allow users to move Compute resources to a different compartment:

```

```

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

## Security Zones

[Security Zones](https://docs.oracle.com/iaas/Content/security-zone/home.htm)ensure that cloud resources comply with Oracle security principles. If any operation on a resource in a security zone compartment violates a[policy for that security zone](https://docs.oracle.com/iaas/Content/security-zone/using/security-zone-policies.htm), then the operation is denied.

The following security zone policies affect your ability to move Compute resources from one compartment to another:
- You can't move a compute instance from a security zone to a compartment that is not in the same security zone.
- You can't move a compute instance to a security zone from a compartment that is not in the same security zone.

## Moving Compute Resource Links

The following Compute resources support move operations.
- [Moving an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/inst-move.htm)
- [Moving a Dedicated Virtual Machine Host to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/dvmh-move_tabs.htm)
- [Moving an Instance Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Concepts/instance_config_moving.htm)
- [Moving an Instance Pool to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instance-pools-move.htm)
- [Moving a Cluster Network](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/cluster-networks-move.htm)
- [Moving a Compute Cluster to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/move-compartment-compute-cluster.htm)
- [Moving a Capacity Reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/capacity-reservations-move.htm)
- [Moving a Custom Image to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-move.htm)

[Moving an Autoscaling Configuration to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movingresourcescompute.htm#)

Using the Console
- Open the navigation menu and select Compute . Under Compute , select Autoscaling Configurations .
- In the List Scope section, select a compartment.
- Click the autoscaling configuration that you're interested in.
- Click Move resource .
- Choose the destination compartment from the list.
- Click Move Resource .

Using the API

Change an autoscaling configuration's compartment with the following API call:[ChangeAutoScalingConfigurationCompartment](https://docs.oracle.com/iaas/api/#/en/autoscaling/latest/AutoScalingConfiguration/ChangeAutoScalingConfigurationCompartment)
