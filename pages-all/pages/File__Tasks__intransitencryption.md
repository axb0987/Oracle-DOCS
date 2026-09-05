# Using In-transit TLS Encryption
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm
- Fetched: 2026-09-05 02:03 CDT

# Using In-transit TLS Encryption

In-transit encryption using`oci-fss-utils`or stunnel provides a way to secure your data between instances and mounted file systems using TLS v.1.3 (Transport Layer Security) encryption. Together with other methods of security such as Oracle Cloud Infrastructure Vault and File Storage's encryption-at-rest, in-transit encryption provides for end-to-end security.
Tip  
  
If you[use Kerberos for authentication](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/kerberos.htm), the KRB5P security option provides authentication over NFS, data integrity (unauthorized modification of data in-transit), and data privacy as an alternative in-transit encryption option.
- For general information about getting started with file systems, see[Overview of File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/filestorageoverview.htm).
- For more information on the Vault service, see[Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm).
- For more information on securing your file system, see[About File Storage Security](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/../Concepts/securitylayers.htm)and the[Securing File Storage](https://docs.oracle.com/iaas/Content/Security/Reference/filestorage_security.htm)reference in the[Security Guide](https://docs.oracle.com/iaas/Content/Security/Concepts/security.htm).

In-transit encryption using`oci-fss-utils`or stunnel doesn't require any updates to your file system's mount target or export configuration, but the steps differ for[Linux users](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#intransitencryption-linux)and[Windows users](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#intransitencryption-windows).

## Prerequisites

Add the required rules to the security list for the mount target subnet. Alternatively, you can add the following rules to a Network Security Group (NSG) and then add the mount target to the NSG. For more information and instructions about adding security list rules for File Storage, see[Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm), in particular[Scenario C: Mount target and instance use TLS in-transit encryption](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/securitylistsfilestorage.htm#scenario-c).
Important  
  

Only the rules for TCP port 2051 are required for encrypted access.

## In-transit Encryption for Linux Users

To enable in-transit encryption, you install a package called`oci-fss-utils`on the instance. The`oci-fss-utils`tool is available for the following instance types:
- Oracle Linux, CentOS 8 x86
- Oracle Linux, CentOS 9 x86
- Oracle Linux, CentOS 8 Arm*
- Oracle Linux, CentOS 9 Arm*

*Oracle offers an Arm-based compute platform based on the Ampere Altra processor. See[Arm-Based Compute](https://docs.oracle.com/iaas/Content/Compute/References/arm.htm)for more information.

### How In-transit Encryption is Enabled

The`oci-fss-utils`package creates a network namespace and virtual network interface on your instance and provides a local NFS endpoint. The`oci-fss-utils`package also runs a forwarder process in the background called`oci-fss-forwarder`.

The network namespace isolates the forwarder process from the instance's networking environment. The virtual network interface provides the forwarder process a unique IP address. The local NFS endpoint provides NFS connection capability.

The file system is mounted using a special command that initiates encryption. After the file system is mounted, the`oci-fss-forwarder`process connects the local NFS client to the NFS endpoint. The process then receives requests from the NFS client, encrypts them and sends them to the mount target using a TLS tunnel.

Here are the general steps for setting up In-transit encryption:
- Ensure that you meet the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#intransitencryption-prerequisites)before setting up in-transit encryption.
- 

Install the`oci-fss-utils`package.
- If you're using Oracle Linux, see[1. Install the OCI-FSS-UTILS package](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#install-ol).
- If you're using CentOS, see[Manual and offline installation](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#install-manual).
- Use the in-transit encryption command to mount the file system. For instructions, see[2. Mount the file system with the encryption command](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#mount).

### Limitations and Considerations

- The in-transit encryption installation package is distributed as an RPM for Oracle Linux and CentOS. Oracle Linux users can install the package using yum. It can also be downloaded from the[Oracle Linux yum Repository](https://yum.oracle.com/).
- You must install the`oci-fss-utils`package on every instance that requires encrypted access to a mount target.
- The number of encrypted NFS/TLS connections for a single mount target is limited to 4096.
- DNS hostnames aren't supported for mounting encrypted file systems with`oci-fss-forwarder`. Use the mount target IP address to mount encrypted file systems.
Important  
  
If you're not using the latest version of the`oci-fss-utils`package, you might experience SSL connection failures. SSL connection failures can cause NFSv3 operations to fail.

We recommend that you always[upgrade to the latest version](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#upgrade)of the`oci-fss-utils`package as soon as it's available. See[File Storage Release Notes](https://docs.oracle.com/iaas/releasenotes/services/filestorage/)for information about new RPM version releases.

### Setting up In-transit Encryption for Linux

[1. Install the OCI-FSS-UTILS package](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#)

Oracle Linux users can directly install the TLS utility from the Oracle Linux yum repository.
- Open a terminal window on the destination instance.
- 

Ensure that the Oracle developer yum repository is enabled for the version of Oracle Linux using the following command:

```

```

Install the package using the following command:

```

```

The package creates a namespace called`ns1`in your instance, which contains a default network interface for ethernet traffic. A network interface pair is created for each mount target.

After the package has finished installing, proceed to[2. Mount the file system with the encryption command](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#mount).

[Manual and offline installation](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#)

Internet access is required to download the RPM installation package. If the destination instance doesn't have internet access, you can download the RPM to a staging instance on your network and then use the`scp`command to securely copy the RPM from the staging instance to the destination instance.

The`scp`command requires an SSH key pair to authenticate a remote user. If your instances are UNIX-style systems, you probably already have the`ssh-keygen`utility installed. To check if it's installed, open a shell or terminal and type`ssh-keygen`on the command line. If it's not installed, you can obtain OpenSSH for UNIX from[http://www.openssh.com/portable.html](http://www.openssh.com/portable.html).
- 

(Optional) Create a directory for the RPM installation package on the destination instance. For example:

```

```

- 

Download the latest`oci-fss-utils`package from the[Oracle Linux yum Repository](https://yum.oracle.com/)to the directory on the destination instance or to a staging instance on your network.
- From the[Oracle Linux yum Repository](https://yum.oracle.com/)page, under Browse the Repositories , select an Oracle Linux version.
- Under Packages for Test and Development , find Developer Packages and then select the Linux architecture type, such as x86_64 or aarch64.
- 

Find and select the latest version of the`oci-fss-utils`package. For more information about the latest version, see[File Storage Release Notes](https://docs.oracle.com/iaas/releasenotes/services/filestorage/).
- 

If you downloaded the package to a staging instance, open a terminal window on the staging instance, and use the`scp`command to securely copy the RPM from the staging instance to the destination instance. For example:

```

```

Skip this step if you downloaded the package directly to the destination instance.
- 

If the file name of the downloaded package doesn't include the package version and architecture, use the following command to identify the RPM file to be installed:
```

```

After the package is identified, rename the file using the RPM returned by the query. For example:
```

```

- 

Install the package using the following command:

```

```

The package creates a namespace called`ns1`in the instance, which contains a default network interface for ethernet traffic. A network interface pair is created for each mount target.

After the package has finished installing, proceed to[2. Mount the file system with the encryption command](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#mount).

[2. Mount the file system with the encryption command](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#)

- Open a terminal window in the instance.
- 

Create a mount point by typing the following, replacing`yourmountpoint`with the local directory from which you want to access the file system.

```

```

- 

Mount the file system using the following command:

```

```

Replace`10.x.x.x:`with the local subnet IP address assigned to the mount target,`fs-export-path`with the export path you specified when associating the file system with the mount target, and`yourmountpoint`with the path to the local mount point. The export path is the path to the file system (relative to the mount target IP address).
If you have installed`oci-fss-utils`version 2.0-1 or later, you can mount the file system in FIPS approved mode by including`-o fips`in the mount command. For example:
```

```

Important  
  
DNS hostnames aren't supported for mounting file systems with the`mount -t oci-fss`command. You must use the mount target IP address.

Each time you mount a file system using this command,`systemd-managed`service creates a new`oci-fss-forwarder`service with a name such as`oci-fss-0 <number> .service`.
Tip  
  

By default, the tool's NFS client uses reserved ports during mounting. Use the mount option`noresvport`if you need to use non-privileged ports.

### Managing In-transit Encryption for Linux

[Auto-mount a file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#)

Auto-mount ensures that a file system is automatically re-mounted on an instance if it is rebooted.
- Open a terminal window on the instance. Mount the file system as described in[2. Mount the file system with the encryption command](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#mount).
- 

Open the`/etc/fstab`file for editing:

```

```

```

```

- 

Add the following line to the`fstab`file:

```

```

Replace`10.x.x.x:`with the local subnet IP address assigned to your mount target,`fs-export-path`with the export path you specified when associating the file system with the mount target, and`yourmountpoint`with the path to the local mount point.
If you have installed`oci-fss-utils`version 2.0-1 or above, you can mount the file system in FIPS approved mode by including`-o fips`in the mount command. For example:
```

```

Important  
  
DNS hostnames aren't currently supported for mounting file systems with the`mount -t oci-fss`command. You must use the mount target IP address.
Tip  
  

You can use the`resvport`option to restrict the client to using a specific reserved port. For example:

```

```

[Unmount a file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#)

When you unmount a file system, you must use another`oci-fss-utils`command to ensure that the associated local network namespace is removed:
- Open a terminal window on the instance.
- 

Use the following command to unmount the file system:

```

```

Replace`yourmountpoint`with the path to the local mount point.

[Upgrade the OCI-FSS-UTILS package](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#)

If you're using a deprecated version of the`oci-fss-utils`utility, such as`oci-fss-utils-3. x`, or you want to take advantage of new features, you can upgrade to a newer version. You can find version information in the[File Storage Release Notes](https://docs.oracle.com/iaas/releasenotes/services/filestorage/).

When upgrading`oci-fss-utils`to a new version, any new settings, such as a new IP address or TLS forwarder process name, won't be applied until the file system is remounted.
Note  
  
Remounting is required if you're upgrading the`oci-fss-utils`utility so that the TLS client can use an IPv6 address. Applications using the mounted file system will experience downtime while you remount the file system.
- Open a terminal window on the destination instance.
- 

Upgrade the package.
- 

Oracle Linux users can upgrade`oci-fss-utils`from the Oracle Linux yum repository. Ensure that the Oracle developer yum repository is enabled for the version of Oracle Linux using the following command:

```

```

Then, upgrade the package using the following command:

```

```

- 

If you don't use Oracle Linux, download the latest`oci-fss-utils`package from the Oracle Linux yum repository. For instructions, see[Manual and offline installation](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#install-manual). Then, upgrade the package using the following command:

```

```

- 

After upgrading, verify the version of`oci-fss-utils`using the following command:

```

```

- [Unmount the file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#unmount)and[remount the file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#mount)so that new settings can take effect.

[To uninstall the OCI-FSS-UTILS package](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#)

- First, unmount all mounted file systems. For instructions, see[Unmount a file system](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#unmount).
- Open a terminal window on the instance.
- 

Type the following command to uninstall the`oci-fss`package:

```

```

## In-transit Encryption for Windows Users

Windows clients can use stunnel to enable in-transit encryption to file systems.

### Limitations and Considerations

- The number of encrypted NFS/TLS connections for a single mount target is limited to 64. This limitation is caused by TLS memory requirements. Unlike NFS connections, TLS connections do not share memory buffers. So, once a TLS connection has been established, the allocated memory stays dedicated to it.
- DNS hostnames are not supported for mounting encrypted file systems. Use the mount target IP address to mount encrypted file systems.

### Setting up In-transit Encryption for Windows

These instructions describe how to install and set up stunnel to use in-transit encryption with your file systems. Ensure that you meet the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#intransitencryption-prerequisites)before setting up in-transit encryption.
Tip  
  
You can automate this process by using a batch script that contains the following steps.

#### Setup Tasks

[Task 1: Install the Windows NFS Client](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#)

- 

Open Windows PowerShell on your target instance and use the following command to install the Windows NFS Client:

```

```

After the client is installed, proceed to[Task 2: Download and Install stunnel](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#intransitencryption-windows-setup-2-stunnel).

[Task 2: Download and Install stunnel](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#)

- 

Download and install stunnel from[https://www.stunnel.org/downloads.html](https://www.stunnel.org/downloads.html).

Note  
  
The last installation step requests certificate information. Entering a value here is optional.

By default, stunnel is installed to the following directory:`C:\Program Files (x86)\stunnel`
- 

Open the file`C:\Program Files (x86)\stunnel\config\stunnel.cfg`for editing and specify the following configuration:

```

```

- 

Start stunnel using`C:\Program Files (x86)\stunnel\bin\tstunnel.exe`.

Proceed to[Task 3: Mount and Test Your Connection](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#intransitencryption-windows-setup-3-test).

[Task 3: Mount and Test Your Connection](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/intransitencryption.htm#)

Open a command prompt and type the following series of commands:
- 

Mount the file system:

```

```

- 

Test the connection to the file system by listing the contents of the directory:

```

```

- 

Unmount the file system:

```

```
