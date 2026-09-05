# License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Concepts/licensemanageroverview.htm
- Fetched: 2026-09-05 02:10 CDT

# License Manager

Learn about License Manager, a free, opt-in service that allows you to bring your own licenses (BYOL) into Oracle Cloud Infrastructure.

Licenses are defined in terms of their requirements and entitlements, according to the metric the license is created for. License Manager helps you better understand your licensing needs, and eases making business decisions based on your licensing needs. After you have created your licenses, your licensing requirements are calculated every hour.

Use License Manager to perform the following tasks:
- Automate the license portability rules for Oracle Database products to OCI Database PaaS services. This eliminates overhead for Software Asset Managers (SAMs) and developers in an enterprise. Developers can create BYOL Oracle Database resources, such as Autonomous AI Database, without needing to worry about creating visibility into their infrastructure for their SAM. A resource can be BYOL , which means Oracles charges you for infrastructure, but not licensing fees for software running on it. A resource can also be license included , which means the cost includes infrastructure and the software licensing fee.
- Track license usage for Oracle Database products or third-party products by Compute resources. As a result, you have a single observation and license usage tracking location of all Oracle and third-party licenses in OCI.
- Obtain reporting of BYOL resources that have licensing needs. Monitor and manage a list of email addresses to be notified about the expiration or over-subscription of licenses.
Note  
  
License Manager is supported for Alloy realms.

You can perform the following product license tasks:

[View a summary of product license activity](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Concepts/../Tasks/overview-license-manager.htm).

[List the product licenses in your tenancy](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Concepts/../Tasks/list-product-license.htm).

[Create a product license](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Concepts/../Tasks/create-product-license.htm).

[Get the details of a product license](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Concepts/../Tasks/get-product-license.htm).

[Update the settings of a product license](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Concepts/../Tasks/update-product-license.htm).

[Remove a product license from License Manager](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Concepts/../Tasks/delete-product-license.htm).

[View a list the resources that are attributed to a license and their individual licensing requirements](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Concepts/../Tasks/list-product-license-consumers.htm).

[View a list of the of the most used OCI resources in a compartment](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Concepts/../Tasks/list-top-utilized-resources.htm).

[Import product licenses you set up using an Excel template into License Manager.](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Concepts/../Tasks/import-product-license.htm)

[Manage the license records for a product license](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Concepts/license-records.htm).

[Manage the list of email addresses that can be notified about expirations or subscription overages](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Concepts/../Tasks/notifications.htm).

## Supported Products

License Manager supports the following Oracle products and options:
- Oracle Database Enterprise Edition
- Oracle Database Standard Edition
- Oracle Database Standard Edition One
- Oracle Database Standard Edition 2
- Real Application Clusters
- Multitenant
- Active Data Guard

## Required IAM Policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm)and[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).

To use License Manager, the following policy statements are required:
```

```

## Authentication and Authorization

Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).

An administrator in an organization needs to set up groups , compartments , and policies that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see[Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).
