# Creating a Subscriber
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans_topic-Creating-a-subscriber.htm
- Fetched: 2026-09-05 01:38 CDT

# Creating a Subscriber

Find out how to create a subscriber as part of a strategy to monitor and manage the number of requests sent to back-end services with API Gateway.

As an API plan manager, you can create subscribers for your customers (API consumers) to specify the usage plans that give them access to your APIs. See[Usage Plans and Entitlements, Subscribers, and Client Tokens](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/../Concepts/apigatewayconcepts.htm#Usage_plans_and_entitlements_subscribers_and_client_tokens).

A subscriber definition includes client names and client tokens to uniquely identify API clients, and specifies the usage plans that give them access to your APIs.

Note the following:
- Before you can create a subscriber, at least one of the usage plans to which you want the subscriber to subscribe must already exist (see[Creating a Usage Plan](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaydefiningusageplans_topic-Creating-a-usage-plan.htm)).
- If you define a subscriber and specify multiple API clients for it, the rate limit and quota in a usage plan's entitlement are shared between all the API clients.
- Having created a subscriber, you can subsequently add and remove clients, and change client tokens.
- The client token you specify for an API client in a subscriber definition is intended for usage plan reporting purposes only. Do not use this token for API client authentication and authorization. Instead, use authorizer functions or JSON Web Tokens (JWTs) for API client authentication and authorization. See[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- If an API deployment appears in more than one of the usage plans to which a subscriber is subscribed, the first usage plan in the list of subscribed usage plans is used to access the API deployment. You can change the order of the list of subscribed usage plans.
- If a subscriber is subscribed to one usage plan and you want to subscribe the subscriber to a new usage plan, Oracle recommends you perform the operation in two steps. To begin with, add the new usage plan to the subscriber definition as the first usage plan in the list of subscribed usage plans, and save the change. Then, remove the previous usage plan from the list of subscribed usage plans, and save the change.
- You can create a subscriber definition that initially doesn't have API clients and/or target usage plans, and then add them later. Note that until you have added both API clients and target usage plans to a subscriber definition, the subscriber cannot access your APIs.

You can create a subscriber by:
- using the Console
- using the CLI and a JSON file

## Using the Console to Create a Subscriber

To create a new subscriber and subscribe it to one or more usage plans using the Console:
- On the Subscribers list page, select Create subscriber . If you need help finding the list page, see[Listing Subscribers](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaylisting-subscribers.htm).
- 

Specify the following values for the subscriber:
- Name: The name of the new subscriber. For example,`Premium-subscriber`. Avoid entering confidential information.
- Compartment: The compartment to which the new subscriber belongs.
- Clients: One or more API clients that will be accessing API deployments using the usage plans to which the subscriber is subscribed. For each API client, specify:
- Name: A name of your choice for the API client. Client names must be unique within a subscriber. For example,`android`. Recommendation: Specify a meaningful name because you might provide it to API consumers for the purpose of usage plan data collection and analysis.
- Token type: Set to Custom token to enter a character string of your choice as the Client token . The client token uniquely identifies the API client. The token you specify must be unique within your tenancy for the current region, and must not be more than 128 characters. For example,`abc123def456ghi789jkl`. If no suitable identifier exists already, set Token type to Generate token to create one.
Note  
  
The token you specify for an API client in a subscriber definition is intended for usage plan reporting purposes only. Do not use this token for API client authentication and authorization. Instead, use authorizer functions or JSON Web Tokens (JWTs) for API client authentication and authorization. See[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- Usage Plans: Select Add Usage Plan to subscribe the subscriber to one or more usage plans.
- (Optional) In the Tags section, select Add tag to apply tags to the resource. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create to create the subscriber.

Note that it can take a few minutes to create the new subscriber. While it is being created, the subscriber is shown with a state of Creating on the Subscribers list page. When it has been created successfully, the new subscriber is shown with a state of Active.

Also note that rather than creating the new subscriber immediately, you can create it later using Resource Manager and Terraform, by selecting Save as stack to save the resource definition as a Terraform configuration. For more information about saving stacks from resource definitions, see[Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
- 

If you have waited more than a few minutes for the subscriber to be shown with an Active state (or if the subscriber creation operation has failed):
- On the subscriber details page, select the name of the subscriber, and select Work requests to see an overview of the subscriber creation operation.
- Select the Create Subscriber operation to see more information about the operation (including error messages, log messages, and the status of associated resources).
- If the subscriber creation operation has failed and you cannot diagnose the cause of the problem from the work request information, see[Troubleshooting API Gateway](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaytroubleshooting.htm).

## Using the CLI and a JSON File to Create a Subscriber

To create a new subscriber and subscribe it to one or more usage plans using the CLI:
- Using your preferred JSON editor, create a subscriber definition file in the format:

```

```

where:
- `"displayName": "<subscriber-name>"`is the name of the new subscriber. For example,`"displayName": "Premium-subscriber"`. Avoid entering confidential information.
- `"clients": [{...}]`specifies one or more API clients that will be accessing API deployments using the usage plans to which the subscriber is subscribed. For each API client, specify:
- `"name": "<api-client-name>"`is a name of your choice for the API client. Client names must be unique within a subscriber. For example,`"name": "android"`. Recommendation: Specify a meaningful name because you might provide it to API consumers for the purpose of usage plan data collection and analysis. Avoid entering confidential information.
- `"token": "<unique-identifier>"`is a character string of your choice to uniquely identify the API client. The token you specify must be unique within your tenancy for the current region, and must not be more than 128 characters. For example,`"token": "abc123def456ghi789jkl"`.
Note  
  
The token you specify for an API client in a subscriber definition is intended for usage plan reporting purposes only. Do not use this token for API client authentication and authorization. Instead, use authorizer functions or JSON Web Tokens (JWTs) for API client authentication and authorization. See[Adding Authentication and Authorization to API Deployments](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayaddingauthzauthn.htm).
- `"usagePlans": [{…}]`specifies the OCID of one or more usage plans to which to subscribe the subscriber. The usage plan can belong to the same compartment as the subscriber, but does not have to. For example,`"usagePlans": "ocid1.usageplan.oc1..aaaaaaaaab______gap"`.
- `"compartmentId": "<compartment-ocid>"`is the OCID of the compartment to which the new subscriber belongs. For example,`"ocid1.compartment.oc1..aaaaaaaa7______ysq"`

For example:

```

```

- Save the subscriber definition file with a name of your choice. For example,`premium-subscriber.json`
- Use the subscriber definition file to create a subscriber using the CLI:
- Configure your client environment to use the CLI ([Configuring Your Client Environment to use the CLI for API Gateway Development](https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewayconfiguringclientocicli.htm)).
- 

Open a command prompt and run`oci api-gateway subscriber create`to create the subscriber from the subscriber definition file:

```

```

where:
- `--from-json file://<subscriber-definition>.json`is the file containing the subscriber definition, including a path.

For example:

```

```

The response to the command includes:
- The subscriber's OCID, and other details.
- The lifecycle state (for example, ACTIVE, FAILED).
- The id of the work request to create the subscriber (details of work requests are available for seven days after completion, cancellation, or failure).

If you want the command to wait to return control until the subscriber is active (or the request has failed), include either or both the following parameters:
- `--wait-for-state ACTIVE`
- `--wait-for-state FAILED`

For example:

```

```

Note that you cannot use the subscriber until the work request has successfully created it and the subscriber is active.
- 

(Optional) To see the status of the subscriber, enter:

```

```

- 

(Optional) To see the status of the work request that is creating the subscriber, enter:

```

```

- 

(Optional) To view the logs of the work request that is creating the subscriber, enter:

```

```

- 

(Optional) If the work request that is creating the subscriber fails and you want to review the error logs, enter:

```

```

For more information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see[CLI Help](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).

## Using the API

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[CreateSubscriber](https://docs.oracle.com/iaas/api/#/en/api-gateway/latest/Subscriber/CreateSubscriber)
