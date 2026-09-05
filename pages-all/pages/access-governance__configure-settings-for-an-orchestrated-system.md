# Configure Settings for an Orchestrated System
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm
- Fetched: 2026-09-05 03:13 CDT

# Configure Settings for an Orchestrated System

With Oracle Access Governance, you can configure an orchestrated system by editing the integration settings, configuring notification settings, transforming inbound and outbound data for identity and account attributes, and applying matching or correlation rules to ensure integrated components work seamlessly together.

## Manage System Settings for your Orchestrated System

Manage system settings for your orchestrated system using the Oracle Access Governance Console.

### Modify Integration Settings for an Orchestrated System

You can configure the integration settings for your orchestrated system, using the Oracle Access Governance Console.

You can update the integration settings for a chosen orchestrated system by accessing the Manage Integration page in the Oracle Access Governance Console and performing the following tasks:

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the action menu for the orchestrated system you want to configure. This displays the manage integration page for the selected orchestrated system.
- From the System settings section of the page, select Manage on the Integration settings tile. This will display the Integration settings page for the selected orchestrated system. The integration settings displayed are dependent on the type of orchestrated system you are updating.
- Update the integration settings as required, and click Save .

### Configure Identities or Email for Sending Orchestrated System Related Notifications

If an issue occurs in an orchestrated system during dataload, you want to be notified in good time so that you can investigate and resolve the issue. You can configure identities or an external email, to route notifications regarding your orchestrated system to assist with this.
To send orchestrated system-related notifications to your preferred identities or an external email address, you can configure Oracle Access Governance as required:

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the action menu for the orchestrated system you want to configure. This displays the manage integration page for the selected orchestrated system.
- From the System settings section of the page, select Manage on the Notification settings tile. This will display the Notification settings page for the selected orchestrated system.
- In the Which identities? field, use the drop-down list to select identities in your Oracle Access Governance instance to send orchestrated system-related notifications to. You can have multiple identities as required.
- In the Email field, add an email for any person external to your Oracle Access Governance instance (who does not have an identity in your system) who you would like to receive notifications. You can only add one external email address for orchestrated system-related notifications.
- Update the notification settings as required, and click Save .

### Add Primary and Additional Owners

