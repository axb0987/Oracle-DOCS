# Policy Inheritance
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm
- Fetched: 2026-09-05 02:26 CDT

# Policy Inheritance

A basic policy feature is the concept of inheritance in IAM.

Compartments inherit any policies from a parent compartment. An example is the Administrators group, which automatically comes with your tenancy (see[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/../roles/understand-administrator-roles.htm)).

The following is the built-in policy that lets the Administrators group (in the default identity domain) do anything in the tenancy:
```

```

Because of policy inheritance, the Administrators group can also do anything in any of the compartments in the tenancy.

For example, consider a tenancy that has three levels of compartments: CompartmentA, CompartmentB, and CompartmentC.

[

Policies that apply to resources in CompartmentA also apply to resources in CompartmentB and CompartmentC.

The following example allows the group NetworkAdmins (in the default identity domain) to manage VCNs in CompartmentA, which also means that it can manage VCNs in CompartmentB, and CompartmentC.
```

```
