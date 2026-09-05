# Configure Notification Settings
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-notification-settings.htm
- Fetched: 2026-09-05 03:13 CDT

# Configure Notification Settings

Notification settings for Oracle Access Governance can be managed in the Oracle Cloud Infrastructure Console and Oracle Access Governance Console.

Oracle Access Governance will keep you informed of significant events occurring within your service instance via email notifications. Notifications are triggered by an event such as account creation, or are sent periodically, such as pending review tasks which are sent daily. Notification types include:
- Account operations: Actions such as account creation and account modification will trigger a notification.
- Approval operations: Actions such as approval assignment or approval escalation.
- Review tasks: Actions such as review task assignment or pending review tasks.
- Error alerts: Actions such as agent disconnected from orchestrated system or failed target operation notification for an orchestrated system.

Notifications are sent by email only, using the default Oracle Access Governance email server, or by your own OCI email delivery service. You can configure global settings such as notification email, logo, and language. Specific notification types can be enabled or disabled, and you can set notification email Subject, and the content for the notification email body.

## Configure Notification Email Display Name Using OCI Console

You can set the Display name for the From field of the notification email in the Oracle Cloud Infrastructure Console.

The notification email for Oracle Access Governance is the sender email address that is used to send all notifications regarding campaigns to your users. The default mail address is`no-reply@access-governance.oci.oraclecloud.com`. Oracle Access Governance does not currently support modification of the default mail address. To set the Display name for the notification email for Oracle Access Governance:

- Log in to the Oracle Cloud Infrastructure Console as an administrator.
- Click the icon in the top left corner to display the navigation menu.
- Click Identity &amp; Security in the navigation menu.
- Select Access Governance from the list of products.
- Select Settings menu.
- In the Notification email section, enter the following details:

- 

Display name : Optionally, enter a display name for the sender's email address.

## Configure an OCI Email Delivery Service for Notifications

By default, Oracle Access Governance uses its own email delivery service to send notifications. You can override the default server by configuring an alternative OCI email delivery service if required.

See[Getting Started with the Email Delivery Service](https://docs.oracle.com/iaas/Content/Email/Reference/gettingstarted.htm).

Specify your OCI email delivery service for notifications by carrying out the following steps:

- From the Oracle Access Governance service home page click on the icon, and select Service Administration , and then Notifications .
- In the top right hand of the page, select Manage notification service .
- From the Manage notification service panel, select Yes to configure your own service for notification delivery. Enter values for the following parameters:

- What do you want to name this service?
- What username should be used?
- What password should be used?
- What is the public endpoint?
- Which port should be used?
- What is the from email address?
- Optionally, you can verify your configuration by sending a test email using the settings you have applied in the previous step. Input a test email address in the Which address should we send the test email to? field and click Send test email to test the connection. Check the email of the test user to confirm that the test email was sent and received.
- If you are happy with the configuration, and your test address verifies the setup, select Save to save your settings.

## Configure Global Settings for Notifications

You can use Oracle Access Governance Console to update global notification settings, including the logo used in the notification email, and the default language to use for notifications in your Oracle Access Governance service instance.

- From the Oracle Access Governance service home page click on the icon, and select Service Administration , and then Notifications .
- Select one of the following global settings to update, from the Logo and languages settings drop-down.

- To update the logo used in your notifications, select the Change logo link. In the Manage logo dialog, select a JPEG or PNG file as the source of your logo, and click Save .
- To update the default language used in all notifications, select the Change default language link. In the Manage default language dialog, select the language you want to use as the default for notifications from the list of values, and click Save .
Note  
  

Your system default locale will be used to build the notification when no user specific locale has been detected. The user locale is detected by reading the locale setting from the browser session when the user logs into Oracle Access Governance.

## Configure Notification Types

You can use Oracle Access Governance Console to update notification types, including enabling/disabling types, setting Subject for the notification email, and setting content for the email body.

- From the Oracle Access Governance service home page click on the icon, and select Service Administration , and then Notifications .
- Select the Actions menu, , for one of the notification types in the Notification types drop-down.
- Select one of the following from the Actions menu.

- Enable/Disable : Select this to either enable or disable the notification type
- View details : Select this to update Subject or email body for the notification type
- If you selected View details in the previous step, then you are navigated to the settings page for the notification type selected, for example, Account creation . The language templates available for the notification type are listed. Select your language and click the edit icon. This will take you to the Edit page for your template.
- Update the settings for the selected notification type.

- Update the Subject with the value you want to display in the Subject field of the email for this notification type.
- Update the content of the email by selecting Download for customization . Save the HTML file for the email body, edit with your changes, and then upload the modified file by clicking on Upload customization
Note  
  

The variables that can be applied for the Subject and email body are listed on the Edit page. Select Show me the available variables to show the variables you can use.
- When you are happy with your changes, select Save to store your settings.

## Configure Identities or Email for Sending Orchestrated System Related Notifications

If an issue occurs in an orchestrated system during dataload, you want to be notified in good time so that you can investigate and resolve the issue. You can configure identities or an external email, to route notifications regarding your orchestrated system to assist with this.
To send orchestrated system-related notifications to your preferred identities or an external email address, you can configure Oracle Access Governance as required:

- From the Oracle Access Governance navigation menu icon , select Service Administration → Orchestrated Systems .
- Select the Manage integration option from the action menu for the orchestrated system you want to configure. This displays the manage integration page for the selected orchestrated system.
- From the System settings section of the page, select Manage on the Notification settings tile. This will display the Notification settings page for the selected orchestrated system.
- In the Which identities? field, use the drop-down list to select identities in your Oracle Access Governance instance to send orchestrated system-related notifications to. You can have multiple identities as required.
- In the Email field, add an email for any person external to your Oracle Access Governance instance (who does not have an identity in your system) who you would like to receive notifications. You can only add one external email address for orchestrated system-related notifications.
-
