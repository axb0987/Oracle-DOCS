# Integrate Oracle Access Governance with Oracle Customer Experience (CX) Sales
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-oracle-cx.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate Oracle Access Governance with Oracle Customer Experience (CX) Sales

You can integrate Oracle Customer Experience (CX) Sales with Oracle Access Governance as a Managed system, to streamline account lifecycle management, reconcile and provision accounts, and assign and revoke permissions.

Oracle CX (Sales) is part of the Oracle Fusion Cloud Applications Customer Experience (CX) suite. This integration manages sales resource directory entities, including resource users, organizations, resource roles, and organization role assignments.

## Oracle CX (Sales) Integration Architecture Overview

You can perform full data load of accounts from Oracle CX (Sales). After a connection is established, you can perform remediation and management tasks for user accounts and privileges.

During data ingestion, account and attribute information is imported into Oracle Access Governance. You can then govern access through provisioning, remediation, access reviews, and compliance workflows. Accounts managed in Oracle Access Governance are provisioned back to Oracle CX (Sales).

Oracle CX (Sales) integration supports management of Oracle CX (Sales) accounts by Oracle Access Governance, including the following use cases.
- Centralized User Provisioning :

Perform Oracle CX (Sales) account updates. View, create, update, and delete accounts within Oracle Access Governance. See[Data Browser: View Accounts and Granted Permissions for Managed Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-overview.htm)
- Access Control :

Assign or revoke Oracle CX (Sales) resource roles, organizations, organization roles managed in Oracle Access Governance Automatically or manually revoke access for users whose access is no longer valid, based on organizational or lifecycle changes. See[Access Controls in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-controls.htm).
- Segregation of Duties :

Enforce segregation of duties (SoD) by implementing metadata-driven rules to define eligibility criteria for granting[Access Bundles](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-bundles.htm)permissions, using Oracle Access Governance[Access Guardrails](https://docs.oracle.com/en-us/iaas/Content/access-governance/enforce-preventive-access-control-conditions.htm#enforce-preventive-access-control-conditions).
- Self-Service Profile Management :

Users can view their own profiles and application owners can manage account attributes from the Oracle Access Governance Console, with updates provisioned into Oracle CX (Sales). See[Self Service in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/self-service.htm).
- Access Reviews and Attestation :

Periodically review and certify Oracle CX (Sales) user access to ensure appropriate entitlements. See[Access Reviews](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#access-reviews-overview).
- Audit and Compliance Support :

Review audit trail for all user and access-related changes to meet regulatory and internal compliance requirements. See[Audit Trail: Monitoring Access Review and Access Request Decisions](https://docs.oracle.com/en-us/iaas/Content/access-governance/understanding-reviewers-actions-for-effective-access-certification.htm#audit-trail-monitoring-access-decisions).

## Functional Overview: Use Cases Supported for Oracle CX (Sales) Integration

You can manage Oracle CX (Sales) accounts with the Oracle CX (Sales) orchestrated system, including the following use cases.

- Configure Oracle CX (Sales) Orchestrated System. See[Configure Integration with Oracle Customer Experience (CX) Sales](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-with-oracle-cx.htm).
- [Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to correlate the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-cx-integration-reference.htm#oracle-cx-matchingrule).
- [Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts (resource users), entitlements (resource roles), and account attributes (resource organizations and resource organization roles) that can be managed by Oracle Access Governance.
- [Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account from the orchestrated system or request access for an identity. Create and provision an Oracle CX (Sales) resource user for an identity. During provisioning, you can assign resource roles and specify required account attributes, such as resource organization and resource organization role.
- Update Account

Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions. You can edit Access Bundle to assign or revoke organization and organization role, change resource role permissions to trigger Update Account activity.
- [Delete Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#delete-account-managed-by-oracle-access-governance)
