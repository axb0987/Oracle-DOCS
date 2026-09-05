# Deny Policies Known Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/known-issues/known-issues-deny-policies.htm
- Fetched: 2026-09-05 02:23 CDT

# Deny Policies Known Issues

Known issues for working with IAM deny policies.

## Initial Propagation Delay for Tag-based Deny Policies

When you enable IAM deny policies in a tenancy for the first time, tag-based deny policies on users, groups, and dynamic groups can take up to 24 hours to become fully effective.

## IAM Deny Policies Don't Override Identity Domain Administration Roles

IAM Deny policies don't override identity domains administration roles (for example, identity domain administrator, security administrator, or user manager).

## Target Resource Tag-based Deny Policies Don't Block Console-initiated Deletions

IAM deny policies that use target tags don't prevent the deletion of users, groups, or dynamic groups when these actions are initiated from the Console.

Example :
```

```

## Deny Conditions Using Dynamic Group Identifiers Aren't Supported

IAM deny policies don't enforce policies that use`target.dynamicgroup.id`or`target.dynamicgroup.name`across the Console, SDK, or API.

You can manage access using tags in two ways:
- By using the tags applied to the requesting resource (which ever resource is requesting the access).
- By using the tags applied to the Target resource (tags on the resource for which access is being restricted).

See[Using Tags to Manage Access](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingaccesswithtags.htm)
Examples :
```

```

```

```
