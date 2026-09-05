# Managing VMware Licenses
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/managing-licenses.htm
- Fetched: 2026-09-05 03:07 CDT

# Managing VMware Licenses

Oracle Cloud VMware Solution (OCVS) runs VMware workloads natively on OCI. Broadcom has introduced significant changes to VMware's licensing model, impacting how licenses are provisioned and allocated within OCVS. This document provides an overview of the Bring Your Own License (BYOL) feature and OCVS changes required to implement Broadcom's licensing changes.

## Bring Your Own License

Broadcom's transition to the Metal as a Service licensing model, or Bring Your Own License (BYOL), requires VMware customers to purchase licenses directly from Broadcom. Licenses are purchased for a specified number of OCPUs or tebibytes (TiBs). New BYOL features added to OCVS allow customers to register and allocate those licenses on OCVS.

## Add-On Licenses

The BYOL model also applies to additional VMware functionalities, such as vDefend Firewall and Avi Load Balancer. To use these add-ons, separate licenses from Broadcom are required. Each add-on is charged based on metrics such as OCPUs or TiBs. Licensing for add-ons follows the same BYOL process as the core VMware functionality.

## Using BYOL with OCVS

To support the BYOL model, OCVS has introduced VMware license management features. The features include:
- Registering licenses with OCI.
- Allocating licenses across OCI regions.
Important  
  
Organizations are responsible for ensuring the accuracy of license information, including the number of cores and license keys.

## Tasks for Managing Licenses

The following tasks provide details on managing BYOL features.
- [Listing VMware Solution Licenses](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/license-list.htm)
- [Creating VMware Solution Licenses](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/license-create.htm)
- [Editing VMware Solution Licenses](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/license-edit.htm)
- [Listing VMware Solution License Allocations](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/license-allocation-list.htm)
- [Creating VMware Solution License Allocations](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/license-allocation-create.htm)
