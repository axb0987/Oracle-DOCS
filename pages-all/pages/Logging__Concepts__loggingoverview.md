# Logging Overview
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/loggingoverview.htm
- Fetched: 2026-09-05 02:36 CDT

# Logging Overview

The Oracle Cloud Infrastructure Logging service is a highly scalable and fully managed single pane of glass for all the logs in your tenancy. Logging provides access to logs from Oracle Cloud Infrastructure resources. These logs include critical diagnostic information that describes how resources are performing and being accessed.
Tip  
  
Watch a[video introduction](https://www.youtube.com/watch?v=JrFAHLbajXg)to the service.

## How Logging Works

Use Logging to enable, manage, and search logs. The three kinds of logs are the following:
- [Audit logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/audit_logs.htm): Logs related to events emitted by the Oracle Cloud Infrastructure Audit service. These logs are available from the Logging Audit page, or are searchable on the Search page alongside the rest of your logs.
- [Service Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/service_logs.htm): Emitted by OCI native services, such as API Gateway, Events, Functions, Load Balancer, Object Storage, and VCN Flow Logs. Each of these[supported services](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/service_logs.htm#supported_services)has predefined logging categories that you can enable or disable on your respective resources.
- [Custom logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/custom_logs.htm): Logs that contain diagnostic information from custom applications, other cloud providers, or an on-premises environment. Custom logs can be ingested through the API, or by configuring the Unified Monitoring Agent. You can configure an OCI compute instance/resource to directly upload Custom Logs through the Unified Monitoring Agent. Custom logs are supported in both a virtual machine and bare metal scenario.

A log is a first-class Oracle Cloud Infrastructure resource that stores and captures log events collected in a given context. For example, if you enable Flow Logs on a subnet, it has its own dedicated log. Each log has an OCID and is stored in a log group. A log group is a collection of logs stored in a compartment. Logs and log groups are searchable, actionable, and transportable.

To get started, enable a log for a resource. Services provide log categories for the different types of logs available for resources. For example, the Object Storage service supports the following log categories for storage buckets: read and write access events. Read access events capture download events, while write access events capture write events. Each service can have different log categories for resources. The log categories for one service have no relationship to the log categories of another service. As a result, the Functions service uses different log categories than the Object Storage service.

When you enable a log, you must add it to a log group that you create. Log groups are logical containers for logs. Use log groups to organize and streamline management of logs by applying IAM policy or grouping logs for analysis. For more information, see[Logs and Log Groups](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/managinglogs.htm).

Logs are indexed in the system, and searchable through the Console, API, and CLI. You can view and search logs on the Logging Search page. When searching logs, you can correlate across many logs simultaneously. For example, you can view results from multiple logs, multiple log groups, or even an entire compartment with one query. You can filter, aggregate, and visualize your logs. For more information, see[Logging Search](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/searchinglogs.htm).
Note  
  
Only UTF-8 text encoding is supported.

After you enable a log, log entries begin to appear on the detail page for the log (see[Enabling Logging for a Resource](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/enabling_logging.htm)for more information).
Note  
  
You can view usage report detail for Logging by accessing[Cost and Usage Reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/costusagereportsoverview.htm).

### Connector Hub Integration

Oracle Cloud Infrastructure Logging integrates with[Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm). If you need more archiving support, you can use Connector Hub for archiving to object storage, writing to stream, and so on. For more information, see[Connectors](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/connectors.htm)and[Scenario: Archiving Logs to Object Storage](https://docs.oracle.com/iaas/Content/connector-hub/archivelogs.htm).

### Logging Workshop

See the[OCI Logging Workshop](https://swigmaster.github.io/index.html?lab=introduction)for step-by-step, lab-based instructions on setting up your environment, enabling service logs, creating custom application logs, searching logs, and exporting log content to Object Storage.

### Logging APIs

Oracle Cloud Infrastructure Logging has the following APIs available:
- [Logging Management API](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/)
- [Logging Ingestion API](https://docs.oracle.com/iaas/api/#/en/logging-dataplane/latest/)
- [Logging Search API](https://docs.oracle.com/iaas/api/#/en/logging-search/latest/)

All Oracle Cloud Infrastructure Logging APIs support both IPv4 and IPv6 connections. While IPV4 is supported by default, you need to enable IPv6 support.
Here's how you can enable IPv6 support:
- API: Use the dual-stack API endpoint format: https://logging. {region} .ds.oci. {secondLevelDomain}
- For logging ingestion, use this dual-stack API endpoint format: https://ingestion.logging. {region} .ds.oci. {secondLevelDomain}

For example,`https://ingestion.logging.us-sanjose-1.ds.oci.oraclecloud.com`
- SDK: Set the`OCI_DUAL_STACK_ENDPOINT_ENABLE`environment variable to`true`.
- CLI: Pass the`-\-enable-dual-stack`option.

Also see the API topics in[Log Management](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/log-management.htm),[Using the (Logging Ingestion) API for custom logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/using_the_api_customlogs.htm), and[Using the (Logging Search) API](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/using_the_api_searchlogs.htm)for more information on logging operations specific to each API.

## Logging Concepts

The following concepts are essential to working with Logging. Service Logs Critical diagnostic information from supported Oracle Cloud Infrastructure services. See[Supported Services](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/service_logs.htm#supported_services). Custom Logs Diagnostic information from custom applications, other cloud providers, or an on-premise environment. To ingest custom logs, call the API directly or configure the unified monitoring agent. Audit Logs Read-only logs from the Audit service, provided for you to analyze and search. Audit logs capture the information about API calls made to public endpoints throughout your tenancy. These include API calls made by the Console, Command Line Interface (CLI), Software Development Kits (SDK), your own custom clients, or other Oracle Cloud Infrastructure services. Log Groups Log groups are logical containers for logs. Use log groups to streamline log management, including applying IAM policy or searching sets of logs. You can move log groups from one compartment to another and all the logs contained in the log group moves with it. Service Log Category Services provide log categories for the different types of logs available for resources. For example, the Object Storage service supports the following log categories for storage buckets: read and write access events. Read access events capture download events, while write access events capture write events. Each service can have different log categories for resources. The log categories for one service have no relationship to the log categories of another service. Connector Hub

[Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm)moves logging data to other services in Oracle Cloud Infrastructure. For example, use Connector Hub to[alarm on log data](https://docs.oracle.com/iaas/Content/connector-hub/alarmlogs.htm),[send log data to databases](https://docs.oracle.com/iaas/Content/connector-hub/dblogs.htm), and[archive log data to Object Storage](https://docs.oracle.com/iaas/Content/connector-hub/archivelogs.htm). For more information, see[Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm). Unified Monitoring Agent The fluentd-based agent that runs on customer machines (OCI instances), to help customers ingest custom logs. Agent Configuration A configuration of the Unified Monitoring Agent that specifies how custom logs are ingested.

## Log Encryption

OCI logs are encrypted according to the following:
- Logs are encrypted in-flight, that is, while they are in the process of being ingested into Oracle Cloud Infrastructure Logging;
- After the logs are in the system, they are encrypted with disk-level encryption for commercial environments; and
- Logs are also encrypted when they are archived, and while in storage.

## Resource Identifiers

Most types of Oracle Cloud Infrastructure resources have a unique, Oracle-assigned identifier called an Oracle Cloud ID (OCID). For information about the OCID format and other ways to identify your resources, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

## Ways to Access Oracle Cloud Infrastructure

You can access Oracle Cloud Infrastructure (OCI) by using the[Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm)(a browser-based interface),[REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or[OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To access the[Console](https://cloud.oracle.com/), you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select Infrastructure Console . You are prompted to enter your cloud tenant, your user name, and your password.

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

For administrators: Use the following topics to find examples of IAM policy for Logging:
- [Required Permissions for Working with Logs and Log Groups](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../Task/managinglogs.htm#required_permissions_logs_groups)
- [Required Permissions for Searching Logs](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/searchinglogs.htm#required_permissions_for_searching_logs)
