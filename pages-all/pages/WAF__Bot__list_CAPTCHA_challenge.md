# Listing the CAPTCHA Challenges for an Edge Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/list_CAPTCHA_challenge.htm
- Fetched: 2026-09-05 03:10 CDT

# Listing the CAPTCHA Challenges for an Edge Policy

Describes how to list the CAPTCHA challenges for an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/list_CAPTCHA_challenge.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/list_CAPTCHA_challenge.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/list_CAPTCHA_challenge.htm#)
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
The CAPTCHA Challenge tab lists all the available CAPTCHA challenges.
- 

Use the[oci waas captcha list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/captcha/list.html)command and required parameters to list the CAPTCHA challenges for an edge policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use the[ListCaptchas](https://docs.oracle.com/iaas/api/#/en/waas/latest/Captcha/ListCaptchas)
