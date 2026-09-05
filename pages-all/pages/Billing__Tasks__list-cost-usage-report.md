# Listing Cost Reports
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-cost-usage-report.htm
- Fetched: 2026-09-05 01:43 CDT

# Listing Cost Reports

View the tenancy's cost reports in Billing and Cost Management.

A cost report is a file stored as an object in a bucket. For general information about listing objects, see[Listing Object Storage Objects in a Bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects_topic-To_list_objects_in_a_bucket.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-cost-usage-report.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-cost-usage-report.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-cost-usage-report.htm#)
- 

- Select the tenancy's home region.

Cost reports are stored in an Object Storage bucket in the tenancy's home region.

For instructions on switching regions, see[Switching Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Switchin).
- Open the navigation menu and select Billing &amp; Cost Management . Under Cost Management , select Cost and Usage Reports .

The Cost and Usage Reports list page opens. All cost reports in the tenancy are displayed in a table, indicating report name, created date, and size. FOCUS reports are initially collapsed at the top of the table, followed by individual OCI proprietary cost reports.
- To browse FOCUS cost reports, expand FOCUS Reports and then expand the year, month, and day that you want.

## Actions

To download a cost report directly from the list table, select Download report from the Actions menu (three dots) in the row for that report.
- 

Note  
  
Cost reports are stored in the tenancy's home region. The Object Storage namespace used for the reports is`bling`. The bucket name is the tenancy OCID.

Use the[oci os object list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/list.html)command and required parameters to list cost reports in the tenancy:

```

```

Examples (reference the Python SDK code example shown in the API task for[Downloading a Cost Report](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/download-cost-usage-report.htm)):

List all cost reports from the Oracle managed namespace "bling" and bucket (customer tenancy OCID):

```

```

List two cost reports from the Oracle managed namespace "bling" and bucket (customer tenancy OCID):

```

```

List all cost reports from the Oracle managed namespace "bling" and bucket (customer tenancy OCID) with the prefix "reports/cost-csv":

```

```

List all cost reports from the Oracle managed namespace "bling" and bucket (customer tenancy OCID) with the prefix "FOCUS Reports":

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Note  
  
Cost reports are stored in the tenancy's home region. The Object Storage namespace used for the reports is`bling`. The bucket name is the tenancy OCID.

Run the[ListObjects](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjects)operation to list cost reports.

See also the Python SDK code example shown in the API task for[Downloading a Cost Report](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/download-cost-usage-report.htm)
