# Moving a Log Saved Search Between Compartments
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-log-saved-search.htm
- Fetched: 2026-09-05 02:37 CDT

# Moving a Log Saved Search Between Compartments

Move a saved search in Logging to a different compartment.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-log-saved-search.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-log-saved-search.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-log-saved-search.htm#)
- 

Note  
  
When[editing a saved search](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-log-saved-search.htm), you can also change the compartment.

- Open the navigation menu and select Observability &amp; Management . Under Logging , select Saved Searches .
- Select the compartment that contains the saved search that you want to move.
- On the Saved Searches page, select the Actions menu for the saved search that you want to move to a different compartment, and then select Move Resource .
- In the Move resource dialog box, select the new compartment.
- Select Move resource .
- 

Use the[oci logging log-saved-search change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log-saved-search/change-compartment.html)command and required parameters to move a saved log search between compartments:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[ChangeLogSavedSearchCompartment](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogSavedSearch/ChangeLogSavedSearchCompartment)
