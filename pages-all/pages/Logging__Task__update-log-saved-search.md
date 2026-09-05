# Editing a Log Saved Search
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-log-saved-search.htm
- Fetched: 2026-09-05 02:38 CDT

# Editing a Log Saved Search

Edit a saved search in Logging.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-log-saved-search.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-log-saved-search.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/update-log-saved-search.htm#)
- 

You can change only the name, compartment, and description of a saved search. If you need to change the search parameters, you must[create a new saved search](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-log-saved-search.htm).
- Open the navigation menu and select Observability &amp; Management . Under Logging , select Saved Searches .
- Select the compartment that contains the saved search that you want to edit.
- On the Saved Searches page, select the name of the saved search.
- On the log details page, select the Actions menu and then select Edit .
- 

In the Edit Saved Search panel, edit the search name and description , as needed.

The compartment and search query are as read-only. To change the search query,[create a new saved search](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/create-log-saved-search.htm). To change the compartment,[move the saved search to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Logging/Task/change-compartment-log-saved-search.htm).
- Select Save Search .
- 

Use the[oci logging log-saved-search update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log-saved-search/update.html)command and required parameters to edit a log saved search:

```

```

For a complete list of parameters and variable options for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
- 

Run the[UpdateLogSavedSearch](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/LogSavedSearch/UpdateLogSavedSearch)
