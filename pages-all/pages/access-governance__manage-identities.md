# Manage Identities
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm
- Fetched: 2026-09-05 03:15 CDT

# Manage Identities

Administrators can manage two types of identity population within the Oracle Access Governance service. The Manage Identities feature allows administrators to activate/inactivate identities within the service, and flag identities as either Workforce or Consumer users.

## Active/Inactive Identities

- Active identities : Identities flagged as active within the Oracle Access Governance service, which enables the following features:
- Access to the Oracle Access Governance console, allowing identities to utilize features including My Access, My Access Reviews, My Preferences and so on.
- Allows the identity's access to be governed in Oracle Access Governance.
- Allows identities to be included in access review campaigns.
- Active identities are considered for billing purposes.
- Inactive identities : Identities flagged as inactive within the Oracle Access Governance service.
- Inactive identities have no access to the Oracle Access Governance Console.
- Inactive identities access governance is not governed in Oracle Access Governance.
- Inactive identities are not included in access review campaigns.
- Inactive identities are not considered for billing.
Note  
  
The default status of identities present in Oracle Access Governance is NULL. In order for identities to use the service functionality, and be considered for billing, you must activate all users for which this is required, using the steps detailed in this article.

Identities imported from Oracle Identity Governance have a status of Disabled or Enabled . This is different from the Oracle Access Governance status Active/Inactive . You should consider the following conditions when dealing with identities imported from Oracle Identity Governance:

- A Disabled identity can be marked as an Active identity in Access Governance to review its access privileges.
- An Oracle Access Governance Administrator may set rules, based on the attributes of disabled identites, to mark those disabled identities as Active in Oracle Access Governance.
- Oracle Access Governance will include only those Disabled identities for billing that are marked as Active.

## Consumer/Workforce Users

A user can be either a Workforce user or a Consumer. The main difference is that a Consumer user has no access to the Oracle Access Governance service. By default, users are Workforce users. The specific differences between the two types are given in the table below:

Workforce and Consumer Users
Capabilities Workforce User Consumer User

Access the Oracle Access Governance service: by console or programmatically.

YES

NO

Perform configurations and integrations, such as orchestrated systems, identity marking, identity attributes.

YES

NO

Manage access control objects (Role, Access Bundle, Identity Collection, Policy).

YES

NO

Manage access review campaigns (event-based, periodic, one-time).

YES

NO

Generate reports for access reviews and approvals.

YES

NO

View access privileges assigned to self or others.

YES

NO

Raise access request for self and/or others.

YES

NO
Perform access approval tasks.

YES

NO

Birthright Access through policies.

YES

YES

## Navigate to Manage Identities

Here's how you can access the Manage Identities page:

- Sign in to the Oracle Access Governance Console as a user with the Administrator application role.
- Select in the top left corner to display the navigation menu .
- Select Service Administration → Manage Identities to begin defining your identity rules.

The Manage Identities page is displayed, where you have to define which identities you want to activate. Oracle Access Governance identities are displayed in this page with each identity showing attributes such as First Name, Last Name, Employee Username, Email, and others. You can change the attributes displayed for each identity by selecting the Edit list settings icon. In the List settings pop-up, you can select to Show or Hide attributes. An example would be that you want to flag identities which have delegations defined. To implement this you would select to Show the Delegation attribute.

You can use the Search field to find the required identity using a string search. Alternatively you can select one of the available filters, for example, if you select the Delegation Yes filter would restrict identities displayed to those for which delegations are defined.

## Select Identities for Activation

In the Manage Identities page, an Administrator defines the identities that you want to include in the Oracle Access Governance service. Active Identities are Workforce identities and can access the service.

You can choose identities to include in your service by selecting criteria based on conditional statements. Either at least one ( Any ) or all ( All ) the set conditions must be satisfied. The list of available attributes is determined by the ingested data from the Managed System, and may include custom attributes.

Select identities based on Membership rule and/or Named identities . Identities satisfying the set criteria for the Membership rule will automatically be included in your service. Using Named identities, you can directly add specific identities based on their full name.

You can also exclude specific members from your service by selecting Manage exclusions and entering the identities you want to exclude.
- In the Oracle Access Governance Console, click the icon, and select Service Administration &gt; Manage Identities &gt; Active . You will see the Active Identities page where you can view and manage active workforce identities.
- Select Edit .
Note  
  
For the first time set up, you'll directly see the edit mode to select the identities or apply conditional membership rules.
- Select appropriate approval workflow to ensure all revisions (updates) to the active identities are reviewed before implementation. By default, No Approval Required is selected. See[Revision Management in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/revision-management.htm).
Note  
  
