# Known Issues for VMware Solution
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/known-issues.htm
- Fetched: 2026-09-05 03:09 CDT

# Known Issues for VMware Solution

These known issues have been identified in VMware Solution.

## NSX 4.2.1.0 environments affected by critical JDK Bug
Details The following symptoms can be caused by a critical JDK Bug - JDK-8330017.
- NSX GUI becomes inaccessible
- NSX to HCX/vCenter connection might go DOWN
- VM operations failure - POWER ON, vMotion, VM connectivity might be affected
- HCX operations failure - HCX migration, L2 extension and so on
- NSX operations impacted - Existing configs might work, but creating new configurations (creating NSX segments, firewall rules) would fail.

See also[Broadcom Knowledge Article 396719](https://knowledge.broadcom.com/external/article?articleNumber=396719). Workaround Upgrade to NSX 4.2.3.1 or later immediately to avoid being impacted by this issue. For step-by-step instructions on upgrading your SDDC’s NSX, see[Upgrade an Oracle Cloud VMware Solution Software-Defined Data Center from 7.x to 8.x](https://docs.oracle.com/en/learn/upgrade-ocvs-sddc-7-to-8/#task-31-upgrade-nsx)
