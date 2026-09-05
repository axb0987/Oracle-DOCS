# Good Bot Allowlist Management for Edge Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/good_bot_allowlist.htm
- Fetched: 2026-09-05 03:10 CDT

# Good Bot Allowlist Management for Edge Policies

Describes the to use and management of the good bot allowlist for an edge policy.

Good bots provides the list of bots managed by known providers, such as Baidu or Google. You can allow the access from a specific good bot, or block the bot if they serve no business purpose. Allowed good bots from this section are allowlisted.

Allowlisted bots are flagged with a Bypass action in the edge policy logs. You can select the Bypass check box from the Action filter in Logs to search for the traffic allowed from these rules. Logged good bot events are categorized as a Threat Intelligence Leads log type, however, they are not a threat when the action taken is to Bypass.

The list of good bots on this menu is managed and continuously updated. Other good bots can be added as a new access control rule in Access Control.

Use one of the following methods to manage the good bot allowlist for an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/good_bot_allowlist.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/good_bot_allowlist.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Bot/good_bot_allowlist.htm#)
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

The Details page of the edge policy you selected appears.
- Select Bot Management under WAF Policy .

The Bot Management list appears.
- Select the Good Bot Whitelist tab.

The Good Bot Whitelist tab lists the bots managed by known providers that you can add to a whitelist. Enabling a good bot lets it bypass all challenges.
- Check each bot that you want to designate as a good bot. You can also check the Disable All or Enable All buttons.
- 

Use the[oci waas good-bot update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/good-bot/update.html)command and required parameters to use and manage the good bot allowlist for an edge policy:

```

```

The`good-bots`value is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the`file://path/to/file`syntax.

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use the[UpdateGoodBots](https://docs.oracle.com/iaas/api/#/en/waas/latest/GoodBot/UpdateGoodBots)
