# Attempts to Mount a File System with In-transit Encryption Do Not Respond or Fail
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/intransit-encryption-hangs.htm
- Fetched: 2026-09-05 02:06 CDT

# Attempts to Mount a File System with In-transit Encryption Do Not Respond or Fail

When mounting a file system using in-transit encryption, the process does not respond or fails.

Cause 1: Port 2051 is not open to TLS (Transport Layer Security) traffic. In-transit encryption uses TLS v.1.2 encryption.

Solution 1: Add the following rules to the security list for the VCN the mount target resides in, or add them to a network security group (NSG) associated to the mount target:
- A stateful ingress rule allowing TCP traffic to a Destination Port Range of 2051 .
- A stateful egress rule allowing TCP traffic from a Source Port Range of 2051 .

For more information about security rules for in-transit encryption, see[Using In-transit TLS Encryption](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/intransitencryption.htm).

For general information about security rules, see[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/securitylistsfilestorage.htm).

Cause 2: The version of`oci-fss-utils`is out of date.

Solution 2: Upgrade to the newest version of`oci-fss-utils`:
- Uninstall the old`oci-fss-utils`package. For instructions, see[To uninstall the OCI-FSS-UTILS package](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/intransitencryption.htm#uninstall).
- Download and install the newest version of the`oci-fss-utils`package. For instructions, see[Manual and offline installation](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/intransitencryption.htm#install-manual)and[1. Install the OCI-FSS-UTILS package](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/intransitencryption.htm#install-ol).
- Remount the file system. For instructions, see[2. Mount the file system with the encryption command](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/intransitencryption.htm#mount)
