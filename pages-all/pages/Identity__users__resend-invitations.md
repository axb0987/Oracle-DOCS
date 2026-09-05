# Resending an Invitation to a User to Activate their Account
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/users/resend-invitations.htm
- Fetched: 2026-09-05 02:30 CDT

# Resending an Invitation to a User to Activate their Account

Resend an invitation to a user so that they can activate their user account in an OCI IAM identity domain.

After a user account is created, it must be activated before it can be used. A welcome email is sent to the user, inviting them to activate the account. The invitation is valid for a set time period designated in the[email configuration tab](https://docs.oracle.com/en-us/iaas/Content/Identity/users/../mfa/configure-email-settings.htm)of the two-factor authentication preferences.

If the user account isn't activated after the designated time period, then the identity domain administrator can send another invitation to the user to activate the account.

You can't resend an invitation to a user who has already activated their account, or whose account is inactive. In these cases, Resend invitation is unavailable. Reactivating an account will automatically send a new email invitation.

If you select several users and select Resend invitation , a confirmation message tells you how many users were sent the invitation and that other selected users are either verified or inactive.

- On the Domains list page, select the domain for which you want to resend invitations. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/users/../domains/to-view-identity-domains.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the User management tab, and then go to the User section of the tab.
- Under Identity domain on the left side of the page, select Users .
- On the details page, select the checkbox of each user account to which you want to resend an invitation.

Tip  
  
To send invitations to all user accounts, select the checkbox in the header row of the Users table to select all.
- Depending on the options you see, select either the Actions or More actions button, and then select Resend invitation .
-
