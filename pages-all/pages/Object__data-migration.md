# Moving Data to and from Object Storage
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/data-migration.htm
- Fetched: 2026-09-05 02:52 CDT

# Moving Data to and from Object Storage

Learn how to move your data between Object Storage and other data hosting systems.

Use the Rclone tool to synchronize files and directories between an Object Storage bucket and other cloud storage providers, or between an Object Storage bucket and on-premises systems. Rclone is known for its simplicity, efficiency, and wide support for many cloud services, including Object Storage. For more information, see[Rclone](https://rclone.org/).

## Prerequisites

Installation and use of Rclone has the following prerequisites:
- You must have permissions to create and edit files, create directories and folder, run commands, and install software on your laptop or workstation
- You must have access to your Object Storage and to your target cloud storage.

## Installing Rclone

If you already have a networking environment set up in your tenancy with VCN and networks and can launch compute instances, you can run this lab on an OCI Compute instance. We recommend using Oracle Linux.

### Linux and BSD Systems

Open a terminal and run the following command:
```

```

### Windows

Download the correct installation file for your processor type:
- [Intel/AMD-64 Bit](https://downloads.rclone.org/rclone-current-windows-amd64.zip)
- [Intel/AMD-32 Bit](https://downloads.rclone.org/rclone-current-windows-386.zip)
- [ARM-64 Bit](https://downloads.rclone.org/rclone-current-windows-arm64.zip)

Extract the file and add the final location of the Rclone executable file (`.exe`) to your Windows system PATH environment variable for easy command line access.

### Mac OS

Open a terminal window and install Rclone on Mac OS X using Homebrew:
```

```

## Installing OCI CLI

Use of the OCI command line interface (CLI) is required to use Rclone to move your data to and from Object Storage. To set up the OCI CLI on your computer, see[Installing the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm).

## Configuring Rclone

- Record the full path to your OCI CLI configuration file, which is named`config`.
This configuration file's location is typically the in`.oci`directory under your home directory. For example:
```

```

On Windows, the CLI configuration file would reside in the following location:
```

```

- Open the CLI configuration file and record the region name and the tenancy OCID.
The following example shows how the CLI configuration file would look with the user OCID, API Key fingerprint, tenancy OCID, home region, and the private API Key_file path:
```

```

- Run the following CLI command to get your tenancy namespace:

```

```

You need this namespace later in the steps.
- Create the directory that will contain the Rclone configuration file (`rclone.conf`) that you will create later.
For example:
```

```

On Windows, create the following directory as:
```

```

- Navigate to the`Rclone`directory you created.
- Using your favorite text editor, create a file named`rclone.conf`containing the following content:

```

```

The first line in square brackets (`[oci]`) is the name of remote. In this example,`oci`is used to identify the remote as Oracle Cloud Infrastructure. You reference this remote name when making Rclone commands.

The following example shows what the`rclone.conf`file might look like with real data:
```

```

- Run the following Rclone command to get information on the prospective target providers for the data you're moving out of OCI Object Storage:

```

```

Running`rclone config`manages the configuration of remotes, allowing you to connect and interact with various cloud storage services and other locations. It helps you to set up, update, and manage the connections to these services by storing the necessary credentials and settings in a configuration file.
- Add another entry to the`rclone.conf`file to specify the target provider of the Object Storage data being moved using the information obtained from running`rclone config`.

## Copy Data from OCI Object Storage

Copy the data from the Object Storage bucket containg your data into the target location.

### Other Cloud Providers

Contact the cloud provider or check[https://rclone.org/](https://rclone.org/)for information on how to copy data from an Object Storage bucket into the bucket of another cloud.

### On-Premises

Run the following to copy data to a local filesystem on-premises:
```

```
