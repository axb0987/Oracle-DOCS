# Oracle Access Governance Licensing Information
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-licensing-plan.htm
- Fetched: 2026-09-05 03:15 CDT

# Oracle Access Governance Licensing Information

Oracle Access Governance offers three types of licensing models covering various service offerings based on identity type and identity segments. Let's explore various licensing types and other requirements to use Oracle Access Governance.

This Licensing Information document is a part of the product or program documentation under the terms of your Oracle services or license agreement and is intended to help you understand the program editions, entitlements, restrictions, prerequisites, special license rights, and/or separately licensed third party technology terms associated with the Oracle services or software program(s) covered by this document (the "Program(s)"). If you have a question about your rights and obligations, please contact your Oracle sales representative and/or contact the applicable Oracle License Management Services representative listed on[http://www.oracle.com/us/corporate/license-management-services/index.html](http://www.oracle.com/us/corporate/license-management-services/index.html).

## Licensing Models, Unit Metrics and SKUs

Licensing and pricing for Oracle Access Governance broadly depends on your licensing model, identity segments (tiers), and identity types.

### Licensing Models in Oracle Access Governance
Oracle Access Governance offers three licensing models:
- Oracle Access Governance for Oracle Cloud Infrastructure : This contains integration support for Oracle Cloud Infrastructure (OCI) only.
- Oracle Access Governance for Oracle Workloads : This includes integration support for Oracle applications and services, including Oracle Cloud Infrastructure.
- Oracle Access Governance Premium : This includes integration support for all the available applications and services, including Oracle applications and services.

Workloads refer to collection of applications or services (Authoritative Source and Managed System) that can be integrated, governed and managed using Oracle Access Governance. Oracle Workloads refers to Oracle applications and services, such as Oracle Unified Directory, Oracle Siebel, Oracle Primavera, Oracle Identity Governance, Oracle Database User Management, and so on.

### Unit Metrics and Stock Keeping Units (SKUs)

You can manage access privileges and perform various governance operations by marking identities as Active in Oracle Access Governance. From licensing and pricing viewpoint, we only bill unique Active identities in Oracle Access Governance. Further, Active identities can be flagged either as Workforce or Consumer identities by the Oracle Access Governance administrator. The main difference is that a Consumer user cannot log on to Oracle Access Governance but you can manage permissions or provision these identities with a fixed set of privileges using Oracle Access Governance.

For example, in a financial institution, employees, such as accountants, tellers, managers, or administrative staff can be your Workforce user, whereas bank account owners, insurance policy holders, and others customers can be your Consumer identities. For more information, see[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm).
Based on these identity types, we have defined our unit metrics:
- Workforce user per month : A unique identity that is configured to access the service either through a user interface or through programmatic configuration during the billing period, regardless of whether the identity is actively accessing the service at any given time. Workforce user can be an individual, such as an employee or contractor, or a service identity, such as bots,applications, or services.
- Consumer user per month : A unique identity that is not configured to access the service through either a user interface or through a programmatic configuration during the billing period, but whose accesses are managed in the Oracle Access Governance Console by workforce identities. Consumer identities can be an individual, such as customers, alumni, outsourced partners, or devices.

So, the metric for Oracle Access Governance Stock Keeping Units (SKUs) is per month . For billing, only the Active identities on an hourly basis are considered and we will generate the bill for the entire month. If you don’t mark any identity as Active , you will not be billed for Oracle Access Governance.

### User Segments or Tiers within each SKU

Based on the type of licensing models and identity types, Oracle Access Governance extends discounts by offering multiple tiers based on number of workforce identities. See the tier details in the[Licensing Plan for Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-licensing-plan.htm#licensing-models-and-offerings)Licensing Plan for Oracle Access Governance.

## Licensing Models and Offerings

Here's a detailed plan on licensing models and offerings for Oracle Access Governance.

Licensing Plan for Oracle Access Governance
Licensing Models Identity Types Tiers
Oracle Access Governance for Oracle Cloud Infrastructure Workforce Identity
- First 100,000 workforce identities
- More than 100,000 workforce identities
Oracle Access Governance for Oracle Workloads Workforce Identity
- First 10,000 workforce identities
- More than 10,000 workforce identities and up to 30,000 workforce identities
- More than 30,000 workforce identities
Oracle Access Governance for Oracle Workloads Consumer Identity No Tiers
Oracle Access Governance Premium Workforce Identity
- First 10,000 workforce identities
- More than 10,000 and up to 30,000 workforce identities
- More than 30,000 workforce identities
Oracle Access Governance Premium Consumer Identity No Tiers

## Choosing the Right Licensing Model

Let's consider a few scenario examples that will help you select the right licensing model based on your requirement.

Oracle Access Governance Licensing for Users beyond Oracle Applications
Let's say you want to manage governance for a total 1000 identities, breakdown as follows:
- Employee data of 800 identities available in Oracle Identity Governance (OIG)
- Contractors data of 200 identities available in Microsoft Entra ID

In such a case to manage governance of employees and contractors data, you need all applications and services, so you need subscription to Oracle Access Governance Premium . You will get integration support for OCI IAM, Oracle workloads and all other available applications and services. You will be billed for identities marked as Active in Oracle Access Governance.

Oracle Access Governance Licensing to Manage Domain Identities in Oracle Cloud Infrastructure
