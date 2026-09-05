# Database Quotas
- Source: https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/resourcequotas_topic-Database_Quotas.htm
- Fetched: 2026-09-05 02:53 CDT

# Database Quotas

Database quota details.

Family name:`database`

## Autonomous AI Database Quotas

For information on setting quotas for Autonomous AI Databases and related infrastructure, see the following links:
- Oracle Autonomous AI Database Serverless:[Manage Resource Availability with Compartment Quotas](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-database-compartment-quotas.html)
- Oracle Autonomous AI Database on Dedicated Exadata Infrastructure:[Manage Resource Availability with Compartment Quotas](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbap/index.html)

## Oracle Base Database Service Quotas

For information on setting quotas for Oracle Base Database Service and related infrastructure, see[Compartment Quotas](https://docs.oracle.com/en/cloud/paas/base-database/quotas/index.html).

## Oracle Exadata Database Service on Dedicated Infrastructure, Oracle Exadata Database Service on Cloud@Customer

Name

Scope

Description
bm-dense-io1-36-count Availability domain

Number of BM.DenseIO1.36 DB systems
bm-dense-io2-52-count Availability domain Number of BM.DenseIO2.52 DB systems
exadata-base-48-count Availability domain Number of Exadata.Base.48 DB systems
exadata-full1-336-x6-count Availability domain Number of Exadata.Full1.336 - X6 DB systems
exadata-full2-368-x7-count Availability domain

Number of Exadata.Full2.368 - X7 DB systems and Autonomous Exadata Infrastructure
exadata-half1-168-x6-count Availability domain Number of Exadata.Half1.168 - X6 DB systems
exadata-half2-184-x7-count Availability domain

Number of Exadata.Half2.184 - X7 DB systems and Autonomous Exadata Infrastructure
exadata-quarter1-84-x6-count Availability domain Number of Exadata.Quarter1.84 - X6 DB systems
exadata-quarter2-92-x7-count Availability domain

Number of Exadata.Quarter2.92 - X7 DB systems and Autonomous Exadata Infrastructure
vm-block-storage-gb Availability domain Total size of block storage attachments across all virtual machine DB systems, in GB
vm-standard1-ocpu-count Availability domain Number of VM.Standard1.x OCPUs for the Intel X7 processor (fixed shape) based DB systems in the Oracle Base Database Service
vm-standard2-ocpu-count Availability domain Number of VM.Standard2.x OCPUs for the Intel X7 processor (fixed shape) based DB systems in the Oracle Base Database Service
vm-standard3-ocpu-count Availability domain Number of VM.Standard3.Flex OCPUs for the Intel X9 processor (flexible shape) based DB systems in the Oracle Base Database Service
vm-standard-a1-ocpu-count Availability domain Number of VM.Standard.A1.Flex OCPUs for the Arm-based Ampere A1 processor (flexible shape) based DB systems in the Oracle Base Database Service
vm-standard-e4-ocpu-count Availability domain Number of VM.Standard.E4.flex OCPUs for the AMD processor (flexible shape) based DB systems in the Oracle Base Database Service

For information about shapes that aren't listed, including non-metered shapes,[contact Oracle Support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).

## Examples

To limit the number of virtual machine Base Database systems in a compartment, you must set a quota for the number of CPU cores and a separate quota for the block storage:

```

```

The following example shows how to prevent the usage of all database resources in the tenancy except for two Exadata full rack X7 resources in a specified compartment:

```

```

This example of nested quotas shows how to distribute limits for a resource type in a compartment among its subcompartments:

```

```
