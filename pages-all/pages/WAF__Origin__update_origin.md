# Editing Origins and Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/update_origin.htm
- Fetched: 2026-09-05 03:11 CDT

# Editing Origins and Groups

Describes how to edit an origin or an origin group for an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/update_origin.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/update_origin.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/update_origin.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.
All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:

- State
- Name
- Policy Type : Select Edge Policy .
- Select the name of the edge policy where you want to configure custom headers for the origins.
The edge policy's details page opens.
- Select Settings under WAF Policy .
The Settings list appears.
- Select the Origin Groups tab. If more than one origin for the edge policy exists, the origins and its group appear.
- Select Edit . If only one origin is defined for the WAF policy, the origin belongs to a default origin group.
- Edit the name of the existing default group or add another group to group multiple origins. You can use origin groups to specify the default origin that is used in your edge policy.
- Select Save Changes
Publish your changes for them to take effect. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/../Bot/publishing_changes.htm#PublishChanges).
- 

Use the[oci waas waas-policy update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/waas-policy/update.html)command and required parameters to edit an origin or an origin group for an edge policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateWaasPolicy](https://docs.oracle.com/iaas/api/#/en/waas/latest/WaasPolicy/UpdateWaasPolicy)
