# Deactivating Delegated Authentication
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/delegatedauth/deactivate-delegated-authentication.htm
- Fetched: 2026-09-05 02:20 CDT

# Deactivating Delegated Authentication

Deactivate delegated authentication for a Microsoft Active Directory (AD) Bridge associated with an AD domain. Users transferred into IAM through this bridge must use their IAM passwords to authenticate into the identity domain.
By deactivating delegated authentication, you can verify that the AD credentials from a user in that domain can be used to sign in to IAM before activating delegated authentication for the bridge.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- Select Security .
- Select Delegated Authentication .
- Expand the node to the right of the AD Bridge for which you want to deactivate delegated authentication.
- Turn off the Activate Delegated Authentication switch.
- In the Deactivate Delegated Authentication window:
- Select the Send a Password Reset Notification (recommended) option if you want users in the AD domain associated with the AD bridge to receive notifications to reset the passwords for their accounts. This is recommended for security purposes.
- Select the Create a Password option if you want to manually reset passwords for the users in the domain associated with the bridge. No notification is sent to users. Selecting this option means that the users in the domain, who were previously able to sign in using delegated authentication, can't sign in to the system. To allow them to sign in to the system, reset their passwords by using the reset passwords option on the Users tab. See[Resetting a User Password](https://docs.oracle.com/en-us/iaas/Content/Identity/delegatedauth/../users/reset-passwords-user-accounts.htm).
-
