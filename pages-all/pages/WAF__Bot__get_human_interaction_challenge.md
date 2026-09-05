# Getting the Human Interaction Challenge's Details for an Edge Policy
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/get_human_interaction_challenge.htm
- Fetched: 2026-09-05 03:10 CDT

# Getting the Human Interaction Challenge's Details for an Edge Policy

Describes how to get details of the human interaction challenge for an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/get_human_interaction_challenge.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/get_human_interaction_challenge.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/get_human_interaction_challenge.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The Policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.
All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:

- State
- Name
- Policy Type : Select Edge Policy .
- Select the name of the edge policy for which you want to edit and enable the human interaction challenge.
The edge policy's details page opens.
- Select Bot Management under WAF Policy .
The Bot Management list opens.
- Select the Human Interaction Challenge tab.

The tab indicates whether the Human Interaction challenge is enabled or not.
- Select Edit Human Interaction Challenge .
The Edit Human Interaction Challenge panel opens.
- View the settings of the Human Interaction challenge.

See[Enabling and Editing the Human Interaction Challenge for an Edge Policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/update_human_interaction_challenge.htm#top)for more information on these settings.
- 

Use the[oci waas human-interaction-challenge get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/human-interaction-challenge/get.html)command and required parameters to get details of the human interaction challenge for an edge policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use the[GetHumanInteractionChallenge](https://docs.oracle.com/iaas/api/#/en/waas/latest/HumanInteractionChallenge/GetHumanInteractionChallenge)
