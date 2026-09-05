# Revoke Access for an Early Termination
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/revoke-access-early-termination.htm
- Fetched: 2026-09-05 03:16 CDT

# Revoke Access for an Early Termination

Early Termination refers to removal of accounts or permissions before the official termination date. Useful for notice periods, garden leave, and so on.

## Revoke Access for an Early Termination

Oracle Access Governance supports:
- Early Termination : End date is in the future.
- Final Termination : End date is now; User is disabled.

Worker State AG Status Status (from Authoritative Source) Join Date (from Authoritative Source) Termination Started Termination Date (from Authoritative Source)
Early termination AG Active Active Less than or equal to today TRUE Greater than today
Final termination AG Active Disabled Less than or equal to today TRUE or FALSE Less than or equal to today

## Prerequisites

Ensure the following prerequisites to grant early termination access from Oracle Access Governance:

Early Termination happens when the global identity attribute`terminationStarted`flag is set to True and final termination when user's status is transitioned from Active to Disabled .

### Step 1: Create System Attribute and Global Identity Attribute for terminationStarted

This flag indicates whether termination has started for the user or not. Leaver flows can be triggered on termination started based on configuration.

- Create a simple system attribute`terminationStarted`and map it to the last working day status value source, such as`terminationStarted`flag. See[Create System Attribute](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#system-attribute).
- Now, go to the Identity Attributes page and search`terminationStarted`core identity attribute.
- Edit the core identity attribute to select the relevant orchestrated system and update the Value source . If`terminationStarted`is directly available, then choose Use the {terminationStarted} value directly , else derive it's value using the single attribute rule.

For detailed steps, see[Manage Attributes Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#manageattributes-settings).

### Step 2: Create Termination Date System Attribute For Final Termination

This attribute value is ingested directly from the Authoritative source and indirectly triggers the final termination flows. When the current date reaches the`terminationDate`, the status of the identity is set as Disabled .

- Create a simple system attribute of Date type,`terminationDate`and map it to the last working date source, such as`lastWorkingDate`flag. See[Create System Attribute](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#system-attribute).

This step isn't required for early termination flows but is necessary for final termination.
- Go to the Identity Attributes page.
- Edit the core identity attribute`terminationDate`to select the relevant orchestrated system and select Use the{terminationDate} value directly in the Value source field.
- Select appropriate identity flags to include this attribute in the Oracle Access Governance features.

## Automated Access Revocation Workflow

Oracle Access Governance supports automatic removal of accounts or permissions triggering the leaver workflow before the official termination date.

Termination can be configured globally or at the orchestrated system level. If global configuration is enabled, account lifecycle management at the orchestrated system level is disabled. Also, you can set up override rules for specific orchestrated systems to exclude certain users, such as those in specific job types or locations, from termination.

To set up global account termination, see[Account Terminations](https://docs.oracle.com/en-us/iaas/Content/access-governance/admin-settings.htm#global-account-termination-settings)
