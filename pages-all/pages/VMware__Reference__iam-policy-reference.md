# VMware Solution Identity and Access Management (IAM) Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Reference/iam-policy-reference.htm
- Fetched: 2026-09-05 03:07 CDT

# VMware Solution Identity and Access Management (IAM) Policies

Learn how to write OCI IAM policies to control access to Oracle Cloud VMware Solution resources.

By default, only the users in the`Administrators`group can access all resources and functions in VMware Solution. To control non-administrator user access to VMware Solution resources and functions, you create IAM groups and then write policies that give the groups proper access.

If you need a complete list of Oracle Cloud Infrastructure policies, see the[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference.htm).

## Resource-Types

`sddcs`

## Supported Variables

Only the general variables are supported (see[General Variables for All Requests](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm)).

## Details for Verb + Resource-Type Combinations

The following tables show the[permissions](https://docs.oracle.com/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi)and API operations covered by each verb for VMware Solution. The level of access is cumulative as you go from`inspect`to`read`to`use`to`manage`. A plus sign`(+)`in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

### sddcs

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

SDDC_INSPECT

`ListSddcs`

`ListWorkRequests`

none
read

INSPECT +

SDDC_READ

INSPECT +

`GetSddc`

`GetWorkRequest`

none
use

READ +

SDDC_UPDATE

SDDC_UPDATE_ESXI_HOST

READ +

`UpdateSddc`

`UpdateEsxiHost`

none
manage

USE +

SDDC_CREATE

SDDC_MOVE

SDDC_ADD_ESXI_HOST

SDDC_DELETE_ESXI_HOST

SDDC_DELETE

USE +

`ChangeSddcCompartment`

`CreateSddc`(also need`manage instances`,`manage vcns`,`use subnets`,`use vnics`,`use vlans`,`use private-ips`,`inspect security-lists`,`use network-security-groups`)

`DeleteSddc`,`CreateEsxiHost`,`DeleteEsxiHost`(also need`manage instances`,`manage vcns`,`use subnets`,`use vnics`,`use vlans`,`use private-ips`)

## Permissions Required for Each API Operation

The following table lists the API operations in a logical order, grouped by resource type.

API Operation Permissions Required to Use the Operation
`ListSddcs`SDDC_INSPECT
`GetSddc`SDDC_READ
`CreateSddc`SDDC_CREATE &amp; INSTANCE_CREATE &amp; INSTANCE_ATTACH_SECONDARY_VNIC &amp; VCN_READ &amp; VCN_ATTACH &amp; SUBNET_READ &amp; SUBNET_ATTACH &amp; VNIC_READ &amp; VNIC_CREATE &amp; VLAN_READ &amp; VLAN_ATTACH &amp; PRIVATE_IP_CREATE &amp; PRIVATE_IP_ASSIGN &amp; SECURITY_LIST_READ &amp; NETWORK_SECURITY_GROUP_LIST_SECURITY_RULES
`ListWorkRequests`SDDC_INSPECT
`GetWorkRequest`SDDC_READ
`ChangeSddcCompartment`SDDC_MOVE
`UpdateSddc`SDDC_UPDATE
`DeleteSddc`SDDC_DELETE &amp; INSTANCE_DELETE &amp; INSTANCE_DETACH_SECONDARY_VNIC &amp; VCN_DETACH &amp; SUBNET_DETACH &amp; VLAN_DETACH &amp; VNIC_READ &amp; VNIC_DELETE &amp; PRIVATE_IP_DELETE &amp; PRIVATE_IP_UNASSIGN
`ListEsxiHosts`SDDC_INSPECT
`CreateEsxiHost`

SDDC_ADD_ESXI_HOST &amp; INSTANCE_CREATE &amp; INSTANCE_ATTACH_SECONDARY_VNIC &amp; VCN_READ &amp; VCN_ATTACH &amp; SUBNET_READ &amp; SUBNET_ATTACH &amp; VLAN_READ &amp; VLAN_ATTACH &amp; VNIC_READ &amp; VNIC_CREATE &amp; PRIVATE_IP_CREATE &amp; PRIVATE_IP_ASSIGN
`UpdateEsxiHost`SDDC_UPDATE_ESXI_HOST
`DeleteEsxiHost`SDDC_DELETE_ESXI_HOST &amp; INSTANCE_DELETE &amp; INSTANCE_DETACH_SECONDARY_VNIC &amp; VCN_DETACH &amp; SUBNET_DETACH &amp; VLAN_DETACH &amp; VNIC_READ &amp; VNIC_DELETE &amp; PRIVATE_IP_DELETE &amp; PRIVATE_IP_UNASSIGN

## Creating a Policy

To create policies for a group of users, you need to know the name of the Oracle Cloud Infrastructure IAM group.

To create a policy:

- In the Console navigation menu, select Identity &amp; Security , then under Identity , select Policies .
- Select Create Policy .
- Enter a Name and Description (optional) for the policy.
- Select the Compartment in which to create the policy.
- Select Show manual editor . Then enter the policy statements you need.
- (Optional) Select Create Another Policy to remain in the Create Policy page after creating this policy.
- To create this policy, select Create .

## Common Policies

### Let users create, manage, and delete SDDCs, ESXi hosts, and VLANs

Type of access: Ability to create, manage, or delete an SDDC, ESXi host, or VLANs.

Where to create the policy : In the tenancy, so that the ability to create, manage, or delete a VMware Solution resource is easily granted to all compartments by way of policy inheritance. To reduce the scope of these administrative functions to SDDCs in a particular compartment, specify that compartment instead of the tenancy.

This policy example also includes permissions for compute and network resources. These compute and network resources are required to create, manage, or delete SDDCs, ESXi hosts, or VLANs. The minimum required permission is shown for each.

```

```
