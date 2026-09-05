# Upgrading a VMware Solution SDDC's HCX
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/upgrading-vmware-hcx.htm
- Fetched: 2026-09-05 03:07 CDT

# Upgrading a VMware Solution SDDC's HCX

Oracle Cloud VMware Solution's (OCVS) VMware software component Hybrid Cloud Extension (HCX) is an application mobility platform that simplifies the migration, rebalancing, and business continuity of VMware-based workloads across data centers and clouds, enabling seamless application mobility and infrastructure hybridity.

Typically, HCX upgrade bundles are pushed online by Broadcom, and you can perform an online upgrade from the HCX console directly. You can continue to follow the same process until April 30th, 2025. After April 30th, 2025, the way you perform HCX upgrades will change for all OCVS users. You will receive all HCX upgrade bundles through the[OCVS Upgrade feature](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/upgrade8.htm), following the same process for vCenter and NSX upgrade bundles. Using these HCX upgrade bundles, you must follow the offline upgrade process recommended by Broadcom.
In order for you to get continued support for the HCX upgrade from Oracle, you must be on the supported version[VMware Product Lifecycle Matrix](https://support.broadcom.com/web/ecx/productlifecycle)of HCX. The HCX upgrade path depends on the current version’s interoperability and can be found here:[HCX Interoperability Upgrade Path](https://sim.esp.spespg1.vmw.saas.broadcom.com/Upgrade?productId=660). HCX Ver 4.10.3 is the latest offered OCI OCVS[VMware software component](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/ocvsoverview.htm#about-vmware).
- Upgrading to HCX[4.10.3](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10.html)is supported by HCX[4.10.x](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10.html)and[4.9.x](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-9.html)for both local and connected sites. See[HCX Update Procedures](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10/vmware-hcx-user-guide-4-10/updating-vmware-hcx/hcx-service-update-procedures.html).
- Upgrading to HCX[4.10.3](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10.html)from all versions between 4.4 and 4.8.3 is a 2-step process and requires an online upgrade to 4.9.2 first. See[Upgrading the HCX Manager for Connected Sites](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10/vmware-hcx-user-guide-4-10/updating-vmware-hcx/hcx-service-update-procedures/upgrade-hcx-manager-for-connected-sites.html). (Available until April 30th, 2025, after which you must follow the offline upgrade process)
- Upgrading to HCX[4.10.3](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10.html)from all versions between 4.2.4 and 4.3.3 is a 3-step process that requires an offline upgrade to 4.8.3 first. Refer to[Upgrade HCX Manager for Local Sites](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10/vmware-hcx-user-guide-4-10/updating-vmware-hcx/hcx-service-update-procedures/upgrade-hcx-manager-for-local-sites.html).
- Versions less than 4.2.4 are not qualified for upgrade. This will require a full redeployment to the latest and supported build. If you need assistance with any binaries or licenses, submit a ticket to[My Oracle Support](http://support.oracle.com/).

Downloading HCX Upgrade Offline Bundles (OCI Console)

- On the Software-Defined Data Centers list page, select the SDDC that you want to upgrade. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/../Tasks/sddc-list.htm).
- In the upgrade banner on the SDDC's details page, start the Upgrade SDDC workflow.
- Upgrade the Management Cluster to match the SDDC version.
- Download required HCX binaries.
- Follow the HCX documentation to upgrade[Upgrade HCX Manager for Local Sites](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10/vmware-hcx-user-guide-4-10/updating-vmware-hcx/hcx-service-update-procedures/upgrade-hcx-manager-for-local-sites.html)
