# Conditions
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/conditions.htm
- Fetched: 2026-09-05 02:27 CDT

# Conditions

The optional conditions element of a policy statement limits access based on the provided attributes in IAM.

A condition returns resources based on specified parameters. For example, use a condition to return resources that have certain characters in their names.

Syntax for a single condition:`variable =|!= value`

Syntax for multiple conditions:`any|all { <condition>,<condition>,... }`

To create a logical OR for a set of conditions, use`any`. To create a logical AND for a set of conditions, use`all`.

Important  
  

Condition matching ignores case-sensitive names. For example, a condition for a bucket named "BucketA" also matches a bucket named "bucketA."
- String :
- `'johnsmith@example.com'`
- `' ocid1 . compartment . oc1 .exampleuniqueID'`(single quotation marks are required around the value)
- Pattern :
- 

`/hr*/`(matches strings that start with "hr")
- 

`/*hr/`(matches strings that end with "hr")
- 

`/*hr*/`(matches strings that contain "hr")
Note  
  
In the following examples, the statements that specify the condition don't let GroupAdmins list all the users and groups. Statements including the`inspect`verb are added for completeness. See[Variables Not Applicable to a Request Result in a Declined Request](https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/conditions.htm#variables_that_arent_applicable_to_request_result_in_declined_request).

Examples:
- Single condition:

Single condition for one resource type (groups)
```

```

Single condition for many resource types (users and groups)
```

```

```

```

```

```

```

```

Many conditions for one resource (groups)
```

```

- Several conditions

The following policy lets GroupAdmins create, update, or delete any groups whose names start with "`A-`", except for the`A-Admins`group itself:
```

```

## Variables Not Applicable to a Request Result in a Declined Request

If the variable is not applicable to the incoming request, the condition evaluates the request as false and the request is declined. For example, here are some basic policy statements that together let someone add or remove users from any group except Administrators :
```

```

If a user in GroupAdmins tried to call a general API operation for users, such as`ListUsers`or`UpdateUser`(which lets you change the user's description), the request is declined, even though those API operations are covered by`use users`. The example policy statement for`use users`includes a`target.group.name`variable, but the`ListUsers`or`UpdateUser`request doesn't specify a group. The request is declined because a`target.group.name`wasn't provided.

To grant access to a general user when an API operation doesn't involve a particular group, you need to add another statement that gives the level of access that you want to grant but doesn't include the condition. For example, to grant access to`ListUsers`, you need a statement similar to this statement:
```

```

To grant access to`UpdateUser`, you need this statement (which also covers`ListUsers`because the`use`verb includes the capabilities of the`inspect`verb):
```

```

This general concept also applies any other resource type with target variables, for example, ListGroups .

## Tag-Based Access Control

Use conditions and a set of tag variables to write policies that define access based on the tags applied to a resource. You can control access based on a tag that exists on the requesting resource (the group or dynamic group in the policy), or on the target of the request (resource or compartment). Tag-based access control provides flexibility to policies, letting you define access that spans compartments, groups, and resources. For details about how to write policies to scope access by tags, see[Using Tags to Manage Access](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm)
