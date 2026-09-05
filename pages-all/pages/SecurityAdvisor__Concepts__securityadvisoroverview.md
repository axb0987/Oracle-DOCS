# Overview of Security Advisor
- Source: https://docs.oracle.com/en-us/iaas/Content/SecurityAdvisor/Concepts/securityadvisoroverview.htm
- Fetched: 2026-09-05 03:05 CDT

# Overview of Security Advisor

Oracle Cloud Infrastructure Security Advisor supports and reinforces Oracle security best practices, including the configuration requirements for resources in Security Zones. It combines and streamlines existing workflows to efficiently create resources that meet baseline security requirements from the outset.

Specifically, you can assign a new customer-managed encryption key to a resource at the time that you create the resource, even if you have never created a vault or encryption key before. Security zones require encryption using customer-managed keys where possible. Because no one but an authorized user can access the keys, sensitive data can only be decrypted and read by those users explicitly allowed to do so.

Streamlined workflows reduce complexity and decision-making. Where you would otherwise need to choose between configuration options, Security Advisor provides only the more secure option. For example, Security Advisor only allows you to create master encryption keys that are 256 bits in length. Longer encryption keys provide greater security than shorter ones.
- [Creating a Secure Bucket](https://docs.oracle.com/en-us/iaas/Content/SecurityAdvisor/Concepts/../Tasks/creatingsecurebucket.htm#creatingsecurebucket)
- [Creating a Secure File System](https://docs.oracle.com/en-us/iaas/Content/SecurityAdvisor/Concepts/../Tasks/creatingsecurefilesystem.htm#creatingsecurefilesystem)
- [Creating a Secure Virtual Machine Instance](https://docs.oracle.com/en-us/iaas/Content/SecurityAdvisor/Concepts/../Tasks/creatingsecurevirtualmachine.htm#creatingsecurevirtualmachine)
- [Creating a Secure Block Volume](https://docs.oracle.com/en-us/iaas/Content/SecurityAdvisor/Concepts/../Tasks/creatingsecureblockvolume.htm#creatingsecureblockvolume)

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in your organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, launch instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).

If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that your company owns, contact your administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you should be using.

Security Advisor leverages the functionality of existing workflows, so the tenancy might not need new policies to grant permissions beyond what's already in place. To be sure, you can compare the tenancy's existing policies with the example permissions described in the chosen workflow. In particular, confirm that you have policies that grant access to Vault resources, especially if you haven't used the service previously.

The example policy statements make it possible for the specified groups to do anything allowed by Security Advisor. If, instead, you wanted to limit the creation of new vaults, you can write a policy that grants permission only to use vaults, rather than the level of access required to manage vaults. With permission to use vaults, a user can select an existing vault, but cannot create a new one. This does not change the options that Security Advisor presents, but it does affect whether all operations succeed when submitted.

## Regions and Availability Domains

You can use Security Advisor in all Oracle Cloud Infrastructure commercial regions. For a list of regions, along with associated locations, region identifiers, region keys, and availability domains, see[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About).

Each service that integrates with Security Advisor has a single regional endpoint for all API operations, with one exception. The Vault service has one regional endpoint for the provisioning service that handles create, update, and list operations for vaults. For create, update, and list operations for keys, service endpoints are distributed across multiple independent clusters.

## Limits on Resources

Security Advisor does not introduce resources and does not impose restrictions on your usage level of any resource. Security Advisor does, however, respect the limits instituted by other services.

For a list of applicable limits and[instructions for requesting a limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti), see[Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). To set compartment-specific limits on a resource or resource family, administrators can use[compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).

For instructions to view your usage level against the tenancy's resource limits, see[Viewing Your Service Limits, Quotas, and Usage](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Viewing)
