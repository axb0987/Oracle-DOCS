# Manage Administrative Console Settings
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/admin-settings.htm
- Fetched: 2026-09-05 03:13 CDT

# Manage Administrative Console Settings

As an`AG_Administrator`, you can customize Console settings from the Settings page.

## CSV Data Export Settings

As an`AG_Administrator`, you can allow non-administrator users to export data to CSV files.

By default, non-administrator users aren't allowed to export identity, account and enterprise-wide data to CSV files.

Overview: CSV Data Export Settings

When CSV download is OFF, you can't export CSV from:
- Enterprise-wide Browser
- Identity Details page: Accounts and Permissions
- Resources
- Access Profile Side Reference Panels: Policies, Identities, Identity Collections, Roles, Workflows, and Delegations
- Manage Identities
- Unmatched Accounts

When CSV export is ON, the following roles can export CSVs:
- Service Desk Administrator`AG_ServiceDesk_Admin`
- Enterprise-wide Access Administrator`AG_Enterprise_Wide_Access_Admin`
- Auditor`AG_Auditor`

### Enable CSV Data Export Settings for Non-Administrator Users

To enable users to export identity, account and enterprise-wide data to CSV.
To enable the users to export identity, account and enterprise-wide data to CSV:

- Sign in to the Oracle Access Governance Console with the appropriate application role.
See[Predefined Application Roles Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm).
- From the icon, select Service Administration , and then Settings . The Settings page opens to customize settings.
- On the CSV data export tab, select Edit .
- Turn on the option to enable non-administrator users to export identity, account and enterprise-wide data to CSV.
- Select Save .
On the CSV data export tab, the value is displayed as On.

## Configure Password Policy

