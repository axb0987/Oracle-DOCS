# Example Usage Plans
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans_topic-Examples.htm
- Fetched: 2026-09-05 01:38 CDT

# Example Usage Plans

Find out about example usage plans to manage subscriber access to APIs with API Gateway.

## Example 1: Two different usage plans (for a 'Free' tier and a 'Premium' tier) for the same API deployment

This example shows how you, as an API plan manager, can create two usage plans for the same API deployment:
- The`Free Tier`usage plan, that limits API access by both the number of calls allowed per second (in this case, a maximum of 1 call per second), and places a quota on the total number of calls in any given day (in this case, ten calls per day).
- The`Premium Tier`usage plan, that allows unlimited calls per day and limits API access to a maximum of 1 call per second.

You define the`Free Tier`usage plan in a JSON file as:

```

```

You define the`Premium Tier`usage plan in a JSON file as:

```

```

## Example 2: Different quotas for different API deployments

This example shows how you, as an API plan manager, can create a single usage plan that specifies both a shared quota for two API deployments in the same entitlement, and also a separate quota for a different API deployment in a different entitlement in the same usage plan.

You define the`Multi-Quota`usage plan in a JSON file as:

```

```

## Example 3: Unlimited quota for a specific API deployment

This example shows how you, as an API plan manager, can include an API deployment in a usage plan and specify an unlimited quota for it. In this case, the usage plan limits API access to a maximum of 1 call per second.

You define the`Unlimited Quota`usage plan in a JSON file as:

```

```

## Example 4: No rate limit for a specific API deployment

This example shows how you, as an API plan manager, can include an API deployment in a usage plan and not specify a rate limit for it. In this case, the usage plan places a quota on the total number of calls in any given day (in this case, ten calls per day)

You define the`Unlimited Rate Limit`usage plan in a JSON file as:

```

```

## Example 5: Unlimited quota and no rate limit for a specific API deployment

This example shows how you, as an API plan manager, can include an API deployment in a usage plan and not specify either a quota or a rate limit. Note that in this case, API clients sending a request to the API deployment must still include a client token in the request.

You define the`Unlimited`usage plan in a JSON file as:

```

```

## Example 6: Triggering an alarm when quota usage reaches an at-risk threshold

This example shows how you, as an API plan manager, can write a metrics query to trigger an alarm when a subscriber consumes more than 80% of an entitlement's quota on a usage plan.

Using the Monitoring service, you define the threshold alarm by entering:

```

```

For more information, see[Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm)
