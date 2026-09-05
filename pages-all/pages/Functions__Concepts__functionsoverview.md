# Overview of Functions
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsoverview.htm
- Fetched: 2026-09-05 02:07 CDT

# Overview of Functions

Learn how the Functions service lets you create, run, and scale business logic without managing any infrastructure .

[Oracle Cloud Infrastructure Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../home.htm)is a fully managed, multi-tenant, highly scalable, on-demand, Functions-as-a-Service platform. It is built on enterprise-grade Oracle Cloud Infrastructure and powered by the Fn Project open source engine. Use OCI Functions (sometimes abbreviated to just Functions, and formerly known as Oracle Functions) when you want to focus on writing code to meet business needs.

The serverless and elastic architecture of OCI Functions means there's no infrastructure administration or software administration for you to perform. You don't provision or maintain compute instances, and operating system software patches and upgrades are applied automatically. OCI Functions simply ensures your app is highly-available, scalable, secure, and monitored. With OCI Functions, you can write code in Java, Python, Node, Go, Ruby, and C# (and for advanced use cases, bring your own Dockerfile, and Graal VM). You can then deploy your code, call it directly or trigger it in response to events, and get billed only for the resources consumed during the execution.

OCI Functions is based on Fn Project. Fn Project is an open source, container native, serverless platform that can be run anywhere - any cloud or on-premises. Fn Project is easy to use, extensible, and performant. You can download and install the open source distribution of Fn Project, develop and test a function locally, and then use the same tooling to deploy that function to OCI Functions.

You can access OCI Functions using the Console, a CLI, and a REST API. You can invoke the functions you deploy to OCI Functions using the CLI or by making signed HTTP requests.

OCI Functions is integrated with Oracle Cloud Infrastructure Identity and Access Management (IAM), which provides easy authentication with native Oracle Cloud Infrastructure identity functionality. See[Overview of Identity and Access Management](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm).

To get set up and running quickly with OCI Functions, see the[Functions QuickStart Guides](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionsquickstartguidestop.htm). A number of related[Developer Tutorials](https://docs.oracle.com/iaas/Content/developer/home.htm#home__functions)are available, as well as other[Samples, Playbooks, Architectures, Tutorials, and Blog Posts](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionsdownloadingsamples.htm).
Important  
  
Advance Notice of Mandatory Requirement to Upgrade the Fn Project CLI, April 2021

If you have installed the Fn Project CLI and are using it to initialize, build, and deploy functions, you will have to upgrade the Fn Project CLI on or before 1st May, 2021. For more information see[Upgrading the Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionsupgradingfncli.htm).

## Ways to Access Oracle Cloud Infrastructure

You can access Oracle Cloud Infrastructure (OCI) by using the[Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm)(a browser-based interface),[REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or[OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To access the[Console](https://cloud.oracle.com/), you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select Infrastructure Console . You are prompted to enter your cloud tenant, your user name, and your password.

For general information about using the REST API, see[REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm).

## Creating Automation with Events

You can create automation based on state changes for Oracle Cloud Infrastructure resources by using event types, rules, and actions. For more information, see[Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).

The following OCI Functions resources emit events:
- applications
- functions

You can also have events in other services invoke functions in OCI Functions. See[Invoking OCI Functions from Other Oracle Cloud Infrastructure Services](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionsintegratingwithother.htm).

## Resource Identifiers

Most types of Oracle Cloud Infrastructure resources have a unique, Oracle-assigned identifier called an Oracle Cloud ID (OCID). For information about the OCID format and other ways to identify your resources, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.

## OCI Functions Capabilities and Limits

The number of functions and applications you can create in a region is controlled by OCI Functions service limits (see[Function Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#Functions_Limits)). The default service limits vary according to your payment method. If you need more capacity, you can submit a request to increase the default service limits (see[Creating a Limit Increase Request](https://docs.oracle.com/iaas/Content/General/service-limits/create-request.htm)).

The maximum amount of data you can send to a function (the function's request payload) is 6MB. The maximum amount of data a function can return in response to a request (the function's response payload) is 6MB. These limits are fixed and cannot be changed.

Some other OCI Functions capabilities and limits are also fixed. However, there are also a number that you can change. See[Changing Default Memory and Timeout Settings](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionscustomizing.htm).

## Required IAM Service Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

For more information about policies for OCI Functions, see:
- [Creating Policies to Control Access to Network and Function-Related Resources](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionscreatingpolicies.htm)
- [Details for Functions](https://docs.oracle.com/iaas/Content/Identity/Reference/functionspolicyreference.htm)
