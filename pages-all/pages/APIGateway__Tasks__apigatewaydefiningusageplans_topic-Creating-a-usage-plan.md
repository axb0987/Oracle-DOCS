# Creating a Usage Plan
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans_topic-Creating-a-usage-plan.htm
- Fetched: 2026-09-05 01:38 CDT

# Creating a Usage Plan

Find out how to create a usage plan as part of a strategy to monitor and manage the number of requests sent to back-end services with API Gateway.

As an API plan manager, you can create usage plans and subscribers to monitor and manage API access, and to set up access tiers. See[Usage Plans and Entitlements, Subscribers, and Client Tokens](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Concepts/apigatewayconcepts.htm#Usage_plans_and_entitlements_subscribers_and_client_tokens).

A usage plan can include an entitlement with one or more target API deployments, and optionally specifies a rate limit and a quota for that entitlement. If the number of requests in a given time period exceeds the entitlement's request quota, you can specify whether requests continue to be allowed, or are rejected. If a request is rejected because the quota has been exceeded, the response header indicates when the request can be retried.

You can create a usage plan that comprises multiple entitlements, enabling you to specify different rate limits and quotas for different API deployments.

Before you can create a usage plan, the API deployment(s) for which you are creating the usage plan must already exist. In addition, you must have already made the API deployment(s) eligible for inclusion in the usage plan (see[Making an API Deployment Eligible for Inclusion in a Usage Plan](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans_topic-Making_an_API_Deployment_Eligible_for_Inclusion_in_a_Usage_Plan.htm)).

Note the following:
- If a usage plan contains an entitlement to multiple API deployments, any rate limit or quota you specify is shared between the API deployments in the entitlement.
- A usage plan cannot contain different entitlements that specify a rate limit or quota for the same API deployment. In other words, an API deployment can be specified as a target in multiple entitlements in different usage plans, but not in multiple entitlements in the same usage plan.
- You can include API deployments from different API gateways in the same entitlement.
- If you do not specify a rate limit and/or quota for an entitlement, an unlimited rate limit and/or quota applies to the entitlement's target API deployments. Note that even if no rate limit and/or no quota is specified for an entitlement, API clients must still be subscribed to the usage plan and must still pass a client token in order to access the target API deployments.
- If you update a usage plan and change an entitlement's quota time period to a different time period (for example, from Day to Week), a new request number count is started. However, if you subsequently update the usage plan again and change the quota time period back to its original value, the previous request number count is resumed from where it left off (unless a new time period has started in the meantime, in which case the count is reset to zero).
- Once an API deployment has been included in a usage plan, requests from subscribed API clients to the API deployment must include the client token in the location specified in the usage plan's request policy. An HTTP-403 error is returned in response to requests that do not include the client token in the specified location, and in response to requests from unsubscribed API clients.
- Requests that return HTTP-4xx error responses count towards both an entitlement's quota and its rate limit. Requests that return HTTP-5xx error responses count towards an entitlement's rate limit, but not towards its quota.
- On receipt of requests to API deployments that are included as targets in usage plan entitlements, API gateways perform authentication and authorization checks before checking entitlement rate limits and quotas. Requests that fail authentication and authorization checks do not count towards either an entitlement's quota or its rate limit.
- You can create a usage plan definition that initially doesn't have entitlements, and then add them later. Note that until you have added entitlements to a usage plan definition, the usage plan cannot be used to access your APIs.

You can create a usage plan by:
- using the Console
- using the CLI and a JSON file

## Using the Console to Create a Usage Plan

To create a new usage plan and one or more entitlements using the Console:
- On the Usage plans list page, select Create usage plan . If you need help finding the list page, see[Listing Usage Plans](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-usageplans.htm).
- 

Specify the following values for the usage plan:
- Name: The name of the new usage plan. For example,`Gold-usage-plan`. Avoid entering confidential information.
- Compartment: The compartment to which the new usage plan is to belong.
- (Optional) In the Tags section, select Add tag to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- 

Select Next to specify the API deployments that API consumers and API clients subscribed to the usage plan are entitled to access.

A usage plan comprises entitlements. Each entitlement specifies one or more target API deployments to which subscribers to the usage plan are entitled to send requests, along with the number of requests they are entitled to send.
- 

On the Entitlements page:
- 

Select Create entitlement and specify details for the usage plan's first entitlement:
- Name: The name of the new entitlement. Entitlement names must be unique within a usage plan. For example,`Entitlement1`. Avoid entering confidential information.
- Description: A description of the new entitlement. For example,`Basic entitlement for all usage plans`. Avoid entering confidential information.
- Rate limit: (Optional) Select Enable rate limit to specify a maximum number of requests to allow per second as Requests per second .
- Quota: (Optional) Select Enable quota to specify a maximum number of requests to allow in a given time period:
- Requests: Maximum number of requests to allow.
- Period : Time period to which the maximum number of requests applies. One of Minute , Hour , Day , Week , or Month .
- 

Reset policy: When to reset the count of the number of requests to zero. The Calendar reset policy is supported. With the Calendar reset policy, the request number count is reset to zero at the start of each new time period, as specified by Period .

For example, if Period is set to Day , the request number count is initially set to zero when the entitlement is first created. The count is then reset to zero at the start of the following day (that is, at midnight UTC). The count is reset to zero at the start of the next day, and so on.
- Operation on breach: What happens if the maximum number of requests in the time period you specify is exceeded. If you specify Reject , additional requests in the time period are rejected and return an`HTTP-429 Too Many Requests`response. The response includes the`Retry-After`header, indicating how long to wait before making a new request. If you specify Allow , additional requests in the time period are still allowed.
- Targeted deployments: Select Add deployment to specify the first API deployment to include in the entitlement:
- Gateway: Select the API gateway on which the API deployment has been created, from the list of API gateways in the specified compartment. The API gateway can belong to the same compartment as the usage plan, but does not have to.
- Deployment: Select the API deployment that you want to include in the entitlement, from the list of API deployments in the specified compartment. The API deployment can belong to the same compartment as the usage plan, but does not have to.

Note that you must have already made the API deployment eligible for inclusion in the usage plan by specifying the location of a client token (see[Making an API Deployment Eligible for Inclusion in a Usage Plan](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans_topic-Making_an_API_Deployment_Eligible_for_Inclusion_in_a_Usage_Plan.htm)).

Select Update to save details of the first API deployment included in the entitlement. Optionally, select Add deployment again to specify additional API deployments to include in the usage plan's first entitlement.
- Select Create to save the usage plan's first entitlement.
- Optionally, select Create entitlement again and specify details for additional entitlements to include in the usage plan.
- Select Next to review the details you entered for the usage plan.
- Select Create to create the usage plan.

Note that it can take a few minutes to create the new usage plan. While it is being created, the usage plan is shown with a state of Creating on the Usage plans list page. When it has been created successfully, the new usage plan is shown with a state of Active.

Also note that rather than creating the new usage plan immediately, you can create it later using Resource Manager and Terraform, by selecting Save as stack to save the resource definition as a Terraform configuration. For more information about saving stacks from resource definitions, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
- 

If you have waited more than a few minutes for the usage plan to be shown with an Active state (or if the usage plan creation operation has failed):
- Select the name of the usage plan, and select Work requests to see an overview of the usage plan creation operation.
- Select the Create Usage Plan operation to see more information about the operation (including error messages, log messages, and the status of associated resources).
- If the usage plan creation operation has failed and you cannot diagnose the cause of the problem from the work request information, see[Troubleshooting API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting.htm).

## Using the CLI and a JSON File to Create a Usage Plan

To create a new usage plan and one or more entitlements using the CLI:
- Using your preferred JSON editor, create a usage plan definition file in the format:

```

```

where:
- `"displayName": "<usage-plan-name>"`is the name of the new usage plan. For example,`"displayName": "Gold-usage-plan"`. Avoid entering confidential information.
- `"entitlements": [{...}]`specifies details of one or more entitlements, where:
- `"name": "<entitlement-name>"`is the name of a new entitlement. Entitlement names must be unique within a usage plan. For example,`"Entitlement1"`. Avoid entering confidential information.
- `"description": "<entitlement-description>"`is a description of the new entitlement. For example,`"description": "Basic entitlement for all usage plans"`. Avoid entering confidential information..
- `"rateLimit": {…}`optionally specifies a maximum number of requests to allow per second. If you define a rate limit, you must include values for all of the following:
- `"value": <rate-limit-value>`is the maximum number of requests to allow. For example,`"value": 100`.
- `"unit": "<rate-limit-unit>"`is the rate limit's unit of time. Must be set to`"SECOND"`.
- `"quota": {…}`optionally specifies a maximum number of requests to allow in a given time period. If you define a quota, you must include values for all of the following:
- `"value": <quota-value>`is the maximum number of requests to allow per time period. For example,`"value": 1000`
- `"unit": "<quota-unit>"`is the time period to which the maximum number of requests applies. Must be set to one of`MINUTE`,`HOUR`,`DAY`,`WEEK`, or`MONTH`. For example,`"unit": "MONTH"`.
- `"resetPolicy": "CALENDAR"`is when the count of the number of requests is reset to zero. The`CALENDAR`reset policy is supported. With the`CALENDAR`reset policy, the request number count is reset to zero at the start of each new time period, as specified by`"unit"`.

For example, if`"unit": "DAY"`, the request number count is initially set to zero when the entitlement is first created. The count is then reset to zero at the start of the following day (that is, at midnight UTC). The count is reset to zero at the start of the next day, and so on.
- `"operationOnBreach": "<REJECT|ALLOW>"`specifies what happens if the maximum number of requests in the quota's time period is exceeded. If you specify`REJECT`, additional requests in the time period are rejected and return an`HTTP-429 Too Many Requests`response. The response includes the`Retry-After`header, indicating how long to wait before making a new request. If you specify`ALLOW`, additional requests in the time period are still allowed. For example,`"operationOnBreach": "REJECT"`
- `"targets": [{…}]`specifies one or more target API deployments that subscribers to the usage plan are entitled to access, where:
- `"deploymentId": "<target-deployment-ocid>"`is the OCID of the API deployment that you want to include in the entitlement. The API deployment can belong to the same compartment as the usage plan, but does not have to. For example,`"deploymentId": "ocid1.apideployment.oc1..aaaaaaaaab______pwa"`

Note that you must have already made the API deployment eligible for inclusion in the usage plan by specifying the location of a client token (see[Making an API Deployment Eligible for Inclusion in a Usage Plan](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans_topic-Making_an_API_Deployment_Eligible_for_Inclusion_in_a_Usage_Plan.htm)).
- `"compartmentId": "<compartment-ocid>"`is the OCID of the compartment to which the new usage plan belongs. For example,`"ocid1.compartment.oc1..aaaaaaaa7______ysq"`

For example:

```

```

- Save the usage plan definition file with a name of your choice. For example,`gold-usageplan.json`
- Use the usage plan definition file to create a usage plan using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

Open a command prompt and run`oci api-gateway usage-plan create`to create the usage plan from the usage plan definition file:

```

```

where:
- `--from-json file://<usageplan-definition>.json`is the file containing the usage plan definition, including a path.

For example:

```

```

The response to the command includes:
- The usage plan's OCID, and other details.
- The lifecycle state (for example, ACTIVE, FAILED).
- The id of the work request to create the usage plan (details of work requests are available for seven days after completion, cancellation, or failure).

If you want the command to wait to return control until the usage plan is active (or the request has failed), include either or both the following parameters:
- `--wait-for-state ACTIVE`
- `--wait-for-state FAILED`

For example:

```

```

Note that you cannot use the usage plan until the work request has successfully created it and the usage plan is active.
- 

(Optional) To see the status of the usage plan, enter:

```

```

- 

(Optional) To see the status of the work request that is creating the usage plan, enter:

```

```

- 

(Optional) To view the logs of the work request that is creating the usage plan, enter:

```

```

- 

(Optional) If the work request that is creating the usage plan fails and you want to review the error logs, enter:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[CreateUsagePlan](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/UsagePlan/CreateUsagePlan)
