# Adding a CAPTCHA Challenge to an Edge Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/update_CAPTCHA_challenge.htm
- Fetched: 2026-09-05 03:10 CDT

# Adding a CAPTCHA Challenge to an Edge Policy

Describes how to add a CAPTCHA challenge to an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/update_CAPTCHA_challenge.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/update_CAPTCHA_challenge.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/update_CAPTCHA_challenge.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.
All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:

- State
- Name
- Policy Type : Select Edge Policy .
- Select the edge policy for which you want to edit and enable the CAPTCHA challenge.
The edge policy's details page opens.
- Select Bot Management under WAF Policy .
The Bot Management list opens.
- Select the CAPTCHA Challenge tab.
- Select Add CAPTCHA Challenge .
The Add CAPTCHA Challenge panel opens.
- Enter the following information:

- Title : Enter the text for the CAPTCHA page title.
- URL Path : Enter the URL path challenged by CAPTCHA.
- Session Duration (seconds) : Enter the number of seconds after which the CAPTCHA challenge cannot be resubmitted to the same user.
- Header : Enter the text that appears before the CAPTCHA image (for example, "I am not a robot").
- Footer : Enter the text that will be shown after the CAPTCHA input box and before the submit button.
- Incorrect CAPTCHA Text : Enter the text that appears when incorrect text is entered (for example, "The CAPTCHA was incorrect. Please try again.").
- Submit button : Enter the text for the Submit button (for example, "Yes, I am human.").
- Preview CAPTCHA : Select to view the CAPTCHA as users would see it. Select Edit CAPTCHA to return.
- Select Add .
The CAPTCHA challenge is added to the list.
Publish your changes for them to take effect. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/publishing_changes.htm#PublishChanges).
- 

Use the[oci waas captcha update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/captcha/update.html)command and required parameters to add a CAPTCHA challenge to an edge policy:

```

```

The`captchas`value is a list of CAPTCHA details. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use the[UpdateCaptchas](https://docs.oracle.com/iaas/api/#/en/waas/latest/Captcha/UpdateCaptchas)
