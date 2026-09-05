# Using Tags to Manage Access
- Source: https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm
- Fetched: 2026-09-05 03:06 CDT

# Using Tags to Manage Access

This topic describes how you can use tags in policy to scope access based on tags applied to either the requestor or the target of an authorization call.

## About Tag-Based Access Control

Using conditions and a set of tag variables, you can write[policy](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)to scope access based on the tags that have been applied to a resource. Access can be controlled based on a tag that exists on the requesting resource (group, dynamic group, or compartment) or on the target of the request (resource or compartment). Tag-based access control provides additional flexibility to your policies by allowing you to define access policies with tags that span compartments, groups, and resources.
Caution  
  

If your organization chooses to create policies that use tags to manage access, then ensure that you have appropriate controls in place to govern who can apply tags. Also, after policies are in place, keep in mind that applying tags to a group, user, or resource has the potential to confer access to resources.

Before you create a policy that specifies a tag on either a target or a requestor, ensure that you are aware of:
- all the potential requestors (users, groups, dynamic groups) that carry the tag
- all the resources that carry the tag

Before you apply a tag to a resource , ensure that you are aware of any policies in place that include the tag and could impact who has access to the resource.

## Managing Access Using Tags Applied to the Requesting Resource

You can control access based on the value of a tag applied to:
- a group (of users) requesting access
- a dynamic group (of instances) requesting access
- a compartment that a resource in a dynamic group resides in

By using tags in your policy statements to scope access, you can define access for multiple groups through a single policy statement. You can also confer access and revoke access for groups by applying or removing tags, without changing the original policies.

