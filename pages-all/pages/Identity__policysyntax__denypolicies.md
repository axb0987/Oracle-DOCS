# Deny Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/denypolicies.htm
- Fetched: 2026-09-05 02:27 CDT

# Deny Policies

Oracle Cloud Infrastructure (OCI) Identity and Access Management (IAM) deny policies are an opt-in feature that enable administrators to explicitly block unwanted actions, which enhances security and streamlines access control. The deny option isn't enabled by default. Administrators must enable it.

IAM deny policies introduce deny statements that simplify policy management, enabling easier restriction of resource access. Only members of the default administrator group in the default domain can enable deny policies through a guided workflow in the Console. During setup, the following default root-level policy restricts who can manage deny statements, ensuring that only the tenancy administrator who enabled IAM deny is allowed to write deny policies, along with members of the default administrators group:
```

```

Members of the default administrator group in the default domain are always exempt from a deny policy to ensure continued access at the highest level.

To help control risk, administrators can enable notifications for deny policy changes. While deny policies enhance security and flexibility, they must be managed carefully, because administrators in child compartments can use deny policies to block parent access. Deny policies take precedence over allow policies.

Advantages of IAM deny policies include the following:
- Opt-In Protection: Disabled by default. Tenancy administrators must explicitly enable the deny feature, thus reducing unintentional risk.
- Stronger Access Control: Enables explicit blocking of access, which permits finer governance even over privileged users.
- Stronger Guardrails: Root administrators can set broad, tenancy-wide restrictions.

## Policy Syntax

Deny policy syntax matches allow policy syntax except that policy statements begin with the`deny`keyword. Allow policies start with`allow`stated or implied:
- `allow`...
- `admit`...
- `endorse`...

Deny policies explicitly state`deny`:
- `deny`...
- `deny admit`...
- `deny endorse`...

### Context Variable

By using the policy-type variable, you can restrict policy authors to create only specific types of policies. For example, you can restrict users to create only allow policies within a specified compartment. To support this, the`target.policy.type`context variable is in the policy create, update, and delete APIs. The`target.policy.type`value is a set and can contain values for both`allow`and`deny`when a single policy has both allow and deny statements.
Note  
  
The`target.policy.type`context variable applies across all three types of deny policies:`deny`,`deny admit`, and`deny endorse`.

Key Value Description
`target.policy.type`allow/deny Specifies whether the policy being modified is 1 of 5 allow policies or 1 of 3 deny policies

The following is an example allow policy using the`target.policy.type`variable:
```

```

Or alternatively:
```

```

The same result can be achieved using a deny policy:
```

```

Note  
  
When using an allow policy, an '=' comparison (instead of sets-equal or '!=') would not behave as expected. An '=' comparison would match if at least one of the statements had the value, but not necessarily all.

### Metaverb Inversion

IAM deny policies limit access by removing specific permissions, ensuring only intended actions are allowed. Deny policies override allow policies to restrict access. In contrast, IAM allow policies grant permissions to access resources.

Note  
  
The level of access is cumulative (from the least level of access to the highest level of access). The hierarchy is`inspect`(the lowest level of access) to`read`to`use`to`manage`(the highest level of access).

For example, when allowing permissions, granting access to`manage`permissions typically means a user is also granted permissions such as`read`or`inspect`. The`manage`verb always expands scope to include the`use`,`read`, and`inspect`permissions on a resource.

However, when denying permissions, the opposite is true. When a policy is written denying access to`manage`permissions, it doesn't necessarily block permissions for`inspect`,`read`, or`use`.

For example, if you write a deny policy to block an`inspect`permission, typically you would also want to restrict the`read`,`use`, or`manage`permissions. In other words, denying the ability to`inspect`a resource would also deny the ability to`read`,`use`, or`manage`it.

For allow policies, include all metaverbs with equal or lower permissions than the specified one.

For deny policies, include all metaverbs with higher permissions than the specified one. For example, the following policy would block SampleGroup from deleting any buckets, but wouldn't block`read`access. This assumes another policy granted that access, as AuthZ is still deny by default.
```

```

Whereas the following policy would block SampleGroup from doing anything to those buckets. Deny access means denying all the lower level permissions as well.
```

```

Specific permission strings can still be denied as they are today with allow policies, if there's a need to do so.
```

```

## Account Lockout Prevention

Deny policies could unintentionally lock out users from a tenancy if an overly broad deny policy is written. For example, if a compartment administrator creates a policy such as`deny any-user to inspect any-resource in compartment X`, the policy blocks all users from accessing resources in that compartment, including the administrator who created the policy. To prevent this, the default administrators group that gets created in each tenancy in the default domain is exempt from deny policies. This allows the default administrators group access if someone is accidentally locked out by a broad deny policy.

## Enabling the IAM Deny Policy Feature

To use IAM deny policies, you must first enable the feature.

- On the Policies list page, select the Actions menu, and then select Policy settings . If you need help finding the list page, see[Listing Polices](https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/../policymgmt/managingpolicies_topic-To_get_a_list_of_your_policies.htm#console).
- Select Enable IAM Deny Policy .

Important  
  
Enabling IAM deny policies is permanent and must be done deliberately. When the feature is enabled, you can't turn it off. You can, however, create a deny policy that restricts the use of other deny policies.
- Confirm the action by selecting Enable .
- Select Yes for the system to automatically create a default deny policy that prevents all users from authoring deny statements.

Note  
  

When the system automatically creates this default deny policy, the default administrative group and the tenancy administrator who enabled IAM deny policies retain permission to manage the policy.
Results: The IAM Deny policy details page displays with information about the policy including OCID, the compartment to which the policy applies, and the date the policy was created.

Important  
  
What to do next: Familiarize yourself with the[Deny Policies Known Issues](https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/../known-issues/known-issues-deny-policies.htm#top)
