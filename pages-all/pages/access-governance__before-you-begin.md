# Before You Begin
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/before-you-begin.htm
- Fetched: 2026-09-05 03:13 CDT

# Before You Begin

This article provides details of suggested preparatory steps you can complete before starting with Oracle Access Governance.

## Oracle Cloud Infrastructure Services

When you order Oracle Access Governance through Universal Credits, you automatically get access to Oracle Cloud Infrastructure and other required services.

Here’s some information about how Oracle Access Governance uses other services and what you need to do if you’re setting up Oracle Access Governance for the first time.

Oracle Cloud Infrastructure Services used by Oracle Access Governance
Service What is it for? Do I need to do anything?
Oracle Cloud Infrastructure Identity and Access Management

Compartments : You use compartments to organize resources on Oracle Cloud Infrastructure.

Policies : You use IAM security policies to grant permissions.

Domains : You use identity domains to manage users and groups in your organization who will be required to use Oracle Access Governance and Oracle Cloud Infrastructure Console.

Yes

Before you create your first Oracle Access Governance instance, Oracle recommends that you set up one or more compartments in which you can deploy and secure your cloud resources.

- [Setting Up Your Tenancy](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm)
- [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm)

Optionally, you can set up security policies that give other users permission to set up and manage Oracle Access Governanceinstances.

See[Set Up Users](https://docs.oracle.com/en-us/iaas/Content/access-governance/set-up-users.htm)for further details.
Oracle Identity Cloud Service

If identity domains aren't available in your cloud account, you use Oracle Identity Cloud Service to manage the users and groups in your organization who will use Oracle Access Governance.

In most cases, Oracle Access Governance is automatically federated with the primary Oracle Identity Cloud Service instance associated with your tenancy.

Yes

You can add users and groups before you create the Oracle Access Governance instance or after; you can decide.

See[Set Up Users](https://docs.oracle.com/en-us/iaas/Content/access-governance/set-up-users.htm)for further details.

If you want to federate with a secondary Oracle Identity Cloud Service instance or your tenancy is a government region where federation isn't set up automatically, you must federate with Oracle Identity Cloud Service manually.

## Typical Workflow for Administrators

This topic outlines a typical workflow for Oracle Access Governance administrators.

If you’re setting up Oracle Access Governance for the first time, follow these tasks as a guide.

Task Description More Information

Place an order for Oracle Access Governance or sign up for a free Oracle Cloud promotion

Sign up for a free credit promotion or subscribe to Oracle Access Governance through Universal Credits.

See[Oracle Global Infrastructure Regions](https://www.oracle.com/cloud/cloud-regions/data-regions/)

[Request and Manage Free Oracle Cloud Promotions](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm)

[Upgrade Your Free Oracle Cloud Promotion](https://docs.oracle.com/iaas/Content/GSG/Tasks/buysubscription_topic-Upgrade_Your_Free_Promotion.htm)

Activate your Oracle Cloud account and sign in for the first time

You receive a welcome email when your account is ready. To activate your account, you must sign in with the credentials provided in the email.

As the Cloud Account Administrator, you can complete all the setup tasks for Oracle Access Governance.

[Manage Service Instance](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-service-instance.htm)

Determine your service requirements

Plan your Oracle Access Governance deployment. Think about what you need before you start.

Service Requirements

- Users
- Region

(Optional) Enable other users to set up services

If you don’t want to set up Oracle Access Governance yourself, give other users permissions to create services.

[Set Up Users](https://docs.oracle.com/en-us/iaas/Content/access-governance/set-up-users.htm)

(Recommended) Create a compartment for your service

Create a compartment for your Oracle Access Governance deployment.

When you sign up for Oracle Cloud Infrastructure, Oracle creates your tenancy with a root compartment that holds all your cloud resources. You then create additional compartments within the tenancy (root compartment) and corresponding policies to control access to the resources in each compartment. Before you create an Oracle Access Governance instance, Oracle recommends that you set up the compartment where you want the instance to belong. You create compartments in Oracle Cloud Infrastructure Identity and Access Management. See[Setting Up Your Tenancy](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm)and[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).

Create a service instance

Deploy a new service with Oracle Access Governance.

[Create Service Instance](https://docs.oracle.com/en-us/iaas/Content/access-governance/set-up-service-instance.htm#create-service-instance)

Verify your service instance

When your service is ready, check that you can sign in and your service is up and running.

[Verify Service Instance](https://docs.oracle.com/en-us/iaas/Content/access-governance/set-up-service-instance.htm#verify-service-instance)

Set up users and groups

Set up users and groups for Oracle Access Governance and assign them to application roles.

[Set Up Users](https://docs.oracle.com/en-us/iaas/Content/access-governance/set-up-users.htm)
Integrate with Authoritative Sources Configure integration with external systems from which you eish to onboard identities.
See:
- [Identity Orchestration Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-overview.htm)
- [Integrate with Orchestrated Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-orchestrated-systems.htm)

Activate Identities for License Management

Define which identities can use your Oracle Access Governance service.

[Activate Identities for License Management](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)
Integrate with Managed Systems Configure integration with external systems which you want to perform access reviews and campaigns against
See:
- [Identity Orchestration Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-overview.htm)
- [Integrate with Orchestrated Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-orchestrated-systems.htm)

Administer services

Monitor services and perform administrative tasks such as edit and delete.

Delegate administrative responsibilities to others through security policies.

See[Manage Service Instance](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-service-instance.htm)and[Set Up Users](https://docs.oracle.com/en-us/iaas/Content/access-governance/set-up-users.htm)
