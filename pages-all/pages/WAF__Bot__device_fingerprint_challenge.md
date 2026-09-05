# Device Fingerprint Challenge for Edge Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/device_fingerprint_challenge.htm
- Fetched: 2026-09-05 03:09 CDT

# Device Fingerprint Challenge for Edge Policies

Describes the use and management of the device fingerprint challenge for an edge policy.

The device fingerprint challenge generates hashed signatures of both virtual and real browsers to identify and block malicious bots.

You can perform the following device fingerprint challenge management tasks:
- [Enabling and Editing the Device Fingerprint Challenge](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/device_fingerprint_challenge.htm#top)
- [Getting the Device Fingerprint Challenge's Details](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/device_fingerprint_challenge.htm#top-7)

## Enabling and Editing the Device Fingerprint Challenge for an Edge Policy

Describes how to enable and edit the device fingerprint challenge for an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/device_fingerprint_challenge.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/device_fingerprint_challenge.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/device_fingerprint_challenge.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.
All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:

- State
- Name
- Policy Type : Select Edge Policy .
- Select the name of the edge policy for which you want to edit and enable the device fingerprint challenge.
The edge policy's details page opens.
- Select Bot Management under WAF Policy .
The Bot Management list opens.
- Select the Device Fingerprint Challenge tab.
- Select Edit Device Fingerprint Challenge .
The Device Fingerprint Challenge panel opens.
- Check the Enable Device Fingerprint Challenge box.
- Enter the following information:

- Device Fingerprint Challenge Action section: Select one of the following options:
- Detect Only : Select this option to be alerted for every matched request.
- Block : Select this option to block requests by returning a response code, error page, or CAPTCHA.

Enter the following information:
- Block Action : Select one of the following actions that's taken when a matching request is blocked.
- Set Response Code :Enter the following information:
- Block response code : Select a status code to return in response to blocked requests.
- Show Error Page :Enter the following information:
- Block response code : Select a status code to return in response to blocked requests.
- Block error page message: : Enter the message that defines the error or error code.
- Block error page description : Enter more details about the error, including the cause and further instructions.
- Block Error Page Code : Enter the error code that's displayed with the error.
- Show CAPTCHA :Enter the following information:
- CAPTCHA Title: Enter the text for the CAPTCHA page title.
- CAPTCHA Header: Enter the text that appears before the CAPTCHA image (for example, "I am not a robot").
- CAPTCHA Footer Text: Enter the text that's shown after the CAPTCHA input box and before the submit button.
- CAPTCHA submit button: Enter the text for the Submit button (for example, "Yes, I am human.").
- Preview CAPTCHA : Select to view the CAPTCHA as users would see it. Select Edit CAPTCHA to return.
- Enter the following information:

- Enter the following information:
- Action threshold (number of requests) : Specify the number of failed requests before the action occurs. Because of the asynchronous request from the browser during page loading, we recommend you set a threshold of 10 for web applications with basic Ajax usage, and 100 for apps with heavy Ajax usage.
- Threshold expiry period (seconds) : The number of seconds before the threshold expires.
- Action expire time (seconds) : Enter the number of seconds between challenges to the same IP address. Because of client IP address changes, we recommend that you set the expiry time to 120 seconds for apps with mobile users and 3,600 seconds for apps with desktop users only.
- Max address count (IP addresses): The maximum number of IP addresses that are added to the list before the specified action is taken.
- Max address count expiration (seconds): The number of seconds an IP address is kept in the list before it's removed.
- Select Save Changes .

Publish your changes for them to take effect. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/publishing_changes.htm#PublishChanges).
- 

Use the[oci waas device-fingerprint-challenge update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/device-fingerprint-challenge/update.html)command and required parameters to enable and edit the device fingerprint challenge for an edge policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use the[UpdateDeviceFingerprintChallenge](https://docs.oracle.com/iaas/api/#/en/waas/latest/DeviceFingerprintChallenge/UpdateDeviceFingerprintChallenge)operation to enable and edit the device fingerprint challenge.

## Getting the Device Fingerprint Challenge's Details for an Edge Policy

Describes how to get the details of the device fingerprint challenge for an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/device_fingerprint_challenge.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/device_fingerprint_challenge.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/device_fingerprint_challenge.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.
All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:

- State
- Name
- Policy Type : Select Edge Policy .
- Select the name of the edge policy for which you want to edit and enable the device fingerprint challenge.
The edge policy's details page opens.
- Select Bot Management under WAF Policy .
The Bot Management list opens.
- Select the Device Fingerprint Challenge tab.

The tab indicates whether the device fingerprint challenge is enabled or not.
- Select Edit Device Fingerprint Challenge .
The Edit Device Fingerprint Challenge panel opens.
- View the settings of the device fingerprint challenge.
See[Enabling and Editing the Device Fingerprint Challenge for an Edge Policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/device_fingerprint_challenge.htm#top)for more information on these settings.
- 

Use the[oci waas device-fingerprint-challenge get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/device-fingerprint-challenge/get.html)command and required parameters to get the details of the device fingerprint challenge for an edge policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use the[GetDeviceFingerprintChallenge](https://docs.oracle.com/iaas/api/#/en/waas/latest/DeviceFingerprintChallenge/GetDeviceFingerprintChallenge)
