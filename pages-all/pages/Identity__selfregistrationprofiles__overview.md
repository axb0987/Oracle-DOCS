# Overview of Self-Registration Profiles
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/overview.htm
- Fetched: 2026-09-05 02:28 CDT

# Overview of Self-Registration Profiles

Use self-registration profiles to create accounts in a verified or unverified state. Customize the self-registration process by specifying the user's email domains allowed when self-registering, and adding header, footer, success, and user consent text.

## Introduction

Using self-registration profiles, you can:

- 

Create a self-registration consumer flow that allows users to create an account in a verified state. Use the REST API to turn off the`activationEmailRequired`option. The user can then directly sign in using a username and password to authenticate.
- Create a self-registration partner flow that allows users to create an account in an unverified state. Use the REST API to turn on the`activationEmailRequired`option so that a user receives a link in the welcome email to verify the user. After the user selects this link, the user's state is changed to verified and the user can sign in.
- 

Delete profiles using the user interface or the REST API.
- 

Specify whether users are prompted and must accept a user consent before self-registering.
- 

Assign groups to a profile so that users are assigned to all the groups that are part of that profile.
- 

Specify the user's email domains allowed when accessing the self-registration process. Only users with access to these specific email domains are allowed to register.
- 

Customize the self-registration sign in page with your header and footer logos.
- 

Customize the header, footer, success, and user consent text.

This section contains the following topics:
- [Listing Self-Registration Profiles](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/list-self-registration-profiles.htm)
- [Creating a Self-Registration Profile](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/create-self-registration-profiles.htm)
- [Constructing a Self-Registration URL](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/construct-self-registration-url.htm)
- [Activating a Self-Registration Profile](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/activating-self-registration-profiles.htm)
- [Updating a Self-Registration Profile](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/editing-self-registration-profiles.htm)
- [Deactivating a Self-Registration Profile](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/deactivating-self-registration-profiles.htm)
- [Deleting a Self-Registration Profile](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/deleting-self-registration-profiles.htm)

## Required Policy or Role

To create self-registration profiles, you must have one of the following access grants:
- Be a member of the Administrators group
- Be granted the Identity Domain Administrator role
- Be a member of a group granted`manage`domains

To understand more about policies and roles, see[The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/../getstarted/identity-domains.htm#The),[Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/../roles/understand-administrator-roles.htm), and[IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/../policieshow/Policy_Basics.htm)
