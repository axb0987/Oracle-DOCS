# Security Policy Examples
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security_topic-Security_Policy_Examples.htm
- Fetched: 2026-09-05 03:04 CDT

# Security Policy Examples

Learn how to use policies to create service-level administrators for least privilege, restrict the ability of administrators to change tenancy administrators group membership, and how to prevent administrators from deleting or updating security policies, as well as prevent them from accessing or altering user credentials.

Common IAM security policy examples are available at[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). In all the examples that follow, the policies are scoped to a tenancy. However, by specifying a compartment name, you can scope down the policies to specific compartments in a tenancy.

## Create Service-level Admins for Least Privilege

To implement security principle of least privilege, you can create service-level admins in the tenancy to further scope down administrative access. This means that service-level administrators can only manage resources of a specific service. For instance, network administrators need administrative (`manage`) access only to VCN resources, and not to other resources. The following example shows how to create administrator groups for block storage (`VolumeAdmins`), VCN (`NetworkAdmins`), databases (`DBAdmins`), and object storage (`StorageAdmins`).

```

```

You can further constrain the security policies to a specific compartment. For example, the HR department in an enterprise can create group`HRAdmins`to manage resources within its compartment,`HR-compartment`. The`HRNetworkAdmins`group has administrative access to VCN resources only within the`HR-compartment`compartment.

```

```

Compliance auditors are tasked with examining cloud resources and verifying for policy violations. The following policy allows group`InternalAuditors`to inspect (`list`) all resources in a tenancy.

```

```

If you want to limit auditors to only inspect users and groups in a tenancy, you can create a group`UserAuditors`with the following policy:

```

```

If you want to create an auditor group that can only inspect VCN firewalls in the tenancy, use the following policy:

```

```

In all the policy examples, you can constrain the policies to a compartment by specifying`Compartment <name>`(where &lt;name&gt; is the compartment name) in the policy.

## Restrict Ability to Change Tenancy Administrators Group Membership

Members in the group`Administrators`can manage all resources in a tenancy. Membership of the`Administrators`group is controlled by users in the group. Usually, it's convenient to have a group to create and add users in the tenancy, but restrict them from making changes to the`Administrators`group membership. The following example creates a group`UserAdmins`to do this.

```

```

Use verb with conditions (third and fourth policy statements) allows`UserAdmins`to add users and groups using APIs (`UpdateUser`,`UpdateGroup`) to all groups in the tenancy except the`Administrators`group. However, because`target.group.name!='Administrators`' is not related to the`list`and`get`APIs (`ListUsers`,`GetUser`,`ListGroups`, and`GetGroup`), these APIs will fail. So you must explicitly add the`inspect`verb (first and second policy statements) to allow`UserAdmins`to get user and group membership information.

## Prevent Delete or Update of Security Policies

The following example creates a group`PolicyAdmins`to be able to create and list security policies created by tenancy administrators, but not delete or update them.

```

```

This security policy statement explicitly only allows`POLICY_CREATE`permission, and not to`POLICY_DELETE`and`POLICY_UPDATE`.

## Prevent Admins from Accessing or Altering User Credentials

Some compliance requirements need separation of duties, especially where user credential management functionality is separated from tenancy management. In this case, you can create two administration groups,`TenancyAdmins`and`CredentialAdmins`where`TenancyAdmins`can perform all tenancy management functions except user credential management, and`CredentialAdmins`can manage user credentials.`TenancyAdmins`can access all APIs except those that list, update, or delete user credentials.`CredentialAdmins`can only manage the user credentials.

```

```
