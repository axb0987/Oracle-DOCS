# Create an Access Bundle
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/bundle-create-access-bundle.htm
- Fetched: 2026-09-05 03:13 CDT

# Create an Access Bundle

An Access Bundle is a collection of permissions that package access to resources, application features, and functionality into a requestable unit. Each access bundle can be associated with only one orchestrated system.

## Overview

With Access Bundles, you need not grant access to each permission individually but can request the access bundle for that resource. This simplifies the process of provisioning accounts with resource permissions.
Example : You can create an access bundle for developers using the target application Oracle Apex. You could call this bundle Apex Developer Access , and select Read, Edit, and Create permissions required for a developer to use the application. When a developer in your organization needs to request developer access to Apex, they only need to request the bundle, not the three individual permissions. You can auto-assign them these permissions through Oracle Access Governance policies.

### Manage Accesses using Oracle Access Governance Access Bundles

You can manage groups for Microsoft Entra ID (formerly Azure Active Directory) and Microsoft Active Directory.
Oracle Cloud Infrastructure (OCI) orchestrated system
For domains managing permissions, permissions are packaged as OCI IAM groups and application roles. You can achieve:
- Group Assignment : Bundle OCI IAM groups in an access bundle, which can then be assigned to identities through a policy or an access request.
- Application Role Assignment : Bundle OCI cloud services application roles in an access bundle, which can then be assigned to identities through a policy or an access request.

## Navigate to Access Bundle

To navigate to the Access Bundle page:

- Sign in to the Oracle Access Governance Console with a user assigned either with the Administrator or Access Control Administrator application role.
- You can select one of the following options to navigate to the Access Bundle page:
- Select the navigation menu icon, and select Access Controls &gt; Access Bundles .
- On the Console home page, select the Access Controls tab and then select the Select button on the Manage Access Bundles tile.
Whichever option you select, you will be navigated to the Access Bundle page, where you can create, view and manage access bundles.
- To create a new access bundle, select the Create an access bundle button. The Create a new access bundle page is displayed.

## Bundle Settings

In the Bundle settings task, you can enter general settings about your access bundle. You are also able to add user friendly tags that can be used in a search for this access bundle when creating policies.

