# Writing Policies for Dynamic Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/Writing_Policies_for_Dynamic_Groups.htm
- Fetched: 2026-09-05 02:20 CDT

# Writing Policies for Dynamic Groups

After you create a dynamic group, you need to create policies to permit the dynamic groups to access Oracle Cloud Infrastructure services.

Policy for dynamic groups follows the syntax described in[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/../policieshow/Policy_Basics.htm). Review that topic to understand basic policy features.

To create policies, see[Creating a Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/../policymgmt/managingpolicies_topic-To_create_a_policy.htm).

The syntax to permit a dynamic group access to resources in a compartment is:
```

```

The syntax to permit a dynamic group access to a tenancy is:
```

```

Here are a few example policies:

To allow a dynamic group (FrontEnd) to use a load balancer in a specific compartment (ProjectA):
```

```

To allow a dynamic group to launch instances in a specific compartment:
```

```
