# Toolkit for Eclipse
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/eclipsetoolkit.htm
- Fetched: 2026-09-05 01:36 CDT

# Toolkit for Eclipse

The Oracle Cloud Infrastructure Toolkit for Eclipse is an open source plug-in for the Eclipse Integrated Development Environment (IDE).

The Oracle Cloud Infrastructure Toolkit for Eclipse is an open source plug-in for the Eclipse Integrated Development Environment (IDE). The toolkit provides a set of features that help developers connect to Oracle Cloud Infrastructure from within Eclipse. For example, you can use the toolkit to deploy an application to a VM in the cloud by using Kubernetes Engine, or upload multiple files to Object Storage with one click. The Compute feature enables you to start a compute instance or restart it if needed. You can also switch between multiple accounts and regions from the Eclipse IDE.

Download : To install the Toolkit, download the`com.oracle.oci.eclipse.zip`toolkit from[the releases section on GitHub](https://github.com/oracle/oci-toolkit-eclipse/releases), then follow the instructions in[Getting Started with Toolkit for Eclipse](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/eclipsegettingstarted.htm).

## Requirements

To use the Oracle Cloud Infrastructure Toolkit for Eclipse, you must have the following:
- An Oracle Cloud Infrastructure account
- A user created in that account, in a group with a policy that grants the desired permissions. This can be a user for yourself, or another person/system that needs to call the API. For an example of how to set up a new user, group, compartment, and policy, see[Adding Users](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingusers.htm). For a list of typical policies you may want to use, see[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
- A key pair used for signing API requests, with the public key uploaded to Oracle. For more information on generating and uploading keys, see[Required Keys and OCIDs](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm).
- [SDK for Java](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/javasdk.htm)
- Eclipse IDE for Java Developers 4.3 or later

## Services Supported

- Compute
- Object Storage
- Autonomous AI Database
- Kubernetes Engine

## Contact Us

### Contributions

Got a fix for a bug or a new feature you'd like to contribute? The plug-in is open source and accepting pull requests on[GitHub](https://github.com/oracle/oci-toolkit-eclipse/).

### Notifications

To be notified when a new version of the toolkit is released, subscribe to the[Atom feed](https://github.com/oracle/oci-toolkit-eclipse/releases.atom).

### Questions or Feedback
- [GitHub Issues](https://github.com/oracle/oci-toolkit-eclipse/issues): To file bugs and feature requests only
- [Developer Tools section](https://cloudcustomerconnect.oracle.com/resources/9c8fa8f96f/search/posts?find=&daysBack=0&userName=&tagName=Developer+Tools&type=)of the Oracle Cloud forums
- [My Oracle Support](https://support.oracle.com/)
