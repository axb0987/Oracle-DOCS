# Adding or Removing a Resource from an NSG
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/nsg-add_remove_resource.htm
- Fetched: 2026-09-05 02:41 CDT

# Adding or Removing a Resource from an NSG

Describes how to add or remove a resource from a network security group (NSG).

In general, you manage the resource membership of an NSG at the[parent resource](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison), and not at the NSG itself. Therefore, to add a parent resource to an NSG, you perform the action on the parent resource (by specifying which NSGs to add the parent resource to). You don't perform the action on the NSG (by specifying which VNICs or parent resources to add to the NSG). Similarly, to remove a VNIC from an NSG, you perform that action by updating the parent resource, not the NSG. For a list of the parent resources that support the use of NSG, see[Support for Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#support).

[Example: Compute Instances](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/nsg-add_remove_resource.htm#)

- When creating an instance: In the Networking section, under the advanced options, select Use network security groups to control traffic . Then, specify one or more NSGs. The instance's primary VNIC is added to the NSGs. See the procedure in[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
- For an existing instance: Adding an existing instance to an NSG means adding its primary VNIC to the NSG. You can also add a secondary VNIC to an NSG. See[Adding or Removing a VNIC from a Network Security Group](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/../Tasks/managingvnics_tasks-nsg.htm).

[Example: Exadata Cloud VM Cluster](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/nsg-add_remove_resource.htm#)

- When creating an Exadata cloud VM cluster: In the Network Information section, you set up the client network and backup network. For each network, select Use network security groups to control traffic , and then specify one or more NSGs for the specific network. See[To create a cloud VM cluster resource](https://docs.oracle.com/iaas/exadatacloud/exacs/ecs-create-instance.html#GUID-11C092BB-2B85-4342-B143-8FC5FC80ECA3). Also see[Network Setup for Exadata Cloud Service Instances](https://docs.oracle.com/iaas/exadatacloud/exacs/ecs-network-setup.html).
-
