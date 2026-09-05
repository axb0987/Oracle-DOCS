# Setting Permissions for Delegated Authentication
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/set-permissions-delegated-authentication.htm
- Fetched: 2026-09-05 02:24 CDT

# Setting Permissions for Delegated Authentication

Set permissions for your Microsoft Active Directory domain administrator account so that you can configure delegated authentication for the AD bridge.

- Open Active Directory Users and Computers .
- Right-click the user, group, or organizational unit (OU) that you want to delegate, and then select Delegate Control .
- On the Delegation of Control wizard, select Next , and then select Add .
- On the Select Users, Computers, or Groups dialog box, in the text area, enter the username or group name that needs to be granted permissions to configure delegated authentication.
- Select Check Names to verify that the user or group has been created in AD. If it hasn't been created, then create it.
- Select OK , and then select Next .
- Select the Delegate the following common tasks option, and then select Reset user passwords and force password change at next logon .
- Select Next , and then select Finish .
The next steps explain how to set specific permissions to lock and unlock user accounts.
- Right-click on the newly modified user or group, and select Properties .
- Select the Security tab, select Advanced .
- On the Advanced Security Settings, select Add .
- On the Permission Entry wizard, select Select a principal , and enter the same username or group name that has been granted reset permission.
- Select OK .
- In the Applies to field, select Descendant User objects .
The list of permissions permitted for the user account (Principal) is displayed.
- Scroll down and enable Read lockoutTime , and Write lockoutTime .
- Select OK and continue to select OK until the end of the setup.
