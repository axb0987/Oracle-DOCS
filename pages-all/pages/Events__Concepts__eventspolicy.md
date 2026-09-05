# Events and IAM Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/eventspolicy.htm
- Fetched: 2026-09-05 02:01 CDT

# Events and IAM Policies

Write policies for the Events service, including authorizations for non-administrator users and the Events service itself.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Policy Builder Policy Templates](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more details about how to write IAM policy for Events, see[Details for the Events Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/cloudeventspolicyreference.htm).

## Allow Users to Work with Rules

These IAM policies allow users to manage or list rules.

### Let Users List Rules in a Compartment

Type of access: Ability to list Events rules.

Where to create the policy: In the tenancy.

```

```

The preceding policy allows RuleReaders to list rules in the tenancy.

### Let Admins Manage Rules in a Compartment

Type of access: Ability to manage Events rules, including creating, deleting, updating or moving rules to a different compartment.

Where to create the policy: In the tenancy.

This line gives the user inspect access to resources in compartments to select actions.

```

```

This line gives the user access to defined tags to apply filter tags to rules.

```

```

These lines give the user access to Streaming resources for actions

```

```

These lines give the user access to Functions resources for actions.

```

```

This line give the user access to Notifications topics for actions.

```

```

This line gives the user manage access to rules for Events.

```

```

### Allow Cross-tenancy Deliveries

Cross-tenancy delivery lets you to trigger an action in a different tenancy from the Events rules. Adjust the permissions on the action use case as needed. Use the following policies to enable cross-tenancy delivery.

Type of access: Ability to trigger actions that are in a different tenancy from the Events rules.
Where to create the policy: In the rule tenancy.
```

```

Where to create the policy: In the action tenancy.
```

```

For more details on cross-tenancy policies, see[Cross-tenancy Policies](https://docs.oracle.com/iaas/database-tools/doc/cross-tenancy-policies.html)
