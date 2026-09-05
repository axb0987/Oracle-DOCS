# Getting the JavaScript Challenge's Details for an Edge Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/get_javascript_challenge.htm
- Fetched: 2026-09-05 03:10 CDT

# Getting the JavaScript Challenge's Details for an Edge Policy

Describes how to get the details of the JavaScript challenge for an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/get_javascript_challenge.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/get_javascript_challenge.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/get_javascript_challenge.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.
All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:

- State
- Name
- Policy Type : Select Edge Policy .
- Select the name of the edge policy whose JavaScript challenge details you want to get.
The edge policy's details page opens.
- Select Bot Management under WAF Policy .
The Bot Management list opens.
- Select the JavaScript Challenge tab.
The tab indicates whether the JavaScript challenge is enabled or not.
- Select Edit JavaScript Challenge .
The Edit JavaScript Challenge panel opens.
View the settings of the JavaScript challenge. See[Enabling and Editing the JavaScript Challenge for an Edge Policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/update_javascript_challenge.htm#top)for more information on these settings.
- 

Use the following[oci waas js-challenge get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/js-challenge/get.html)and required parameters to get the details of the JavaScript challenge for an edge policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use the[GetJsChallenge](https://docs.oracle.com/iaas/api/#/en/waas/latest/JsChallenge/GetJsChallenge)
