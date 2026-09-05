# Accessing Streaming
- Source: https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/accessing-streaming.htm
- Fetched: 2026-09-05 03:05 CDT

# Accessing Streaming

Review ways to access Streaming and required authentication and authorization.

You can access Streaming using any of the following options, based on your preference and use case, provided you are[authenticated and authorized](https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/accessing-streaming.htm#authentication)to do so.

## Ways to Access Streaming

You can access the service the following ways:
- Oracle Cloud Console: An easy-to-use, browser-based interface.

Open the navigation menu and select Analytics &amp; AI . Under Messaging , select Streaming .

You can use the Console to create and manage streams, stream pools, and Kafka Connect configurations, but you can't publish or consume messages using the Console.

To access the Console, you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of the page and select Infrastructure Console . You're prompted to enter your cloud tenant, your username, and your password.
- Oracle Cloud Infrastructure REST APIs: Provide the most functionality, but require programming expertise.[API Reference and Endpoints](https://docs.oracle.com/iaas/api/)provides endpoint details and links to the available API reference documents. For general information about using the API, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm). The Streaming service is accessible with the[Streaming API](https://docs.oracle.com/iaas/api/#/en/streaming/).
Tip  
  
Because Streaming is compatible with Apache Kafka API, applications written for Kafka can also access Streaming.
- Oracle Cloud Infrastructure SDKs: You can interact with Streaming without having to create a framework. Basic Streaming usage examples are included with our SDKs. For more information about using the SDKs, see the[SDK Guides](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
- Command line interface (CLI): Provides both quick access and full functionality without the need for programming. For more information, see[Using the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Using_the_CLI)
- 

[Resource Manager : An Oracle Cloud Infrastructure (OCI) service that lets you automate the process of provisioning your OCI resources. Using Terraform, Resource Manager helps you install, configure, and manage resources through the "infrastructure-as-code" model. You can use Resource Manager to create streams, stream pools, and Kafka Connect configurations.

## Authentication and Authorization

Regardless of the method you use to access Streaming, you must be authorized to interact with the service's resources.

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

For common policies used to authorize Streaming users, see[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For administrators: The policy in[Let streaming admins manage streaming resources](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#streaming-manage-streams)lets the specified group do everything with Streaming and related Streaming service resources.

For in-depth information on granting users permissions for the Streaming service, see[Details for the Streaming Service](https://docs.oracle.com/iaas/Content/Identity/Reference/streamingpolicyreference.htm)
