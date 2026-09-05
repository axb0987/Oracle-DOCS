# Managing DNS Resources Across Tenancies
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/dns-cross-tenancy.htm
- Fetched: 2026-09-05 01:59 CDT

# Managing DNS Resources Across Tenancies

Create IAM policies that let a tenancy access DNS resources in other tenancies.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[DNS Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/dnspolicyreference.htm).

## Cross-Tenancy Policies

An organization might want to share resources with another organization that has its own tenancy. It could be another business unit in a company, a company's customer, a company that provides services to another company, and so on. In these cases, you need cross-tenancy policies in addition to the required user and service policies already described.

All OCI API operations support cross tenancy requests where the calling principal is from a tenancy that's different than the tenancy the resource lives in. Some OCI API operations also support a different type of cross tenancy request where the resources involved are in different tenancies. For these types, the following apply:
- The permission of the first resource in that resources tenancy.
- The permission of the second resource in that resources tenancy.
- Association between the two types of resources involved between the two tenancies.

To access and share resources, the administrators of both tenancies need to create special IAM policy statements that explicitly state the resources that can be accessed and shared.

For resource types that you can use in association statements, see[Individual Resource-Types](https://docs.oracle.com/iaas/Content/Identity/Reference/dnspolicyreference.htm#individual).

### Endorse, Admit, and Define Statements

Here's an overview of the special verbs used in cross-tenancy statements:
- Endorse : States the general set of abilities that a group in one tenancy can perform in the other tenancies. The Endorse statement always belongs in the tenancy with the group of users crossing the boundaries into the other tenancy to work with that tenancy's resources. In the examples, this tenancy is called the source.
- Admit : States the kind of ability in a tenancy that you want to grant to a group from another tenancy. The Admit statement belongs in the tenancy who is granting "admittance" to the tenancy. The Admit statement identifies the group of users that requires resource access from the source tenancy and identified with a corresponding Endorse statement. In the examples, this tenancy is called the destination.
- 

Define : Assigns an alias to a tenancy OCID for Endorse and Admit policy statements. A Define statement is also required in the destination tenancy to assign an alias to the source IAM group OCID for Admit statements.

Define statements must be included in the same policy entity as the endorse or the admit statement.

The Endorse and Admit statements work together, but they reside in separate policies, one in each tenancy. Without a corresponding statement that specifies access, a particular Endorse or Admit statement grants no access. Agreement is required from both tenancies.
Important  
  
In addition to policy statements, you must also be subscribed to a region to share resources across regions.

### Source Tenancy Policy Statements

The administrator for source tenancy creates policy statements that endorse an IAM group allowed to manage resources in the destination tenancy.

Here is an example of a broad policy statement that endorses the IAM group`DNSAdmins`to do anything with all DNS resources in any tenancy:

```

```

To write a policy that reduces the scope of tenancy access, the destination administrator must provide the destination tenancy OCID. Here is an example of policy statements that endorse the IAM group`DNSAdmins`group to manage DNS resources in the`DestinationTenancy`only:

```

```

### Destination Tenancy Policy Statements

The destination administrator creates policy statements that:
- Defines the source tenancy and IAM group that's allowed to access resources in another tenancy. The source administrator must provide this information.
- Admits those defined sources to access DNS resources that you want to allow access to in the local tenancy.

Here is an example of policy statements that admit the IAM group`DNSAdmins`in the source tenancy to do anything with all DNS resources in the local tenancy:

```

```

Here is an example of policy statements that endorse the IAM group`DNSAdmins`in the source tenancy to manage DNS resources only in the`SharedZones`compartment:

```

```

### Example: To create a child zone in a different tenancy from the parent zone

Here's an example of a commonly used scenario where the child zone resides in a different tenancy from the parent zone:

Parent zone policies :
```

```

Child zone policies :
```

```

### Example: To create a parent zone in a different tenancy from an existing child zone

To create a parent zone (`example.com`) when one or more child zones (`child.example.com`) already exist in other tenancies, the user in the parent zone tenancy must have permission to delete any child zones that exist.

Parent zone tenancy policies :
```

```

Child zone tenancy policies :
```

```

If child zones exist in many tenancies, create a set of policies for each tenancy.

### Example: To update attached views on a resolver where the resolver is in a different tenancy than the views and the calling principal

Identity policy in the tenancy of the caller and views :
```

```

Identity policy in the tenancy of the resolver :
```

```

It doesn't matter if you associate`dns-resolver`with`dns-views`or if you associate`dns-views`with`dns-resolver`, but you must have one of those on the admit and one on the endorse. For example, the last Identity policy statement of the second Identity policy could be either of these:
```

```

or
```

```

### Example: To update Identity policies for UpdateResolver where an attached view is in a different tenancy

Policy for tenancy VIEW_TENANCY
```

```

Policy for tenancy RESOLVER_TENANCY
```

```

### DNS Operations that require policy statements to function across tenancies

The following table shows DNS operations that require admit and endorse policy statements to function across tenancies. For each use case, you need the minimum listed user or group permissions for the source and destination tenancy.

To Source Tenancy Permission Destination Tenancy Permission
Create a private zone where the view is in a different tenancy DNS_ZONE_CREATE DNS_VIEW_INSPECT
Create a zone with a TSIG key in a different tenancy DNS_ZONE_CREATE DNS_TSIG_KEY_READ
Create a child zone in a different tenancy than the parent zone. DNS_ZONE_CREATE DNS_RECORD_UPDATE
Create a child zone with TSIG key in a different tenancy than the parent zone.

DNS_ZONE_CREATE

DNS_TSIG_KEY_READ (if the TSIG key is in the source tenancy.)

DNS_RECORD_UPDATE

DNS_TSIG_KEY_READ (if the TSIG key is in the destination tenancy.)
Update a zone with a TSIG key in a different tenancy DNS_ZONE_UPDATE DNS_TSIG_KEY_READ
Create an attachment for a zone to a steering policy in a different tenancy DNS_ZONE_UPDATE DNS_STEERING_POLICY_READ
Update an attachment for a zone to a steering policy in a different tenancy DNS_ZONE_UPDATE DNS_STEERING_POLICY_READ
Delete an attachment from a zone to a steering policy in a different tenancy DNS_ZONE_UPDATE DNS_STEERING_POLICY_READ
