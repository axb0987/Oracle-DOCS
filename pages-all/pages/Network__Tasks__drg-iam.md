# IAM Policies for Routing Between VCNs
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm
- Fetched: 2026-09-05 02:44 CDT

# IAM Policies for Routing Between VCNs

Learn about IAM policies used with peering and dynamic routing gateways.

For more general IAM policies used in networking, see[IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/overview.htm#Policies).

For IAM policies specific to local or remote peering using DRGs, see:
- [Remote Peering with DRG (in the Same Tenancy)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__remote-peer-policy)
- [Remote Peering with DRG (Different Tenancies)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__IAM_cross-tenancy)

For IAM policies specific to local peering using LPGs, see:
- [Local Peering using an LPG (VCNs in the Same Tenancy)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__local-LPG)
- [Local Peering using an LPG (VCNs in Different Tenancies)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__local-LPG-xten)

For IAM policies specific to attaching DRGs and VCNs, see:
- [Attaching to VCNs in the Same Tenancy](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__VCN-attachments)
- [Attaching to VCNs in Other Tenancies](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__xtenancy-VCN)

## Controlling the Establishment of Peerings

With IAM policies, you can control:
- Who can[subscribe your tenancy to another region](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm)(required for remote VCN peering).
- Who in an organization has the authority to establish VCN peerings (for example, see the IAM policies in[Setting Up a Local Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Setting)and[Setting Up a Remote Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Setting)). Deletion of these IAM policies doesn't affect any existing peerings, only the ability for future peerings to be created.
- For local VCN peering through a mutually attached DRG in the same tenancy and region, no special IAM policies are needed. Whether peering can occur with VCNs in a different tenancy (which might belong to your organization, Oracle, or a third party) would require special policy statements to enable cross-tenancy peering. In the statements, you can specify which particular tenancy. For local VCN peering through a mutually attached DRG in a different tenancy but the same region, see[Attaching to VCNs in Other Tenancies](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__xtenancy-VCN). For remote VCN peering (possibly to a different tenancy), see[Remote Peering with DRG (in the Same Tenancy)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__remote-peer-policy).
- Who can[manage route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm)and[security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/../Concepts/securitylists.htm).

## Explicit Agreement Required from Both Sides

Peering and transit routing involve two VCNs owned by the same party or two different ones. The two parties might both be in the same company but in different departments. Or the two parties might be in entirely different companies (for example, in a service-provider model). See[Accessing Object Storage Resources Across Tenancies](https://docs.oracle.com/iaas/Content/Object/Concepts/accessingresourcesacrosstenancies.htm)for further examples of cross-tenant policies.

The agreement is in the form of Oracle Cloud Infrastructure Identity and Access Management policies that each party implements for their own VCN's compartment or tenancy. If the VCNs are in different tenancies, each administrator must provide their tenancy[OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)and put in place special policy statements to enable the peering. For details on the IAM policies required to connect to a VCN in another tenancy, see[Remote Peering with DRG (Different Tenancies)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__IAM_cross-tenancy).

## Endorse, Admit, and Define Statements

Here's an overview of the verbs used in these statements:
- Endorse : States the general set of abilities that a group in your own tenancy can perform in other tenancies. The`Endorse`statement always belongs in the tenancy that contains the group of users crossing the boundaries into the other tenancy to work with that tenancy's resources. In the examples, we call this tenancy the source tenancy.
- Admit : States the kind of ability in your own tenancy that you want to grant a group from the other tenancy. The`Admit`statement belongs in the tenancy granting "admittance" to the tenancy. The`Admit`statement identifies the group of users that requires resource access from the source tenancy and is identified with a corresponding`Endorse`statement. In the examples, we call this tenancy the destination tenancy.
- 

Define : Assigns a local alias to a tenancy OCID for`Endorse`and`Admit`policy statements. A`Define`statement is also required in the destination tenancy to assign an alias to the source IAM group OCID for`Admit`statements.

Include a`Define`statement in the same policy entity as the`Endorse`or`Admit`statement.

The`Endorse`and`Admit`statements work together. An`Endorse`statement resides in the source tenancy while an`Admit`statement resides in the destination tenancy. Without a corresponding statement that specifies access, a particular`Endorse`or`Admit`statement grants no access. Both tenancies must agree on access.
Important  
  
In addition to policy statements, you must also subscribe to a region to share resources across regions.

## Remote Peering with DRG (in the Same Tenancy)

A DRG can connect to another DRG (and any attached VCN) in another region provided the compartments containing the requestor and the acceptor have the corect policies in place. These consist of:
- 

Policy R (implemented by the requestor):

```

```

The requestor is in an IAM group called RequestorGrp . This policy lets anyone in the group start a connection from any DRG in the requestor's compartment ( RequestorComp ). Policy R can be attached to either the tenancy (root compartment) or to RequestorComp . For information about why you would attach it to one compartment or the other, see[Policy Basics](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm#Policy).
- 

Policy A (implemented by the acceptor):

```

```

This policy lets the requestor connect to any RPC in the acceptor's compartment ( AcceptorComp ). This statement reflects the required agreement from the acceptor for the peering to be established. Policy A can be attached to either the tenancy (root compartment) or to AcceptorComp .
[

Both Policy R and Policy A give RequestorGrp access. However, Policy R has a resource-type called remote-peering- from , and Policy A has a resource-type called remote-peering- to . Together, these policies let someone in RequestorGrp establish the connection from an RPC in the requestor's compartment to an RPC in the acceptor's compartment. The API call to create the connection specifies which two RPCs.
Tip  
  
The permission granted by Policy R might already be in place if the requestor has permission in another policy to manage all Networking components in RequestorComp . For example, there might be a general Network Admin policy similar to this:`Allow group NetworkAdmin to manage virtual-network-family in compartment RequestorComp`. If the requestor is in the NetworkAdmin group, then they already have the required permissions covered in Policy R (the virtual-network-family includes RPCs). And further, if the policy is instead written to cover the entire tenancy (`Allow group NetworkAdmin to manage virtual-network-family in tenancy`), then the requestor already has all the required permissions in both compartments to establish the connection. In that case, policy A isn't required.

## Remote Peering with DRG (Different Tenancies)

Both the requestor and acceptor must ensure that the necessary policies are in place. This example shows the minimal identity policies needed to create a cross-tenancy remote peering connection:
- 

Policy R (implemented by the requestor):

```

```

- 

Policy A (implemented by the acceptor):

```

```

## Local Peering using an LPG (VCNs in the Same Tenancy)

In this use case, both VCNs are in the same tenancy. If they're in different tenancies, instead see[Local Peering using an LPG (VCNs in Different Tenancies)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__local-LPG-xten).

Admins for the requestor and acceptor VCNs must ensure that the necessary policies are in place:
- 

Policy R (implemented by the requestor):

```

```

The requestor is in an IAM group called requestorGrp . This policy lets anyone in the group start a connection from any LPG in the requestor's compartment ( requestorComp ). Policy R can be attached to either the tenancy (root compartment) or to requestorComp . For information about why you would attach it to one compartment or the other, see[Policy Basics](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm#Policy).
- 

Policy A (implemented by the acceptor):

```

```

The statements in the policy lets the requestor connect to any LPG in the acceptor's compartment ( acceptorComp ). This statement reflects the required agreement from the acceptor for the peering to be established. Policy A can be attached to either the tenancy (root compartment) or to acceptorComp .
Tip  
  
The statements in Policy A let the requestor list the VCNs and LPGs in acceptorComp . The statements are required for the requestor to use the Console UI to select from a list of VCNs and LPGs in acceptorComp and establish the connection. The following diagram focuses only on the first statement, which is the critical one that allows the connection.
[

Both Policy R and Policy A give requestorGrp access. However, Policy R has a resource-type called local-peering- from , and Policy A has a resource-type called local-peering- to . Together, these policies let someone in requestorGrp establish the connection from an LPG in the requestor's compartment to an LPG in the acceptor's compartment. The API call to create the connection specifies which two LPGs.
Tip  
  

The permission granted by Policy R might already be in place if the requestor has permission in another policy to manage all Networking components in RequestorComp . For example, there might be a general Network Admin policy similar to this:

```

```

If the requestor is in the NetworkAdmin group, then they already have the required permissions covered in Policy R (the virtual-network-family includes LPGs). And further, if the policy is instead written to cover the entire tenancy instead of only compartment requestorComp, then the requestor already has all the required permissions in both compartments to establish the connection. In that case, policy A isn't required.

## Local Peering using an LPG (VCNs in Different Tenancies)

In this use case, the VCNs are in different tenancies (so it's a cross-tenancy peering). If the VCNs are in the same tenancy, instead see[Local Peering using an LPG (VCNs in the Same Tenancy)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__local-LPG).

Both the requestor and acceptor must ensure that the necessary policies are in place:
- 

Policy R (implemented by the requestor):

```

```

The requestor is in an IAM group with an assigned OCID you provide. This policy lets anyone in that group start a connection from any LPG in the requestor's compartment ( requestorComp ).

The first statement is a`Define`statement that assigns a friendly label to the acceptor's tenancy OCID. The statement happens to use "Acceptor" as the label, but it could be a value of the requestor's choice. All`Define`statements in a policy must be the first ones (at the top).

The second statement lets the requestorGrp establish a connection from an LPG in the requestor's compartment.

The`Allow`and`Endorse`statements are special ones required because the LPGs are in different tenancies. They let the requestorGrp connect an LPG in the requestor's tenancy to an LPG in the acceptor's tenancy.

If the intent is to give the requestorGrp permission to connect to an LPG in any tenancy , the policy would instead look similar to this:

```

```

Regardless, Policy R must be attached to the requestor's tenancy (root compartment), and not the requestor's compartment. Policies that enable cross-tenancy access must be attached to the tenancy. For more information about attachment of policies, see[Policy Basics](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm#Policy).
- 

Policy A (implemented by the acceptor):

```

```

Similar to the requestor's policy, this policy first uses`Define`statements to assign friendly labels to the requestor's tenancy OCID and the requestor admin group's OCID. As mentioned earlier, the acceptor could use other values for those labels if wanted.

The fourth and fifth statements let the requestorGrp connect to an LPG in the acceptor's compartment ( acceptorComp ). These statements reflect the critical agreement required for the peering to be established. The word`Admit`indicates that the access applies to a group outside the tenancy where the policy resides.

Policy A must be attached to the acceptor's tenancy (root compartment), and not the acceptor's compartment.
[

## Attaching to VCNs in the Same Tenancy

If you want the VCN administrators group to create and manage VCN attachments and assign DRG route tables to the attachments, implement the following policy:

```

```

Note  
  
To associate a VCN route table with the attachment, add this line:

```

```

## Attaching to VCNs in Other Tenancies

"Cross-tenancy attachments" are special VCN attachments used to connect a DRG directly to a VCN in another tenancy but homed in the same region. The VCN is attached to a DRG in a separate tenancy. The example policy that follows details the minimum IAM policy requirements for both tenancies to allow this type of connection.

This example of a set of policies allows the following set of actions:
- DRG administrators in the DRG tenant can create a DRG attachment in the VCN tenant.
- VCN administrators in the VCN tenant can associate a VCN route table to the attachment (used when the VCN attached is a transit VCN). If the VCN administrator has a policy to manage all-resources in the VCN tenant, they already have this ability, because the VCN attachment resides in the VCN tenancy.
- VCN administrators can't change the DRG route table association for the DRG attachment.
- 

Policy R (DRG in this tenancy)

```

```

vcnAdminGroupOcid is the OCID of the vcnAdmin group in the Acceptor tenancy and endorsed in the Acceptor policy.
- 

Policy A (VCN in this tenancy)

```

```
