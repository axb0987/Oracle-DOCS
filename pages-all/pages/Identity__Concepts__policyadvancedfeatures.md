# Advanced Policy Features
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm
- Fetched: 2026-09-05 02:14 CDT

# Advanced Policy Features

This section describes policy language features that let you grant more granular access.

## Conditions

As part of a policy statement, you can specify one or more conditions that must be met in order for access to be granted.

Each condition consists of one or more predefined variables that you specify values for in the policy statement. Later, when someone requests access to the resource in question, if the condition in the policy is met, it evaluates to true and the request is allowed. If the condition is not met, it evaluates to false and the request is not allowed.

There are two types of variables: those that are relevant to the request itself, and those relevant to the resource being acted upon in the request, also known as the target . The name of the variable is prefixed accordingly with either`request`or`target`followed by a period. For example, there's a request variable called`request.operation`to represent the API operation being requested. This variable lets you write a broad policy statement, but add a condition based on the specific API operation. For an example, see[Let users write objects to Object Storage buckets](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#write-objects-to-buckets).

Important  
  
Condition matching is case insensitive. This is important to remember when writing conditions for resource types that allow case-sensitive naming. For example, the Object Storage service allows you to create both a bucket named "BucketA" and a bucket named "bucketA" in the same compartment. If you write a condition that specifies "BucketA", it will apply also to "bucketA", because the condition matching is case insensitive.

### Variables that Aren't Applicable to a Request Result in a Declined Request

If the variable is not applicable to the incoming request, the condition evaluates to false and the request is declined. For example, here are the basic policy statements that together let someone add or remove users from any group except Administrators:
```

```

