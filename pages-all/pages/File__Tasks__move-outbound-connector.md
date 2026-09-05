# Moving an Outbound Connector Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-outbound-connector.htm
- Fetched: 2026-09-05 02:04 CDT

# Moving an Outbound Connector Between Compartments

Move an outbound connector to another compartment within the same tenancy.

- [Console](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-outbound-connector.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-outbound-connector.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-outbound-connector.htm#)
- 

- On the Outbound Connectors list page, select the outbound connector that you want to work with. If you need help finding the list page or the outbound connector, see[Listing Outbound Connectors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Tasks/list-outbound-connectors.htm).
- From the Actions menu (three dots) for the outbound connector, select Move resource .
- Select a Destination compartment .
- Select Move resource .
- 

Use the`[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/outbound-connector/change-compartment.html)oci fs outbound-connector change-compartment`command with the required parameters to move an outbound connector to another compartment.

```

```

For a complete list of flags and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Use[ChangeOutboundConnectorCompartment](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/OutboundConnector/ChangeOutboundConnectorCompartment)to move an outbound connector to another compartment.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