For the first time set up, select the identities or apply conditional membership rules After setting up approval workflows in the Console, edit and select the required approval workflow.
- In the Membership rule tab:
- Select Any if any one of the set conditions should be satisfied, or select All if all the set conditions must be satisfied for that identity.
- Select the attribute name from the list.
Note  
  
Based on the Managed System, you can select both core and/or custom attributes. To enable custom attributes, see[Manage Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm).
- Select the conditional operator. Based on the data type of the attribute selected, the usage of these operators will vary.
- Type the attribute value.
- Continue to add the conditional statements or rules for more attributes. By default all the identities matching the criteria will be included.
- To directly add identities, select the Included named identities tab.
- Search and select identities from the list.
- Select the Manage Exclusions button next to Excluding # identity from the attribute conditions and then select the identities that you want to exclude from your service.
- Select Publish . Once published, all the future revisions (exclusions or inclusions) follow the defined approval workflow before the changes are implemented.

### Viewing Preview Summary for Included Workforce Identities

Once you have defined your rules, select Preview summary based on the rule above to go to the Preview Summary pane. The following information is displayed:
- Count of matching identities out of total ingested identities
- In the Table and Chart view, distribution of identities based on core attributes, such as Source Organization, Job Code, Location, Employe Type, and so on.
- Identity details with Identity name, email, manager, and other associated core attributes.

### Example: Membership Rules for Active Workforce Identities
Let's assume you have defined the following rules:
- Condition Type: All
- Status Equals Enabled
- Employee type Equals Full time
- Email Contains @company.com

Result : Active, full time employees with official company email addresses are included as active identities.

## Select Consumer Users

In the Manage Identities page, an Administrator select the identities that you want to be flagged as consumer users in the Oracle Access Governance service. Consumer users cannot access the service but accesses are managed in the Oracle Access Governance Console by workforce identities.

Choose identities to include as consumers in your service by selecting criteria based on conditional statements. Either at least one ( Any ) or all ( All ) the set conditions must be satisfied. The list of available attributes is determined by the ingested data from the Managed System, and may include custom attributes.

Select identities based on Membership rule and/or Named identities . Identities satisfying the set criteria for the Membership rule will automatically be included as consumers in your service. Using Named identities, you can directly add specific identities based on their full name.

You can also exclude specific members from your service by selecting Manage exclusions and entering the identities you want to exclude.
- In the Oracle Access Governance Console, click the icon, and select Service Administration &gt; Manage Identities &gt; Consumer . You will see the Active Consumer page where you can view and manage consumer identities.
- Select Edit .
- Select appropriate approval workflow to ensure all revisions (updates) to the consumer identities are reviewed before implementation. By default, No Approval Required is selected. See[Revision Management in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/revision-management.htm).
Note  
  
For the first time set up, select the identities or apply conditional membership rules After setting up approval workflows in the Console, edit and select the required approval workflow.
- In the Membership rule tab:
- Select Any if any one of the set conditions must be satisfied, or select All if all the set conditions must be satisfied for that identity.
- Select the attribute name from the list.
Note  
  
Based on the Managed System, you can select both core and/or custom attributes. To enable custom attributes, see[Manage Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm).
- Select the conditional operator. Based on the data type of the attribute selected, the usage of these operators will vary.
- Type the attribute value.
- Continue to add the conditional statements or rules for more attributes. By default all the identities matching the criteria will be included.
- To directly add identities, select the Included named identities tab.
- Search and select identities from the list.
- Select the Manage Exclusions button next to Excluding # identity from the attribute conditions and then select the identities that you want to exclude from your service.
- Select Publish . Once published, all the future revisions (exclusions or inclusions) follow the defined approval workflow before the changes are implemented.

### Viewing Preview Summary for Included Consumer Identities

After you have defined the rules, select Preview summary based on the rule above to go to the Preview Summary pane. The following information is displayed:
- Count of matching identities out of total ingested identities
- In the Table and Chart view, distribution of identities based on core attributes, such as Source Organization, Job Code, Location, Employee Type, and so on.
- Identity details with Identity name, email, manager, and other associated core attributes.

## Create and Manage Organizations

You can now structure identities and form relationships between identities by creating and managing Organization with the Oracle Access Governance Console.
You can use Organizations to perform various operations within the Oracle Access Governance Console. For example, you can use it as an attribute ( Organization ) to create an Identity Collection, which can then be used for identity reviews, assigning access privileges, or for provisioning operations.
Note  
  