The basic syntax for each variable is shown in the following table. Note that the syntax is the same for group and dynamic group, but each is presented in a different row. See[Supported Operators](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#operators)more usage examples.

Tag Applied to Requestor Variable Syntax Description

group`request.principal.group.tag. {tagNamespace} . {tagKeyDefinition} = ' <value> '`

Sample policy for user group:

`allow any-user to manage instances in compartment HR where request.principal.group.tag.Operations.Project= 'Prod'`

Any user who belongs to a group that has been tagged with Operations.Project='Prod' can manage instances in the HR compartment.

The tags applied to the groups that the user belongs to are evaluated for a match.

dynamic group`request.principal.group.tag. {tagNamespace} . {tagKeyDefinition} = ' <value> '`

Sample policy for dynamic group:

`allow dynamic-group InstancesA to manage instances in compartment HR where request.principal.group.tag.Operations.Project= 'Prod'`

Instances that are members of the dynamic group InstancesA and that are also members of a dynamic group tagged with Operations.Project='Prod' can manage instances in the compartment HR.

The tags applied to the dynamic groups that the instance belongs to are evaluated for a match.

compartment`request.principal.compartment.tag. {tagNamespace} . {tagKeyDefinition} = ' <value> '`

Sample policy:

`allow dynamic-group InstancesA to manage instances in tenancy where request.principal.compartment.tag.Operations.Project= 'Prod'`

Instances that are members of the dynamic group InstancesA and that also reside in a compartment tagged with Operations.Project='Prod' can manage instances in the tenancy.

The tags applied to the compartment that the requesting resource belongs to are evaluated.
Note  
  
Users reside in the root compartment of your tenancy, so tags must be applied to the root compartment for those policy statements to work.

## Managing Access Using Tags Applied to the Target Resource

You can control access based on the value of a tag applied to:
- a resource
- a compartment that the target resource resides in

The basic syntax for these variables is shown in the following table. See[Supported Operators](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#operators)for more usage examples.

Tag Applied to Target Variable Syntax Description

resource`target.resource.tag. {tagNamespace} . {tagKeyDefinition} =' <value> '`

Sample policy:

`allow group GroupA to manage all-resources in compartment HR where target.resource.tag.Operations.Project= 'Prod'`

The tag applied to the target resource of the request is evaluated.

There are limitations to the permissions that can be granted in this type of policy. See the following sections in this topic for details.

compartment`target.resource.compartment.tag. {tagNamespace} . {tagKeyDefinition} =' <value> '`

Sample policy:

`allow group GroupA to manage all-resources in tenancy where target.resource.compartment.tag.Operations.Project= 'Prod'`

The tag applied to the target compartment of the request is evaluated.

See[Compartment Hierarchies](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#comphier)for details on how access is granted in nested compartments.

## Permissions to List a Resource Must Be Granted Separately

Policies that scope access based on the tag applied to the target resource can't allow the permissions that enable you to return a list of resources. Therefore, permissions to allow listing a resource must be granted through an additional policy statement. This means that if you have defined a policy like:

`allow group GroupA to manage all-resources in compartment Operations where target.resource.tag.Operations.Project= 'Prod'`

GroupA will not be able to list any of the resources that they are otherwise allowed to manage. Members of GroupA would not be able to use the Console to interact with these resources and users would need to know the OCID of the resource they are attempting to manage, which makes using the SDK and CLI cumbersome, also.

To allow GroupA to list those resources, you need to add another policy statement like:

`allow group GroupA to inspect all-resources in compartment Operations`

This approach improves the tag-based policy because it allows users to use the Console more easily (by allowing them to see the resource they want to manage), but still limits the permissions to only inspect. The members of GroupA cannot take any action on those resources unless they are tagged appropriately. Keep in mind when using tag-based access control that the added flexibility requires this additional potential expansion of access.

Another approach you can use to avoid this limitation is to tag the compartments that contain the resources you want to grant access to. An example policy looks like this:

```

```

This policy allows the members of GroupA to manage all resources in the tenancy that are in compartments that are tagged with the Operations.Project='Prod' tag.

## Policies that Require a Tag on the Target Resource Can't Grant Create Permissions

When you write a policy to scope access based on the value of a tag on the resource, keep in mind that the policy cannot grant create permissions. A request to create an instance would fail because the target resource has not been created yet and therefore does not have the appropriate tag to be evaluated. So a policy like:

`allow group GroupA to manage instances in compartment Operations where target.resource.tag.Operations.Project='Prod'`

allows the members of GroupA to use and delete instances that are tagged with Operations.Project='Prod', but they cannot create instances.

## Supported Operators

Your policy using these tag variables can include these operators and match types:

Operator Type Example Description
= String`request.principal.group.tag.MyTagNamespace.MyTag='sample'`Evaluates to true if any of the groups that the requestor belongs to is tagged with the matching value "sample" for MyTagNamespace.MyTag. (The value is case insensitive.)
Pattern`request.principal.group.tag.MyTagNamespace.MyTag=/*sample/`Evaluates to true if any of the values of MyTagNamespace.MyTag ends with "sample". (Simple case insensitive pattern match.)
Policy variable`request.principal.group.tag.mytagnamespace.mytag``=``target.resource.tag.mytagnamespace.mytag`Evaluates to true when the specified resource mytagnamespace.mytag has a value that matches the specified target mytagnamespace.tag.
!= String`request.principal.group.tag.MyTagNamespace.MyTag !='sample'`Evaluates to true if none of the string values of the policy variable equals "sample". (Simple case insensitive string comparison.)
Pattern`request.principal.group.tag.MyTagNamespace.MyTag !=/*sample/`Evaluates to true if none of the values of MyTagNamespace.MyTag ends with "sample". (Simple case insensitive pattern match.)
Policy variable`request.principal.group.tag.mytagnamespace.mytag``!=``target.resource.tag.mytagnamespace.mytag`Evaluates to true if neither side is a subset of the other.

### In / Not In

Operator Type Example Description
in String`request.principal.group.tag.MyTagNamespace.MyTag in ('sample', 'sample1')`The clause evaluates to true if any of the values of MyTagNamespace.MyTag for any group of the current requesting principal either equals to "sample" or "sample1".
Pattern`request.principal.group.tag.MyTagNamespace.MyTag in (/*sample/, /sample1*/)`The clause evaluates to true if any of the values of MyTagNamespace.MyTag for any group of the current requesting principal either ends with "sample" or starts with "sample1".
Policy variable`request.principal.group.tag.MyTagNamespace.MyTag in``(target.resource.tag.mytagnamespace.mytag, 'sample')`

The clause evaluates to true if any of the following conditions are met:

1. Either request.principal.group.tag.MyTagNamespace.MyTag or target.resource.tag.mytagnamespace.mytag is a subset of the other.

2. Any string values of request.principal.group.tag.MyTagNamespace.MyTag equals "sample".
not in String`request.principal.group.tag.MyTagNamespace.MyTag not in ('sample', 'sample1')`The clause evaluates to true if none of the values of MyTagNamespace.MyTag for any group of the current requesting principal equals to "sample" or "sample1".
Pattern`request.principal.group.tag.MyTagNamespace.MyTag not in (/*sample/, /sample1*/)`The clause evaluates to true if none of the values of MyTagNamespace.MyTag for any group of the current requesting principal ends with "sample" or starts with "sample1".
Policy variable`request.principal.group.tag.MyTagNamespace.MyTag not in``(target.resource.tag.mytagnamespace.mytag, 'sample')`

The clause evaluates to true if all of the following conditions are met:

1. Neither request.principal.group.tag.MyTagNamespace.MyTag nor target.resource.tag.mytagnamespace.my tag is a subset of the other.

2. None of the string values of request.principal.group.tag.MyTagNamespace.MyTag equals "sample".

### Support for Wildcards

You can use the * character to match all occurrences of {tagNamespace} . {tagKeyDefinition} regardless of the value. In the policy, you can place * in single quotes '*' or between backslashes /*/ . For example,

`allow group GroupA to use all-resources in compartment HR where target.resource.tag.HR.Project= '*'`

In this example, GroupA can use all resources in the compartment HR that are tagged with the tag namespace and tag key: HR.Project with any value.

## Limitations on Characters in Tag Namespaces and Tag Key Definitions Used in Policy Variables

Tag namespaces and tag key definitions support a broader set of characters than are allowed in policy variables. Therefore, if you use tag namespaces and tag key definitions in variables, ensure that they only include the characters also supported by policy variables. Supported characters are:

a-z, A-Z, 0-9, _, @, -, :

If tag namespaces or tag keys have characters other than these, you can't use them in policy variables. Tag namespaces and tag keys can't be renamed, so you must create new tag namespaces and tag key definitions.

## Considerations for Case

When working with tags in policies, be aware that tag values are case insensitive. For example:

`request.principal.group.tag.MyTagNamespace.MyTag='sample'`

is the same as

`request.principal.group.tag.MyTagNamespace.MyTag='Sample'`

## Compartment Hierarchies

When you write a condition to allow access based on the tag applied to a target compartment, remember that this policy also allows access to all compartments nested inside the tagged compartment. All subcompartments in the tagged compartment are resources in the tagged compartment, and therefore the policy grants access.

For example, in this scenario:

[

The policy:
```

```

allows GroupA to use all the resources in CompartmentA, CompartmentA1, and CompartmentA1.1, even though the tag is applied to CompartmentA only.

## Supported Services

All Oracle Cloud Infrastructure services support the`request.principal.compartment`,`request.principal.group`, and`target.resource.compartment.tag`policy variables.

Not all services support the`target.resource.tag`policy variable. The following table lists the supported services . If the service is not listed in the table, it is not supported at this time.

Some services have limitations. See the appropriate link in the table.

Services Supported More Information
API Gateway See[API Gateway Service Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#apig).
Big Data Service See[Big Data Service Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#bigd).
Blockchain Platform Fully supported, no limitations.
Block Volume See[Block Volume Service Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#Service).
Certificates Fully supported, no limitations.
Compute See[Compute Service Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#Service2).
Compute Management See[Compute Management Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#Compute).
Content Management See[Content Management Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#cande).
Data Catalog See[Data Catalog Service Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#DCAT).
Data Flow Fully supported, no limitations.
Data Science See[Data Science Service Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#datasci).
Database See[Database Service Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#bm).
Digital Assistant See[Digital Assistant Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#digad).
DNS See[Public DNS Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#dns).
Email Delivery Fully supported, no limitations.
FastConnect Fully supported, no limitations.
Functions Fully supported, no limitations.
Health Checks Fully supported, no limitations.
IAM Supported resources are:`users`,`groups`,`policies`,`dynamic-groups`,`network-sources`, and`identity-providers`
Load Balancer See[Load Balancing Service Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#Load).
MySQL HeatWave Fully supported, no limitations.
Networking See[Networking Service Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#Networki).
NoSQL Database Cloud See[Networking Service Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#Networki).
Notifications Fully supported, no limitations.
Object Storage See[Object Storage Service Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#bm2).
Quotas Service Fully supported, no limitations.
Tagging Namespace See[Tagging Namespace Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#Tagging).
Vault Encryption not supported.
WAF See[WAF Limitations](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#waf).

## Limitations and Additional Policies Needed for Specific Target.Resource.Tag Scenarios

For some services, not all permissions or resource types are supported. When a permission is not supported, that means that even if the resource is tagged and the permission is included in the verb granting access, that permission is not allowed and authorization fails for the operation governed by the permission. For example, the Block Volume service resource`volume-backups`, does not support tag-based access control for the VOLUME_BACKUP_COPY permission. Therefore, this policy:

```

```

does not allow members of the group TestGroup to perform the`CopyVolumeBackup`operation. To grant that permission to TestGroup, you would need to add another policy statement to cover it.

In addition, some operational scenarios require authorization to access multiple resources. When scoping access to tags that are applied to the target resource, you must include a separate policy for each resource involved in the operation. Also, because of the limitations for listing resources and other service-specific permissions, additional policies (not scoped by tag) are required.

### API Gateway Service Limitations

In addition to the expected tag-based access control policy for API Gateway resources, you'll need policy allowing manage permissions for`api-workrequests`.

Here is an example policy with the additional permissions:

```

```

### Big Data Service Limitations

In addition to the expected tag-based access control policy for Big Data Service resources, you'll need policy allowing manage permissions for`cluster-work-requests`.

Here is an example policy with the additional permissions:

```

```

### Block Volume Service Limitations

Service Resource Type with Limitations Permissions Not Supported with the target.resource.tag Policy Variable
Block Volume`backup-policy-assignments`BACKUP_POLICY_ASSIGNMENT_DELETE
`volume-backups`VOLUME_BACKUP_COPY

Scenarios requiring additional policy:

Attach a block volume to a compute instance:

To attach a block volume to a compute instance, in addition to the tag-based access control policy to allow the`use`verb on volumes and instances, you'll need some additional permissions.

For example:

```

```

These two policies allow members of TestGroup to use volumes and instances in Compartment1, when the resources have the appropriate tag. To allow members to attach a block volume to an instance, you'll also need policies that allow the permissions shown in the following statements:

```

```

### Compute Service Limitations

Service Resource Type Permissions Not Supported with the target.resource.tag Policy Variable
Compute`instance-console-connection`

INSTANCE_CONSOLE_CONNECTION_DELETE
`instances`INSTANCE_POWER_ACTIONS

Scenarios requiring additional policy:

Attach compute instance to subnet:

To manage a compute instance's subnet attachment, in addition to the expected tag-based access control policy for`instances`and`subnets`, shown here:

```

```

You'll need additional permissions on`vnics`:

```

```

Delete a VNIC from a compute instance:

To delete a VNIC from a compute instance, in addition to the expected tag-based access control policy for`instances`and`subnets`shown here:

```

```

You'll need policy allowing you permissions on`vnics`:

```

```

### Compute Management Limitations

Service Resource Type Permissions Not Supported with the target.resource.tag Policy Variable Notes
Compute Management`instance-pools`All permissions The`instance-pools`resource type is not supported.
`auto-scaling-configurations`AUTO_SCALING_CONFIGURATION_UPDATE .

### Content Management Limitations

In addition to the expected tag-based access control policy for Content Management resources, you'll need policy allowing manage permissions for`oce-work-requests`.

Here is an example policy with the additional permissions:

```

```

### Database Service Limitations

Service Resource Type Permissions Not Supported with the target.resource.tag Policy Variable
Database`all`DATABASE_DELETE

Update Tags for ExaData Infrastructure:

Not supported at this time using tag-based access control policies.

Scenarios requiring additional policy:

Delete a DB-System:

To delete or update a DB-System, in addition to the expected tag-based access control policy for`db-systems`, shown here:

```

```

You'll need policy allowing you permissions for`db-backups, db-homes, vnics`,`subnets`and`databases`. Here is an example policy showing the additional permissions:

```

```

Move a DB-system to another compartment:

To move a DB-System to another compartment, in addition to the expected tag-based access control policy for`db-systems`shown here:

```

```

You'll need policy allowing you permissions for`databases`,`db-homes`, and`db-backups`. Here is an example policy with the additional permissions:

```

```

Database delete for Exadata DB-System:

To delete a database resource for an Exadata DB-System, you'll need the expected tag-based access control policy for`db-systems`and`databases`shown here:

```

```

You'll also need permissions for`db-homes`and`db-backups`. Here is an example policy with the additional permissions:

```

```

Delete Database:

Deleting a database for a baremetal or virtual machine DB system is not supported using tag-based policies on the target resource.

Database backup create:

To create a database backup, you'll need the expected tag-based access control policy for`databases`:

```

```

You'll also need permissions for`db-backups`. Here is an example policy with the additional permissions:

```

```

Database restore:

To restore a database backup, you'll need the expected tag-based access control policy for`databases`:

```

```

You'll also need permissions for`backups`, like the one shown here:

```

```

Create Data Guard association:

Creating a Data Guard association is not supported using tag-based policies on the target resource.

### Data Catalog Service Limitations

In addition to the expected tag-based access control policy for Data Catalog resources, you'll need the following additional policies for`data-catalog-family`:

```

```

### Data Science Service Limitations

In addition to the expected tag-based access control policy for Data Science resources, you'll need policy allowing manage permissions for`data-science-work-requests`.

Here is an example policy with the additional permissions:

```

```

### Digital Assistant Limitations

Service Resource Type Permissions Not Supported with the target.resource.tag Policy Variable
Digital Assistant`oda-design`

All permissions
`oda-insights`All permissions

In addition to the expected tag-based access control policy for the Oracle Digital Assistant resources, you'll need the following additional policies for`oda-instances`:

```

```

### Load Balancing Service Limitations

Scenarios requiring additional policy:

Update Load Balancer :

To perform any update to load balancers, in addition to the expected tag-based access control policy for`load-balancers`:

```

```

You'll need policy that allows the GetWorkRequest API operation. Here is an example policy with the additional permission:

```

```

Delete Load Balancer:

To delete a load balancer, in addition to the expected tag-based access control policy for`load-balancers`,`subnets`, and`network-security-group`:

```

```

You'll need these additional permissions for`vnics`:

```

```

### Networking Service Limitations

Service Resource Type Permissions Not Supported with the target.resource.tag Policy Variable Notes
Networking`private-ips`

PRIVATE_IP_UPDATE

PRIVATE_IP_DELETE

VNIC_UNASSIGN

SUBNET_DETACH
`route-tables`UPDATE (INTERNET_GATEWAY_DETACH) Removing a route rule is not supported.
`vnics`

VNIC_UPDATE

VNIC_DELETE

Attach service gateway or NAT gateway to a route table:

Attaching a service gateway or a NAT gateway to a route table is not supported using tag-based policies on the target resource.

Scenarios requiring additional policy:

Attach DRG to VCN:

To attach DRG to VCN, in addition to the following expected tag-based access control policy for`virtual-network-family`and`vcns`:

```

```

You'll need policy allowing you`manage`permissions for`drgs`. Here is an example policy with the additional permissions:

```

```

### NoSQL Database Cloud Service Limitations

Supported resources are:`nosql-tables`,`nosql-rows`, and`nosql-indexes`.

In addition to the expected tag-based access control policy for the NoSQL Database Cloud resources, you'll need these additional policies:

```

```

```

```

```

```

Note that the preceding policies are required to navigate the NoSQL Database Cloud resources in the Console.

### Object Storage Service Limitations

Service Resource Type Permissions Not Supported with the target.resource.tag Policy Variable Notes
Object Storage`objects`All permissions related to accessing`objects`Objects are not taggable.
Note  
  
Access to objects can be managed by using the tags on the bucket that the objects belong to. Use`target.bucket.tag`policy variable. See[Let users write objects to Object Storage buckets](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm#write-objects-to-buckets).

### Public DNS Limitations

In addition to the expected tag-based access control policy for`dns`resources, you'll need policy allowing you`manage`permissions for`dns-records`. Here is an example policy with the additional permissions:

```

```

### Tagging Namespace Limitations

Policy that grants a user access to a tag namespace based on a tag on the namespace does not allow the user to create or delete tag key definitions in that tag namespace.

For example, the policy:

```

```

does not allow the users in TestGroup to create or delete tag key definitions in the tag namespaces tagged with TagNS.TagKey='test'.

### WAF Limitations

In addition to the expected tag-based access control policy for the WAF resources, you'll need policy allowing you manage permissions for`waas-work-request`. Here is an example policy with the additional permissions:

```

```

## Illustrated Examples

- [Illustrated Examples](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#exam)
- [Example Using Tags Applied to a Target Resource](https://docs.oracle.com/en-us/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm#Example2)

### Example Using Tags Applied to a Group

Following is an example that demonstrates how you can use tags applied to user groups to manage access to resources in a compartment.

Assume you have three compartments: ProjectA, ProjectB, and ProjectC

[

For each compartment, there is an admin group set up: A-Admins, B-Admins, and C-Admins.

Each admin group has full access over their compartment through the following policies:
- `allow group A-Admins to manage all-resources in compartment ProjectA`
- `allow group B-Admins to manage all-resources in compartment ProjectB`
- `allow group C-Admins to manage all-resources in compartment ProjectC`

[

Your organization has set up the following tag namespace and key to tag each group by its role:
- EmployeeGroup.Role

Some values for this tag are 'Admin', 'Developer', 'Test-Engineer'.

All your admin groups are tagged with EmployeeGroup.Role='Admin'

[

Now you want to set up a Test compartment for members of the three projects to share. You want to give Admin access to all three of your existing admin groups. To accomplish this, you can write a policy like:

`allow any-user to manage all-resources in compartment Test where request.principal.group.tag.EmployeeGroup.Role='Admin'`

[

With this policy, all of your existing admin groups with the tag will have access to the Test compartment. Also, any new or existing groups that you tag with EmployeeGroup.Role='Admin' in the future will have access to the Test compartment without having to update the policy statements.

### Example Using Tags Applied to a Target Resource

In this example, each of your organization's project compartments contains two child compartments: Test and Prod. You want to give your test engineers access to the test compartments across all three projects. To accomplish this, you create a tag:

ResourceGroup.Role='Test'

and apply this to the Test compartments in each of your project compartments.

[

You can then use a policy like:

`allow group Testers to use all-resources in tenancy where target.resource.compartment.tag.ResourceGroup.Role='Test'`