- Select the orchestrated system in the Which system is this bundle for? field.
You will see the applications available for selection, dependent on the data ingested from your integrated systems.
- [OCI-only] Select domain in the Which domain? field from which you want to select application roles or OCI IAM groups.
- [OCI-only] In the Which type of permission? field, select any one:
- Application role : To package OCI application roles in an access bundle and assign it to identities.
- Group access : To package and assign OCI IAM groups in an access bundle.
You cannot combine Application role and Group access in a single access bundle. You may create a role in Oracle Access Governance and associate two separate access bundles with it. These can then either be requested through self service flows or provisioned through Oracle Access Governance policies. For details, see[Manage Roles](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-roles.htm).
- Select who can request this bundle from the available choices:
- Anyone : Any identity can request the access to this access bundle.
- No one : The access bundle can only be assigned by an Administrator through policies. You cannot request access to this access bundle through self service flows.
- Members of organization : Only members of specific organizations can request access to this bundle through self service flows. For additional details about managing Oracle Access Governance Organization, see[Create and Manage Organizations](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#create-and-manage-organizations).
- For Members of organization , select one or more organization names that can request access to this access bundle.
- Select the appropriate approval workflow in the Which approval workflow should be used? field.
The displayed list is based on the custom approval workflows created in the Oracle Access Governance Console. For more information, see[Create an Approval Workflow](https://docs.oracle.com/en-us/iaas/Content/access-governance/create-approval-workflow.htm).
Note  
  
If you have selected No one , then this field will be disabled as the access bundles can be provisioned using policies.
- Primary Business approver : Select a user to review and approve access requests based on business needs. This role grants approval responsibility only and doesn't provide ownership or management of access resources. See[Business Approvers](https://docs.oracle.com/en-us/iaas/Content/access-governance/workflow-approval-workflow-overview.htm#workflow-approval-workflows-types__business-approver).
- Who else can be business approver : Select one or more business approvers to approve the task.
- Select the Auto-approve requests without Access Guardrail or SoD violations checkbox to trigger selected approval workflow only when an access request results in a violation against an access guardrail or Segregation of Duties (SoD), else request gets auto-approved.
- Select one or more tags for this access bundle in the Would you like to add any tags? field. Examples might include`General-org`,`Database Admin`, or similar.
- In the Select an access guardrail required to allow access list, select the appropriate access guardrail to enforce access separation of duties or constraints for the access bundle. For more information, see[Access Guardrails - Enforcing Preventive Access Control Constraints](https://docs.oracle.com/en-us/iaas/Content/access-governance/enforce-preventive-access-control-conditions.htm).
- Select Next .

## Select Permissions

In the Select Permissions task, you can select permissions to include in this access bundle. Based on the orchestrated system, you might see additional attributes required for account provisioning. Refer to the specific orchestrated system articles to know more about the default attributes. For OCI, you can select OCI IAM groups or application roles.

- Select one or more permissions associated with the target application. Alternatively, you can use the Search field to locate the required permission or role.
- Select Next .

## Add Primary and Additional Owners

You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
For assigning resource ownership, you must have active Oracle Access Governance users. When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section.
No special application roles are necessary for assigning resource ownership. Any Oracle Access Governance active user can be assigned as the owner of the resources. All the owners can read, update, or delete the resources that they own. However, the Primary Owner is assigned as the access reviewer when you choose the Owner template in the approval workflow for performing Ownership reviews in Campaigns. For more information, refer[Types of Access Reviews Offered by Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/access-reviews-overview.htm#types-of-access-certifications).

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the action menu for the orchestrated system you want to configure. This displays the manage integration page for the selected orchestrated system.
- From the System settings section of the page, select Manage on the Ownership settings tile. This will display the Ownership settings page for the selected orchestrated system.
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource.
You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

## Time Limit Access

Set an expiration period to limit access by days or hours. You can also allow users to request an extension before access is revoked upon expiry. Time-bound access ensures identities have access only for the required period, enhancing security.
Time-bound access applies only to self-service access requests and does not apply when access is granted through a policy.

- How long should access be granted? : Select one of the following:
- Indefinitely : Allows permanent access with no time limits. Access is recoked only if manually revoked or the account is disabled.
- Maximum number of days [1-365] : Enter the maximum number of days to grant access. Access will be revoked after this period.
- Maximum number of hours [1-24] : Enter the maximum number of hours to grant access. Access will be revoked after the specified hours.
- How many days/hours before expiration should we send a notification? : Based on your selection of days or hours for access, enter the number of days or hours before expiry to send an email notification to the user.
- What is the maximum extension days/hours allowed? : Based on your selection of days or hours for access, enter the maximum number of days/hours allowed for an extension after access expires. If allowed, identities can raise a self-service access extension request from the My Access page.

- If the access bundle is time-bound, the extension period is determined by the access bundle’s configuration.
- If the access bundle is indefinite, extensions are allowed for up to 90 days by default.
- Which approval workflow should be used for extension requests? : Select the appropriate approval workflow to be used to approve extension request.

## Add Details

In this Add Details task, you can give a name to your access bundle, add a supporting description, and attach an account profile.
- Enter name for your access bundle in the Name field.
- Add a description for your access bundle in the Description field.
Note  
  
The other fields on the screen depends on the target type and permissions selected in the previous tasks.
- Select one of the following actions for the Do you want to use an account profile? field. For more information see,[Setting Up Account Profiles in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-setting-up-account-profiles-in-oracle-access-governance).
- Yes : Select an account profile from the Which account profile? list.
- No : Enter values in the other fields that appear depending on the managed system.
- Click Next to go to the Review and submit task.

## Review and Submit

The Review and Submit task displays the information you have added in the previous tasks.
If everything looks correct, then click Create to create the access bundle. You may select addition actions:
- Cancel : To cancel the process.
- Back : To go back to the previous step.
-
