# Configure Integration Between Oracle Access Governance and Oracle Fusion Cloud Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-integration-between-oracle-access-governance-and-oracle-fusion-cl.htm
- Fetched: 2026-09-05 03:13 CDT

# Configure Integration Between Oracle Access Governance and Oracle Fusion Cloud Applications

You can establish a connection between Oracle Fusion Cloud Applications and Oracle Access Governance by entering connection details. To achieve this, use the orchestrated systems functionality available in the Oracle Access Governance Console.

## Prerequisites

Before you integrate and configure orchestrated system for Oracle Fusion Cloud Applications, complete the following prerequisites:
- [Prepare Oracle Fusion Cloud Applications for Integration](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#top)
- [Configure Risk Management Cloud (RMC) for Segregation of Duties (SoD) Check](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-rmc-segregation-of-duties.htm#top)
- [Migrate Oracle Fusion Cloud Applications Credentials to OCI Vault](https://docs.oracle.com/en-us/iaas/Content/access-governance/migrate-fusion-cloud-apps-credentials-to-oci-vault.htm#top)

## Navigate to the Orchestrated Systems Page

The Orchestrated Systems page of the Oracle Access Governance Console is where you start configuration of the orchestrated system.
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

## Select system

On the Select system step of the workflow, you can specify which type of system you would like to integrate with Oracle Access Governance.

You can search for the required system by name using the Search field.
- Select Oracle Fusion Cloud Applications .
- Select Next .

## Add Details

Add details such as name, description, and configuration mode.
On the Add Details step of the workflow, enter the details for the orchestrated system:
- Enter a name for the system you want to connect to in the Name field.
- Enter a description for the system in the Description field.
- Decide if this orchestrated system is an authoritative source, and if Oracle Access Governance can manage permissions by setting the following check boxes.
- This is the authoritative source for my identities

Select one of the following:
- Source of identities and their attributes : System acts as a source identities and associated attributes. New identities are created through this option.
- Source of identity attributes only : System ingests additional identity attributes details and apply to existing identities. This option doesn't ingest or creates new identity records.
- I want to manage permissions for this system The default value in each case is Unselected .
- Select Next .

Additionally:
If you're managing permissions with this then an additional checkbox is displayed for Segregation of Duties Checks:
- In Oracle Fusion Cloud Applications ensure that a user account is created and linked to the worker's person record. A successfully linked account displays the associated person information in the Security Console under the Users page. See[Configure Risk Management Cloud (RMC) for Segregation of Duties (SoD) Check](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-rmc-segregation-of-duties.htm).
- Select Enable Risk Management and Compliance (RMC) integration for separation of duties check .

## Add Owners

Add primary and additional owners to your orchestrated system to allow them to manage resources.
You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

## Account settings

Outline details of how to manage account settings when setting up your orchestrated system including notification settings, and default actions when an identity moves or leaves your organization.
On the Account settings step of the workflow, enter how you want Oracle Access Governance to manage accounts when the system is configured as a managed system:
- When a permission is requested and the account doesn't already exist, select this option to create new accounts . This option is selected by default. When selected, Oracle Access Governance creates an account if one doesn't exist when a permission is requested. If you clear this option, permissions are provisioned only for existing accounts in the orchestrated system. If no account exists, the provisioning operation fails.
- Select the recipients for notification emails when an account is created. The default recipient is User . If no recipients are selected, notifications aren't sent when accounts are created.
- User
- User manager
- Configure Existing Accounts
Note  
  
You can only set these configurations if allowed by the system administrator. When global account termination settings are enabled, application administrators can't manage account termination settings at the orchestrated-system level.
- Select what to do with accounts when early termination begins : Choose the action to perform when an early termination begins. This happens when you need to revoke identity accesses before official termination date.
- Delete : Deletes all accounts and permissions managed by Oracle Access Governance.
Note  
  
If specific orchestrated system doesn't support the action, no action is taken.
- Disable : Disables all accounts and disables permissions managed by Oracle Access Governance.
- Delete the permissions for disabled accounts : To ensure zero residual access, select this to delete directly assigned permissions and policy-granted permissions during account disablement.
- No action : No action is taken when an identity is flagged for early termination by Oracle Access Governance.
- Select what to do with accounts on the termination date : Select the action to perform during official termination. This happens when you need to revoke identity accesses on the official termination date.
- Delete : Deletes all accounts and permissions managed by Oracle Access Governance.
Note  
  
If specific orchestrated system doesn't support Delete action, then no action is taken.
- Disable : Disables all accounts and disables permissions managed by Oracle Access Governance.
- Delete the permissions for disabled accounts : To ensure zero residual access, select this to delete directly assigned permissions and policy-granted permissions during account disablement.
Note  
  
If specific orchestrated system doesn't support the Disable action, then account is deleted.
- No action : No action is taken on accounts and permissions by Oracle Access Governance.
- When an identity leaves your enterprise you must remove access to their accounts.
Note  
  
You can only set these configurations if allowed by your system administrator. When global account termination settings are enabled, application administrators cannot manage account termination settings at the orchestrated-system level.

Select one of the following actions for the account:
- Delete : Delete all accounts and permissions managed by Oracle Access Governance.
- Disable : Disable all accounts and mark permissions as inactive.
- Delete the permissions for disabled accounts : Delete directly assigned and policy-granted permissions during account disablement to ensure zero residual access.
- No action : Take no action when an identity leaves the organization.
Note  
  
These actions are available only if supported by the orchestrated system type. For example, if Delete is not supported, you will only see the Disable and No action options.
- When all permissions for an account are removed, for example when an identity moves between departments, you may need to decide what to do with the account. Select one of the following actions, if supported by the orchestrated system type:
- Delete
- Disable
- No action
- Manage accounts that aren't created by Access Governance : Select to manage accounts that are created directly in the orchestrated system. With this, you can reconcile existing accounts and manage them from Oracle Access Governance.
- Do not allow users to do password resets : Select to prevent users from resetting the passwords for the orchestrated system. If the orchestrated system doesn't support password change operation, password resets are unavailable, and a message is displayed.
Note  
  
If you don't configure the system as a managed system then this step in the workflow will display but is not enabled. In this case you proceed directly to the Integration settings step of the workflow.
Note  
  
If your orchestrated system requires dynamic schema discovery, as with the Generic REST and Database Application Tables integrations, then only the notification email destination can be set (User, Usermanager) when creating the orchestrated system. You cannot set the disable/delete rules for movers and leavers. To do this you need to create the orchestrated system, and then update the account settings as described in[Configure Orchestrated System Account Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-orchestrated-system-account-settings).

## Integration settings

Enter details of the connection to the Oracle Fusion Cloud Applications system.
- On the Integration settings step of the workflow, enter the details required to allow Oracle Access Governance to connect to the Oracle Fusion Cloud Applications system.

Integration settings
Pre condition Parameter Name Description
Application Type
- Both : To integrate both HCM and ERP within the same orchestrated system
- Oracle Human Capital Management (HCM)
- Oracle Enterprise Resource Planning (ERP)
Mode : Authoritative Source
- User Account
- Person
- Select User Account to ingest identities that represent security identities and have system access to Oracle Fusion Cloud Applications.
- Select Person to ingest identities containing employment details, such as employee number, work relationships, job code, person record.
Oracle Fusion Cloud Applications Host Name Host name to access your Oracle Fusion Cloud Applications system. For example, in your URL, the host name is`fa-test.example.com`
```

```

Oracle Fusion Cloud Applications Port Enter the port number at which the source Oracle Fusion Cloud Applications system is listening. For example, in the URL, enter port`443`
```

```

Application Type : Both, ERP OAuth: OCI IAM for Authentication Select the checkbox to use OCI IAM for authenticating your Oracle Fusion Cloud Applications instance. Perform the prerequisites for OAuth. See[Authenticating with OCI OAuth](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#oracle-fusion-oauth-prereqs).
How do you want to give access to the credentials?
- 
- From an OCI vault secret : (Recommended) Select this to use OCI Vault for managing and storing credentials.
- Credentials received and stored in Access Governance : Select this to store credentials within Oracle Access Governance.
OCI Vault What is the OCI tenancy OCID hosting the vault secret? Enter the tenancy OCID where you have created your vault. See[Configuring OCI Vault for Credentials](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#create-oci-vault-store-credentials).
OCI Vault What is the secret OCID for access credentials? Enter the OCI Secret OCID where you have stored credentials. See[Configuring OCI Vault for Credentials](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#create-oci-vault-store-credentials).

Note : You must add the displayed IAM policies in the root compartment of the tenancy where the vault is created.

- Application Type : Both and HCM
- Mode : Managed System Areas of Responsibility Select Areas of Responsibility to ingest AOR as an account attribute when a user account is linked to a person. This option only loads existing AOR data and can't be used for provisioning. To provision AOR assignments, use Area of Responsibility Templates instead. For more information, see[Area of Responsibility (AOR)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-fusion-cloud-applications.htm#oracle-fusion-ofa-functional-overview__aor-concept).

- Application Type : Both and HCM
- Mode : Managed System Do you want to manage Areas of Responsibility with Areas of Responsibility template Select to enable template-based assignment of AOR using Oracle Access Governance. In the[Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm#bundle-create-access-bundle), select an AOR template with Granted permission type as Responsibility template . See[Area of Responsibility (AOR)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-fusion-cloud-applications.htm#oracle-fusion-ofa-functional-overview__aor-concept)and[AOR Template-Based Provisioning](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#create-aor-template).
Application Type : Both, ERP Do you want to manage Procurement Agent (PO) from Access Governance? Select this to manage procurement agent provisioning using Access Bundles. In the[Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm#bundle-create-access-bundle), select a procurement agent with Granted permission type as Procurement business unit , and then select attributes for that procurement business unit.
- Access Bundle displays all available business units. However, you must select a business unit that's configured as a Procurement Business Unit in Oracle Fusion Cloud Applications, otherwise an Add Permission failing error occurs. To configure business unit as a procurement business unit, see[Configure Business Unit for Procurement Agent (PO Agent) in Oracle Fusion Cloud Applications](https://docs.oracle.com/en-us/iaas/Content/access-governance/prepare-fusion-cloud-apps-for-integration.htm#po-agent).
- User must be registered as an employee and must have an associated worker information. The user must have an active predefined security role to create the PO agent. See[Predefined Roles for Procurement](https://docs.oracle.com/en/cloud/saas/applications-common/26a/faser/overview-of-security-for-oracle-fusion-cloud-procurement.html#Predefined-Roles-for-Procurement).

For more information on Procurement Agents, see[Integrate with Fusion Cloud Applications](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-fusion-cloud-applications.htm#oracle-fusion-ofa-functional-overview__procurement-agent).

- Application Type : Both and HCM
- Mode : Authoritative Source Do you want to load additional lookup objects? Enter lookup object name to load additional attributes. For example, enter`job`.

Currently, you can load additional attributes for job and location lookup objects. Use inbound transformation to use these system attributes. See[Support for Lookup Objects.](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-fusion-cloud-application-integration-reference.htm#additional-lookup-objects)
Mode : Authoritative Source (Person) Home Email Select to exclude a Home Email (Type = H1) marked as primary for a person record from ingestion. The primary email is set to null.
Mode : Authoritative Source (Person) Do you want to override the default Future Hire status? Select to mark person records with a start date in the future as AG_Active before their effective start date. By default, person records with a start date in the future are marked as disabled until their effective start date is reached.

- Application Type : Both and HCM
- Mode : Authoritative Source Do you want to fetch a specific manager type? If the Oracle Fusion Cloud Applications instance supports several manager types for a worker, enter the Manager type Lookup code. For example,`LINE_MANAGER`. If not specified, system uses the first/default manager type ingested during the data load.
- Select Test Integration to validate the configuration.
- Select Add to create the orchestrated system.

## Finish Up

Complete the configuration of your orchestrated system by specifying whether to customize the system or activate it and run a data load.

The final step of the workflow is Finish Up .
You can further configure the orchestrated system before running a data load, or accept the default configuration and begin a data load. Select one of the following:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## Post Configuration
