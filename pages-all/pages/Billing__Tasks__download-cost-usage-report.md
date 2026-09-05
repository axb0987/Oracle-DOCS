# Downloading a Cost Report
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/download-cost-usage-report.htm
- Fetched: 2026-09-05 01:43 CDT

# Downloading a Cost Report

Download a cost report in Billing and Cost Management.

A cost report is a file stored as an object in a bucket. For general information about downloading an object, see[Downloading an Object Storage Object](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects_topic-To_download_an_object_from_a_bucket.htm).

For information about listing cost reports, see[Listing Cost Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-cost-usage-report.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/download-cost-usage-report.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/download-cost-usage-report.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/download-cost-usage-report.htm#)
- 

- On the Cost and Usage Reports list page, find the cost report that you want to download. If you need help finding the list page or the cost report, see[Listing Cost Reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/list-cost-usage-report.htm).
- From the Actions menu (three dots) for the cost report, select Download report .
- 

Note  
  
Cost reports are stored in the tenancy's home region. The Object Storage namespace used for the reports is`bling`. The bucket name is the tenancy OCID.

Use the[oci os object get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/get.html)command and required parameters to download cost reports in the tenancy:

```

```

Example (reference the Python SDK code example shown in the API task):

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Note  
  
Cost reports are stored in the tenancy's home region. The Object Storage namespace used for the reports is`bling`. The bucket name is the tenancy OCID.

Run the[GetObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/GetObject)operation to download a cost report.

The following example shows how to download a cost report using a Python script:
Note  
  
This example has a specific tenancy OCID, because the reports are stored in an Oracle-owned Object Storage bucket hosted by Oracle Cloud Infrastructure, and not a customer's tenancy.

```

```
