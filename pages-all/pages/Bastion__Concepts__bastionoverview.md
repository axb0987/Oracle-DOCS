# Bastion Overview
- Source: https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/bastionoverview.htm
- Fetched: 2026-09-05 01:42 CDT

# Bastion Overview

Oracle Cloud Infrastructure Bastion provides restricted and time-limited access to target resources that don't have public endpoints.

Bastions let authorized users connect from specific IP addresses to target resources using Secure Shell (SSH) sessions. When connected, users can interact with the target resource by using any software or protocol supported by SSH. For example, you can use the Remote Desktop Protocol (RDP) to connect to a Windows host, or use Oracle Net Services to connect to a database.

Targets can include resources like compute instances , DB systems , and Autonomous AI Transaction Processing databases.

Bastions are essential in tenancies with stricter resource controls. For example, you can use a bastion to access Compute instances in compartments that are associated with a security zone . Instances in a security zone cannot have public endpoints.

Integration with Oracle Cloud Infrastructure Identity and Access Management (IAM) lets you control who can access a bastion or a session and what they can do with those resources.
Tip  
  
Watch a[video introduction](https://apexapps.oracle.com/pls/apex/f?p=44785:265:0:::265:P265_CONTENT_ID:31770)to the service.

## Bastion Concepts
  
  

The following concepts are key to understanding the Bastion service. BASTION Bastions are logical entities that provide secured, public access to target resources in the cloud that you cannot otherwise reach from the internet. Bastions reside in a public subnet and establish the network infrastructure needed to connect a user to a target resource in a private subnet . Integration with the IAM service provides user authentication and authorization. Bastions provide an extra layer of security through the configuration of CIDR block allowlists. Client CIDR block allowlists specify what IP addresses or IP address ranges can connect to a session hosted by the bastion. To learn more about private subnets, see[Connectivity Choices](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm#connectivity). SESSION Bastion sessions let authorized users in possession of the private key in an SSH key pair connect to a target resource for a predetermined amount of time. You provide the public key in the SSH key pair at the time you create the session, and then supply the private key when you connect. In addition to presenting the private key, an authorized user must also attempt the SSH connection to the target resource from an IP address within the range allowed by the bastion's client CIDR block allowlist. To learn more, see[Session Types](https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/bastionoverview.htm#session_types). TARGET RESOURCE A target resource is an entity that resides in your organization's VCN (virtual cloud network) , which you can connect to by using a session hosted on a bastion. TARGET HOST A target host is a specific type of target resource that provides access to a Linux or Windows operating system using SSH (port 22 by default). Compute instances and Virtual Machine DB systems are examples of target hosts.
Note  
  

A bastion is associated with a single VCN. You can't create a bastion in one VCN and then use it to access target resources in a different VCN.

## Session Types

The Bastion service recognizes three types of sessions. The type of session you create, or choose to connect to, depends on the type of target resource. MANAGED SSH SESSION

Allows SSH access to a compute instance that meets all of the following requirements:
- The instance must be running a[Linux platform image](https://docs.oracle.com/iaas/Content/Compute/References/images.htm)(Windows is not supported).
- The instance must be running an OpenSSH server.
- The instance must be running the Oracle Cloud Agent.
- 

The Bastion[plugin](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#console)must be enabled on the Oracle Cloud Agent.

The agent is enabled by default on compute instances that were created from certain Compute images (especially those images provided by Oracle). In other cases, you need to enable the agent on the instance before creating a session. The Bastion plugin is not enabled by default and must be enabled before creating a session. SSH PORT FORWARDING SESSION

Doesn't require an OpenSSH server or the Oracle Cloud Agent to be running on the target resource.

Port forwarding (also known as SSH tunneling) creates a secure connection between a specific port on the client machine and a specific port on the target resource. Using this connection you can relay other protocols. You can tunnel most TCP services and protocols over SSH, including the following ones:
- Remote Desktop Protocol (RDP)
- Oracle Net Services
- MySQL

For example, you can use an SSH port forwarding session to connect Oracle SQL Developer to the private endpoint of an Autonomous AI Transaction Processing database.

Because the connection is encrypted using SSH, port forwarding can also be useful for transmitting information that uses an unencrypted protocol such as Virtual Network Computing (VNC). DYNAMIC PORT FORWARDING (SOCKS5) SESSION

A dynamic port forwarding (SOCKS5) session has the same benefits of an SSH port forwarding session, but allows you to dynamically connect to any target resource in a private subnet. Unlike other session types that you configure to connect to a specific target resource (IP address or DNS name), with a dynamic port forwarding (SOCKS5) session you create a tunnel to a target subnet and the client decides which resource and port to connect to.

## Regions and Availability Domains

Bastion is available in all Oracle Cloud Infrastructure commercial regions. See[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About)for the list of available regions for Oracle Cloud Infrastructure, along with associated locations, region identifiers, region keys, and availability domains.

## Resource Identifiers

The Bastion service supports bastions and sessions as Oracle Cloud Infrastructure resources. Most types of resources have a unique, Oracle-assigned identifier called an Oracle Cloud ID (OCID). For information about the OCID format and other ways to identify your resources, see[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Resource_Identifiers).

## Ways to Access Bastion

You can access Bastion using the Console (a browser-based interface), the command line interface (CLI), or the REST API. Instructions for the Console, CLI, and API are included in topics throughout this guide.

To access the Console, you must use a[supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and click Infrastructure Console . You are prompted to enter your cloud tenant, your user name, and your password.

For a list of available SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm). For general information about using the APIs, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm).

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in your organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, launch instances, create buckets, download objects, etc. For more information, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm).
- For details about writing Bastion policies, see[Bastion IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/../Reference/bastionpolicyreference.htm).
- For details about writing policies for other services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that your company owns, contact your administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you should be using.

## Security

In addition to creating IAM policies, there are other security best practices for Bastion.

For example:
- Maximize SSH security
- Integrate target instances with IAM and enable multi-factor authentication
- Perform a security audit of Bastion operations

See[Securing Bastion](https://docs.oracle.com/iaas/Content/Security/Reference/bastion_security.htm).

## Monitoring

Bastions are Oracle-managed services. You use a bastion to create Secure Shell (SSH) sessions that provide access to other private resources. But you can't connect directly to a bastion with SSH and administer or monitor it like a traditional host.

To monitor activity on your bastions, the Bastion service integrates with these other services in Oracle Cloud Infrastructure.
- The Audit service automatically records calls to all public Bastion API endpoints as log entries. See[Overview of Audit](https://docs.oracle.com/iaas/Content/Audit/Concepts/auditoverview.htm).
- The Monitoring service enables you to monitor your Bastion resources using metrics and alarms. See[Bastion Metrics](https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/../Reference/metrics.htm).
- The Events service allows your development teams to automatically respond when a Bastion resource changes its state. See[Bastion Events](https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/../Reference/events.htm).

## Limits

Bastions have service limits, but do not incur costs.

See[Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm)for a list of applicable limits and instructions for requesting a limit increase.

For instructions to view your usage level against the tenancy's resource limits, see[Viewing a Tenancy's Limits and Usage](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits-view-tenancy.htm).

## Getting Started

After completing some prerequisite steps, create a bastion and session.

Before creating a bastion, you must have access to a target resource without a public endpoint, such as a Compute instance or database that's on a private subnet.

- [Create the required IAM policy](https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/../Tasks/managingbastions.htm#managingbastions_topic-Required_IAM_Policy).

If you're not an administrator, you must be given access to the Bastion service in a policy (IAM) written by an administrator.
- [Choose a session type](https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/bastionoverview.htm#session_types).

Before creating a managed SSH session, verify the following information:
- The bastion plugin is enabled on the target Compute instance . For details, see[Managing Plugins with Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#console).
- The VCN (virtual cloud network) includes a gateway ( service gateway , internet gateway , or NAT gateway ) and a route rule for the gateway.

For details, see[Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm),[Internet Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm), or[NAT Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm).
- [Create a bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/../Tasks/create-bastion.htm).
- [Verify that the target resource allows incoming traffic from the bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/../Tasks/connectingtosessions.htm#allowing-network-access).
- [Create a session for the target resource](https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/../Tasks/create-session.htm).
- [Connect to the session](https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/../Tasks/connectingtosessions.htm).

The specific steps depend on the session type and target resource type.

If you run into any problems, see[Troubleshooting Bastion](https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/../Tasks/troubleshooting.htm)
