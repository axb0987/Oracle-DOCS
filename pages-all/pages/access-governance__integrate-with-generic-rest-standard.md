# Integrate with Generic REST (Standard UI-driven)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-generic-rest-standard.htm
- Fetched: 2026-09-05 03:14 CDT

# Integrate with Generic REST (Standard UI-driven)

The Generic REST Orchestrated System provides a way to integrate Oracle Access Governance with REST-based target applications without custom code. You can configure the REST endpoints, request details, response mapping, permissions, and data transformations through the Oracle Access Governance Console.

## Generic REST Orchestrated System Overview

Use Generic REST when you don't have a direct end-to-end connector but have REST APIs for identities (users/accounts) and entitlements (permissions/groups). It ensures onboarding and lifecycle management as the schema, request, response, and test templates are configured directly in Oracle Access Governance and validated at the onboarding time.

Generic REST (Standard UI-driven) Orchestrated System supports the capabilities:
- Onboard any REST-based identity-aware application
- Full data load for Managed Systems
- Manage accounts, and entitlements (permissions)
- Configure request/response templates and authentication in the Console
- Validate schemas and APIs during onboarding
- Support provisioning and reconciliation operations
- Import initial data using flat files when APIs aren't available

## Generic REST Integration Functional Flow

The UI-driven Generic REST uses the following setup sequence.
- Configure Orchestrated System using the Oracle Access Governance Console
- Create the Generic REST (Standard UI-driven) orchestrated system
- Configure credentials manually or store them using the OCI vault secret.
- You can either use flat file for the full data load or configure listing APIs.
- At this stage, no permissions, lookups, or account schema are defined, and the connection isn't Active.

See[Configure Integration with Generic REST (Standard UI-driven)](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#configure-integration-with-grest-standard).
- Define Permissions

Define permissions to represent entitlements or accesses in the target system. The default attributes are`uid`and`name`. Based on the orchestrated system configuration, you can load data either from flat file or use REST APIs. These permissions can be used in an access bundle to enable provisioning and reconciliation operations. See[Create Permissions for the Generic REST System](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#define-permissions).
- Define Lookups

Define lookups to manage reference data, such as countries or languages. Based on the orchestrated system configuration, lookup data can be loaded using flat files or REST APIs.

You can also upload a static file for lookup values instead of configuring REST APIs. In this case, dynamic lookup reconciliation isn't supported. See[Manage Lookups](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#lookups).
- Define Account Attributes

Define the account schema for the system. You can create account attributes manually, or import an account schema file. See[Define Account Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#account-attrs-import-schema)
- Configure authentication and connectivity APIs

Define REST APIs required to establish connectivity with the target system.
- Configure a Bearer Token API when Bearer authentication is selected. This ensures Authentication is configured correctly. For Basic authentication, no token API is required. See[Configure Authentication - For Bearer Token](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#configure-rest-api).
- Configure a Test Connection API to validate connectivity. This ensures that the target REST endpoint is reachable.
- Define REST APIs for entities required for account lifecycle

Configure APIs for operations, such as create account, update account, delete account, change password, enable or disable account, get account details and list accounts. For each API, you configure Endpoint URL, Headers and parameters, request body and response. See[Configure REST APIs for Entities](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#rest-api-settings).
- Activate orchestrated system.
- Configure outbound transformation to map identity attributes to account attributes for provisioning operations. See[Apply Outbound Transformations for Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#apply-outbound-transformations-for-identity-attributes).

### Load Permissions
While configuring permissions, you can select how to bring permission data into the system:
- Flat File : Upload CSV from Object Storage for data load. This is available only when Flat File option is selected during configuration. Upload CSV files in the Permission folder of the bucket.
- REST API : Configure listing or search APIs in the REST APIs section to enable ongoing synchronization.

See[Create Permissions for the Generic REST System](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-generic-rest-standard.htm#define-permissions)

## Use Cases Supported by the Generic REST Orchestrated System

Use Generic REST (Standard UI-driven) to onboard REST-based applications and manage accounts and entitlements without building or maintaining custom connectors.

A logistics company uses several cloud applications that expose REST APIs for managing users, accounts, groups, and access. There is no centralized governance as identity data is manually entered and access is managed using custom scripts or spreadsheets.

Use Generic REST (Standard UI-driven) to onboard all applications using a single, standardized integration model.
- Access Control
The Generic REST Orchestrated System manages access control through identity collections, roles, access bundles, and Oracle Access Governance policies. Depending on the orchestrated system being used, you can manage access using Oracle Access Governance self service features, specifically[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm). For example, you can use the Generic REST Orchestrated System:
- Create New Accounts
- Reconcile Accounts
- Update Accounts
- Disable/Enable Accounts
- Delete Accounts
- Add or Remove Permissions
-