You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
For assigning resource ownership, you must have active Oracle Access Governance users. When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section.
No special application roles are necessary for assigning resource ownership. Any Oracle Access Governance active user can be assigned as the owner of the resources. All the owners can read, update, or delete the resources that they own. However, the Primary Owner is assigned as the access reviewer when you choose the Owner template in the approval workflow for performing Ownership reviews in Campaigns. For more information, refer[Types of Access Reviews Offered by Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#types-of-access-certifications).

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the action menu for the orchestrated system you want to configure. This displays the manage integration page for the selected orchestrated system.
- From the System settings section of the page, select Manage on the Ownership settings tile. This will display the Ownership settings page for the selected orchestrated system.
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource.
You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

### Manage Virtual Systems

Update the CSV file to add new virtual systems for an orchestrated system.
Applies to : Flat File
See[Understanding Virtual Systems](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#virtual-systems).

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the action menu for the orchestrated system you want to configure. This displays the manage integration page for the selected orchestrated system.
- From the System settings section of the page, select Manage on the Virtual Systems tile. The preview of existing virtual systems is displayed.
- Select the Update button to upload the CSV file and include new virtual systems or update existing ones.
Existing virtual systems can't be deleted but can be updated. If you remove the virtual system from the CSV file, an invalid file error is displayed stating that the defined virtual system is not present in the file and cannot be removed.
- Click Save .

## Manage Data Settings for Your Orchestrated System

Manage data settings for your orchestrated system by creating system attributes, applying transformation rules, configuring safety checks during data loads, and applying matching rules to build a global identity profile in Oracle Access Governance.

### Configure Data Load Schedule Settings for Orchestrated Systems

Set how often data should be loaded and updated in Oracle Access Governance from the orchestrated system. Schedule timing and frequency by choosing specific days, hours, or minutes.
To configure data load settings:
You can configure the timing and frequency for all orchestrated system except generic integration of Flat File and Oracle Cloud Infrastructure.

Navigate to Data Load Settings
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the action menu for the orchestrated system you want to configure. This displays the manage integration page for the selected orchestrated system.
- From the System settings section of the page, select Manage on the Data load settings tile. This will display the Data load settings page for the selected orchestrated system.
- If you want to run the data load one time after the full data load, select Only run the data load one time? and supply a date and time to run the data load.
- If you want to run the data load periodically, perform the steps that follow:
Select Frequency
- In the Run every field, choose a number to specify how often the data load should occur
- In the Frequency drop-down, select one:
- Hours
- Minutes
- Days
Limits have been applied to ensure reliable data is available and prevent outdated data. For example, the frequency cannot be less than 5 minutes.
Select Start Date
- In the Starting on field, select the date time icon to specify when the data load should begin, and then click Done .
- Click Save . To save your settings for the orchestrated system, in the conformation pop-up box, click Confirm .
If the previous data load takes longer to complete, the next schedule load will be skipped. To avoid skipped syncs, ensure your settings allow enough time for each load to finish before the next one starts.
To disable automatic data loads for the orchestrated system, select Disable data loads . This allows provisioning and permission assignments, but stops automatic reconciliation. If required, you can choose to manually run the data load.

### Configure Partial Data Load Schedule Settings for Orchestrated Systems

Enable incremental data ingestion by loading only the new or updated records because the last load, instead of performing a full data load on entire dataset. This helps to optimize data ingestion process. You can auto schedule partial data load by selecting timing and frequency.
To configure partial data load settings:
Applies to :[Oracle Fusion Cloud Applications](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-fusion-cloud-applications.htm#integrate-with-fusion-cloud-applications),[Database Application Tables (Oracle)](https://docs.oracle.com/en-us/iaas/Content/access-governance/integrate-with-database-application-tables-oracle.htm#integrate-with-database-application-tables-oracle).

Navigate to Partial Data Load Settings
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the action menu for the orchestrated system you want to configure. This displays the manage integration page for the selected orchestrated system.
- From the System settings section of the page, select Manage on the Data load settings tile. This will display the Data load settings page for the selected orchestrated system.
- In the Partial data loads section, select the Enable partial data loads . check box.
- If you want to run the data load periodically, perform the steps that follow:
Select Frequency
- Select Run partial data loads on a schedule check box.
- In the Run every field, choose a number to specify how often the partial data load should occur
- In the Frequency drop-down, select one:
- Hours
- Minutes
- Days
Limits have been applied to ensure reliable data is available and prevent outdated data. For example, the frequency cannot be less than 5 minutes.
Select Start Date
- In the Starting on field, select the date time icon to specify when the data load should begin, and then click Done .
- Click Save . To save your settings for the orchestrated system, in the conformation pop-up box, click Confirm .
In Activity Log , you can verify by checking the Data Load activity.

### Configure Safety Checks for Orchestrated System

Set safety checks to prevent accidental or unintended data loss while managing identities in Oracle Access Governance.
To configure safety checks:
You can configure the maximum allowed decrease (in percentage) for identities, accounts, or permissions during data load. This action detects total changes in the total number of identities, accounts, or permissions with each data load.
Based on configuration mode and orchestrated system, you can configure the following:
- For an orchestrated system configured as an Authoritative Source , you can set only the identities threshold.
- For an orchestrated system configured as a Managed System , you can set accounts and permissions threshold.
- For an orchestrated system configured both as an Authoritative Source and a Managed System , you can set identities, accounts, or permissions.
- For Oracle Cloud Infrastructure (OCI) Managed System mode, you can set accounts, permissions, resource and policies (only if allowed during data load).
- For Oracle Cloud Infrastructure (OCI) Authoritative Source and Managed System mode, you can set identities, accounts, permissions, resources and policies.

Navigate to Data Load Settings
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the action menu for the orchestrated system you want to configure. This displays the manage integration page for the selected orchestrated system.
- From the System settings section of the page, select Manage on the Data load settings tile. This displays the Data load settings page for the selected orchestrated system.
- Select Enable safety checks .
- What is the max percentage of decrease allowed for identities? : Set a limit on how much the number of identities (in percentage) can decrease during automated data loads or provisioning.
- What is the max percentage of decrease allowed for accounts? : Set a limit on how much the number of accounts (in percentage) can decrease during automated data loads or provisioning.
- What is the max percentage of decrease allowed for permissions? : Set a limit on how much the number of permission (in percentage) can decrease during automated data loads or provisioning.
- Select Save .
The provisioning operation fails if the percentage of decrease exceeds the configured threshold.

### Manage Identity Attributes for your Orchestrated System

Manage default system attributes and create non-standard attributes, either simple or complex, to address specific business requirements. You can create rule-based, user-defined functional attributes using Affiliations.

For more information, see[Create System Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#system-attribute)and[Configure and Manage Affiliations](https://docs.oracle.com/en-us/iaas/Content/access-governance/affiliations-configure-affiliations.htm).

### Apply Inbound Transformations for Identity and Account Attributes

To modify the incoming data ingested into Oracle Access Governance, you need to apply inbound data transformations. To do so, perform the following tasks:
- In the Oracle Access Governance Console, access the navigation menu by selecting the icon. Select Service Administration → Orchestrated Systems .
- Select the orchestrated system from the list which you want to configure inbound data transformation rules for.
- Expand the Configurations drop-down menu and select the Manage button on the Inbound data transformations tile. The Inbound data transformations page displays a list of any rules that you have configured, and an option to add new attribute rules.
- To create an attribute rule for your orchestrated system, select the Add attribute rule button.
- In the Add attribute rule panel enter the following information to configure your rule.
- Which configuration mode? : Select one configuration mode, from the drop down list, that you want this attribute rule to apply to.
- Authoritative source : Authoritative Sources that contain identity data and its attributes.
- Managing permissions : Managed Systems containing account information and permissions.
- Which attribute? : Select the Oracle Access Governance attribute you want to apply the transformation to from the drop down list. The list of attributes available will depend on the orchestrated system type, and configuration mode you select.
- Rule : Enter the rule you want to apply to this operation/attribute.
- Select the Validate button to check your rule. If the rule is valid then you will see a confirmation message and the rule will be marked as validated. If there is an issue with the rule, then you will see an error message and the rule will be marked as invalid. You cannot save your rule if it is marked as invalid.
- When your rule is valid select Add to save your configuration.

### Apply Outbound Transformations for Identity Attributes

To modify the outgoing data provisioned in Oracle Access Governance, you need to apply outbound data transformations. To do so, perform the following tasks:
- In the Oracle Access Governance Console, access the navigation menu by selecting the icon. Select Service Administration → Orchestrated Systems .
- Select the orchestrated system from the list for which you want to configure the outbound data transformation rules.
- Expand the Configurations drop-down menu and select the Manage button on the Outbound data transformations tile. The Outbound data transformations page displays a list of any rules that you have configured, and an option to create attribute rules.
- To create an attribute rule for your orchestrated system, select the Add attribute rule button.
- In the Add attribute rule panel enter the following information to configure your rule.
- Which operations : Select one or more of the operations from the drop down list that you want this attribute rule to apply to.
- Create Account
- Change Password
- Which attribute? : Select the attribute in the orchestrated system you want to apply the transformation to from the drop down list. The list of attributes available will depend on the orchestrated system type.
- Rule : Enter the rule you want to apply to this operation/attribute.
- Click the Validate button to check your rule. If the rule is valid then you will see a confirmation pop-up message and the rule will be marked as validated. If there is an issue with the rule, then you will see an error pop-up message and the rule will be marked as invalid. You cannot save your rule if it is marked as invalid.
- When your rule is valid click Add to save your configuration.

### Match Identity and Account Attributes using Correlation Rules

Oracle Access Governance leverages correlation or matching rules to correlate incoming identities and accounts to existing identities.

To understand the concept, see[Matching rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#matching-rules).

To configure matching rules in Oracle Access Governance perform the following steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select one of the following to view the configuration of a specific orchestrated system:
- The connected system link in the Name column.
- Manage connection from the navigation menu . This displays the configuration page for the selected orchestrated system.
- From the Configurations section of the page, select Manage on the Matching rules tile. The Matching rules page is opened.
- Select the tab that you want to configure:
- Identity matching : For identity correlation
- Account matching : For account correlation.
- Set the matching mode to apply for this orchestrated system:
- Enabled : Matching rules apply to incoming identities or accounts.
- Enabled for new : Matching rules apply only to new identities or accounts. Existing links remain unchanged.
- Disabled : Matching rules don't apply. New identities or accounts that aren't already correlated appear as Unmatched .
- To apply rules, select one of the following conditions:
- All : All rules must be matched in this case so order of the rules isn't significant.
- Any : Any one rule must match. Order matters. To move a rule up, select the menu for the rule, and select Move up .
- Add a rule by selecting an Equals or Not equals operator.
- Update the matching rules as required, and select Save .

To view insights of the incoming identities and accounts, see[Insights for Match Results](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#matching-rules__insights-matching-rules). Based on the application role, you can perform the actions from other modules within Oracle Access Governance. See[Performing Account Lifecycle Operations in Data Browser](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-operations.htm#data-browser-ops).

## Manage Account Settings for your Orchestrated System

Manage system settings for your orchestrated system using the Oracle Access Governance Console.

### Modify Account Lifecycle Settings for an Orchestrated System

Configure account lifecycle settings for an orchestrated system, including account creation, notifications, and actions for movers and leavers. You can also manage external accounts and restrict user password resets, based on system support and administrator permissions.

To update the account details used by Oracle Access Governance to connect to an orchestrated system, perform the following tasks.
Navigate to Account Settings for an Orchestrated System
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the navigation menu. to view the configuration of a specific orchestrated system. This displays the configuration page for the selected orchestrated system.
- From the Account settings section of the page, select Manage on the Account lifecycle tile.
Edit Account Lifecycle Settings

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
  
If you do not configure your system as a managed system then this step in the workflow will display but is not enabled. In this case you proceed directly to the Integration settings step of the workflow.
Note  
  
If your orchestrated system requires dynamic schema discovery, as with the Generic REST and Database Application Tables integrations, then only the notification email destination can be set (User, Usermanager) when creating the orchestrated system. You cannot set the disable/delete rules for movers and leavers. To do this you need to create the orchestrated system, and then update the account settings as described in[Configure Orchestrated System Account Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-orchestrated-system-account-settings).

### Configure Account Attributes

You can configure account attributes for your orchestrated system in addition to the default account attributes supported out-of-the box. Values for your account attributes can come from a managed system, global key-values, transformations or defined when creating an access bundle. You can use and configure these attributes for inbound or outbound transformations, or for account provisioning operations, such as account creation. You can also use these account attributes to define the account profile required for provisioning. Oracle Access Governance supports simple and complex data types when defining account attributes.

#### Manage Simple Account Attributes

To create a simple account attribute :

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the navigation menu. to view the configuration of a specific orchestrated system. This displays the configuration page for the selected orchestrated system.
- From the Account settings section of the page, select Manage on the Account attributes tile. This will display the Account attributes page for your orchestrated system, which displays default attributes created when you initialise your orchestrated system, as well as additional account attributes created by the user.
- Click on the Create an attribute button.
- In the Create a new account attribute flow, enter details of your simple account attribute:
- Enter values for the Add details step:

Add details
Parameter Name Mandatory? Description
What is the system attribute name? Yes The attribute name for the account attribute in the associated orchestrated system.
What should AG call it? Yes The name for the account attribute in Oracle Access Governance.
What is the display name? Yes The name for the account attribute when displayed in Oracle Access Governance.
What is the data type? Yes Any of the simple data types listed in the drop-down, including:
- String
- Long
- Double
- Date
- Sensitive string
- Integer
- Boolean
Is there an associated identity attribute? No Name of any identity attribute that is associated with the account attribute. Any change in the value of the account attribute will be reflected in the identity attribute.
Which key-values lookup should be used? No Select orchestrated system lookups or[global key-values](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-global-key-values.htm)to populate the account attribute.
- Select the options that apply for the Setup usage step:

Setup usage
Parameter Name Description
Mandatory for account creation Is the account attribute a mandatory value when creating an account.
Included in inbound data from the system Is the account attribute included in inbound data coming from the orchestrated system. If selected, this attribute will be available to inbound transformations.
Populated in outbound data to the system Is the account attribute included in outbound data sent to the orchestrated system. If selected, this attribute will be used to provision and update account values in the orchestrated system.
Supports multiple values Does the account attribute allow for multiple values.
Value is provided after account creation The value will be populated from the orchestrated system after the account has been created.
Mask value when displayed Sets the value for this attribute to be obscured (replaced by eight asterisks, "********") when displayed, such as in the[Who Has Access To What](https://docs.oracle.com/en-us/iaas/Content/access-governance/explore-access-insights.htm#explore-access-insights),[My Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/view-access-details-and-manage-account.htm#view-access-details-and-manage-account),[Data Browser](https://docs.oracle.com/en-us/iaas/Content/access-governance/data-browser-overview.htm#data-browser-overview), and[Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#matching-rules__insights-matching-rules)pages.
- Select the options that apply for the Value source step:

Value source
Parameter Name Description
How will the value be provided? Select one of:
- System provided : Value is populated by the managed system.
- Access bundle definition : Value is populated as part of an access bundle definition.
If you select Access bundle definition then you should enter values for the following additional parameters:
- How should we ask for it? : Enter the text that the user will see when asked for the account attribute value, on requesting the access bundle.
- Any tips to understand what it is? : Enter any help text that explains what the account attribute requested is. This will be displayed below the account attribute field next to the information icon.
- What is the minimum length? : Enter the minimum length of the account attribute value.
- What is the maximum length? : Enter the maximum length of the account attribute value.
- Complete the Review and submit step by checking the information you have provided for this account attribute, and if complete, select Create .
- You can view the full details of the account attribute you created from the Account attributes page, by selecting the View details option from the navigation menu for the account attribute you created.
To edit a simple account attribute :
- Navigate to the Account attributes page for your orchestrated system
- Select the Edit option from the navigation menu for the account attribute you want to edit.
Note  
  
The edit option is only available for user defined account attributes. Default account attributes created as part of the orchestrated system cannot be edited. If you select the navigation menu for a default attribute you will see the message This is a default attribute with restricted edits . The only option you have to edit a default account attribute is to select the option Edit associated identity attribute which allows you to modify the identity attribute which is associated with your default account attribute.
- In the Edit attribute flow, edit any of the values for your attribute.
Note  
  
You can edit any of the configuration values for your account attribute except for the Source attribute name . This value is set at create time and cannot be edited. If you need to change the Source attribute name value for any reason, you are required to delete the account attribute and recreate.
To delete a simple account attribute :
- Navigate to the Account attributes page for your orchestrated system
- Select the Delete option from the navigation menu for the account attribute you want to edit.
Note  
  
The delete option is only available for user defined account attributes. Default account attributes created as part of the orchestrated system cannot be deleted.
- Confirm the deletion.

#### Manage Complex Account Attributes

To create a complex account attribute :

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the navigation menu. to view the configuration of a specific orchestrated system. This displays the configuration page for the selected orchestrated system.
- From the Account settings section of the page, select Manage on the Account attributes tile. This will display the Account attributes page for your orchestrated system, which displays default attributes created when you initialise your orchestrated system, as well as additional account attributes created by the user.
- Click on the Create an attribute button.
- In the Create a new account attribute flow, enter details of your complex account attribute:
- Enter values for the Add details step:

Add details
Parameter Name Mandatory? Description
What is the system attribute name? Yes The attribute name for the account attribute in the associated orchestrated system.
What should AG call it? Yes The name for the account attribute in Oracle Access Governance.
What is the display name? Yes The name for the account attribute when displayed in Oracle Access Governance.
What is the data type? Yes Complex
What kind of complex type? Yes Each orchestrated system can have multiple complex attribute types (Entitlements) such as Role or Group . This dropdown lists any complex attributes that are not included by default, together with an option, Custom which allows you to define your own complex attribute type.

If you select Custom for the complex type:

Which attribute is it uniquely identified by? No The attribute name that uniquely identifies the complex attribute in the orchestrated system that supports the account attribute.

If you select an entitlement such as group or role which is not currently used by any existing complex account attribute for the complex type:

Which attribute should be used for reference? Select the entitlement to use from the list of values displayed. For example, if the Group entitlement is unused, then the user should select the group entitlement attribute such as UID or name from the list of values which defines the reference binding.
- Select the options that apply for the Setup usage step:

Setup usage
Parameter Name Description
Mandatory for account creation Is the account attribute a mandatory value when creating an account.
Included in inbound data from the system Is the account attribute included in inbound data coming from the orchestrated system. If selected, this attribute will be available to inbound transformations.
Populated in outbound data to the system Is the account attribute included in outbound data sent to the orchestrated system. If selected, this attribute will be used to provision and update account values in the orchestrated system.
Supports multiple values For complex attributes this option is set to enabled by default and cannot be changed as complex attributes always support multiple values.
Value is provided after account creation The value will be populated from the orchestrated system after the account has been created.
- Select the options that apply for the Value source step:

No inputs are required for this step for complext attributes. Complex attributes do not have a direct value source. After creation, add child attributes and select value sources for them individually.
- Complete the Review and submit step by checking the information you have provided for this account attribute, and if complete, select Create .
- After selecting to create the attribute you navigate to the Complex attribute page, which allows you to enter details of the child attributes that make up the complex attribute you have created in the previous steps. So, for example, if you created a complex attribute Address , you would create the child attributes for that attribute which might include First address line , Second address line , Postcode . To do this select the Create a child attribute button. Steps are similar to those you have performed for simple attributes:
- Enter values for the Add details step as you would for a simple attribute.
- Select the options that apply for the Setup usage step:

Setup usage
Parameter Name Description
Mandatory for account creation Is the account attribute a mandatory value when creating an account.
The following options are inherited from the parent attribute so the attribute will:
- Be included in inbound data from the system
- Be populated in outbound data to the system
- Not have its value provided after account creation
- Select the options that apply for the Value source step:
Child attribute values are always provided in access bundle definitions, so you should provide the following details on how to present the attribute when requesting an access bundle:
- How should we ask for it? : Enter the text that the user will see when asked for the account attribute value, on requesting the access bundle.
- Any tips to understand what it is? : Enter any help text that explains what the account attribute requested is. This will be displayed below the account attribute field next to the information icon.
- What is the minimum length? : Enter the minimum length of the account attribute value.
- What is the maximum length? : Enter the maximum length of the account attribute value.
- Complete the Review and submit step by checking the information you have provided for this account attribute, and if complete, select Create .
- Repeat this process for all child attributes.
To edit a complex account attribute :
- To edit the complex attribute values you can edit the complex attribute object in the same way you would a simple attribute.
- To edit the child attributes for the complex attribute object you should perform the following:
- On the Account attributes page select the complex attribute for which you want to edit the child attribute values.
- Select the View type link, which is displayed in the type column next to the  

  
label. The child attributes page is displayed.
- Select the Edit option from the navigation menu for the child account attribute you want to edit. Make any changes and save.

To delete a complex account attribute :
- To delete the complex attribute and all its child attributes, you can delete the complex attribute object in the same way you would a simple attribute, by selecting the Delete option from the navigation menu on the Account attributes page.
- To delete child attributes for the complex attribute object you should perform the following:
- On the Account attributes page select the complex attribute for which you want to delete child attributes.
- Select the View type link, which is displayed in the type column next to the  

  
label. The child attributes page is displayed.
- Select the Delete option from the navigation menu for the child account attribute you want to remove. Make any changes and save.

### Setting Up Account Profiles in Oracle Access Governance

You can configure account profiles for your orchestrated system using the Oracle Access Governance Console.

Account profiles in Oracle Access Governance act as reusable templates. They simplify and standardize new user account creation in managed systems by pre-defining default values for their account attributes.

For more information about account profiles, see[Account Profiles - Reusable Templates for Access Bundle Generation](https://docs.oracle.com/en-us/iaas/Content/access-governance/identity-orchestration-components-and-process-flow.htm#account-profiles-reusable-templates-for-access-bundle-generation).
Note  
  
Not all orchestrated systems will display the Account profiles tile. This tile is only shown for orchestrated systems that support account attributes.

- Log in to the Oracle Access Governance Console.
- Click the navigation menu icon, and select Service Administration and then Orchestrated Systems . The Orchestrated Systems page appears that lists the orchestrated systems that you have configured in your Oracle Access Governance service instance.

Once you have reviewed the orchestrated systems in your Oracle Access Governance service instance, you can select a specific orchestrated system and drill down into further information or update various configuration elements.
- Click the icon for the orchestrated system you want to create an account profile, and then select Manage integration .

The configuration page for the selected orchestrated system appears.
- From the Account settings section of the page, click Manage on the Account profiles tile.

The Account profiles page for the orchestrated system is displayed.
- On the Account profiles page, click Create account profile .

The Create a new account profile page is displayed.
- Enter the following information in the Add details section, and then click Next :
- Name: Specify a name for the account profile.
- Description: Specify a description for the account profile.
- Tag: (Optional) – Define tags for the account profile.
- Do the following in the Define profile section, and then click Next :

Account attributes are specific to a managed system. While defining an account profile, you may choose to provide default values or ask the requester to provide values during the self-service request.
- Enter the default values for the account attributes that are mandatory. It’s optional for others.
- Convert the account attributes to a question by clicking the icon, if you are unsure what default value to provide.

When a user requests access using this profile, the system will ask these questions, and the user will be prompted to provide a value for this account attribute during self-service request.
Note  
  
Questions to ask the requestor are not applicable for Role-Based Access Control (RBAC) and Policy-Based Access Control (PBAC) provisioning. Default values are used for any mandatory attributes during provisioning.
- In the Review and submit section, review the details and click Create .

An account profile is created.
