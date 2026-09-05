# Adding a Rule to a Sign-On Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/add-more-rules-policy.htm
- Fetched: 2026-09-05 02:29 CDT

# Adding a Rule to a Sign-On Policy

Add a rule to an identity domain sign-on policy in IAM.

- On the Sign-on policies list page, select the sign-on policy that you want to add a rule to policy. If you need help finding the list page, see[Listing Sign-On Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/list-signon-policy.htm).
- On the sign-on policy details page, select Add sign-on rule .
- Set the following parameters:

- Rule name : Enter the name of the sign-on rule.
- Authenticating identity provider (Optional): Enter or select all identity providers used to authenticate the user accounts evaluated by this rule. If you leave this empty, the other conditions are used for authentication.
- Group membership : Enter or select the groups that the user must be a member of to meet the criteria of this rule. You must enter at least three characters to begin a search of groups.
- Administrator : If the user must be assigned to administrator roles in the identity domain to meet the criteria of this rule, then select this checkbox.
- Exclude users : Enter or select the users to exclude from the rule. You must enter at least three characters to begin a search of users.
- Filter by client IP address : Filter by: Anywhere or Restrict to the following network perimeters .
- 

Anywhere : All sign-in requests will match the criteria of this rule irrespective of the IP address, Country, VCN.
- 

Restrict to the following network perimeters : Sign-in requests will match the criteria of this rule only if the requests originate from any of the selected Network Perimeters. For more information, see[Managing Network Perimeters](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/../networkperimeters/overview.htm)and[Creating a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/../networkperimeters/add-network-perimeter.htm).
- Allow access or Deny access : Select whether a user can access the Console if the user account meets the criteria of this rule. When you select Allow access , the more options are presented.
- Prompt for reauthentication : Select this checkbox to force the user to sign in to the identity domain again. If not selected, the user will be authenticated the next time they sign in to the identity domain.
- Prompt for an additional factor : Select this checkbox to prompt the user for another factor to sign in to the identity domain. If you select this checkbox, then you must specify whether the user is required to enroll in multifactor authentication (MFA) and how often this additional factor is to be used to sign in. Select Any factor to prompt the user to enroll and verify any factor enabled in the MFA tenant level settings. Select Specified factors only to prompt the user to enroll and verify a subset of factors enabled in the MFA tenant level settings. After you select Specified factors only , you can select factors that must be enforced by this rule.
- Frequency :
- 

Select Once per session or trusted device , so that for each session that the user has opened from an authoritative device, they must use both their usernames and passwords, and a second factor.
- 

Select Every time , so that each time users sign in from a trusted device, they must use their user names and passwords, and a second factor.
- 

Select Custom interval , and then specify how often users must provide a second factor to sign in. For example, if you want users to use this additional factor every two weeks, then select Number , enter 14 in the text field, and then select the Interval drop-down menu to select Days . If you configured multifactor authentication (MFA), then this number must be less than or equal to the number of days a device can be trusted according to MFA settings. For more information, see[Managing Multifactor Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/../mfa/understand-multi-factor-authentication.htm).
- Enrollment : This menu contains two options: Required and Optional .
- 

Select Required to force the user to enroll in MFA.
- 

Select Optional to give users the option of skipping enrolling in MFA. Users see the inline enrollment setup process after they enter their username and password, but can select Skip . Users can then enable MFA later from the 2–Step Verification setting in the Security settings of 'My profile.' Users aren't prompted to set up a factor the next time that they sign in.

Note: If you set Enrollment to Required , and later change it to Optional , the change only affects new users. Users already enrolled in MFA will not see the inline enrollment process and will not be able to select Skip when signing in.
- Select Add sign-on rule .

Note  
  
If you have added multiple sign-on rules to this policy, then you can change the order that they will be evaluated. See[Changing the Priority of a Rule for a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/change-priority-sign-rule-policy.htm)
