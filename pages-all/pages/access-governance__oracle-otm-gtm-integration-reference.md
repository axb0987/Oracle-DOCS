# Oracle Transport and Global Trade Management (OTM/GTM) Integration Reference
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-otm-gtm-integration-reference.htm
- Fetched: 2026-09-05 03:16 CDT

# Oracle Transport and Global Trade Management (OTM/GTM) Integration Reference

Lists certified components, supported operations, configuration modes, default out-of-the-box attributes for the integration between Oracle Transport and Global Trade Management (OTM/GTM) and Oracle Access Governance.

## Oracle Transport and Global Trade Management (OTM/GTM) Components Certified for Integration with Oracle Access Governance

The Oracle Transport and Global Trade Management (OTM/GTM) components that you can integrate with are listed below.

Certified Components
Component Type Component
System Oracle Transport and Global Trade Management (OTM/GTM)
APIs REST APIs with OAUTH 2.0 Authorization

## Supported Configuration Modes for Oracle Transport and Global Trade Management (OTM/GTM) Integrations

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

Oracle Transport and Global Trade Management (OTM/GTM) Orchestrated System supports the following mode:
- Managed System

You can manage Oracle Transport and Global Trade Management (OTM/GTM) accounts, roles and business intelligence roles and business intelligence applications.

## Supported Operations When Provisioning To Oracle Transport and Global Trade Management (OTM/GTM)

When you provision an account from Oracle Access Governance to Oracle Transport and Global Trade Management (OTM/GTM) certain operations are supported.

The Oracle Transport and Global Trade Management (OTM/GTM) Orchestrated System supports the following account operations when provisioning a user:

- Create Account
- Update Account
- Enable Account
- Disable Account
- Delete Account
- Add Roles
- Remove Roles
- Add Business Intelligence Roles
- Remove Business Intelligence Roles
- Add Business Intelligence Application
- Remove Business Intelligence Application

For more details see[Oracle Access Governance Integration Functional Overview](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm)and[Integrate Oracle Access Governance with Oracle Transport and Global Trade Management (OTM/GTM)](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-otm-integrate-with-otm-gtm.htm).

## Default Supported Attributes

Oracle Access Governance supports the following default Oracle Transport and Global Trade Management (OTM/GTM) attributes.

Account Attribute Mapping
Entity Oracle Transport and Global Trade Management (OTM/GTM) Account Attribute Oracle Access Governance Account Attribute Oracle Access Governance Display name
User __UID__(GL_USER_GID) uid Unique Id
__NAME__ name User login
GL_USER_XID userName User name
__ENABLE__ status Status
__PASSWORD__(PASSWORD) password Password
USERNAME nickName Nick name
IS_EXTERNAL isExternal External user
UNSUCCESSFUL_LOGIN_ATTEMPTS unsuccessfulLoginAttempts Unsuccessful login attempts
LAST_LOGIN_DATE lastLoginDate Last login date
LAST_NAME lastName Last name
FIRST_NAME firstName First name
EMAIL_ADDRESS email Email
IS_OBIEE obieeNonSSOUser OBIEE non sso user
EFFECTIVE_DATE startDate Start date
EXPIRATION_DATE endDate End date
DOMAIN_NAME domainName Domain name
GL_ACCOUNT_POLICY_GID accountPolicy Account policy
AUTO_APPROVE_RULE_PROFILE_GID approveRuleProfile Approval rule profile
DOCUMENT_USE_PROFILE_GID documentUseProfile Document use profile
PW_EXPIRATION_DATE passwordExpirationDate Password expiration date
ACCOUNT_LOCKOUT_TIME accountLockoutTime Account lockout time
Business Intelligence Role BI_ROLE_GID businessIntelligenceRoleId Business intelligence role id
Business Intelligence Application GL_USER_BI_APP businessIntelligenceApplication Business intelligence application
Role DEFAULT_USER_ROLE_GID roles Roles

## Default Matching Rules

To map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the Oracle Transport and Global Trade Management (OTM/GTM) orchestrated system is as follows:

Default Matching Rules
Mode Default Matching Rule
Managed System

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User name = Employee user name`

## Supported Special Characters

For successful provisioning and data load, adhere to the list of special characters for the default attributes

Special Characters for UserName (GL_USER_XID)

- Supported Special Characters:`(@ . {} [] () : * ! ^ ~ ` | \ )`
- Unsupported Special Characters:`( - $ # ; & ? / , < > )`

Special Characters for Other Default Attributes

Unsupported Special Characters:`(& <)`

For additional details, refer[Basic Data Entry in OTM/GTM](https://docs.oracle.com/en/cloud/saas/transportation/25c/otmol/general/basic_data_entry.htm).

## Limitations

The following limitations exist by design while working with orchestrated system.
- You cannot assign Administration roles using the`USER-ADMINISTRATION`role from Oracle Access Governance. To do so, assign`DBA.ADMIN`.
- If you assign`DBA.ADMIN`
