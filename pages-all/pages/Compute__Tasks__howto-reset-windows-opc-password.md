# How-to: Reset the Windows OPC Password
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/howto-reset-windows-opc-password.htm
- Fetched: 2026-09-05 01:51 CDT

# How-to: Reset the Windows OPC Password

To reset the Oracle Public Cloud (OPC) password on Windows, you can use the OS Safe Mode feature and complete the steps on this page.
Note  
  
Before you complete the steps on this page, you must create a VNC (Virtual Network Computing) Console connection so that you can boot the OS in Safe Mode. For information, see[Connecting to the VNC Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../References/serialconsole.htm#connecting-to-vnc-console)for instructions.

After you set up the VNC Console connection, you can boot the OS in Safe Mode by following these steps:
- From the Console sign-in page, select the Restart button.
- While the OS restarts, press the`F8`key repeatedly to bring up the advanced options of Windows Boot Manager.
Note  
  
If pressing the`F8`key doesn't work, see[How to Reset a Forgotten Password for a Windows Instance](https://learnoci.cloud/how-to-reset-your-forgotten-windows-password-in-oci-596b4e99f4ca)for another way to reset the password.
- Select Safe Mode .
- When the OS boots up in Safe Mode, select the Administrator account.
- Create a new password for the Administrator user and sign in.
- After you sign in, open Computer Management , select Start , then Run , and then`compmgmt.msc`.
- Select Local Users and Groups , and then select Users.
- Select the OPC user and then Set a new password .
- Reboot normally and sign in with the new password.

After you regain access to the OPC user account, disable the administrator account for security purposes.

For a more in depth tutorial, see[How to Reset a Forgotten Password for a Windows Instance](https://learnoci.cloud/how-to-reset-your-forgotten-windows-password-in-oci-596b4e99f4ca)
