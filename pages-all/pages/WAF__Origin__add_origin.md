# Adding Origins and Origin Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/add_origin.htm
- Fetched: 2026-09-05 03:10 CDT

# Adding Origins and Origin Groups

Describes how to add an origin or an origin group to an edge policy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/add_origin.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/add_origin.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/add_origin.htm#)
- 

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .
The policies list opens. All edge policies are listed in a table.
- Select the Compartment from the list.
All the edge policies in that compartment are listed in a table.
- (Optional) Apply one or more of the following Filters to limit the edge policies displayed:

- State
- Name
- Policy Type : Select Edge Policy .
- Select the name of the edge policy to which you want to add an origin.
The edge policy's details page opens.
- Select Settings under WAF Policies .
The Settings list appears.
- Select the Origin Groups tab.
If more than one origin for the edge policy exists, the origins and its group appear.
- Select Edit .
The Origin Groups dialog box appears. If only one origin defined for the edge policy exists, the origin belongs to a default origin group.

Optionally, you can edit the name of the existing default group or add another group to group multiple origins. You can use origin groups to specify the default origin that is used in your edge policy.
- Select + Additional Origin below the origin group where you want to add an origin.
- Enter the following information:

- Name : Accept the existing Default Group name, or enter a new origin group name. The origin you create resides under this origin group.
- Default Origin : If several origins are listed, select which one you want to be the default origin.
- Name : Enter the name of the origin.
- URI : Enter the IPv4 address or FQDN of the origin.
- HTTP Port : Enter the HTTP port on the origin that the web application listens on. The default port is 80.
- HTTPS Port : The HTTPS port on the origin that the web application listens on. The default port is 443.
- Weight : The weight of the origin within the group is used for load balancing purposes. Origins with higher weights receive larger proportions of client requests.

Select + Additional Origin to add another origin row for you to complete. Select X to remove an associated origin.
- (Optional) Select + Additional Group to add another origin group.

Enter a name for the origin group and add at least one origin using the same method as described earlier. Indicate which origin is the default if your origin group has multiple origins.
- Select Save Changes .
Publish your changes for them to take effect. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/Origin/../Bot/publishing_changes.htm#PublishChanges).
- 

Use the[oci waas waas-policy create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/waas-policy/create.html)command and required parameters to add an origin or an origin group to an edge policy:

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[CreateWaasPolicy](https://docs.oracle.com/iaas/api/#/en/waas/latest/WaasPolicy/CreateWaasPolicy)
