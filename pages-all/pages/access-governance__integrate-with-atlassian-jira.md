# Integrate with Atlassian JIRA
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-atlassian-jira.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with Atlassian JIRA

## Overview: Integrate Oracle Access Governance with Atlassian Jira

Integration between Oracle Access Governance and Atlassian Jira streamlines user lifecycle management of Atlassian Jira users, ensuring seamless access control and compliance through automated provisioning and enforcement of the principle of least privilege through reviews of users and groups.

Atlassian Jira can be integrated with Oracle Access Governance as a managed system, allowing you to reconcile users, and groups, and provision identities and accounts.

## Atlassian Jira Integration Architecture Overview

You can perform full data load for accounts in Atlassian Jira. Once a connection is established using Atlassian Jira REST APIs, you can perform remediation and management tasks for user accounts and groups.

Atlassian Jira integration supports management of Atlassian Jira accounts by Oracle Access Governance, including the following use cases.
- Centralized User Provisioning :

Perform Atlassian Jira user identity updates. create, modify, and deactivate accounts from within Oracle Access Governance.
- Access Control :

Assign or revoke Atlassian Jira group memberships using governance policies defined in Oracle Access Governance. Automatically or manually revoke access for users whose access is no longer valid, based on organizational or lifecycle changes.
- Segregation of Duties :

Enforce segregation of duties (SoD) by implementing metadata-driven rules to define eligibility criteria for granting access bundle permissions, using Oracle Access Governance Access Guardrails
- Self-Service Profile Management :

Enable users to view and update their own profile attributes using Oracle Access Governance, with updates reflected in Atlassian Jira.
- Access Reviews and Attestation :

Periodically review and certify Atlassian Jira user access to ensure appropriate entitlements.
- Audit and Compliance Support :

Maintain full audit logs of all user and access-related changes to meet regulatory and internal compliance requirements.

## Functional Overview: Use Cases Supported for Atlassian Jira Integration

Atlassian Jira integration supports management of Atlassian Jira accounts by Oracle Access Governance, including the following use cases.

- 

Configure Atlassian Jira Orchestrated System

See[Configure Integration Bertween Oracle Access Governance and Atlassian JIRA](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-atlassian-jira.htm).
- 

[Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/atlassian-jira-integration-reference.htm#jira-matchingrule).
- 

[Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts and groups that can be managed by Oracle Access Governance.
- 

[Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from your orchestrated system or request an access for an identity. This allows you to provision entitlements.
- 

Update Account

Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions.This allows you to update entitlements.
- 

[Delete Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#delete-account-managed-by-oracle-access-governance)
