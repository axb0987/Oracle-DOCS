# Quota Policy Syntax
- Source: https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/quota_policy_syntax.htm
- Fetched: 2026-09-05 02:52 CDT

# Quota Policy Syntax

The following topic describes compartment quota policy syntax.

Three types of quota policy statements are available:

- `set`: Sets the maximum number of a cloud resource that can be used for a compartment.
- `unset`: Resets quotas back to the default service limits.
- `zero`: Removes access to a cloud resource for a compartment. Quota policy statements have the following format:
[
[
[

The language components for a quota policy statement are:
- The`action`keyword, which corresponds to the type of quota being defined. The keyword can be`set`,`unset`, or`zero`.
- The name of the service family; for example:`compute-core`.
- The`quota`or`quotas`keyword.
- The name of the quota, which varies by service family. For example, a valid quota in the`compute-core`family is`standard-e4-core-count`.
- You can also use[wildcards](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/quota_policy_syntax.htm#advanced_features)to specify a range of names. For example,`"/standard*/"`matches all Compute quotas that start with the phrase "standard."
- For set statements, the value of the quota.
- The compartment that the quota covers.
- An optional condition. For example,`where request.region = 'us-phoenix-1'`. Currently supported conditionals are`request.region`and`request.ad`.

Also see[Sample Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/sample_quotas.htm)for some common usage examples.

## Scope

Quotas can have different scopes , and work at the availability domain, the region, or globally. The following are some important points to understand about scope when working with compartment quotas:
- 

When setting a quota at the availability domain (AD) level, the quota is allocated to each AD. So, for example, setting a quota of 120 OCPUs on a compartment actually sets a limit of 120 OCPUs per AD. To target a specific AD, use the`request.ad`parameter in the`where`clause.
- 

Regional quotas apply to each region. See[Sample Quotas](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/sample_quotas.htm)for an example of a regional quota.
- Usage for subcompartments counts toward usage for the main compartment.

For more information, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

## Permissions and Nesting

You can set compartment quotas in any compartment in the tenancy. An administrator can set quotas for their compartments and any child compartments.

A quota policy can contain statements that apply to a compartment and its child compartments. The location of a quota policy doesn't affect its precedence. A quota statement applies when the statement is in scope for the compartment where the resource request occurs.
Note  
  
Policies that target nested compartments are written like the following:
```

```

## Quota Evaluation and Precedence

The following rules apply when quota statements are evaluated:
- 

Within a policy, quota statements are evaluated in order. A later statement supersedes an earlier statement that targets the same resource.
- 

If several policies target the same resource, the most restrictive policy applies.
- 

The compartment where a quota policy is created doesn't determine precedence. For policies that target the same resource within the same compartment lineage, the most restrictive policy applies.
- 

Service limits take precedence over quotas. You can specify a quota that exceeds the service limit for a resource, but the service limit still applies.

## Wildcards

Some quota family have many resources, for example, the[Database](https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-Database_Quotas.htm)quota family is composed of many quotas. Quota name wildcards can be used in such cases to specify a range of names.

This example uses a wildcard to allocate all`exadata`resources to the`ProductionApp`compartment:
```

```