As an`AG_Administrator`, you can specify rules for password complexity and rotation intervals.
Specify rules for password complexity, such as minimum and maximum length and required character types, and set mandatory password rotation intervals. Oracle Access Governance users can request or set passwords that are valid for up to 7 days. After this period, the current password would be replaced with system generated password. Users must request and use a new password to regain access after expiration. See[Reset Password for Managed System Accounts](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm#change-account-password).

- Sign in to the Oracle Access Governance Console with the appropriate application role.
See[Predefined Application Roles Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm).
- From the icon, select Service Administration , and then Settings . The Settings page opens to customize settings.
- On the Password policy tab, select Edit .
- Configure the fields according to the organization policies.
- Select Save .

## Global Account Terminations Settings

As an`AG_Administrator`, you can configure global account termination settings for all orchestrated systems.

As an`AG_Administrator`, configure global account termination settings for all orchestrated systems. You can also define override rules based on identity attribute values to exclude specific users from account termination.
Note  
  
When global account termination settings are enabled, application administrators`AG_AppOwner_Admin`can't manage account termination settings at the orchestrated system level.

### Enable Global Account Termination Settings

To enable global account termination settings for all orchestrated systems.

- Sign in to the Oracle Access Governance Console with the appropriate application role.
See[Predefined Application Roles Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm).
- From the icon, select Service Administration , and then Settings . The Settings page opens to customize settings.
- Select Account Terminations .
- Select Edit .
- Enable the Do you want administrators to manage the termination settings? option to configure account termination settings.

### Configure Termination Settings

Select actions to perform with accounts during early termination and on termination date.

- Select what to do with accounts when early termination begins. This happens when you need to revoke identity accesses before official termination date. Select from the following options:
- Delete : Deletes all accounts and permissions managed by Oracle Access Governance.
Note  
  
If specific orchestrated system doesn't support the action, then no action is taken.
- Disable : Disables all accounts and disables permissions managed by Oracle Access Governance. You can also select Delete the permissions for disabled accounts to ensure zero residual access.
- No action : No action is taken when an identity is flagged for early termination by Oracle Access Governance.
- Select what to do with accounts on the termination date. This happens when you need to revoke identity accesses on the official termination date. Select from the following options:
- Delete : Deletes all accounts and permissions managed by Oracle Access Governance.
Note  
  
If specific orchestrated system doesn't support the action, then no action is taken.
- Disable : Disables all accounts and disables permissions managed by Oracle Access Governance. You can also select Delete the permissions for disabled accounts to ensure zero residual access.
- No action : No action is taken when an identity is flagged for early termination by Oracle Access Governance.

### Setting Override Rules for Account Termination

Overrides enable you to exclude specific orchestrated systems from global account termination settings.
Overrides enable you to exclude specific orchestrated systems from global account termination settings. Use overrides to control how accounts are deprovisioned when termination starts and when termination ends. Use override rules when certain users with specific identity attributes, such as job types or locations, must be excluded. For example, users in particular locations or roles can retain their accounts or permissions (with No Action) on specific systems, even when global identity termination rules are triggered.

Each override includes:
- Orchestrated systems : One or more systems the override applies to.
- Identity attribute values : One or more values. If omitted, the override applies to all values.
- Termination-start configuration : How to handle accounts when termination starts.
- Termination-end configuration : How to handle accounts when termination ends. When termination starts or ends for an identity, the system evaluates overrides to decide account de-provisioning. If an override exists that matches both the identity attribute value and the orchestrated system, the system uses that override's configuration.

- On the Account terminations page, go to the Overrides section.
- In the Override attribute list, select an identity attribute to use to apply override rules.
- Select + Add override .
- In the Name field, enter override name.
- Select one or more orchestrated systems that you want to exclude.
- (Optional) In the list, select Identity attribute values to apply override rules for specific values.
- Select the action to perform when an early termination begins. This happens when you need to revoke identity accesses before official termination date.
- Select the action to perform during official termination. This happens when you need to revoke identity accesses on the official termination date.

### Rules for Duplicate Overrides

- If a new override would create a scope that already exists (same attribute value + same system), it's rejected.
- You can add new specific rules in addition to wild card rules (that allows all values for an identity attribute)
```

```

- If you create a single override involving several orchestrated systems, Oracle Access Governance divides the rule into separate entries based on`{OS + Identity Attribute value}`. If any one of these entries already exists, the entire override rule is rejected, and none of the changes are saved.

## Session Idle Timeout

Configure automatic sign out after a period of inactivity. Set the session idle timeout between 5 and 60 minutes.

As an Oracle Access Governance administrator, enter value within the supported range [5,60] or disable the idle timeout. However, it's not recommended to disable the idle timeout because of the security risk. After configuration Oracle Access Governance users would see a warning one minute before the configured session timeout. If the user doesn't respond within the one minute, the session ends automatically.
- Applies to: New and existing users
- Minimum timeout: 5 minutes
- Default timeout: 60 minutes of inactivity (when not selected)

- Sign in to the Oracle Access Governance Console with an appropriate application role.
See[Predefined Application Roles Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm).
- From the icon, select Service Administration , and then Settings . The Settings page opens to customize settings.
- Select Session idle timeout .
- Select Edit .
- Select an idle timeout value from the list.
- Select Save .

## Enable Sequential Access Request Processing

As an`AG_Administrator`, you can optionally enforce sequential processing of multiple access requests for a single identity, whether as an access bundle, role, or both.

Note  
  
If this setting is enabled while access requests are pending, all new requests are queued. After every pending request has been completed, provisioned, or has exceeded the maximum provisioning time, the next queued request is released for processing.

To enable or disable the sequential processing of multiple access requests for a single identity:

- Sign in to the Oracle Access Governance Console with the appropriate application role.
See[Predefined Application Roles Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm).
- From the icon, select Service Administration , and then Settings . The Settings page opens to customize settings.
- Select Access requests . The page summarizes whether sequential processing is enabled, and, if so, what the current settings are.
- To change the current settings, select Edit .
- Select whether to apply or remove sequential processing to access bundles, roles, or both.
- Select the number of days to wait after request approval for provisioning to complete before starting the next request.

This helps ensure that access requests can continue to be processed when the provisioning for a system takes a long time or fails.
- Select Save .