Given the above policy, if GroupAdmins tried to call a general API operation for users such as`ListUsers`or`UpdateUser`(which lets you change the user's description), the request would be declined, even though those API operations are covered by`use users`.This is because the above policy statement for`use users`also includes the`target.group.name`variable, but the`ListUsers`or`UpdateUser`request doesn't involve specifying a group. There is no`target.group.name`for those requests, so the request is declined.

If you want to also grant access to general user API operations that don't involve a particular group, you would need an additional statement that gives the level of access you want to grant, but without the condition . For example, if you want to grant access to`ListUsers`, you need this additional statement:
```

```

Or if you want to grant access to`UpdateUser`, you need this additional statement (which also covers`ListUsers`because the`use`verb includes the capabilities of the`inspect`verb):
```

```

This general concept also applies to groups (for example,`ListGroups`and`UpdateGroup`), and any other resource type with target variables.

For more information about the syntax of conditions, see[Conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/../policysyntax/conditions.htm). For a list of all the variables you can use in policies, see the tables in the[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/../policieshow/Policy_Basics.htm).

### Tag-Based Access Control

Using conditions and a set of tag variables, you can write policy to scope access based on the tags that have been applied to a resource. Access can be controlled based on a tag that exists on the requesting resource (the group or dynamic group in the policy) or on the target of the request (resource or compartment). Tag-based access control provides additional flexibility to your policies by allowing you to define access that spans compartments, groups, and resources. For details about how to write policies to scope access by tags, see[Using Tags to Manage Access](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm).

## Permissions

Permissions are the atomic units of authorization that control a user's ability to perform operations on resources. Oracle defines all the permissions in the policy language. When you write a policy giving a group access to a particular[verb](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/../Reference/policyreference.htm#Verbs)and resource-type, you're actually giving that group access to one or more predefined permissions. The purposes of verbs is to simplify the process of granting multiple related permissions that cover a broad set of access or a particular operational scenario. The next sections give more details and examples.

### Relation to Verbs

To understand the relationship between permissions and verbs, let's look at an example. A policy statement that allows a group to`inspect volumes`actually gives the group access to a permission called VOLUME_INSPECT (permissions are always written with all capital letters and underscores). In general, that permission enables the user to get information about block volumes.

As you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`, the level of access generally increases, and the permissions granted are cumulative. The following table shows the permissions included with each verb for the`volumes`resource-type. Notice that no additional permissions are granted going from`inspect`to`read`.

Inspect Volumes Read Volumes Use Volumes Manage Volumes
VOLUME_INSPECT VOLUME_INSPECT

VOLUME_INSPECT

VOLUME_UPDATE

VOLUME_WRITE

VOLUME_INSPECT

VOLUME_UPDATE

VOLUME_WRITE

VOLUME_CREATE

VOLUME_DELETE

See a service's[Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/../Reference/corepolicyreference.htm#Core)for full list of detailed commands.

### Relation to API Operations

Each API operation requires the caller to have access to one or more permissions. For example, to use either`ListVolumes`or`GetVolume`, you must have access to a single permission: VOLUME_INSPECT. To attach a volume to an instance, you must have access to multiple permissions, some of which are related to the`volumes`resource-type, some to the`volume-attachments`resource-type, and some related to the`instances`resource-type:
- VOLUME_WRITE
- VOLUME_ATTACHMENT_CREATE
- INSTANCE_ATTACH_VOLUME

The policy reference lists which permissions are required for each API operation. For example, for the Core Services API operations, see the table in[Permissions Required for Each API Operation](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/../Reference/corepolicyreference.htm#Permissi).

### Understanding a User's Access

The policy language is designed to let you write simple statements involving only verbs and resource-types, without having to state the desired permissions in the statement. However, there may be situations where a security team member or auditor wants to understand the specific permissions a particular user has. The tables in the policy reference for each service show supported verbs and the associated permissions. You can look at the groups the user is in and the policies applicable to those groups, and from there compile a list of the permissions granted. However, having a list of the permissions isn't the complete picture. Conditions in a policy statement can scope a user's access beyond individual permissions (see the next section). Also, each policy statement specifies a particular compartment and can have conditions that further scope the access to only certain resources in that compartment.

## Scoping Access with Permissions or API Operations

In a policy statement, you can use[conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#one)combined with permissions or API operations to reduce the scope of access granted by a particular verb.

For example, let's say you want group XYZ to be able to list, get, create, or update groups (i.e., change their description), but not delete them. To list, get, create, and update groups, you need a policy with`manage groups`as the verb and resource-type. According to the table in[Details for Verbs + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/../Reference/iampolicyreference.htm#Identity), the permissions covered are:
- GROUP_INSPECT
- GROUP_UPDATE
- GROUP_CREATE
- GROUP_DELETE

To restrict access to only the desired permissions, you could add a condition that explicitly states the permissions you want to allow :

```

```

An alternative would be a policy that allows all permissions except GROUP_DELETE:

```

```

However, with this approach, be aware that any new permissions the service might add in the future would automatically be granted to group XYZ. Only GROUP_DELETE would be omitted.

Another alternative would be to write a condition based on the specific API operations . Notice that according to the table in[Permissions Required for Each API Operation](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/../Reference/iampolicyreference.htm#Details), both`ListGroups`and`GetGroup`require only the GROUP_INSPECT permission. Here's the policy:

```

```

It can be beneficial to use permissions instead of API operations in conditions. In the future, if a new API operation is added that requires one of the permissions listed in the permissions-based policy above, that policy will already control XYZ group's access to that new API operation.

But notice that you can further scope a user's access to a permission by also specifying a condition based on API operation. For example, you could give a user access to GROUP_INSPECT, but then only to`ListGroups`.

```

```

## Scoping Policy by the IP Address of the Requestor

You can scope access to only a set of allowed IP addresses. For example, you can write policy to allow only requests from a given public IP range to access a specific Object Storage bucket; or, you can allow only specific subnets of a specific VCN to make requests over a service gateway.

To restrict access to a set of IP addresses, do the following:
- Create a network source object that specifies the allowed IP addresses. See[Managing Network Sources](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/../Tasks/managingnetworksources.htm#Managing_Network_Sources)for details.
- Write a policy that uses the network source object in a condition.

Use the following variable in your policy:

```

```

For example:

```

```

## Restricting Access to Resources Based on Time Frame

You can use time-based variables in your policies to restrict the access granted in the policy to only certain time frames. This feature allows you to restrict actions on resources to particular times. For example, you can create a policy that allows access only through a specified date. A policy like this would be useful if your company hires contractors and you want to ensure access is not allowed past the contract end date. Or, you could allow access to resources only during business hours (for example, Monday-Friday 9:00 AM - 5:00 PM). This restriction can lower the risk of a bad actor making changes when they are more likely to go unnoticed.

The variables that you can use to scope access based on time are:

- `request.utc-timestamp`
- `request.utc-timestamp.month-of-year`
- `request.utc-timestamp.day-of-month`
- `request.utc-timestamp.day-of-week`
- `request.utc-timestamp.time-of-day`

Usage for these variables is described in more detail in the following sections.

### Information for Working with Time-Based Variables

You must specify the time the variables using[ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html)format: YYYY-MM-DDThh:mm:ssZ. Examples of this format are:

- Date and time with seconds: '2020-04-01T15:00:00Z'
- Data and time with minutes: '2020-04-01T05:00Z'
- Date only: '2020-04-01Z'
- Time only: '05:00:00'

Even though you can specify a time down to seconds, you should allow for a 5 minute time difference between the timestamp on the request and the time the request is evaluated by the IAM service. This time difference can be caused by several factors, therefore be aware of this potential discrepancy when you plan and implement your time-based policies.

The time that you specify is evaluated as Coordinated Universal Time (UTC). This means that you must calculate the correct UTC time for the time zone in which the policy is evaluated. For example, to specify 9:00 AM Pacific Standard Time for the value of a variable, you would enter '17:00:00'. If your locale participates in daylight savings, you'll need to update any policies that refer to a specific hour when the time change goes into effect.

### Details for Each Time-Based Variable

Usage for each variable is described in the following sections:

[request.utc-timestamp](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#)

Description: The time the request is received for authorization. You can write a policy that allows access only before or after a specific date-time timestamp. The timestamp must follow the[ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html)format: YYYY-MM-DDThh:mm:ssZ and be in Coordinated Universal Time (UTC).

Supported operators: before | after

Allowed values: Coordinated Universal Time (UTC) timestamp in[ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html)format: YYYY-MM-DDThh:mm:ssZ
Example Values:
- '2020-04-01T00:00:00Z'
- '2020-04-01T00:00Z'

Example policy: Allow group, Contractors, to access the`instance-family`resources only until a certain date:

```

```

The access granted by the policy to the group Contractors will expire on January 1, 2022, 12:00 AM, UTC.

[request.utc-timestamp.month-of-year](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#)

Description: The month of the year that the request is received for authorization. You can write a policy that allows access only during specific months.

Supported operators: = | != | in

Allowed values: Numeric month (matching[ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html))

Example Values: '1', '2', '3', ... '12'

Example policy: Allow group, SummerInterns, to access the`instance-family`resources only during June, July, and August:

```

```

The access granted by the policy to the group SummerInterns is only valid during June, July, and August of a given year.

[request.utc-timestamp.day-of-month](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#)

Description: The day of the month that the request is received for authorization. You can write a policy that allows access only for specific days of the month. Keep in mind that the span of the day is calculated based on UTC. For example, suppose you are in Miami, FL, USA, and you enter '1' to indicate the first day of the month. For the month of February, the policy will be in effect for 12:00 AM through 11:59 PM UTC on February 1, which in Miami is 7:00 PM on January 31 through 6:59 PM on February 1.

Supported operators: = | != | in

Allowed values: Numeric day of month

Example Values: '1', '2', '3', ... '31'

Example policy: Allow group, ComplianceAuditors, to read`all-resources`only on the first day of the month.

```

```

The access granted by the policy to the group ComplianceAuditors is only valid on the first day of each month (the day is defined by UTC time).

[request.utc-timestamp.day-of-week](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#)

Description: The day of the week that the request is received for authorization. You can write a policy that allows access only for specific days of the week. Note that the span of the day is calculated based on UTC. For example, suppose you are in Miami, FL, USA, and you enter 'monday'. The policy will be in effect for 12:00 AM through 11:59 PM UTC on Monday, which in Miami is 7:00 PM (EST) on Sunday through 6:59 PM on Monday.

Supported operators: = | != | in

Allowed values: Name of day of week in English

Example Values: 'Monday', 'Tuesday', 'Wednesday', etc.

Example policy: Allow group, WorkWeek, to manage`instance-family`only during the company work week.

```

```

The access granted by the policy to the group WorkWeek is only valid on the days specified (the day is defined by UTC time).

[request.utc-timestamp.time-of-day](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#)

Description: The time of day that the request is received for authorization. You can write a policy that allows access only for a specific span of time during the day. Note that the time of the day is calculated based on UTC. If you live in a time zone that implements daylight savings, you will need to update the policy when the time changes.

Supported operators: between

Allowed values: UTC time interval in ISO 8601 format: hh:mm:ssZ

Example Values: '01:00:00Z' AND '2:01:00Z'

Example policies: Allow group DayShift to manage instances and related resources between the hours of 9:00 AM and 5:00 PM Pacific Standard Time (PST).

Note that the times are converted to UTC:

```

```

I want to allow group NightShift to manage instances and related resources between 5:00 PM and 9:00 AM PST.

```

```
