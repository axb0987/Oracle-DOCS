# Deleting Origins and Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/delete_origin.htm
- Fetched: 2026-09-05 03:10 CDT

# Deleting Origins and Groups

Describes how to delete an origin or an origin group from an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/delete_origin.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/delete_origin.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/delete_origin.htm#)
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
- Select the X next to any origin or origin group you want to delete.
If you delete an origin group, all the origins assigned to that group are deleted.
- Select Save Changes
Publish your changes for them to take effect. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/../Bot/publishing_changes.htm#PublishChanges).
- 

Use the[oci waas waas-policy delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/waas-policy/delete.html)command and required parameters to delete an origin or an origin group from an edge policy:

```

```

Deleting origins and origin groups are configured as an optional parameter.

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[DeleteWaasPolicy](https://docs.oracle.com/iaas/api/#/en/waas/latest/WaasPolicy/DeleteWaasPolicy)operation to delete an origin using the API.
