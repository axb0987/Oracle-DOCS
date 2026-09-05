# Managing Oracle Identity Cloud Service Users and Groups in the Oracle Cloud Infrastructure Console
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm
- Fetched: 2026-09-05 02:15 CDT

# Managing Oracle Identity Cloud Service Users and Groups in the Oracle Cloud Infrastructure Console

This topic describes how to use the Oracle Cloud Infrastructure Console to manage your Oracle Identity Cloud Service users and groups. Before you get started, understand basic federation concepts. See[Federating with Identity Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/../Concepts/federation.htm#top).
Important  
  

Oracle Cloud Infrastructure (OCI) Identity and Access Management (IAM) support for managing Identity Cloud Service (IDCS) federated resources through the OCI Console is ending. See the IAM service change announcement[IAM (Service Change Announcements)](https://docs.oracle.com/iaas/Content/servicechanges.htm#servicechanges_topic_IAM).

## Overview of Working with Oracle Identity Cloud Service Users and Groups in the Console

The Oracle Cloud Infrastructure Console provides an integration with Oracle Identity Cloud Service (IDCS) that lets you perform many management tasks for your IDCS users and groups in the Console.

User Management Tasks

In the Console, you can do the following user management tasks:
- Add users
- Remove users
- Add users to groups
- Assign roles to users to access services and instances
- Reset user password

For information on more user management tasks, see[Managing Oracle Identity Cloud Service Users](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/manage-oracle-identity-cloud-service-users1.html)in Administering Oracle Identity Cloud Service .

Group Management Tasks

In the Console, you can do the following group management tasks:
- Add groups
- Remove groups
- Add users to groups
- Map IDCS groups to IAM groups

For information on more group management tasks, see[Managing Oracle Identity Cloud Service Groups](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/manage-oracle-identity-cloud-service-groups1.html)in Administering Oracle Identity Cloud Service .

## Required Policies and Permissions

To manage Oracle Identity Cloud Service users and groups in the Console, you'll need to be granted permissions in both the Oracle Cloud Infrastructure IAM service and in Oracle Identity Cloud Service.

Members of the OCI_Administrators group have the required permissions to create groups and policies in Oracle Cloud Infrastructure.

Important: To create users and groups in the Oracle Identity Cloud Service federation, you'll need the Identity Domain Administrator role, or be a member of a group that has been granted that role. For information on Oracle Identity Cloud Service roles, see[Administering Oracle Identity Cloud Service](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/understand-administrator-roles.html).

To quickly create a user with the required permissions, see[Add a User with Oracle Cloud Administrator Permissions](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingusers.htm#Add).

## Navigating to Your Oracle Identity Cloud Service Users and Groups in the Console

In the Console, you can add users and groups to Oracle Identity Cloud Service from the Identity Provider Details page.

To view your identity provider details:
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation .
- 
Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named OracleIdentityCloudService . The identity provider details page is displayed.

[

From the Identity Provider Details page, select Users to display the users created in Oracle Identity Cloud Service. Select Groups to display the groups created in Oracle Identity Cloud Service.

## Working with Oracle Identity Cloud Service Groups

The Console lets you perform the following tasks to manage groups in Oracle Identity Cloud Service:
- Add groups
- Delete groups
- Edit the name and description
- Add users to groups
- Remove users from groups
- Map groups to Oracle Cloud Infrastructure groups

Some tasks you can't perform in the Oracle Cloud Infrastructure Console. To add the predefined application roles for some Oracle Cloud products, you need to assign roles in the Identity Cloud Service console. For more information about using Oracle Identity Cloud Service, see[Administering Oracle Identity Cloud Service](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/understand-administrator-roles.html).

For the members of a group in Oracle Identity Cloud Service to have permissions in Oracle Cloud Infrastructure, you must map the IDCS group to a group in IAM. Before you set up any new groups in IDCS, ensure that you understand how to assign permissions to groups in Oracle Cloud Infrastructure. See[Overview of Identity and Access Management](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/../Concepts/overview.htm#Overview_of_Oracle_Cloud_Infrastructure_Identity_and_Access_Management).

## Working with Oracle Identity Cloud Service Users

The Console lets you perform the following tasks to manage users in Oracle Identity Cloud Service:
- Add users
- Delete users
- Edit user details
- Add users to groups
- Add roles to users
- Remove users from groups
- Reset user passwords

### User Management Tasks You Can't Perform in the Console

The Oracle Cloud Console does not support management of the following Oracle Identity Cloud Service user features and tasks:
- Manage multifactor authentication

For information about managing these tasks, see[Administering Oracle Identity Cloud Service](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/understand-administrator-roles.html).

## Managing Oracle Identity Cloud Service Groups in the Console

[To create a group in Oracle Identity Cloud Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

This procedure creates a new group in Oracle Identity Cloud Service. Optionally, you can add users to the group at the time you create it. This group will not have any permissions in Oracle Cloud Infrastructure until you map it to an Oracle Cloud Infrastructure group.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation . A list of the federations in your tenancy is displayed.
- 
Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named OracleIdentityCloudService . The identity provider details page is displayed.
- 

Under Resources , select Groups .

The list of existing groups is displayed.
- Select Create IDCS Group .
- 

Enter the following:
- Name: A unique name for the group. Avoid entering confidential information.
- Description: A friendly description. You can change this later if you want to.
- Users: Add Oracle Identity Cloud Service users to this group. You can add users when you create the group, or later. Select users from the list. To find a specific user, you can start typing the user name to filter the list as you type.
- Select Create .

After you create a group in Oracle Identity Cloud Service, you'll want to give the group permissions to user services:
- To grant the group access to map it to an Oracle Cloud Infrastructure group as described in the next procedure.
- To add roles to this group, see[Managing Oracle Identity Cloud Service Roles for Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managinggrouprolesidcs.htm#Managing_Oracle_Identity_Cloud_Service_Roles_for_Groups).

[To map an Oracle Identity Cloud Service group to an IAM group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation .
- 
Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named OracleIdentityCloudService . The identity provider details page is displayed.
- 

Select Edit Mapping .
- In the Edit Identity Provider dialog, select + Add Mapping .
- 

Select the Identity Provider Group you want to map from the list. To find a group without scrolling through the list, you can start typing the group name to filter the list as you type.
- Select the OCI Group you want to map this Identity Cloud Service group to. To find a group without scrolling through the list, you can start typing the group name to filter the list as you type.
- 

To add more mappings, select + Add Mapping and continue adding the mappings.
- Select the group you want to map this group to from the list under OCI Mapped User Group .

Members of this group now have the permissions granted to the OCI Mapped User Group.

[To add roles to a group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

Oracle Cloud Infrastructure services use polices to control access to services. However, some Oracle Cloud services use roles to manage access. This procedure describes how to add roles to an IDCS group.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation . A list of the identity providers in your tenancy is displayed.
- 

Select the Oracle Identity Cloud Service Console link.

The Identity Cloud Service console is displayed.
- 

In the Identity Cloud Service console, expand the Navigation Drawer , and then select Applications .

The list of applications is displayed. Notice that the service that the application corresponds to is displayed underneath the application name. For example, underneath the JAAS application entry, you'll see Oracle Java Cloud Service.
- 

Select the name of the service that you are interested in.

The Details page is displayed.
- 

Select Application Roles .

The roles are displayed.
- 

Select the menu for the role you want to assign and select Assign Groups .
- Select the group you want to assign to the role, and select OK .
- Select the Applications breadcrumb to return to the list of applications.
- Repeat steps 4 through 7 for each role you want to assign to this group.

[To remove roles from a group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation . A list of the identity providers in your tenancy is displayed.
- 

Select the Oracle Identity Cloud Console link.

The Identity Cloud Service console is displayed.
- 

In the Identity Cloud Service console, expand the Navigation Drawer , and then select Applications .

The list of applications is displayed. Notice that the service that the application corresponds to is displayed underneath the application name. For example, underneath the JAAS application entry, you'll see Oracle Java Cloud Service.
- 

Select the name of the service that you are interested in.

The Details page is displayed.
- 

Select Application Roles .

The roles are displayed.
- 

Select the menu for the role you want to remove from the group and select Revoke Groups .
- Select the group you want to remove the role from, and select OK .
- Select the Applications breadcrumb to return to the list of applications.
- Repeat steps 4 through 7 for each role you want to remove from this group.

[To edit details for an Oracle Identity Cloud Service group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation .
- 
Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named OracleIdentityCloudService . The identity provider details page is displayed.
- 

Under Resources , select Groups .

The list of existing groups in the federation is displayed.
- 

Find the group you want to edit and select its name.

The Group Details page is displayed.
- 

Select Edit .
- 

You can update the Group Name or the Description . Avoid entering confidential information.
Caution  
  

Changing the group name will break mappings to Oracle Cloud Infrastructure (OCI) groups. If you change the group name, ensure that you delete any existing group mappings and add new mappings with the new name. See the previous task on editing mappings.
- Select Update to save your changes.

[To add users to a group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation .
- 
Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named OracleIdentityCloudService . The identity provider details page is displayed.
- 

Under Resources , select Groups .

The list of existing groups is displayed.
- 

Find the group you want add a user to.

The User Group Details page is displayed.
- 

Select Add IDCS User .
- Select the user you want to add to this group from the Users list.
- Select Add .

[To remove users from a group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation .
- 
Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named OracleIdentityCloudService . The identity provider details page is displayed.
- 

Under Resources , select Groups .

The list of existing groups is displayed.
- 

Find the group you want to remove the user from.

The list of users is displayed in the Group Details page.
- Find the user you want to remove, and then select the the Actions menu (three dots) .
- 

Select Remove User .
- Confirm when prompted.

[To delete a group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation .
- 
Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named OracleIdentityCloudService . The identity provider details page is displayed.
- 

Under Resources , select Groups .

The list of existing groups is displayed.
- 

Find the group you want to edit and select its name.

The Group Details page is displayed.
- 

Select Delete .
- Confirm when prompted.

[Create a policy to grant the group permissions on Oracle Cloud Infrastructure resources](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

The group you created in Oracle Identity Cloud Service gets permissions to access resources in Oracle Cloud Infrastructure through the policy you assign to the Oracle Cloud Infrastructure group. Before you complete this step, you need to decide what permissions you want to give your new group. For more information, see[Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/../Concepts/policygetstarted.htm#Getting_Started_with_Policies)and[Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/../Concepts/commonpolicies.htm#top).

Prerequisite: The group and compartment that you're writing the policy for must already exist.
- Open the navigation menu and select Identity &amp; Security . Under Identity , select Policies . A list of the policies in the compartment you're viewing is displayed.
- If you want to attach the policy to a compartment other than the one you're viewing, select the desired compartment from the list on the left. Where the policy is attached controls who can later modify or delete it (see[Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/../Concepts/policies.htm#Policy3)).
- Select Create Policy .
- Enter the following:
- Name: A unique name for the policy. The name must be unique across all policies in your tenancy. You cannot change this later. Avoid entering confidential information.
- Description: A friendly description. You can change this later if you want to.
- 

Statement: A policy statement. For the correct format to use, see[Policy Basics](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/../Concepts/policies.htm#Policy)and also[Policy Syntax](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/../Concepts/policysyntax.htm#Policy_Syntax). If you want to add more than one statement, select + .

For example:

To allow your group to manage all resources within a specified compartment enter a statement like the following:

```

```

For more policy examples, see[Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/../Concepts/commonpolicies.htm#top).
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .

## Managing Oracle Identity Cloud Service Users in the Console

After you add a user in Oracle Identity Cloud Service, a user is also automatically provisioned in Oracle Cloud Infrastructure. This provisioned user can have the Oracle Cloud Infrastructure credentials, such as API keys and auth tokens. To understand this provisioning, see[User Provisioning for Federated Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/usingscim.htm#User_Provisioning_for_Federated_Users).

[To create a user](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation .
- 
Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named OracleIdentityCloudService . The identity provider details page is displayed.
- Select Create IDCS User .
- 

In the Create IDCS User dialog enter the following:
- User Name : Enter a unique name or email address for the new user. The value will be the user's login to the Console and must be unique across all other users in your tenancy.
- Email : Enter an email address for this user. The initial sign-in credentials will be sent to this email address.
- First Name: Enter the user's first name.
- Last Name: Enter the user's last name.
- Phone Number: Optionally, enter a phone number.
- Groups: Optionally, select groups to add this user to.
- Select Create User .
Important  
  
For the user to have permissions in Oracle Cloud Infrastructure, you must assign the user to a group that is mapped to an Oracle Cloud Infrastructure group. Or, if you are also creating a new group, you can perform this mapping later. The user will not be able to sign in to the Console until the mapping is accomplished.

The user creation process generates an email that is sent to the address provided that you entered. The email includes the new user's username and password to use with the Oracle Cloud InfrastructureConsole.

To add API keys, auth tokens, customer secret keys, or SMTP credentials for this user, see[Managing User Capabilities for Federated Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusersfederated.htm#Managing_User_Capabilities_for_Federated_Users).

[To edit a user](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation .
- 
Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named OracleIdentityCloudService . The identity provider details page is displayed.
- 

Under Resources , select Users .

The list of existing users is displayed.
- 

Find the user you want to edit and select its name.

The User Details page is displayed.
- 

Select Edit .
- Update the fields.
- Select Save when finished.

[To reset a user's password](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation .
- 
Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named OracleIdentityCloudService . The identity provider details page is displayed.
- 

Under Resources , select Users .

The list of existing user groups in the federation is displayed.
- 

Find the user you want to reset the password for and select the name.

The User Details page is displayed.
- 

Select Reset Password .

The user's password is reset. This user can't access their account until they complete the password reset steps.
- 

Select Email Password Instructions to send the password link and instructions to the user.

The password link is good for 24 hours. If the user does not reset their password in time, you can generate a new password link by selecting Reset Password for the user again.

[To manage roles for services managed through IDCS](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

See see[Managing Oracle Identity Cloud Service Roles for Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managinguserrolesidcs.htm#Managing_Oracle_Identity_Cloud_Service_Roles_for_Users).

[To add API keys, auth tokens, or other Oracle Cloud Infrastructure credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

- 

View the user's details:
- If you're adding credentials for yourself : In the navigation menu , select the Profile menu and then select User settings .
- 

If you're an administrator adding credentials for another user : Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation .
Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named OracleIdentityCloudService . The identity provider details page is displayed.

Find the user in the list and select the OCI Synched User link.
- Add the credentials for the user.

For more details about these credentials, see[Managing User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#top).

[To delete a user](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation .
- 
Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named OracleIdentityCloudService . The identity provider details page is displayed.
- 

Under Resources , select Users .

The list of existing user groups in the federation is displayed.
- 

Find the user you want to delete and select the name.

The User Details page is displayed.
- 

Select Delete .

## Managing Group Mappings

[To add group mappings for Oracle Identity Cloud Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

- 

Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation .

A list of the identity providers in your tenancy is displayed.
- 
Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named OracleIdentityCloudService . The identity provider details page is displayed.
- Select Edit Provider Details .
- 

Add at least one mapping:
- Select + Add Mapping .
- Select the Oracle Identity Cloud Service group from the list under Identity Provider Group .
- 

Choose the IAM group you want to map this group to from the list under OCI Group .
- Repeat the above sub-steps for each mapping you want to create, and then select Submit .

Your changes take effect typically within seconds in your home region. Wait several more minutes for changes to propagate to all regions.

Users that are members of the Oracle Identity Cloud Service groups mapped to the Oracle Cloud Infrastructure groups are now listed in the Console on the Users page. See[Managing User Capabilities for Federated Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusersfederated.htm#Managing_User_Capabilities_for_Federated_Users)for more information on assigning these users additional credentials.

[To update or delete a group mapping](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#)

- 

Open the navigation menu and select Identity &amp; Security . Under Identity , select Federation .

A list of the identity providers in your tenancy is displayed.
- Select the identity provider to view its details.
- Select Edit Mapping .
- Update the mappings (or select the X to delete a mapping), and then select Submit .
