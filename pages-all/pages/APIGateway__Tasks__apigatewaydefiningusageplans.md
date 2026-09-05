# Defining Usage Plans to Manage Subscriber Access to APIs
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans.htm
- Fetched: 2026-09-05 01:38 CDT

# Defining Usage Plans to Manage Subscriber Access to APIs

Find out how to define usage plans to manage subscriber access to APIs with API Gateway.

Having created an API gateway and deployed one or more APIs on it, API plan managers typically want to:
- monitor and manage the API consumers and API clients that access APIs
- set up different access tiers for different customers.

As an API plan manager, you can monitor and manage API access by creating usage plans and subscribers. See[Usage Plans and Entitlements, Subscribers, and Client Tokens](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Concepts/apigatewayconcepts.htm#Usage_plans_and_entitlements_subscribers_and_client_tokens).

You can make API access subject to rate limits and quotas tailored to particular customer needs, enabling you to set up different access tiers for different customers. For example, you might want to offer three tiers of access to your APIs: a Gold tier, allowing up to 1000 requests per hour; a Silver tier, allowing up to 500 requests per hour; and a Bronze tier, allowing up to 100 requests per hour. You might also want to impose a general rate limit of 10 requests per second for each customer, to ensure that heavy use by one customer does not affect other customers.

To set up a usage plan and a subscriber to manage access to an API, you have to:
- 

Make an API deployment eligible for inclusion in a usage plan.

To make an API deployment eligible for inclusion in a usage plan, you have to specify the location of a client token passed in a request. Once the API deployment has been included in a usage plan, requests from subscribed API clients must include the client token in this location in order to access the API deployment. You specify the client token location in a global usage plan request policy for all routes in an API deployment specification. See[Making an API Deployment Eligible for Inclusion in a Usage Plan](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans_topic-Making_an_API_Deployment_Eligible_for_Inclusion_in_a_Usage_Plan.htm).
- 

Create a usage plan with an entitlement that specifies the API deployment as a target.

Having made the API deployment eligible for inclusion, you can create a usage plan definition that includes an entitlement that specifies the API deployment as a target, and optionally specifies a rate limit and a quota. If the number of requests in a given time period exceed a request quota, you can specify whether requests continue to be allowed, or are rejected. If a request is rejected because the quota has been exceeded, the response header indicates when the request can be retried. See[Creating a Usage Plan](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans_topic-Creating-a-usage-plan.htm).
- 

Create a subscriber definition that specifies the usage plan.

Having created a usage plan, you can create one or more subscriber definitions for your customers (API consumers) and their API clients. A subscriber definition includes client names and client tokens to uniquely identify API clients, and specifies the usage plan that gives them access to your APIs. See[Creating a Subscriber](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans_topic-Creating-a-subscriber.htm).

Having set up a usage plan, you can use metrics to understand patterns of usage, and to send alarm messages when rate limits and quotas are approached and exceeded. See[API Gateway Metrics](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Reference/apigatewaymetrics.htm)
