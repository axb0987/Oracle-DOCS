# Enabling Logs
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-dns-logging-enable.htm
- Fetched: 2026-09-05 02:46 CDT

# Enabling Logs

Learn how to enable private DNS resolver logging.

## Using the Console

- Open the navigation menu , select Networking , and then select Virtual cloud networks .
The Virtual Cloud Networks page opens. All virtual cloud networks (VCNs) in the selected compartment are displayed in a table.
- Select the name of the VCN where the private DNS resolver resides.
The VCN's details page opens.
- Find DNS Resolver and select the associated link.
The Private Resolver Information page opens.
- Select Monitoring .
The Logs page opens.
- Find Query response logs in the list. In the Actions menu (three dots), select Enable .
The Enable resource log panel opens.
- Enter the following information:

- Create new group : (Optional) Select to create a new log group for the logs if you do not want to use one of the existing ones available in your compartment. Log groups are logical containers for organizing logs. Logs must always be inside log groups. For more information, see[Creating a Log](https://docs.oracle.com/iaas/Content/Logging/Task/create-logging-log.htm).
- Compartment : The compartment the log and log group reside in.
- Log Group : The first log group in the compartment. You can select another log group, or create a new group by selecting Create new log group .
- Log Name : Already filled as the name of the resource and the category, which are combined with an underscore ( &lt;resource&gt; _ &lt;category&gt; ). You can change this name.
- Log Retention : (Advanced options) The default retention period for the log measured in 30-day increments, up to a maximum of 180 days. You can select a different retention period.
Note  
  
If you change the retention period from six months to one month, all the logs older than one month are no longer accessible. The future time and date that a log no longer becomes available is based on the exact time and date that you created the log. For example, if you created a log on July 21 at 15:05 UTC with a retention period of three months, then on October 19 at 15:05 the log is no longer be searchable.
- Enable legacy archival logs : When enabled, an Object Storage bucket is automatically created in the compartment and a copy of the log is placed there.
Note  
  
This is legacy functionality. New and improved functionality is now available in[Connector Hub](https://docs.oracle.com/iaas/Content/connector-hub/home.htm).
-
