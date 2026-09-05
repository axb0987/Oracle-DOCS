# Service Limits
- Source: https://docs.oracle.com/en-us/iaas/Content/General/service-limits/overview.htm
- Fetched: 2026-09-05 02:13 CDT

# Service Limits

Learn about the service limits for Oracle Cloud Infrastructure.

When you sign up for Oracle Cloud Infrastructure, a set of service limits is configured for your tenancy. The service limit is the[quota](https://docs.oracle.com/iaas/Content/Quotas/home.htm)or allowance set on a resource. For example, a tenancy is allotted a maximum number of Compute instances per availability domain. These limits are established with the Oracle sales representative when you buy Oracle Cloud Infrastructure. If you didn't establish limits with the Oracle sales representative, or, if you signed up through the Oracle Store, default or trial limits are set for your tenancy. These limits might be increased for you automatically based on your Oracle Cloud Infrastructure resource usage and account standing. You can also[request a service limit increase](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/create-request.htm).

Depending on whether you have a subscription, you can[view the limits and usage](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/view-tenancy.htm)for it. The same service can have two different limit values, depending on which subscription you have selected on the Limits, Quotas and Usage page. Some services aren't tied to any subscription, but still have limit values associated with them.

## Tasks

- [Viewing a Tenancy's Limits and Usage](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/view-tenancy.htm)
- [Working with Limit Increase Requests](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/requests.htm)
- [Listing Limit Increase Requests](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/list-requests.htm)
- [Getting Details for a Limit Increase Request](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/get-request.htm)
- [Creating a Limit Increase Request](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/create-request.htm)
- [Withdrawing an Item from a Limit Increase Request](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/withdraw-item-request.htm)
- [Withdrawing a Limit Increase Request](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/withdraw-request.htm)

You can also look up the default limits for a service. See[Limits by Service](https://docs.oracle.com/en-us/iaas/Content/General/service-limits/default.htm).

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're in the[Administrators group](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm#The), you have permission to view limits and usage. If you're not, here's an example[IAM policy](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm)that grants the required permission to users in a group called`LimitsAndUsageViewers`:

```

```

For the resource availability API (usage) the policy can be at the tenant or compartment level:
```

```

For limit definitions, services, and values APIs (only at the tenant level):
```

```

For limit values APIs (doesn't include definitions or services), the following policy is also supported:
```

```

READ resource-availability is required to obtain the resource availability. Four APIs are available:
- [ListServices](https://docs.oracle.com/iaas/api/#/en/limits/latest/ServiceSummary/ListServices)
- [ListLimitDefinitions](https://docs.oracle.com/iaas/api/#/en/limits/latest/LimitDefinitionSummary/ListLimitDefinitions)
- [ListLimitValues](https://docs.oracle.com/iaas/api/#/en/limits/latest/LimitValueSummary/ListLimitValues)
- [GetResourceAvailability](https://docs.oracle.com/iaas/api/#/en/limits/latest/ResourceAvailability/GetResourceAvailability)

[ListServices](https://docs.oracle.com/iaas/api/#/en/limits/latest/ServiceSummary/ListServices),[ListLimitDefinitions](https://docs.oracle.com/iaas/api/#/en/limits/latest/LimitDefinitionSummary/ListLimitDefinitions), and[ListLimitValues](https://docs.oracle.com/iaas/api/#/en/limits/latest/LimitValueSummary/ListLimitValues)all require INSPECT at the tenancy level, while[GetResourceAvailability](https://docs.oracle.com/iaas/api/#/en/limits/latest/ResourceAvailability/GetResourceAvailability)requires READ at the compartment level to read the data.

## Compartment Quotas

Compartment quotas are similar to service limits, however, the biggest difference is that service limits are set by Oracle, and compartment quotas are set by administrators, using policies that allow administrators to allocate resources with a high level of flexibility. Compartment quotas are set using policy statements written in a declarative language that's similar to the IAM policy language.

To learn more, see[Overview of Compartment Quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).

## When You Reach a Service Limit

When you reach the service limit for a resource, you receive an error when you try to create a new resource of that type. You're then prompted to submit a request to increase the limit. You can't create a new resource until you're granted an increase to the service limit, or you delete an existing resource.

In addition, limit increase requests might not be approved because of security concerns or if limit increases aren't allowed for a particular resource.
Note
