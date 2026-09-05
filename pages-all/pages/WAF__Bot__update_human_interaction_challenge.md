# Enabling and Editing the Human Interaction Challenge for an Edge Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/update_human_interaction_challenge.htm
- Fetched: 2026-09-05 03:10 CDT

# Enabling and Editing the Human Interaction Challenge for an Edge Policy

Describes how to enable and edit the human interaction challenge for an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/update_human_interaction_challenge.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/update_human_interaction_challenge.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/update_human_interaction_challenge.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.
All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:

- State
- Name
- Policy Type : Select Edge Policy .
- Select the name of the edge policy for which you want to edit and enable the JavaScript challenge.
The edge policy's details page opens.
- Select Bot Management under WAF Policy .
The Bot Management list opens.
- Select the Human Interaction Challenge tab.
- Select Edit Human Interaction Challenge .
The Edit Human Interaction Challenge panel opens.
- Check the Enable Human Interaction Challenge box.
- Enter the following information:

- Human Interaction Challenge Action section: Select one of the following options:
- Detect Only : Select this option to be alerted for every matched request.

Enter the following information:
- Set header for failed request : Check to add an HTTP header to requests that fail the challenge.

Under Additional Header , enter the Header name (the name displayed in the HTTP request header) and the Header value (the data requested by the header) in the corresponding boxes.
- Block : Select this option to block requests by returning a response code, error page, or CAPTCHA.

Enter the following information:
- Enable Conditions : Check to enable conditions. The JavaScript Challenge is applied only for the requests that match all the listed conditions. Select the condition and corresponding action from the lists. Select + Another Condition to display another condition row where you can enter a condition and action pair. Select X to delete the associated condition row.

See[Access Control for Edge Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/../Tasks/wafaccesscontrol.htm#Access_Control)for more information about conditions and rules.
- Block Action : Select one of the following actions that is taken when a matching request is blocked.
- Set Response Code :

Enter the following information:
- Block response code : Select a status code to return in response to blocked requests.
- Show Error Page :

Complete the following:
- Block response code : Select a status code to return in response to blocked requests.
- Block error page message: : Enter the message that defines the error or error code.
- Block error page description : Enter more details about the error, including the cause and further instructions.
- Block Error Page Code : Enter the error code that is displayed with the error.
- Show CAPTCHA :

Enter the following information:
- CAPTCHA Title: Enter the text for the CAPTCHA page title.
- CAPTCHA Header: Enter the text that appears before the CAPTCHA image (for example, "I am not a robot").
- CAPTCHA Footer Text: Enter the text that will be shown after the CAPTCHA input box and before the submit button.
- CAPTCHA submit button: Enter the text for the Submit button (for example, "Yes, I am human.").
- Preview CAPTCHA : Select to view the CAPTCHA as users would see it. Select Edit CAPTCHA to return.
- Complete the following:

- Action threshold (number of requests) : Specify the number of failed requests before the action occurs. Because of the asynchronous request from the browser during page loading, We recommend that you set a threshold of 10 for web applications with basic Ajax usage, and 100 for apps with heavy Ajax usage.
- Threshold expiry period (seconds) : Enter the number of seconds before the threshold expires.
- Action expire time (seconds): : Enter the number of seconds between challenges to the same IP address. Because of client IP address changes, Oracle recommends that you set the expiry time is set to 120 seconds for apps with mobile users and 3,600 seconds for apps with desktop users only.
- Interaction threshold (number of interactions) : Enter the number of interactions before the threshold expires.
- Recording period (seconds) : Enter the number of seconds to record the user's events.
- Enable NAT Support box. (optional) Check to enable. When enabled, the user is identified by the IP address and also by a unique hash. This checking prevents blocking visitors with shared IP addresses. Oracle recommends that you disable this NAT support for high-load apps (200+RPS).

Publish your changes for them to take effect. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/publishing_changes.htm#PublishChanges).
- 

Use the[oci waas human-interaction-challenge update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/human-interaction-challenge/update.html)command and required parameters to enable and edit the human interaction challenge for an edge policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use the[UpdateHumanInteractionChallenge](https://docs.oracle.com/iaas/api/#/en/waas/latest/HumanInteractionChallenge/UpdateHumanInteractionChallenge)
