# Overview of Audit
- Source: https://docs.oracle.com/en-us/iaas/Content/Audit/Concepts/auditoverview.htm
- Fetched: 2026-09-05 01:39 CDT

# Overview of Audit

Describes the Oracle Cloud Infrastructure Audit service, which automatically records calls to all supported Oracle Cloud Infrastructure public application programming interface (API) endpoints as log events.

Currently, all services support logging by Audit. Object Storage service supports logging for bucket-related events, but not for object-related events. Log events recorded by the Audit service include API calls made by the Oracle Cloud Infrastructure Console, Command Line Interface (CLI), Software Development Kits (SDK), your own custom clients, or other Oracle Cloud Infrastructure services. Information in the logs includes the following:
- Time the API activity occurred
- Source of the activity
- Target of the activity
- Type of action
- Type of response

Each log event includes a header ID, target resources, timestamp of the recorded event, request parameters, and response parameters. You can view events logged by the Audit service by using the Console, API, or the SDK for Java. Data from events can be used to perform diagnostics, track resource usage, monitor compliance, and collect security-related events.

## Version 2 Audit Log Schema

On October 8, 2019, Oracle introduced the Audit version 2 schema, which provides the following benefits:
- Captures state changes of resources
- Better tracking of long running APIs
- Provides troubleshooting information in logs

The new schema is being implemented over time. Oracle continues to provide Audit logs in the version 1 format, but you cannot access version 1 format logs from the Console. The Console displays only the version 2 format logs. However, not all resources are emitting logs using the version 2 schema. For those services that are not emitting in the version 2 format, Oracle converts version 1 logs to version 2 logs, leaving fields blank if information for the version 2 schema cannot be determined.

## Ways to Access Oracle Cloud Infrastructure

You can access Oracle Cloud Infrastructure (OCI) by using the[Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm)(a browser-based interface),[REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or[OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

For general information about using the API, see[REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm).

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

Administrators: For an example of policy that gives groups access to audit logs, see[Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Audit/Concepts/../Tasks/viewinglogevents.htm#policy). To modify the Audit log retention period, you must be a member of the Administrators group. See[The Administrators Group and Policy](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm#The)
