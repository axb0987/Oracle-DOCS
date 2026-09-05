# Integrate with Oracle Warehouse Management Cloud (WMS)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-wms-cloud.htm
- Fetched: 2026-09-05 03:15 CDT

# Integrate with Oracle Warehouse Management Cloud (WMS)

Integrate Oracle Warehouse Management Cloud (WMS)with Oracle Access Governance as a Managed system to reconcile and manage accounts.

## Overview

With Oracle Warehouse Management Cloud (WMS) orchestrated system, you can orchestrate identities, on-board identity data, and provision accounts, assign permissions (groups, companies, facilities, and reset password).

### Oracle Warehouse Management Cloud (WMS) Integration Architecture Overview

You can perform full data load for accounts in Oracle Warehouse Management Cloud (WMS). After a connection is established, you can perform remediation tasks for user accounts and groups.

### Functional Overview: Use Cases Supported for Oracle Warehouse Management Cloud (WMS) Integration

Oracle Warehouse Management Cloud (WMS) integration supports management of Oracle Warehouse Management Cloud (WMS) accounts from Oracle Access Governance, including the following use cases.
- Configure Oracle Warehouse Management Cloud (WMS) Orchestrated System. See[Configure Integration with Oracle Warehouse Management Cloud (WMS)](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-with-wms.htm#configure-integration-wms).
- [Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/wms-integration-reference.htm#default-matching-rules).
- [Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts and roles that can be managed by Oracle Access Governance.
- [Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from the orchestrated system or request an access for an identity. This allows you to provision entitlements (Create Account) and account details.
- Update Account

Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions. With this, you can update entitlements (Add Group, Delete Group, Update Group).
- [Enable or disable account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#retry-provisioning-for-failed-or-pending-accesses)
