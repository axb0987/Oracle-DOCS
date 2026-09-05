# IAM Policies Overview
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm
- Fetched: 2026-09-05 02:26 CDT

# IAM Policies Overview

IAM policies govern control of resources in Oracle Cloud Infrastructure (OCI) tenancies.

A policy contains one or more policy statements. Each statement uses basic or conditional syntax.

Basic syntax:
```

```

Conditional syntax:
```

```

The following table briefly explains the elements in the syntax and provides links to detailed information about each element.

Element Description
Allow Required start word. A policy statement always begins with the word`Allow`. Policies only allow access; they can't deny it.
[&lt;subject&gt;](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/../policysyntax/subject.htm)

A user, group, or other principal to be granted access. The subject includes the principal type and identifier (name or OCID), and is prefixed by the name of the identity domain unless the default identity domain is used.

An administrator in your organization defines the groups and compartments in your tenancy.
```

```

[&lt;verb&gt;](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Verbs.htm)The level of access. Oracle defines the possible verbs and resource-types you can use in policies, see[Verbs](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Verbs.htm).
[&lt;resource&gt;](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/../policiesgs/policies_topic-ResourceTypes.htm)

Resources to which the policy grants access. Oracle defines the possible resource-types you can use in policies, see[Resources](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/../policiesgs/policies_topic-ResourceTypes.htm). Some API operations require access to several resource-types. For example,`LaunchInstance`requires the ability to create instances and work with a cloud network. The`CreateVolumeBackup`operation requires access to both the volume and the volume backup. That requires separate policy statements to give access to each resource type. These individual statements don't have to be in the same policy. A user can gain the required access from being in different groups.
[&lt;location&gt;](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/../policysyntax/location.htm)

(Optional) A compartment or tenancy to which the policy applies. For a compartment, the value includes an identifier (name or OCID).

Sometimes the policy needs to apply to the entire tenancy, and not a compartment inside the tenancy. The following is an example of a compartment-specific policy statement, in which the &lt;location&gt; is a specific compartment:
```

```

Following is an example of a tenancy-wide policy statement, in which the &lt;location&gt; is tenancy:
```

```

[&lt;condition&gt;](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/../policysyntax/conditions.htm)(Optional) Limits access to a resource.
[

OCI also lets you create cross-tenancy policies. For more information, see[Cross-Tenancy Access Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/iam-cross-domain.htm).

## Cross-tenancy Policies

Cross-tenancy policy statements give subjects permission to use resources in other tenancies. See[Cross-Tenancy Access Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/iam-cross-domain.htm)
