# Accessing Roving Edge
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Access/access.htm
- Fetched: 2026-09-05 02:57 CDT

# Accessing Roving Edge

Learn about the different methods for accessing Roving Edge Infrastructure resources.

There are two two browser-based consoles you can use to manage Roving Edge resources:
- [Oracle Cloud Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/access.htm#OCIConsole): Use to manage Roving Edge nodes in your tenancy, and to manage all your Oracle Cloud Infrastructure (OCI) resources.
- [Roving Edge Device Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/access.htm#RoverConsole): Use to manage all the resources on Roving Edge devices.
Note  
  

Use only ASCII text for all inputs to Roving Edge Infrastructure and Roving Edge Infrastructure devices. This requirement applies to the browser-based Consoles, CLIs, and APIs.

In addition to the consoles, you can also manage OCI and Roving Edge device resources using the OCI CLI and API.

## Accessing the Oracle Cloud Console

You can manage your Roving Edge Infrastructure nodes that are in your OCI tenancy using the Oracle Cloud Console.
Note  
  
You must have internet access to access the Oracle Cloud Infrastructure Cloud Console.

A Roving Edge node is an Oracle Cloud Infrastructure (OCI) resource that represents a Roving Edge device. You can create, view, edit and delete nodes. You can also request a system upgrade bundle for the device.

To manage your Roving Edge nodes or request upgrade bundles, perform these steps:
- 

Sign in to the Oracle Cloud Console as you normally sign in to your OCI tenancy. The sign-in URL is[https://www.oracle.com/cloud/sign-in.html](https://www.oracle.com/cloud/sign-in.html).

For more information about signing in to the Oracle Cloud Console, see[Sign in to the Oracle Cloud Console](https://docs.oracle.com/iaas/visual-builder/doc/signing-oci-console-1.html).
- 

Use the navigation menu to go to Hybrid , then select Nodes .

For more information about managing nodes, see[Managing Device Nodes](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/../Setup-RED/managing-device-nodes.htm#managing-device-nodes).

For more information about requesting upgrade bundles, see[Upgrading the Roving Edge Device Software while Disconnected](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/../Device_Software/upgrade_devices_offline.htm#update-device-software-disconnected).

To manage resources on Roving Edge devices, see[Accessing the Roving Edge Device Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/access.htm#RoverConsole).

## Accessing the Roving Edge Device Console

Use the browser-based Roving Edge Device Console to manage your workloads, perform tasks, and monitor system health. No internet access is required to access the Device Console.
Important  
  

Securely store the Device Console password. If you lose or forget this password, you can't retrieve it and you're no longer able to access the Device Console. Don't share this password with other users who might reset the password and not communicate the change. We recommend you closely manage your Device Console passwords within your organization.

Requirement

Your browser must have a valid CA certificate downloaded from each Roving Edge device you access. See[Download the Root CA Certificate](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/../Setup-RED/downloading-the-root-ca-certificate.htm#downloading-the-root-ca-certificate)and[Certificate Management](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/../certificate-management.htm#certificate-management).
- 

Enter the following address in your browser address field:

```

```

- Enter your username.
- 

Enter your password.

When you first sign in to the Device Console, you're prompted to regenerate a new password.

Device Console user passwords expire after 90 days. An administrator with access to the serial console root user can reset the user passwords. See[Resetting a Device Console Password](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/../Getting_Started/resetting-web-console-user-accounts.htm#managing-web-console-user-accounts).

### User Management

We recommend creating users and assigning them to user groups. You can then apply permissions to these user groups for better access management. See[Identity and Access Management (IAM)](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/../IAM/identity_management.htm#IAM).

### Device Console Sessions

You can have a maximum of three Device Console sessions per user connected to a Roving Edge Infrastructure device at a time. A session is considered a user sign-in into Roving Edge Infrastructure device from a single browser. You can have several tabs open within a specific browser, such as Chrome or Firefox, but it's still considered a single session. However, using two or more different browsers counts as separate sessions toward the maximum.

If you try to access Device Console sessions beyond this maximum limit, you receive an error. If you're at the maximum number of allowed sessions, close an existing session by logging out of the Device Console before opening a new one.

A Device Console session is automatically ended after 15 minutes of inactivity. When active, a session is automatically ended after 4 hours.

### API Keys

You can set up API keys and use them to communicate with the RED using the Oracle Cloud Infrastructure command line interface (CLI). See[API Signing Keys](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/../IAM/User_Credentials/API_Key/api-key_management.htm#APISigningKeyManagement).

The following example shows how you can use the CLI to set up API keys for managing the password:
```

```

## Command Line Interface

The Oracle Cloud Infrastructure Command Line Interface (CLI) provides a set of commands for configuring and running Roving Edge Infrastructure tasks. Use the CLI as an alternative to running commands from the Device Console. Sometimes you must use the CLI to complete certain tasks where no Device Console equivalent is available.

Use the CLI to perform Roving Edge Infrastructure service tasks within the Oracle Cloud Infrastructure cloud. These tasks can include requesting nodes, and running tasks directly on device nodes. Install the CLI separately on each device. CLIs installed on devices run locally within your environment and don't require internet access.

See[Using the Command Line Interface](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI)for information on how to install, set up, and use CLIs with Roving Edge Infrastructure.

## API

Roving Edge Infrastructure provides REST APIs for most of its supported features and functionality.[API Reference and Endpoints](https://docs.oracle.com/iaas/api/)provides endpoint details and links to the available API reference documents. For general information about using the API, see[REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs)
