# Configure Integration Between Oracle Access Governance and Oracle Cloud Infrastructure (OCI)
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/oci-iam-ociintegration.htm
- Fetched: 2026-09-05 03:15 CDT

# Configure Integration Between Oracle Access Governance and Oracle Cloud Infrastructure (OCI)

You can establish a connection between Oracle Cloud Infrastructure Identity and Access Management (OCI IAM) and Oracle Access Governance as an authoritative source and as a managed system. To achieve this, use the Orchestrated Systems functionality available in the Oracle Access Governance Console.

The OCI Orchestrated System supports the following modes and both included, by default:
- Authoritative Source : You can use OCI as an authoritative (trusted) source of identity information for Oracle Access Governance.
- Managed System : You can manage OCI IAM groups and application roles, including certifying policies and group membership using Oracle Access Governance. See[Supported Operations for Oracle Cloud Infrastructure (OCI)](https://docs.oracle.com/en-us/iaas/Content/access-governance/oci-iam-ociintegration.htm#supported-operations-for-provisioning-to-oracle-cloud-infrastructure-oci).

Note  
  
Earlier releases of Oracle Access Governance used API Key Access to connect with OCI IAM. This method is now deprecated and is replaced with Resource Principal Access. Details of how to setup a new orchestrated system using this method is provided in[Configure Integration with OCI IAM](https://docs.oracle.com/en-us/iaas/Content/access-governance/oci-iam-ociintegration.htm#oci-iam-configure-integration-ociiam). If you have existing orchestrated systems using the deprecated API Key Access you should migrate to the new method by following the instructions in[How To Migrate API Key Access To Resource Principal Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/oci-iam-ociintegration.htm#oci-iam-rpmigration).

## Terminology

Before configuring integration of Oracle Access Governance with OCI IAM you should have an understanding of the following terms:

Terminology
Term Description
OCI Orchestrated System Represents an OCI tenancy integrated with Oracle Access Governance.
Requesting Tenancy Tenancy of the Oracle Access Governance Service Instance that needs to access OCI IAM API in the same or a different tenancy to retrieve/update IAM entities being governed.
Responding Tenancy Customer tenancy where OCI IAM identity data is present.
Intra Tenant Access Use case when you have a single OCI tenancy acting as Requestor and Responder.
Cross Tenant Access Use case when you have multiple OCI tenancies, and the Requesting Tenancy is a separate instance from the Responding Tenancy.
Resource Principal A principal type in OCI IAM that eliminates the need to create and manage OCI User credentials for integration access.

## Prerequisites

Before you can establish a connection, you need to create OCI policies that allow your orchestrated system to access the OCI instance you want to integrate with.

### General Requirements

General prerequisites required to integrate Oracle Access Governance with OCI IAM include:

- Your cloud account must use Identity Domains to manage identities on OCI.
- As a cloud administrator, you must be able to manage policies in the root compartment of your tenancy.
- If the responding OCI Tenancy being governed is outside the region of the requesting Oracle Access Governance Service Instance, then it must subscribe to a tenancy residing in the region of the requesting Oracle Access Governance Service Instance.

### How Oracle Access Governance Connects With Target OCI IAM Instances

In order to integrate Oracle Access Governance with OCI IAM orchestrated systems, you need to configure a connection using the OCI IAM API and Resource Principal authentication. Resource principal is a principal type in OCI IAM that eliminates the need to create and manage OCI user credentials for integration access. In order to configure resource principal authentication you need to generate and deploy a set of policies to the tenancy or tenancies involved in your orchestrated system. The placement of these policies is explained in the following diagrams:

#### Policy Placement when Oracle Access Governance Service Instance (Requester) and OCI Tenancy (Responder) being governed are in the same tenancy
You can have a use case where a single OCI tenancy performs both of the following functions:
- Host tenancy on which the Oracle Access Governance Service Instance resides. This is the requesting tenancy which needs to access the OCI IAM API from a responding tenancy, so that data can be retrieved/updated for the identities that are being governed.
- Tenancy where OCI IAM identity data is present.

In this use case you only have to deploy the generated policies to the one tenancy. They will cover the access required for the tenancy as both requestor and responder.

#### Policy Placement when Oracle Access Governance Service Instance (Requester) and OCI Tenancy (Responder) being governed are in different tenancies
You can also have a use case where the requesting tenancy and responding tenancy reside on separate OCI tenancies. In this case, you need to deploy policies on the relevant tenancy depending on their function:
- Policies relevant to the requesting tenancy should be deployed to the OCI where your Oracle Access Governance Service Instance resides.
- Policies relevant to the responding tenancy should be deployed to the tenancy where your OCI IAM identity data is present.

### How To Setup Required Policies For OCI IAM Integration With Oracle Access Governance

Before you can establish a connection, you need to create OCI policies that allow your orchestrated system to access the target system.

To setup the required policies for integration of OCI IAM with Oracle Access Governance you need to perform the following steps:
- Obtain the policy statements generated in the Integration Settings of your orchestrated system. Depending on the use case this may be a single set of statements for a Single Tenancy integration, or two sets of statements for an AG Service Instance/External Tenancy setup. The policies for your specific configuration are generated based in information you provide during the creation of your orchestrated system, details of which are provided in[Configure Integration with OCI IAM](https://docs.oracle.com/en-us/iaas/Content/access-governance/oci-iam-ociintegration.htm#oci-iam-configure-integration-ociiam)for the Integration Settings dialog. Ensure that you copy the statements exactly as they are shown in the Integration Settings.
- [Create the policies](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm)in the root compartment of the relevant tenancy.

## Configure Integration with OCI IAM

Integration with Oracle Cloud Infrastructure Identity and Access Management (OCI IAM) is achieved by configuring a new orchestrated system with the Oracle Access Governance Console.

### Navigate to the Orchestrated Systems Page
Navigate to the Orchestrated Systems page of the Oracle Access Governance Console, by following these steps:
- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Add an orchestrated system button to start the workflow.

### Select system

On the Select system step of the workflow, you can specify which type of application you would like to onboard.
- Select Oracle Cloud Infrastructure .
- Click Next .

### Enter details
On the Enter Details step of the workflow, enter the details for the orchestrated system:
- Enter a name for the system you want to connect to in the What do you want to call this system? field.
- Enter a description for the system in the How do you want to describe this system? field.
- Click Next .

### Add owners
You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

### Account settings
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

### Integration settings

On the Integration settings step of the workflow, enter the configuration details required to allow Oracle Access Governance to connect to the system.
- Enter the following configuration settings:

Field Description
What is the OCID of the OCI tenancy being integrated? Enter the OCID for the responding tenancy. For further information regarding OCIDs see[Oracle Cloud Identifier](https://docs.oracle.com/iaas/Content/GSG/Concepts/concepts-account.htm#gsg-concepts-ocid),[OCID Syntax](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle), and[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).
Note  
  
Use a unique tenancy for each orchestrated system.
What is the OCI tenancy's home region? Enter the home region for the target OCI tenancy, using the region identifier. The region identifier for your home region can be found in[Regions](https://docs.oracle.com/en-us/iaas/Content/access-governance/set-up-service-instance.htm), the identifier for US East (Ashburn) is`us-ashburn-1`. See[The Home Region](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm#The), and[How do I find my tenancy home region?](https://docs.oracle.com/iaas/Content/GSG/Reference/faq.htm#How).
Include all domains as an authoritative source Select the check box to include all available domains as a trusted source of identity data and identity attributes.
Which domain names should be included as an authoritative source? Select the domains which should act as trusted source of identity data and identity attributes.
Include all domains when managing permissions Select the check box to include all domains for provisioning and managing accounts.
Which domain names should we manage permissions for? Select the domains for which you want to manage permissions and perform provisioning operations.
Do you want to exclude resources and policies from the data load? Select this to include only accounts and permissions (groups and roles). This won't ingest resources and policies and you can't manage these from Oracle Access Governance.
Note  
  
You won't be able to see any policy or resource associated with an identity in the Enterprise-wide Browser page.
Required OCI Policies? Copy the exact statements in the root compartment of the relevant tenancy. Further details on the required policies can be found in[How Oracle Access Governance Connects With Target OCI IAM Instances](https://docs.oracle.com/en-us/iaas/Content/access-governance/oci-iam-ociintegration.htm#oci-iam-rpprereqconnectoverview). See[Managing Policies](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm)to apply the policies to your tenancy.
- Click Add .

### Finish Up
Finally, you are given a choice whether to further configure your orchestrated system before running a data load, or accept the default configuration and initiate a data load. Select one from:
- Customize before enabling the system for data loads
- Activate and prepare the data load with the provided defaults

## How To Migrate API Key Access To Resource Principal Access

If you have existing OCI orchestrated systems that use the API Key access method to connect, then you should migrate at your earliest convenience to Resource Principal access method. While the API Key access method will continue to function, no edits to the existing configuration can be made. The API Key access method will, in time. be deprecated and Resource Principal is the required method moving forward.
In order to migrate from API Key access to Resource Principal access you should complete the following tasks:
- Navigate to the Integration settings page following the instructions given in[Configure Orchestrated System Integration Settings](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-orchestrated-system-integration-settings).
- On the Integration settings page you will see a deprecation warning if the orchestrated system is using the API Key access method. To initiate the migration process click on the Learn more about migrating button. The policies required to update your OCI tenancies to use Resource Principal access will be displayed and should be copied and applied exactly as generated. Further details on the required policies can be found in[How Oracle Access Governance Connects With Target OCI IAM Instances](https://docs.oracle.com/en-us/iaas/Content/access-governance/oci-iam-ociintegration.htm#oci-iam-rpprereqconnectoverview). See[Managing Policies](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm)for details on how to apply the policies to your tenancy.
- Once you have applied your policies, click the Test integration button to check the connection. If you have any errors or messages, review your configuration. You will not be able to complete the migration until the test is successful.
- If your connection is confirmed then click on the Migrate button to start the migration.
- When the migration completes, you will see a message confirming that the integration is now using the required access method.
Note  
  
Once you have completed migration to the Resource Principal method you cannot reverse the procedure and reinstate API Keys method on your orchestrated system.

## Supported Configuration Modes for OCI IAM

Oracle Access Governance integrations can be setup in different configuration modes depending on your requirement for on-boarding identity data, and provisioning accounts.

OCI IAM Orchestrated System supports the following mode:
- Authoritative Source

You can choose OCI IAM domains as a trusted source of identity data and identity attributes in Oracle Access Governance. The domains selected as Authoritative Source would be used for building a composite identity profile. For more details, see[Manage Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm).
- Managed System

You can manage OCI accounts, IAM groups, application roles, policies, and resources from Oracle Access Governance. The domains selected as Managed Systems would only be used for provisioning activities, such as managing identity lifecycle, executing access reviews, setting up access controls, and so on.

## Supported Operations for OCI

The Oracle Cloud Infrastructure Orchestrated System supports the following account operations when provisioning an identity.
- Configure Orchestrated System

See[Configure Integration with OCI](https://docs.oracle.com/en-us/iaas/Content/access-governance/oci-iam-ociintegration.htm#oci-iam-configure-integration-ociiam).
- [Load Data](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-load-data)

Ingest accounts that can be managed by Oracle Access Governance.
- [Match Identity and Account Attributes using Correlation Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#match-identity-and-account-attributes-using-correlation-rules)

Review or configure matching rules to match the identity and account data and build a composite identity profile. To view the default matching rule for this orchestrated system, see[Default Matching Rules](https://docs.oracle.com/en-us/iaas/Content/access-governance/oci-iam-ociintegration.htm#oci-iam-default-matching-rules).
- [Create Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-create-account)

Ingest account data from your orchestrated system or request an access for an identity. This allows you to provision entitlements.
- [Delete Account](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#delete-account-managed-by-oracle-access-governance)

Delete an account associated with an identity. This removes the access for the account. Delete workflow is also triggered when the`status`identity attribute ingested from an Authoritative source is set to null . For more details, see[Manage Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm).
- Update account details by[assigning](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-assign-permissions)or[removing](https://docs.oracle.com/en-us/iaas/Content/access-governance/oracle-access-governance-integration-functional-overview.htm#integration-overview-remove-permissions)permissions.
- Assign OCI IAM Groups
- Remove OCI IAM Groups
- Assign Application Roles
- Remove Application Roles

### Edit User Capabilities with OCI Account Profile

Configure account profile for your OCI IAM - Managed System to edit user capabilities from Oracle Access Governance Console. You can set capabilities, such as API keys, Auth token, SMTP credentials, Customer secret keys, OAuth 2.0 client credentials, and Database passwords

You can edit user capabilities during create account or an update account event. To do so:

- Create Account Profiles : First, set up the account profile required for provisioning users from Oracle Access Governance to the OCI IAM domain set as a managed system. See[Setting Up Account Profiles in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-setting-up-account-profiles-in-oracle-access-governance).
- Configure the user capabilities account attributes in the account profile.
- Create an access bundle for your OCI IAM orchestrated system and associate the account profile. See[Create Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm).
- Raise a self-request or request access for another identity. See[Request Access to a Resource](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm#request-access-to-a-resource).
- After approval, verify the changes in the activity log:
- For Create or Update account activity, select View details .
- Under the Account Data section, you can view the provisioned user capabilities as per configured account profile.

## Default Matching Rules

In order to map accounts to identities in Oracle Access Governance you need to have a matching rule for each orchestrated system.

The default matching rule for the OCI IAM orchestrated system is as follows:

Default Matching Rules
Mode Default Matching Rule
Identity Matching

Identity matching checks if incoming identities match with existing identities or new.

Screen value :

`Employee user name = Employee user name`
Account Matching

Account matching checks if incoming accounts match with existing identities.

Screen value :

`User login = Employee user name`

## Functional Overview: Use Cases Supported for OCI Integration

OCI IAM integration supports management of OCI accounts from Oracle Access Governance:

### Use Case Provisioning Examples

### Group Provisioning - Assign Groups to Users

Assign multiple OCI IAM groups for an OCI domain from Oracle Access Governance. For example, you can provision developers working on multiple projects to different OCI IAM resources, each group associated with specific resources.
To do this:
- Create an access bundle for the OCI orchestrated system and select the OCI IAM groups available in the domain. For details, see[Create Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm).
- To assign users in OCI with OCI groups:
- Create an Oracle Access Governance policy and associate the groups part of the access bundle with identity collection in that policy. For details, see[Manage Policies](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm)and[Create Identity Collections](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-collections.htm).
- You may also request access bundles or roles directly by raising a request from the self service flows. For details, see[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm).

Certify identity access reviews for the groups granted through access request by Oracle Access Governance. For more information, see[Eligible System Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#eligible-system-oracle-cloud-infrastructure).

### Application Role Provisioning - Assign RolesUsing Oracle Access Governance, you can provision OCI application roles to OCI identities for services running in an OCI domain. You can even use this to provision Oracle Access Governance roles to other identities. For example, you can package relevant Oracle Access Governance application roles and provision the access bundle to an IAM Specialist group.
- Create an access bundle for the OCI orchestrated system and select application roles for services available in the domain. For details, see[Create Access Bundle](https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm).
- To assign users in OCI with application roles:
- Create an Oracle Access Governance policy. Associate access bundles comprising application roles with an identity collection in that policy. For details, see[Manage Policies](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-policies.htm)and[Create Identity Collections](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-collections.htm).
- You may also request this access bundle or role directly by raising a request from the self service flows. For details, see[Request Access](https://docs.oracle.com/en-us/iaas/Content/access-governance/request-access.htm).

You may further certify identity access reviews for the roles granted through access request by Oracle Access Governance. For more information, see[Eligible System Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#eligible-system-oracle-cloud-infrastructure).

### OCI Policy Reviews : Revoke Over-privileged Policy Statements from OCI Policies

Using Oracle Access Governance, you can certify OCI policies by creating on-demand policy review campaigns from the Oracle Access Governance Console. For example, you may run quarterly reviews on the defined network and storage policy of your tenancy to assess if these meet the principle of least privilege and applicable regulatory requirements.

Create a policy review campaign for OCI policies. Based on the prescriptive insights and recommendations, reviewers can make informed decision to either Approve or Reject entire policy at once, or make decision to Approve or Reject specific policy statement in that policy.

For more information, see[Review Access to Systems Managed by Oracle Cloud Infrastructure (OCI)](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#eligible-system-oracle-cloud-infrastructure)and[Create Policy Review Campaigns](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-policy-review-campaigns.htm).

### Group Membership Reviews: Accept or Revoke Membership Access from OCI IAM Group

Using Oracle Access Governance, you can certify membership for OCI IAM groups by creating on-demand Identity Collection Review campaigns. For example, you may run group membership reviews to certify that only eligible members are part of the Database Administrator group, managing and maintaining the database infrastructure for your project. An identity with the Sales Analyst role should not be associated with this group.

Create an identity collection review campaign for OCI IAM Groups. Based on the prescriptive insights and recommendations, reviewers can make informed decision to either Approve or Revoke members of the group. If you choose to review OCI IAM groups and it contains a few members provisioned from Oracle Access Governance , then with this review, you can only accept or revoke directly assigned members. For members provisioned from Oracle Access Governance, choose to review the OCI Access Bundles using the Which permissions? tile. For more information, see[Review Access to Systems Managed by Oracle Cloud Infrastructure (OCI)](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#eligible-system-oracle-cloud-infrastructure)and[Create Identity Collection Review Campaigns](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-identity-collection-review-campaigns.htm)
