# API Gateway Concepts
- Source: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Concepts/apigatewayconcepts.htm
- Fetched: 2026-09-05 01:37 CDT

# API Gateway Concepts

Find out how about key concepts you need to understand when using API Gateway.

## API Gateways

In the API Gateway service, an API gateway is a virtual network appliance in a regional subnet.

An API gateway routes inbound traffic to back-end services including public, private, and partner HTTP APIs, as well as OCI Functions. Each API gateway is a private endpoint that you can optionally expose over a public IP address as a public API gateway:
- A private API gateway can only be accessed by resources in the same private network (VCN), or by resources in another private or on-premise network that is peered to that private network. A private API gateway has a private IP address, and an automatically generated hostname in the format`<gatewayidentifier>.apigateway.<region-identifier>.oci.customer-oci.com`. Note that although the host name is publicly resolvable from the internet, it resolves to the API gateway's private IP address. Traffic to the private IP address is not routable from the public internet; only clients within the VCN can access the API gateway. The public DNS resolvability of a private IP address is expected behavior, supporting various networking configurations within OCI environments.
- A public API gateway is publicly accessible and can be reached from the internet, provided an internet gateway is present in the API gateway's VCN. A public API gateway has both a private IP address and a public IP address, and an automatically generated hostname in the format`<gatewayidentifier>.apigateway.<region-identifier>.oci.customer-oci.com`. The generated hostname resolves from the internet to the public IP address, enabling internet-based clients to access the API gateway.

To ensure high availability, you can only create API gateways in regional subnets (not AD-specific subnets). You can create private API gateways in private or public subnets, but you can only create public API gateways in public subnets. The API Gateway service is regional in scope and fault-tolerant across availability domains (in multiple-AD regions), and fault domains (in single AD regions). In multiple-AD regions, the API Gateway service automatically selects an active availability domain to terminate the API gateway endpoint. Note that depending on the source and destination of the traffic, traffic might be routed across availability domains. If an availability domain or fault domain fails, the API Gateway service automatically handles failover and routes traffic to a functioning availability domain or fault domain.

An API gateway is bound to a specific VNIC.

You create an API gateway within a compartment in your tenancy. Each API gateway has a single front end, zero or more back ends, and has zero or more APIs deployed on it as API deployments.

## APIs

In the API Gateway service, an API is a set of back-end resources, and the methods (for example, GET, PUT) that can be performed on each back-end resource in response to requests sent by an API client.

To enable an API gateway to process API requests, you must deploy the API on the API gateway by creating an API deployment.

To deploy an API on an API gateway, you have the option to create an API resource in the API Gateway service. An API resource includes an API description that defines the API resource. Note that creating an API resource is optional. You can deploy an API on an API gateway without creating an API resource in the API Gateway service.

## API Deployments

In the API Gateway service, an API deployment is the means by which you deploy an API on an API gateway. Before the API gateway can handle requests to the API, you must create an API deployment.

When you create an API deployment, you set properties for the API deployment, including an API deployment specification. Every API deployment has an API deployment specification.

You can deploy multiple APIs on the same API gateway, so a single API gateway can host multiple API deployments.

## API Deployment Specifications

In the API Gateway service, an API deployment specification describes some aspects of an API deployment.

When you create the API deployment, you set properties for the API deployment, including an API deployment specification. Every API deployment has an API deployment specification. You can create an API deployment specification:
- by using dialogs in the Console
- by using your preferred JSON editor to create a JSON file
- by using an API description that you've uploaded from an API description file written in a supported language (for example, OpenAPI Specification version 3.0)

Each API deployment specification describes one or more back-end resources, the route to each back-end resource, and the methods (for example, GET, PUT) that can be performed on each resource. The API deployment specification describes how the API gateway integrates with the back end to execute those methods. The API deployment specification can also include request and response policies.

## API Resources and API Descriptions

In the API Gateway service, you have the option to create an API resource. An API resource is the design-time representation of an API. You can use an API resource to deploy an API on an API gateway.

An API description defines an API resource, including:
- available endpoints
- available operations on each endpoint
- parameters that can be input and output for each operation
- authentication methods

If you use an API resource to deploy an API on an API gateway, its API description pre-populates some of the properties of the API deployment specification.

You import the API description from a file (sometimes called an 'API specification', or 'API spec') written in a supported language. Currently, OpenAPI Specification version 2.0 (formerly Swagger Specification 2.0) and version 3.0 are supported.

You can also can generate an SDK from the API description file.

