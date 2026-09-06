# Access Audit and Diagnostic Logs for Oracle Analytics Cloud Using the Console
- Source: https://docs.oracle.com/iaas/analytics-cloud/doc/access-audit-diagnostic-logs-oracle-analytics-cloud-using-console.html
- Fetched: 2026-09-05 18:58 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/analytics-cloud/doc/access-audit-diagnostic-logs-oracle-analytics-cloud-using-console.html#dcoc-content-body)

# Access Audit and Diagnostic Logs for Oracle Analytics Cloud Using the Console

You can use the Logging service in Oracle Cloud Infrastructure Console to collect and monitor logs for Oracle Analytics Cloud, and other resource types such as Oracle Cloud Database, virtual cloud network, and so on.

For Oracle Analytics Cloud, you can view logs that report service usage and events. If you check these logs regularly, you'll learn to recognize usage trends, troubleshoot issues, and prevent problems in the future.
- In Oracle Cloud Infrastructure Console, click in the top left corner.
- Click Observability &amp; Management . Under Logging , click Log Groups .
- In Compartment , select the compartment where you want to create the log group.
- Click Create Log Group .
- Enter a log group name, optional description, tag, and click Create .
- Click Logs .

- Click Actions , Enable service log , and enter the following details.

- Resource Compartment : Select the compartment containing the Oracle Analytics Cloud instance you want to collect logs for.
- Service : Select Analytics Cloud .
- Resource : Select the Oracle Analytics Cloud instance.
- Log Category : Select either Audit Logs or Diagnostic Logs .
- Log Name : Enter a name for the log.
- Optional: Click Show Advanced Options to change the default log location and retention period.

By default, logs are retained for 1 month.
- Click Enable Log .

The Status field changes from Creating to Active when the log set up is complete.

You can explore, search, and monitor log events in the Explore Log panel.
- Click the Explore log tab, then select Edit to specify the time range you want to display event logs for and click Update . For example, Past hour .

- To view more detail about a particular event, click the expand arrow .

The data section provides additional details about the event, including the user who initiated it.

To learn how to use the Logging service in Oracle Cloud Infrastructure to manage and search your logs, and find out about developer tools (API and CLI), see[Logging](https://docs.oracle.com/iaas/Content/Logging/home.htm).

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
