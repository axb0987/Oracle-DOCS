# Overview of the Health Checks Service
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Concepts/healthchecks.htm
- Fetched: 2026-09-05 02:13 CDT

# Overview of the Health Checks Service

The Oracle Cloud Infrastructure Health Checks service provides users with high frequency external monitoring to determine the availability and performance of any publicly facing service, including hosted websites, API endpoints, or externally facing load balancers. By using Health Checks, users can ensure that they're immediately aware of any availability issue affecting their customers.

## Key Components

Review key components used in creating a health check. monitors Monitors allow you to continuously monitor the health of public-facing endpoints. You can configure monitors to use either HTTP and ping protocols. Monitors are classified as either Basic or Premium , based on the configured test interval. A monitor is considered Premium if the test interval is set to 10 seconds, and considered Basic if the test interval is greater than 10 seconds. Behavioral differences do not exist between a Basic and Premium monitor, other than the frequency that the monitor is run. on-demand probes On-demand probes allow you to run a one-time probe to assess the health of a public-facing endpoint. You can configure on-demand probes to use either or both HTTP and ping protocols. This feature is only available through the[REST API](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/). A limit exists on how many on-demand probes can be run in a 24-hour period. On-demand credits are consumed as the probes are run, and replenished gradually over time. vantage points Vantage points are geographic locations from which monitors and probes can be run to your specified target. Oracle Cloud Infrastructure maintains dozens of vantage points around the world. When creating a health check, we recommend selecting three or more vantage points across three different providers. protocols The Health Checks service allows you to configure both HTTP and ping type monitors. Each type has respective protocols.

## Ways to Access

Access Health Checks using the Console, SDK, CLI, or API.

You can access Oracle Cloud Infrastructure (OCI) by using the[Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm)(a browser-based interface),[REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or[OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To access the[Console](https://cloud.oracle.com/), you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select Infrastructure Console . You are prompted to enter your cloud tenant, your user name, and your password.

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.
- For details about writing policies for access to health checks, see[IAM Policies (Securing Health Checks)](https://docs.oracle.com/iaas/Content/Security/Reference/healthchecks_security.htm#iam-policies).
- For details about writing policies for other services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm)(for tenancies that haven't been updated to use identity domains) or[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference.htm)(for tenancies that have been updated to use identity domains).

## Service Capabilities and Limits

The Oracle Cloud Infrastructure Health Checks service is limited to 1000 endpoint tests per account.

For a list of applicable limits and[instructions for requesting a limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti), see[Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). To set compartment-specific limits on a resource or resource family, administrators can use[compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).

## Moving Health Checks to a Different Compartment

When you move a health check to a new compartment, its associated monitor and test results moves with it. After the move, health checks are accessible through the SDK, CLI, and Console.

For instructions, see the following pages:
- [Moving an HTTP Monitor to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Concepts/../Tasks/change-compartment-http-monitor.htm#top)
- [Moving a Ping Monitor to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Concepts/../Tasks/change-compartment-ping-monitor.htm#top)

For general information about moving resources, see[Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).

## Security

For information about how to secure Health Checks, including security information and recommendations, see[Securing Health Checks](https://docs.oracle.com/iaas/Content/Security/Reference/healthchecks_security.htm)