Note that creating an API resource in the API Gateway service is optional. You can deploy an API on an API gateway without creating an API resource in the API Gateway service. Note also that you can create an API resource that doesn't have an API description initially, and then add an API description later.

## Front ends

In the API Gateway service, a front end is the means by which requests flow into an API gateway. An API gateway can have either a public front end or a private front end:
- A public front end exposes the APIs deployed on an API gateway via a public IP address.
- A private front end exposes the APIs deployed on an API gateway to a VCN via a private endpoint.

## Back ends

In the API Gateway service, a back end is the means by which a gateway routes requests to the back-end services that implement APIs. If you add a private endpoint back end to an API gateway, you give the API gateway access to the VCN associated with that private endpoint.

You can also grant an API gateway access to other Oracle Cloud Infrastructure services as back ends. For example, you could grant an API gateway access to OCI Functions, so you can create and deploy an API that is backed by a serverless function.

## API Providers, API Consumers, API Clients, and End Users

An API provider is a person or team who designs, implements, delivers, and operates APIs. These users interact with interfaces such as the Oracle Cloud Infrastructure Console, SDK, CLI, and Terraform provider. They use the API Gateway service to deploy, monitor, and operate APIs. Some organizations segment the API provider role further, for example into:
- API developers, with responsibility for building APIs and deploying them on API gateways.
- API plan managers, with responsibility for monitoring and managing API usage (for example, by defining usage plans and subscribers).
- API Gateway managers, with responsibility for administering API gateways, typically in production.

An API consumer is a person or team who builds apps and services (API clients) and wants to leverage one or more APIs offered by an API provider. The API consumer is typically not sharing an Oracle Cloud Infrastructure tenancy with the API provider. The API consumer is a customer of the API provider.

An API client is an application or device created by an API consumer. The API client invokes the API at runtime by sending requests to the API gateway on which the API is deployed. API clients communicate with the API gateway over HTTPS (including HTTP/2). API clients typically authenticate with the API using OAuth, Basic Auth, mTLS and might use some other token such as an API key for metering and monetization.

An end user is a user of an API client, and is sometimes referred to as the "resource-owner" in terms of authorization. The end user only ever interacts with an API using the API client, and is typically unaware of the API itself. The end user is a customer of the API consumer.

## Usage Plans and Entitlements, Subscribers, and Client Tokens

In the API Gateway service, API plan managers can manage and monitor the usage of their APIs by defining usage plan resources and subscriber resources.

A usage plan resource comprises entitlements. Each entitlement specifies:
- A rate limit: The maximum number of API requests allowed per second.
- A quota: The total number of API calls allowed in a given time period (between a minute and a month).
- One or more target API deployments. The API deployments that subscribers to the usage plan are entitled to access.

You can specify an API deployment as a target in multiple entitlements in different usage plans, but not in multiple entitlements in the same usage plan. An entitlement can include API deployments from different API gateways.

As an API plan manager, usage plans enable you to control the API access available to your customers (API consumers) and their API clients. You can make API access subject to rate limits and quotas tailored to particular customer needs, enabling you to set up different access tiers for different customers.

A subscriber resource comprises:
- A single API consumer.
- Client names and client tokens to uniquely identify API clients created by the API consumer.
- Usage plans to which the API consumer and its API clients are subscribed.

As an API plan manager, you can create subscribers for your customers (API consumers) to specify the usage plans that give their API clients access to your APIs.

To make an API deployment eligible for inclusion in a usage plan, you specify the location of the client token passed in requests. Once the API deployment has been included in a usage plan, requests must include the client token in this location in order to access the API deployment. You specify the client token location in a usage plan request policy in the API deployment specification. (Note that the client tokens you define in subscriber resources are for usage plan reporting purposes only, and not for client authentication and authorization.)

## Routes

In the API Gateway service, a route is the mapping between a path, one or more methods, and a back-end service. Routes are defined in API deployment specifications.

## Policies

In the API Gateway service, there are different types of policy:
- a request policy describes actions to be performed on an incoming request from an API client before it is sent to a back end
- a response policy describes actions to be performed on a response returned from a back end before it is sent to an API client
- a logging policy describes how to store information about requests and responses going through an API gateway, and information about processing within an API gateway

You can use request policies and/or response policies to:
- limit the number of requests sent to back-end services
- enable CORS (Cross-Origin Resource Sharing) support
- provide authentication and authorization
- validate requests before sending them to back-end services
- modify incoming requests and outgoing responses
- make API deployments eligible for inclusion in usage plans that monitor and manage subscriber access

You can add policies to an API deployment specification that apply globally to all routes in the API deployment specification, as well as policies that apply only to particular routes.
