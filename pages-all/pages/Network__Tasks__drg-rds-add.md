# Adding a Route Distribution Statement
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-add.htm
- Fetched: 2026-09-05 02:44 CDT

# Adding a Route Distribution Statement

Add a statement to an import or export route distribution for a dynamic routing gateway (DRG) in Oracle Cloud Infrastructure.

All match criteria in a statement must be met for the action to take place.

For details about DRG routing, see[Working with DRG Route Tables and Route Distributions](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__rd_rt).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-add.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-add.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-add.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- On the Routing tab, go to either the Import route distributions or Export route distributions sections. Select the route distribution you want to you want to add a statement to, then select the Statements tab.
- Under Resources , select either Import route distributions or Export route distributions . Select the route distribution you want to you want to add a statement to.
- Select Add route distribution statements .
- Enter the following values for each statement:

- Priority : Enter 10 or some other priority number between 1 and 65535. Statements are evaluated in ascending order and carried out when a match is found, so low numbers effectively have a high priority.
- Match type : Select Attachment type , Attachment , or Match all .
- 

If you select Attachment Type , then select one of the possible DRG attachment types. When you use this option, the import route distribution includes routes from all attachments to this DRG with the chosen type.
- 

If you select Attachment , then select the type of DRG attachment and then select the specific attachment, changing compartments as necessary.
- (Optional) Select +Another statement to add another route distribution statement to the import route distribution.
- Select Add import route distribution statements .

New statements are added to the list of existing statements for the distribution, in priority order.
- 

Use the[network drg-route-distribution-statement add](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-distribution-statement/add.html)command and required parameters to add a statement to a specified import or export route distribution:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[AddDrgRouteDistributionStatements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteDistributionStatement/AddDrgRouteDistributionStatements)
