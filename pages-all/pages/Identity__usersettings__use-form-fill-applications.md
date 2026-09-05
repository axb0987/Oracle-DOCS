# Using Form Fill Applications
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/use-form-fill-applications.htm
- Fetched: 2026-09-05 02:31 CDT

# Using Form Fill Applications

Store your application credentials using form fill apps so that you have one select access to the websites you use most.

For applications where your administrator enables the Oracle Secure Form Fill plugin, collects your credentials the first time you access the app from the My Apps page, and then seamlessly logs you in on future accesses.
Prerequisite: You must be using a Google Chrome or Mozilla Firefox browser.
Note  
  
Internet Explorer and Edge are not supported.

## Installing the Oracle Form-Fill Plugin

Learn when and how to install the plugin that's required to use form fill apps.

When your administrator grants you access to an application that requires the Oracle Form Fill Plugin, you see a prompt to install the plugin the next time you open the My Apps page.

Follow the steps below to install the plugin after you see the prompt in My Apps .

- Go to your My Profile console page, and select More Actions , and then select Applications launcher . If you need help finding the My Profile console page, see[Getting Your Profile Details](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/get-details-my-profile.htm).
- If you see a message at the top of the page that says, "One or more applications granted to you requires the Secure Form Fill Plugin...", proceed with the steps below to install the form fill plugin.

If you don't see the message:
- Select Install Plugin at top right.

You might need to disable pop-up blocking to proceed.
- Follow browser-specific instructions to complete the plugin installation.

- In Google Chrome, select the Add to Chrome button.
- 

In Firefox:
- Save the plugin file (`stf.xpi`) locally.
- In the file system, right-click the file and open it with Firefox.
- On the My Apps page, refresh the browser window after completing the plugin installation.
- Select the icon for an app that requires the form fill plugin.

In the Enter Credentials dialog box that opens in front of the My Apps page, enter your credentials and select OK to proceed to the application's home page.
Note  
  

If instead of the Enter Credentials dialog box you see the application's login page – the app doesn't support the form fill plugin.

You can now access form fill applications from the My Apps page:
- The first time you access a form fill application:
- Instead of going to the application's login page, an Enter Credentials dialog box opens in front of the My Apps page.
- Enter the login credentials for the application in the Enter Credentials dialog box and select Login .

The Oracle Form Fill Plugin captures your credentials and logs you in to the application.
- When you access the same form fill application from My Apps in the future, you are automatically logged in to the application.

Note  
  

If you later change your login credentials in the application, you must update your credentials from the application tile on the My Apps page.

## Updating Credentials for a Form Fill Application

If you change your login credentials with an application that uses the Oracle Form Fill Plugin, you must update your credentials from the My Apps page.

After the first time you access a form fill application from the My Apps page, the Oracle Form Fill Plugin automatically logs you in to that application in the future. But when you change your login credentials within the application, the automatic login using your old credentials fails, and you must manually enter your credentials in the application's login page.

To restore your automatic login through the form fill plugin:

- Go to your My Profile console page, and select More Actions , and then select Applications launcher . If you need help finding the My Profile console page, see[Getting Your Profile Details](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/get-details-my-profile.htm).
- Locate the form fill application for which your credentials have changed.
- Select the gear icon in the bottom-right corner of the application's tile and select Update Credentials .
-
