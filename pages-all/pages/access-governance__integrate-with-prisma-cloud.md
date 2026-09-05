# Integrate with Palo Alto Networks Prisma Cloud
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-prisma-cloud.htm
- Fetched: 2026-09-05 03:15 CDT

# Integrate with Palo Alto Networks Prisma Cloud

You can integrate Palo Alto Networks Prisma Cloud with Oracle Access Governance as a Managed system, allowing you to reconcile and provision accounts and manage groups.

## Overview: Integrate Oracle Access Governance with Palo Alto Networks Prisma Cloud

Oracle Access Governance can be integrated with Prisma Cloud, enabling identity orchestration, including on-boarding of identity (user) data, and provisioning of accounts.

Prisma Cloud can be integrated with Oracle Access Governance to ensure synchronized lifecycle management of accounts within your enterprise.

### Prisma Cloud Integration Architecture Overview

You can perform full data load for accounts in Prisma Cloud. Once a connection is established, you can perform remediation tasks for user accounts and groups.

### Functional Overview: Use Cases Supported for Prisma Cloud Integration

Prisma Cloud integration supports management of Prisma Cloud accounts from Oracle Access Governance, including the following use cases.
- Configure Prisma Cloud Orchestrated System. See[Configure Integration Between Oracle Access Governance and Prisma Cloud](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-prisma-cloud.htm).
- [Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/peoplesoft-integration-reference.htm#peoplesoft-default-matching-rules).
- [Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts and roles that can be managed by Oracle Access Governance.
- [Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from the orchestrated system or request an access for an identity. You can then provision entitlements (Create Account) and account details.
- Update Account

Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions. With this, you can update entitlements (Add Group, Delete Group, Update Group).
- [Enable or disable account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#retry-provisioning-for-failed-or-pending-accesses)
