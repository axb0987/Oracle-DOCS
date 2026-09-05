# Setting Up Cluster Access
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm
- Fetched: 2026-09-05 01:55 CDT

# Setting Up Cluster Access

Find out about the steps to set up access to the clusters you create using Kubernetes Engine (OKE). Having completed the steps, you can start using kubectl to manage the cluster.

To access a cluster using kubectl, you have to set up a Kubernetes configuration file (commonly known as a 'kubeconfig' file) for the cluster. The kubeconfig file (by default named`config`and stored in the`$HOME/.kube`directory) provides the necessary details to access the cluster. Having set up the kubeconfig file, you can start using kubectl to manage the cluster.

The steps to follow when setting up the kubeconfig file depend on how you want to access the cluster:
- 

To access the cluster using kubectl in Cloud Shell, run an Oracle Cloud Infrastructure CLI command in the Cloud Shell window to set up the kubeconfig file.

See[Setting Up Cloud Shell Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#cloudshelldownload).
- 

To access the cluster using a local installation of kubectl:
- Generate an API signing key pair (if you don't already have one).
- Upload the public key of the API signing key pair.
- Install and configure the Oracle Cloud Infrastructure CLI.
- Set up the kubeconfig file.

See[Setting Up Local Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#localdownload).

## Setting Up Cloud Shell Access to Clusters

When a cluster's Kubernetes API endpoint has a public IP address, you can access the cluster in Cloud Shell by setting up a kubeconfig file.
Note  
  

To access a cluster with a private Kubernetes API endpoint in Cloud Shell, you can configure a bastion using the Oracle Cloud Infrastructure Bastion service. For more information, see[Setting Up a Bastion for Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm).

To set up the kubeconfig file:

[Step 1: Set up the kubeconfig file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#)

- On the Clusters list page, select the name of the cluster you want to access using kubectl. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- From the Actions menu, select Access cluster .
- In the Access cluster dialog, select Cloud Shell Access .
- Select Launch Cloud Shell to display the Cloud Shell window. For more information about Cloud Shell (including the required IAM policy), see[Cloud Shell](https://docs.oracle.com/iaas/Content/API/Concepts/devcloudshellintro.htm).
- 

Run the Oracle Cloud Infrastructure CLI command to set up the kubeconfig file and save it in a location accessible to kubectl.

For example, enter the following command (or copy and paste it from the Access cluster dialog) in the Cloud Shell window:

```

```

where:
- `ocid1.cluster.oc1.phx.aaaaaaaaae...`is the OCID of the current cluster. For convenience, the command in the Access cluster dialog already includes the cluster's OCID.
- `--kube-endpoint PUBLIC_ENDPOINT`specifies to add the public IP address of the cluster's Kubernetes API endpoint to the kubeconfig file. For more information, see[Kubernetes Cluster Control Plane and Kubernetes API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengclustersnodes.htm#processes).

Note that if a kubeconfig file already exists in the location you specify, details about the cluster will be added as a new context to the existing kubeconfig file. The`current-context:`element in the kubeconfig file will be set to point to the newly-added context.
Tip  
  
For clipboard operations in the Cloud Shell window, Windows users can use Ctrl-C or Ctrl-Insert to copy, and Shift-Insert to paste. For Mac OS users, use Cmd-C to copy and Cmd-V to paste.
- 

If you don't save the kubeconfig file in the default location (`$HOME/.kube`) or with the default name (`config`), set the value of the KUBECONFIG environment variable to point to the name and location of the kubeconfig file. For example, enter the following command in the Cloud Shell window:

```

```

[Step 2: Verify that kubectl can access the cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#)

Verify that kubectl can connect to the cluster by entering the following command in the Cloud Shell window:

```

```

Information about the nodes in the cluster is shown.

You can now use kubectl to perform operations on the cluster.

## Setting Up Local Access to Clusters

When a cluster's Kubernetes API endpoint does not have a public IP address, you can access the cluster from a local terminal if your network is peered with the cluster's VCN.
Note  
  

To access a cluster with a private Kubernetes API endpoint from a local terminal, you can also configure a bastion using the Oracle Cloud Infrastructure Bastion service. For more information, see[Setting Up a Bastion for Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm).

To set up the kubeconfig file:

[Step 1: Generate an API signing key pair](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#)

If you already have an API signing key pair, go straight to the next step. If not:
- Use OpenSSL commands to generate the key pair in the required PEM format. If you're using Windows, you'll need to install Git Bash for Windows and run the commands with that tool. See[How to Generate an API Signing Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#two).
- 

Copy the contents of the public key to the clipboard (you'll need to paste the value into the Console later).

[Step 2: Upload the public key of the API signing key pair](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#)

- 

In the navigation menu , select the Profile menu and then select User settings .
- 

On the Tokens and keys tab, select Add API Key .
- 

Select Paste a public key , paste the public key's value into the Public key field, and select Add .

The key is uploaded and its fingerprint is displayed (for example, d1:b2:32:53:d3:5f:cf:68:2d:6f:8b:5f:77:8f:07:13).

[Step 3: Install and configure the Oracle Cloud Infrastructure CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#)

- 

Install the Oracle Cloud Infrastructure CLI version 2.6.4 (or later). See[Installing the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm).
- Configure the Oracle Cloud Infrastructure CLI. See[Configuring the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliconfigure.htm).

[Step 4: Set up the kubeconfig file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#)

- On the Clusters list page, select the name of the cluster you want to access using kubectl. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- From the Actions menu, select Access cluster .
- Select Local Access .
- 

Create a directory to contain the kubeconfig file. By default, the expected directory name is`$HOME/.kube`.

For example, on Linux, enter the following command (or copy and paste it from the Access cluster dialog) in a local terminal window:

```

```

- 

Run the Oracle Cloud Infrastructure CLI command to set up the kubeconfig file and save it in a location accessible to kubectl.

For example, on Linux, enter the following command (or copy and paste it from the Access cluster dialog) in a local terminal window:

```

```

where:
- `ocid1.cluster.oc1.phx.aaaaaaaaae...`is the OCID of the current cluster. For convenience, the command in the Access cluster dialog already includes the cluster's OCID.
- `--kube-endpoint PRIVATE_ENDPOINT|PUBLIC_ENDPOINT`specifies whether to add the private IP address or the public IP address of the cluster's Kubernetes API endpoint to the kubeconfig file. For more information, see[Kubernetes Cluster Control Plane and Kubernetes API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengclustersnodes.htm#processes).

Note that if a kubeconfig file already exists in the location you specify, details about the cluster will be added as a new context to the existing kubeconfig file. The`current-context:`element in the kubeconfig file will be set to point to the newly-added context.
- 

If you don't save the kubeconfig file in the default location (`$HOME/.kube`) or with the default name (`config`), set the value of the KUBECONFIG environment variable to point to the name and location of the kubeconfig file. For example, on Linux, enter the following command (or copy and paste it from the Access cluster dialog) in a local terminal window:

```

```

[Step 5: Verify that kubectl can access the cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#)

- 

Verify that kubectl is available by entering the following command in a local terminal window:

```

```

The response shows:
- the version of kubectl installed and running locally
- the version of Kubernetes (strictly speaking, the version of the kube-apiserver) running on the cluster's control plane nodes

Note that the kubectl version must be within one minor version (older or newer) of the Kubernetes version running on the control plane nodes. If kubectl is more than one minor version older or newer, install an appropriate version of kubectl. See[Kubernetes version and version skew support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/)in the Kubernetes documentation.

If the command returns an error indicating that kubectl is not available, install kubectl (see the[kubectl documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl/)), and repeat this step.
- 

Verify that kubectl can connect to the cluster by entering the following command in a local terminal window:

```

```

Information about the nodes in the cluster is shown.

You can now use kubectl to perform operations on the cluster.

## Notes about Kubeconfig Files

Note the following about kubeconfig files:
- A single kubeconfig file can include the details for multiple clusters, as multiple contexts. The cluster on which operations will be performed is specified by the`current-context:`element in the kubeconfig file.
- A kubeconfig file includes an Oracle Cloud Infrastructure CLI command that dynamically generates an authentication token and inserts it when you run a kubectl command. The Oracle Cloud Infrastructure CLI must be available on your shell's executable path (for example, $PATH on Linux).
- The authentication tokens generated by the Oracle Cloud Infrastructure CLI command in the kubeconfig file are short-lived, cluster-scoped, and specific to individual users. As a result, you cannot share kubeconfig files between users to access Kubernetes clusters.
- 

The Oracle Cloud Infrastructure CLI command in the kubeconfig file uses your current CLI profile when generating an authentication token. If you have defined multiple profiles in different tenancies in the CLI configuration file (for example, in ~/.oci/config), specify which profile to use when generating the authentication token as follows. In both cases,`<profile-name>`is the name of the profile defined in the CLI configuration file:
- 

Add`--profile`to the`args:`section of the kubeconfig file as follows:

```

```

- 

Set the OCI_CLI_PROFILE environment variable to the name of the profile defined in the CLI configuration file before running kubectl commands. For example:

```

```

```

```

- The authentication tokens generated by the Oracle Cloud Infrastructure CLI command in the kubeconfig file are appropriate to authenticate individual users accessing the cluster using kubectl. However, the generated authentication tokens are unsuitable if you want other processes and tools to access the cluster, such as continuous integration and continuous delivery (CI/CD) tools. In this case, consider creating a Kubernetes service account and adding its associated authentication token to the kubeconfig file. For more information, see[Adding a Service Account Authentication Token to a Kubeconfig File](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingserviceaccttoken.htm).
- 

An IAM policy might have been defined to restrict cluster access to only users that have been verified with multi-factor authentication (MFA). If such a policy exists, you have to add`--profile`and`--auth`arguments to the kubeconfig file to enable an MFA-verified user to access the cluster using kubectl, as follows. In both cases,`<profile-name>`is the name of the MFA-verified user's profile defined in the Oracle Cloud Infrastructure CLI configuration file:
- 

Add the following arguments to the`args:`section of the kubeconfig file:

```

```

For example:

```

```

- 

Set the OCI_CLI_PROFILE environment variable to the name of the MFA-verified user's profile defined in the CLI configuration file before running kubectl commands. For example:

```

```

```

```

After updating the kubeconfig file, the user you use to access the cluster must be MFA-verified. If you attempt to access the cluster using a user that has not been MFA-verified, the message`error: You must be logged in to the server (Unauthorized)`is displayed.

For more information about MFA-verified users, see[Managing Multifactor Authentication](https://docs.oracle.com/iaas/Content/Identity/Tasks/usingmfa.htm).

## Upgrading Kubeconfig Files from Version 1.0.0 to Version 2.0.0

Kubernetes Engine currently supports kubeconfig version 2.0.0 files, and no longer supports kubeconfig version 1.0.0 files.

Enhancements in kubeconfig version 2.0.0 files provide security improvements for your Kubernetes environment, including short-lived cluster-scoped tokens with automated refreshing, and support for instance principals to access Kubernetes clusters. Additionally, authentication tokens are generated on-demand for each cluster, so kubeconfig version 2.0.0 files cannot be shared between users to access Kubernetes clusters (unlike kubeconfig version 1.0.0 files).

Note that kubeconfig version 2.0.0 files are not compatible with kubectl versions prior to version 1.11.9. If you are currently running kubectl version 1.10.x or older, upgrade kubectl to version 1.11.9 or later. For more information about compatibility between different versions of kubernetes and kubectl, see the[Kubernetes documentation](https://kubernetes.io/docs/setup/release/version-skew-policy/).

Follow the instructions below to determine the current version of kubeconfig files, and how to upgrade any remaining kubeconfig version 1.0.0 files to version 2.0.0.

### Determine the kubeconfig file version

To determine the version of a cluster's kubeconfig file:

1. In a terminal window (the Cloud Shell window or a local terminal window as appropriate), enter the following command to see the format of the kubeconfig file currently pointed at by the KUBECONFIG environment variable:

```

```

2. If the kubeconfig file is version 1.0.0, you see a response in the following format:
```

```

If you see a response in the above format, you have to upgrade the kubeconfig file. See[Upgrading Kubeconfig Files from Version 1.0.0 to Version 2.0.0](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#upgrading).

3. If the kubeconfig file is version 2.0.0, you see a response in the following format:
```

```

If you see a response in the above format, no further action is required.

### Upgrade a kubeconfig version 1.0.0 file to version 2.0.0

To upgrade a kubeconfig version 1.0.0 file:
- 

In the case of a local installation of kubectl, confirm that Oracle Cloud Infrastructure CLI version 2.6.4 (or later) is installed by entering:

```

```

If the Oracle Cloud Infrastructure CLI version is earlier than version 2.6.4, upgrade the CLI to a later version. See[Upgrading the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliupgrading.htm).
- 

Follow the appropriate instructions to set up the kubeconfig file for use in Cloud Shell or locally (see[Setting Up Cloud Shell Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#cloudshelldownload)or[Setting Up Local Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#localdownload)). Running the`oci ce cluster create-kubeconfig`command shown in the Access Your Cluster dialog box upgrades the existing kubeconfig version 1.0.0 file. If you change the name or location of the kubeconfig file, set the KUBECONFIG environment variable to point to the new name and location of the file.
- Confirm the kubeconfig file is now version 2.0.0:
- 

In a terminal window (the Cloud Shell window or a local terminal window as appropriate), enter:

```

```

- 

Confirm that that the response is in the following format:
```

```