This Organization concept is native to Oracle Access Governance and is different than the source organization, which is loaded from an orchestrated system. It will be available in the core attribute list as agOrganization (where the orchestrated system is Internal) with the Manage Identities flag set to true. See[View and Configure Custom Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#manageattributes-settings). If this flag is set to true, you can use this Organization to create/manage an Identity collection within Oracle Access Governance.

In the Oracle Access Governance Console, click the icon, and select Service Administration &gt; Manage Identities &gt; Organizations . You will see the Organizations page where you can view and manage existing organization, or create new ones.

### Create Organization

To create a new organization, click the Create an organization button. The Add Details task is displayed. In the Add Details task, you can enter specifics about your organization. Here, you can give a meaningful name and add its supporting description.
- Enter a name for your organization in the What do you want to call this organization? field.
- Add a description for your organization in the How would you describe this organization? field.
- Select one or more identities from the Who else can manage this organization list. The owner along with the listed identities can manage this organization.
- Add one or more tags to identify or search your organization.
- Select appropriate approval workflow to ensure all revisions (update or delete) to this organization are reviewed before implementation. By default, No Approval Required is selected. See[Revision Management in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/revision-management.htm).
- Once you have set your preferences, select Next to go to the Select Identities step.

Add Owners
You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

Select Identities

In the Select Identities task, add identities that you want be part of your organization. You can select identities based on Membership rule and/or Named identities . For Membership rule, the identities satisfying the set criteria will automatically be included in organization. In Named identities, you can directly add identities based on their full name. All the available active identities (configured from the[Licence Management](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)page) will be displayed. You can also exclude specific members from your organization by selecting Manage exclusions and entering the identities you want to exclude.
- Select Any if any one of the set conditions should be satisfied, or select All if all the set conditions must be satisfied for that identity.
- Select the attribute name from the list.
Note  
  
Based on the orchestrated system, you can select both core and/or custom attributes. To enable custom attributes, see[View and Configure Custom Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#manageattributes-settings)
- Select the conditional operator. Based on the data type of the attribute selected, the usage of these operators will vary.
- Type the attribute value.
- Continue to add the conditional statements or rules for more attributes.

By default all the identities matching the criteria will be included. Click the Manage Exclusions button next to Excluding # identity from the attribute conditions and then select the identities that you want to exclude from an organization.
- Once you have set your preferences, select Next to go to the Review and submit step.
- You can preview graphical summary of how many identities are included in your organization by clicking the Preview the organization link. This link is available on the right-side, towards the bottom of the Who is included panel.
- If you are satisfied with your organization preview, click Create .

### Manage Organization
Oracle Access Governance Administrators can view and manage organizations from the Oracle Access Governance Console. You can view existing organization and manage the ones that you created, or are authorized to manage, using the Oracle Access Governance Console. Use the Actions menu icon to edit, delete or view details of the organization.
Note  
  
Only organization owners and/or authorized users (selected while creating/modifying an identity collection) can edit or delete the organization.

You can perform the following:
- Search and Filter available organizations : You can use the Search field to locate the required organization by its name. You can narrow down the results by applying the available filters.
- Edit an organization : The Edit an organization page provides the same guided tasks as you see while creating a new identity collection. Owner of the organization and/or authorized users can modify its description, identity type, or added identities. After updating the details, on the Review and submit step, select Update / Publish to update the organization or send the revision request to approval workflow. You cannot edit an organization with an in progress or pending revision status.
- View organization details : You can see Organization page displaying complete organization details, such as Organization owner, created and last modified dates, current members, as well as how the current members were included (through named identities or membership rule).
- View Revision History : From the details page, view all active versions of organization, including those that are created, modified, requested, remediated, approved, or rejected.
- Delete an organization : You can delete the organization if you are the owner of the organization or you have been given the rights by the owner. If an identity collection is based on the deleted organization value, then those identities would no longer be members of that identity collection. You cannot delete an organization with an in-progress or pending revision status.
- View Revision Request : You can view revision request details for Revision requested , Info requested , or Delete requested revision status. For more information, see[View Revision Request Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/revision-management.htm#revision-revision-request-details).

## Manage Account Lifecycle with Oracle Access Governance Service Desk Administrator Support

As a user with`AG_ServiceDesk_Admin`role, you can directly initiate account management operations with no approval process. You may enable, disable, delete accounts, or terminate all accounts and associated accesses for an identity. You can also retry provisioning for failed or pending statuses, and revoke permissions assigned directly or through requests from the Manage Identities → Identities page.

Additionally,`AG_ServiceDesk_Admin`can manage delegations or change password. For more details, see[Manage Delegation Preferences](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-delegation-preferences.htm)and[View Access Details and Manage Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm).

### Terminate all Accounts and Accesses for an Identity

You can terminate accounts and associated accesses for an identity immediately without an approval process. The identity would still remain Active in Oracle Access Governance.
Required roles :`AG_ServiceDesk_Admin`

For more details, see[Application Roles and Responsibilities Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm).

You can view access information, accounts, permissions, and identities from multiple views in Oracle Access Governance, depending on the application role and operational needs.
- Use Enterprise-wide Browser (EWB) for enterprise-wide access visibility on all the components, access information, and resources within an enterprise framework. Typically used by users with the`AG_Enterprise_Wide_Access_Admin`application role. See[Explore Access Profile in an Enterprise](https://docs.oracle.com/en-us/iaas/Content/access-governance/explore-access-insights.htm)
- Use Manage Identities for identity administration and identity-level operational tasks. Typically used by users with the`AG_ServiceDesk_Admin`application role. See[Manage Account Lifecycle with Oracle Access Governance Service Desk Administrator Support](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#manage-account-lifecycle-with-service-desk-executive-support).
- Use My Access and My Directs’ Access to review your own access or access assigned to your direct reports. Typically used by managers and Oracle Access Governance users. See[View Access Details and Manage Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm#view-access-details-and-manage-account).
- Use Data Browser for reviewing reconciled accounts and permissions and performing account management operations at the orchestrated system-level, such as matching accounts with identities, retrying provisioning for failed operations, and revoking permissions. Typically used by users with the`AG_AppOwner_Admin`or`AG_AppOwner_Admin_Restricted`as the resource owner. See[Data Browser: View Accounts and Granted Permissions for Managed Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-overview.htm#data-browser-overview). Accounts and accesses with Grant Type`DIRECT`cannot be terminated. You may view the termination status by selecting the Terminated in Access Governance column from the Manage Identities → Identities page.

Terminate Accounts and Accesses for an Identity
- Log in to Oracle Access Governance Console.
- Click the navigation icon in the top left corner to display the navigation menu.
- Select Service Administration &gt; Manage Identities . The Identities page opens by default.
- From the Identities list, select the Actions icon and select Terminate .
A confirmation dialog box is displayed confirming that all accounts and accesses for an identity will be deleted or disabled based on account settings.
- Select the acknowledgment check box to terminate an identity access.
- Select Terminate in the dialog box. A confirmation message stating termination request has been initiated will be displayed.
Once terminated, the status changes to Yes in the Terminated in Access Governance column along with a flag`Terminated`in the Identity details page. You may have to edit the list settings to view the column. You cannot manage these accounts from Oracle Access Governance.

### Activate Accounts and Accesses for an Identity

You can re-provision terminated accounts and accesses using the Activate operation, ensuring seamless account management in Oracle Access Governance.

For more details, see[Application Roles and Responsibilities Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm).

Terminated accounts with Grant Type`Policy`can be re-provisioned into Oracle Access Governance.

- From the Identities list, select the Actions icon and select Activate .
A confirmation dialog box is displayed confirming accesses for an identity will be enabled.
- Select the acknowledgment check box to activate an identity access.
- Select Activate . A confirmation message stating activation request has been initiated will be displayed.
- Once activated, the status changes back to No in the Terminated in Access Governance column. You can now manage these accounts for an identity from Oracle Access Governance.

### Revoke Permissions for an Account Managed by Oracle Access Governance

Permissions assigned directly, with grant type`Direct`, or access bundles granted through a self-service request, with grant type`Request`, can directly be revoked for an identity from the Manage Identities → Identities page.
You cannot revoke permissions Oracle Identity Governance (OIG).

For OCI IAM, you can directly revoke OCI IAM groups and application roles. Based on the application role, you can also perform this operation from the Data Browser page. See[Performing Account Lifecycle Operations in Data Browser](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-operations.htm#data-browser-ops).

- Sign in to Oracle Access Governance Console.
- Click the navigation icon in the top left corner to display the navigation menu.
- Select Service Administration &gt; Manage Identities . The Identities page opens by default.
- From the Identities list, select the Actions icon and select View details .
The Identity details page is displayed with the Permissions tab selected by default.
- Select the Actions icon corresponding to the permission that you want to revoke.
- Select Revoke permission . A confirmation dialog box is displayed confirming that permission accesses will be revoked.
- Select Revoke . A confirmation message stating revocation request has been initiated will be displayed.
During the revocation process, a transitional state indicator with an icon and tool tip are displayed. Once the process is complete, the final status is displayed in the Status column. For failed or pending statuses, you may again retry provisioning for the permissions provisioned within Oracle Access Governance.

### Retry Provisioning for Failed or Pending Accesses

You can retry provisioning for accesses with the Failed or Pending statuses. You can perform this operation for access bundles granted through request or granted via policy, that is, Grant Type Request or Grant Type Policy .
Based on the application role, you can also perform this operation from the Data Browser page. See[Performing Account Lifecycle Operations in Data Browser](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-operations.htm#data-browser-ops).

- Log in to Oracle Access Governance Console.
- Select the navigation icon in the upper left corner to display the navigation menu .
- Select Service Administration &gt; Manage Identities . The Identities page opens by default.
- From the Identities list, select the Actions icon and select View details .
The Identity details page is displayed with the Permissions tab selected by default.
- Select the Actions icon corresponding to the permission for which you want to retry provisioning.
- Select Retry provisioning . A confirmation dialog box is displayed confirming that provisioning for the accesses will be retried.
- Select Retry . A confirmation message will be displayed.
During the retry provisioning process, a transitional state indicator with an icon and tool tip are displayed. Once the process is complete, the final status is displayed in the Status column.

### Disable and Enable an Account Managed by Oracle Access Governance

You can directly disable one or more accounts that are managed by Oracle Access Governance. You can perform this operation for the orchestrated systems that support this operation.
Based on the application role, you can also perform this operation from the Data Browser page. See[Performing Account Lifecycle Operations in Data Browser](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-operations.htm#data-browser-ops).

Disable an Account Managed by Oracle Access Governance
- Sign in to Oracle Access Governance Console.
- Select the navigation icon in the top left corner to display the navigation menu .
- Select Service Administration &gt; Manage Identities . The Identities page opens by default.
- From the Identities list, select the Actions icon and select View details .
The Identity details page is displayed with the Permissions tab selected by default.
- Select the Accounts tab.
- Select the Actions icon corresponding to the account that you want to disable.
- Select Disable account . A confirmation dialog box is displayed confirming that account will be disabled and access will be removed.
- Select Disable . A success message is displayed.
During the process, a transitional state indicator with an icon and tool tip are displayed. Once the process is complete, the final status changes to Disabled in the Status column.
Enable an Account to be Managed by Oracle Access Governance
- To enable a disabled account and restore the accesses, select the Actions icon corresponding to the account that you want to enable.
- Select Enable account . A confirmation dialog box is displayed confirming that account will be enabled and access will be granted or re-provisioned.
- Select Enable . A success message is displayed.
During the process, a transitional state indicator with an icon and tool tip are displayed. Once the process is complete, the final status changes to Enabled in the Status column.

### Delete an Account Managed by Oracle Access Governance

You can directly delete one or more accounts that are managed by Oracle Access Governance. Once deleted, you can no longer manage these accounts from Oracle Access Governance.
Based on the application role, you can also perform this operation from the Data Browser page. See[Performing Account Lifecycle Operations in Data Browser](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-operations.htm#data-browser-ops).

Delete an Account Managed by Oracle Access Governance
- Sign in to Oracle Access Governance Console.
- Click the navigation icon in the top left corner to display the navigation menu.
- Select Service Administration &gt; Manage Identities . The Identities page opens by default.
- From the Identities list, select the Actions icon and select View details .
The Identity details page is displayed with the Permissions tab selected by default.
- Select the Accounts tab.
- Select the Actions icon corresponding to the account that you want to delete.
- Select Delete account . A confirmation dialog box is displayed confirming that account will be deleted and access will be removed.
- Select Delete . A success message is displayed.
During the process, a transitional state indicator with an icon and tool tip are displayed. Once the process is complete, the account is removed from the list.

### Modify Account Attributes from Oracle Access Governance

You can directly modify values for account attributes from the Oracle Access Governance Console. You can edit values for any account attribute that the configured orchestration system permits.

Edit Account from Oracle Access Governance
- Log in to Oracle Access Governance Console.
- Click the navigation icon in the top left corner to display the navigation menu.
- Select Service Administration &gt; Manage Identities . The Identities page opens by default.
- From the Identities list, select the Actions icon and select View details .
The Identity details page is displayed with the Permissions tab selected by default.
- Select the Accounts tab.
- Select the Actions icon corresponding to the account that you want to edit.
- Select Edit account .
- Modify the account attributes, as needed.
- Select Save . A confirmation message displays that the modification has been requested.
- Select Reset changes to undo all the changes.
You can request multiple account edits at the same time and would see the "Account update is in progress" message. Click the view change details link to see all the in-progress edits.

This initiates the Update Account activity in the activity log. For more details, see[View Activity Log](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-integrations-with-orchestrated-system.htm#view-activity-log)
