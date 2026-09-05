# Using Toolkit for Eclipse
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/eclipseusing.htm
- Fetched: 2026-09-05 01:36 CDT

# Using Toolkit for Eclipse

This section describes how to use the OCI Toolkit for Eclipse.

After configuring the[Oracle Cloud Infrastructure Preferences](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/eclipsegettingstarted.htm#Configuring_the_Toolkit__Prefere), you can connect to your tenancy via Eclipse and use the Oracle Cloud Infrastructure Explorer to view and update your resources. You can also switch between different accounts saved in the profile.

To change the region, click the region icon in the Explorer navigation bar and select from the dropdown.

To change the compartment, click the compartment icon and select from the dropdown.

## Using the Toolkit for Eclipse with Compute Instances

In the Oracle Cloud Infrastructure Explorer, double-click Compute to view available resources.

Double-click Instances to display a list of instances. You can right-click each one in the list to start, stop, or reboot it.

You can also double-click Block Volumes to view a list of block volumes.

## Using the Toolkit for Eclipse with Object Storage

In the Oracle Cloud Infrastructure Explorer, double-click Object Storage to view available resources.

### Working with Buckets

To create a bucket, right-click Object Storage and select Create New Bucket .

To view content and details, double-click or right-click the bucket and select Open Bucket .

To delete a bucket, view the bucket's details and click Delete Bucket .

### Working with Objects

To upload an object, select the destination bucket and view its details. Right-click the Object list and select Upload Object . You can also drag one or more files to the Object list to upload.

To download one or more objects, right-click and select Download Object .

To delete one or more objects, right-click and select Delete Object .

## Deploy Applications using Kubernetes Engine

### Prerequisites
- Install[Docker Desktop v2.2.0.0](https://docs.docker.com/docker-for-windows/release-notes/#docker-desktop-community-2200)or higher.
- Verify that Docker desktop is running, and that the Docker CLI client and Kubernetes CLI client (kubectl) are available in the command line.
- Install the[Oracle Cloud Infrastructure command line client (OCI CLI)](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm).
- Verify that OCI CLI works by typing "oci" on command prompt. This should return a list of all the services supported by OCI CLI.

### Deploy an Application to Kubernetes Engine
- In the Oracle Cloud Infrastructure Explorer, double-click Container Engine for Kubernetes .
- Double-click Container Cluster (OKE) to display a list of available clusters. A cluster should be created prior to this step in the console.
- Right click on the cluster name and select Deploy Docker Image to OKE .
-
