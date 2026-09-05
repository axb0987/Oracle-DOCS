# Managing Email Notifications in License Manager
- Source: https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/notifications.htm
- Fetched: 2026-09-05 02:11 CDT

# Managing Email Notifications in License Manager

Create and manage the list of email addresses that can be notified about product license activity.

You can manage the list of email addresses that get notifications about expirations or subscription overages in the License Manager Notifications page. Emails are sent on a weekly basis.

For items that require action, you receive an email that provides a License Manager summary. The email highlights the product licenses that are over-subscribed, and license records near or past their license or support contract expiration dates.

- [Console](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/notifications.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/notifications.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/General/LicenseManager/Tasks/notifications.htm#)
- 

- Open the navigation menu and select Governance &amp; Administration . Under License Management, select Notifications .
The License Manager Notifications page opens.
- Select Edit .
The Email Notifications panel opens.
- Enter an email address to receive notifications in the Email recipients box and select Add to list .
The email address you entered is added to the Email recipients box and appears in the list underneath with a checkbox enabled to indicate it's an active recipient.
- Add more email addresses using the same method. Select Add to list for each email address before adding the next one.
Each email address you add appears both within Email recipients and the list. You can enable or disable an email address in the list by selecting or clearing the checkbox next to it.
- Select Save .
- 

## Getting the List of Notification Email Addresses

Use the[oci license-manager configuration get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/configuration/get.html)command and required parameters to get the notification email addresses for License Manager:

```

```

`compartment_ocid`is the root compartment of your tenancy.

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Updating the List of Notification Email Addresses

Use the[oci license-manager configuration update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/license-manager/configuration/update.html)command and required parameters to add email address to the notification list in License Manager:

```

```

`compartment_ocid`is the root compartment of your tenancy.

`email_ids`is the list of email IDs associated with the configuration. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.
- 

## Getting the List of Notification Email Addresses

Run the[GetConfiguration](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/Configuration/GetConfiguration)operation to get the notification email addresses for License Manager.

## Updating the List of Notification Email Addresses

Run the[UpdateConfiguration](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/Configuration/GetConfiguration)
