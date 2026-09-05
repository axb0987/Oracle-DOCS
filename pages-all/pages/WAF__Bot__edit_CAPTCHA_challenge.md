# Editing a CAPTCHA Challenge for an Edge Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/edit_CAPTCHA_challenge.htm
- Fetched: 2026-09-05 03:09 CDT

# Editing a CAPTCHA Challenge for an Edge Policy

Describes how to edit a CAPTCHA challenge for an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/edit_CAPTCHA_challenge.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/edit_CAPTCHA_challenge.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/edit_CAPTCHA_challenge.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.
All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:

- State
- Name
- Policy Type : Select Edge Policy .
- Select edge policy for which you want to edit and enable the CAPTCHA challenge.
The edge policy's details page opens.
- Select Bot Management under WAF Policy .
The Bot Management list opens.
- Select the CAPTCHA Challenge tab.
The CAPTCHA Challenge tab lists all the available CAPTCHA challenges.
- Select the Actions menu (three dots) for the CAPTCHA challenge you want to edit and select Edit .
The Edit CAPTCHA Challenge panel opens.
- Edit the CAPTCHA challenge settings.
See[Adding a CAPTCHA Challenge to an Edge Policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/update_CAPTCHA_challenge.htm#top)for more information on these settings.
- Select Save Changes .
Publish your changes for them to take effect. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/publishing_changes.htm#PublishChanges).
- 

Use the[oci waas captcha update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/captcha/update.html)command and required parameters to edit a CAPTCHA challenge for an edge policy:

```

```

The`captchas`value is a list of CAPTCHA details. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use the[UpdateCaptchas](https://docs.oracle.com/iaas/api/#/en/waas/latest/Captcha/UpdateCaptchas)
