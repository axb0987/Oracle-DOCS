# Known Issues for Kubernetes Engine (OKE)
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/conteng-known-issues.htm
- Fetched: 2026-09-05 01:58 CDT

# Known Issues for Kubernetes Engine (OKE)

Known issues have been identified in Kubernetes Engine.

## Worker node properties out-of-sync with updated node pool properties
Details

The properties of new worker nodes starting in a node pool do not reflect the latest changes to the node pool's properties. The likely cause is use of the deprecated quantityPerSubnet and subnetIds attributes when using the UpdateNodePoolDetails API operation to update node pool properties. Workaround

Do one of the following:
- Start using the nodeConfigDetails attribute when using the UpdateNodePoolDetails API operation. First, scale the node pool to 0 using quantityPerSubnet. Then stop using the subnetIds and quantityPerSubnet attributes, and use the nodeConfigDetails attribute instead.
- Contact Oracle Support to restart the back-end component responsible for synchronization (the tenant-agent component).

## Unable to launch Kubernetes Dashboard
Details

When you launch the Kubernetes Dashboard, in some situations you might encounter "net/http: TLS handshake timeout" and "connection reset by peer" error messages in your web browser. This issue has only been observed in newly created clusters running Kubernetes version 1.11. For details about a related Kubernetes issue, see[https://github.com/kubernetes/dashboard/issues/3038](https://github.com/kubernetes/dashboard/issues/3038). Workaround
- 

In a terminal window, enter:
```

```

- In your web browser, go to`https://localhost:8443`

## Unable to access in-cluster Helm
Details

When you use a Kubeconfig token version 2.0.0 to access Helm/Tiller versions prior to version 2.11, you will receive one of the following errors:
- `Error: Unauthorized`
- `Error: could not get Kubernetes client: exec plugin: invalid apiVersion "client.authentication.k8s.io/v1beta1"`Workaround

Upgrade Helm/Tiller as follows:
- 

In a terminal window, download a Kubeconfig token version 1.0.0 by entering the following command:

```

```

- 

Identify the region key to use to specify the Oracle Cloud Infrastructure Registry registry in the cluster's region (see[Availability by Region](https://docs.oracle.com/iaas/Content/Registry/Concepts/registryprerequisites.htm#regional-availability)). For example, if the cluster is in US East (Ashburn),`iad`is the region key to use to specify the registry in that region.
- 

Upgrade Tiller by entering the following command:

```

```

where`<region-key>`is the key that you identified in the previous step.
- 

In a browser, navigate to[https://helm.sh/docs/using_helm/#installing-the-helm-client](https://helm.sh/docs/using_helm/#installing-the-helm-client)and follow the instructions to download and install the Helm client binary.
- 

Having upgraded Helm/Tiller, download a Kubeconfig token version 2.0.0 by entering the following command:

```

```

## Some Kubernetes features (for example, the Metrics Server) cannot communicate with the kubelet via http/2
Details

The Kubernetes Engine 1.8.0 release included a security improvement to improve cipher strength on the kubelet running on customer worker nodes. New worker nodes created between August 20, 2019 and September 16, 2019 include this configuration. The new set of ciphers does not allow connections to the kubelet via http/2. This restriction impacts the Metric Server, and also the Horizontal Pod Autoscaler which depends on the Metrics Server. Workaround

For each existing worker node in turn:
- 

Prevent new pods from starting and delete existing pods on the worker node by entering`kubectl drain <node_name>`. For more information:
- about using kubectl, see[Accessing a Cluster Using Kubectl](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Tasks/contengaccessingclusterkubectl.htm)
- about the drain command, see[drain](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#drain)in the Kubernetes documentation

Recommended: Leverage pod disruption budgets as appropriate for your application to ensure that there's a sufficient number of replica pods running throughout the drain operation.
- Delete the worker node (for example, by terminating it in the Console).
- Wait for a replacement worker node to start.

The replacement worker nodes include include new settings to enable communication with the kubelet.

## Kubernetes pods fail to mount volumes due to timeouts
Details

When a new pod starts on a worker node in a cluster, in some situations the pod fails to mount all volumes attached to the node due to timeouts and you see a message similar to the following:
```

```

One possible cause identified for this issue is if the pod spec includes an`fsGroup`field in the`securityContext`field. If the container is running on a worker node as a non-root user, setting the`fsGroup`field in the`securityContext`can cause timeouts due to the number of files to which Kubernetes must make ownership changes (see[https://github.com/kubernetes/kubernetes/issues/67014](https://github.com/kubernetes/kubernetes/issues/67014)).

If the pod spec does not include an`fsgroup`field in the`securityContext`, the cause is unknown. Workaround

If the pod spec includes the`fsgroup`field in the`securityContext`and the container is running a non-root user, consider the following workarounds:
- Remove the`fsgroup`field from the`securityContext`.
- Use the`supplementalGroups`field in the`securityContext`(instead of`fsgroup`), and set`supplementalGroups`to the volume identifier.
- Change the pod spec so that the container runs as root.

If the pod spec does not include the`fsgroup`field in the`securityContext`, or if the container is already running as root, you have to restart or replace the worker node. For example, by stopping and starting the instance, by rebooting the instance, or by terminating the instance so that a new instance is started. Follow the instructions in[Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm)or[Terminating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/terminatinginstance.htm)as appropriate to use the Console or the API. Alternatively you can use CLI commands, such as the following example to terminate an instance:
```

```

where`<name>`is the worker node name, derived from the Private IP Address property of the instance (for example,`10.0.10.5`).

## OS Management causes Kubernetes cluster node pools to fail
Details

When using the OS Management service to manage operating system updates and patches on Oracle Cloud Infrastructure instances, there are some situations in which cluster node pools created by Kubernetes Engine fail to come online. Workaround

There are two possible workarounds:
- Workaround 1: If you want to use OS Management to manage Oracle Cloud Infrastructure instances, enable Oracle Enterprise Linux in OS Management. See[Managing Software Sources](https://docs.oracle.com/iaas/os-management/osms/osms-software-sources.htm).
- Workaround 2: If you don't want to use OS Management to manage Oracle Cloud Infrastructure instances, make sure there are no policies that allow OS Management to run. Specifically, remove the policy that grants a dynamic group of instances access to the OS Management service. See[Setting Up Policies for OS Management](https://docs.oracle.com/iaas/os-management/osms/osms-getstarted.htm#osms-setup-policies).

## Volume mount issues in node pools with master nodes running Kubernetes version 1.19 (or later) and worker nodes running Kubernetes version 1.18 (or earlier)

Details

If node pools have master nodes running Kubernetes version 1.19 (or later) and worker nodes running Kubernetes version 1.18 (or earlier), mounting block volumes attached to the cluster using the FlexVolume volume plugin might not work as expected. For example, you might see:
- A`FailedMount`warning message in the events of a pod running on a worker node, even though the block volume has been attached successfully.
- A`Volume not attached according to node status for volume`error message in the logs of the kubelet running on a worker node. Workaround
- If there isn't already a node pool in the cluster with worker nodes running Kubernetes version 1.19 (or later), add such a node pool now.
- Remove the affected worker node that is running Kubernetes version 1.18 (or earlier), as follows:
- Prevent new pods from starting and delete existing pods on the affected worker node by entering`kubectl drain <node_name>`. For more information:
- about using kubectl, see[Accessing a Cluster Using Kubectl](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Tasks/contengaccessingclusterkubectl.htm)
- about the drain command, see[drain](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#drain)in the Kubernetes documentation
- Delete the affected worker node (for example, by terminating it in the Console).

## Issues resolving with DNS (nslookup, dig, or curl)
Details
If the Bridge Netfilter kernel module is not enabled, traffic communication with`localhost`doesn't route correctly. For example:
```

```

To verify this issue, open a terminal window on the instance and run the following command:
```

```

If no results are returned, then the Bridge Netfilter kernel module is not enabled. The Bridge Netfilter kernel module is required to masquerade VxLAN traffic for Kubernetes pods. Workaround

Enable the Bridge Netfilter kernel module. Open a terminal window on the instance and run the following commands:
```

```

## Source client IP is not preserved for traffic through a LoadBalancer Service using externalTrafficPolicy: Local
Details

When using VCN-native pod networking, the source client IP address of inbound requests to a pod might not be preserved as expected. Instead, inbound requests received via a Kubernetes service of type LoadBalancer that has`externalTrafficPolicy: Local`set in the manifest file might be shown as originating from the worker node's IP address. Workaround

For inbound TCP requests received via a Kubernetes service of type LoadBalancer that has the`oci.oraclecloud.com/load-balancer-type: "lb"`annotation in the manifest file, obtain the source client IP address from the`X-Forwarded-For`or`X-Real-IP`header.

## Pod network connectivity issues on bare metal instances
Details

When using VCN-native pod networking, pods might be unable to communicate over the network if you have specified a bare metal shape for worker nodes in one or more of the node pools in the cluster. Workaround

Specify a VM shape for worker nodes in every node pool in the cluster when using VCN-native pod networking.

## Incorrect maximum pods per node limit for flexible shapes
Details

When using VCN-native pod networking, the maximum number of pods per worker node in a node pool might be limited to 31, regardless of the number of OCPUs you specify for the flexible shape you have selected for the node pool. Workaround

If you want more than 31 pods per worker node in a node pool, select a different shape for worker nodes in the node pool.

## Pod network connectivity issues on VCNs with added CIDR blocks
Details

When using VCN-native pod networking, pods running on worker nodes connected to a pod subnet with a CIDR block outside the first CIDR block specified for the VCN might be unable to communicate with Kubernetes services. Workaround

Create pod subnets with CIDR blocks within the first CIDR block specified for the VCN.

## Node Doctor script displays FileNotFoundError: [Errno 2] exception
Details

When using the Node Doctor script to troubleshoot node issues, the script might display an exception error message similar to the following:
```

```

The Node Doctor script will probably continue to run and, having displayed the message`Generating node doctor bundle`, produce troubleshooting output. Workaround

We are aware of the issue and working on a resolution. In the meantime, if the Node Doctor script displays the message`Generating node doctor bundle`, note that the troubleshooting output is still valid.

If you do not want the Node Doctor script to display the`FileNotFoundError: [Errno 2]...`exception error message, update the Node Doctor script by entering:

```

```

For more information about the Node Doctor script and how to update it, see[Troubleshooting Node Issues for Kubernetes Clusters Using the Node Doctor Script](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Tasks/contengtroubleshooting_topic-node_troubleshooting.htm).

## RESOLVED: DNS resolution sometimes fails in clusters using VCN-native pod networking
Details

If a cluster uses VCN-native pod networking and has both a workload pod and the CoreDNS pod running on the same worker node, DNS resolution sometimes fails because traffic is incorrectly NATed. Resolution

On 2023-03-21, an update to the OCI VCN-Native Pod Networking CNI plugin was released that resolved this issue. Follow the instructions in[Updating the OCI VCN-Native Pod Networking CNI plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_vcn_native_upgrade)to deploy the update.

## RESOLVED: Pods sometimes fail to start on a worker node running Oracle Linux 8, in clusters using VCN-native pod networking
Details

If a cluster uses VCN-native pod networking and has worker nodes running Oracle Linux 8 (OL8), pods sometimes fail to start on one of the worker nodes. The issue has the following characteristics:
- The worker node is running an OL8 image.
- Host-network related pods run as expected on the worker node, but all other pods fail to start.
- The crictl logs contain the message`Adding address to IPVLAN parent device`(indicating that an IP address is being attached to the worker node's secondary VNIC), followed by the error message`Error adding secondary VNIC IP`.
- Running the Linux`ip address`command on the worker node shows that one (or more) secondary VNICs does not have an attached IP address.
- All (or most) other worker nodes are operating as expected.

A likely cause identified for this issue is related to the NetworkManager, which manages network devices and connections. In some cases, the NetworkManager detaches the IP address attached to one or more of the worker node's secondary VNICs, causing the OCI VCN-Native Pod Networking CNI plugin to fail. Resolution

On 2023-03-21, an update to the OCI VCN-Native Pod Networking CNI plugin was released that resolved this issue. Follow the instructions in[Updating the OCI VCN-Native Pod Networking CNI plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_vcn_native_upgrade)to deploy the update.

## Worker node status unexpectedly changes to NotReady when running Oracle Linux 8.7 or Oracle Linux 8.8 with Kubernetes version 1.24.1, 1.25.4, or 1.26.2
Details

If you have specified Oracle Linux 8.7 or Oracle Linux 8.8 for a node pool (by selecting an Oracle Linux 8.7 or Oracle Linux 8.8 platform image, or an OKE worker node image built on top of Oracle Linux 8.7 or Oracle Linux 8.8), the status of the node pool's worker nodes might unexpectedly change to`NotReady`. The issue has the following characteristics:
- The worker nodes are running Oracle Linux 8.7 or Oracle Linux 8.8.
- The worker nodes are running Kubernetes version 1.24.1, 1.25.4, or 1.26.2. (Worker nodes running Kubernetes version 1.25.12, 1.26.7, and 1.27 are not affected.)
- Short-lived pods are frequently deployed on the worker nodes.
- Pods deployed on worker nodes in the node pool might also remain in the`ContainerCreating`status for longer than you expect. Workaround

We are aware of the issue and working on a resolution.

In the meantime, if you encounter this issue, use whichever of the following workarounds best meets your requirements:
- Specify an Oracle Linux 7 image for the node pool.
- Specify an Oracle Linux 8.6 image (or an earlier Oracle Linux 8 image) for the node pool.
- Specify a later version of Kubernetes for the node pool. (Worker nodes running Kubernetes version 1.25.12, 1.26.7, and 1.27 are not affected.)

To obtain the OCIDs of images that no longer appear in the Console:
- Platform images: See[All Oracle Linux 7.x Images](https://docs.oracle.com/iaas/images/oraclelinux-7x/)and[All Oracle Linux 8.x Images](https://docs.oracle.com/iaas/images/oracle-linux-8x/)
- OKE worker node images: See[All OKE Worker Node Oracle Linux 7.x Images](https://docs.oracle.com/iaas/images/oke-worker-node-oracle-linux-7x/)and[All OKE Worker Node Oracle Linux 8.x Images](https://docs.oracle.com/iaas/images/oke-worker-node-oracle-linux-8x/)

## Provisioning new worker nodes takes longer than expected in clusters using VCN-native pod networking
Details

In clusters created before June 26, 2023 that use VCN-native pod networking, you might see a delay in the provisioning of new worker nodes.

When bootstrapping worker nodes with the OCI VCN-Native Pod Networking CNI plugin, Kubernetes Engine deploys a Kubernetes custom resource (the NativePodNetwork, or NPN, resource) on each compute instance. When a worker node has been successfully bootstrapped, Kubernetes Engine gives a status of SUCCESS to the NPN resource associated with the compute instance .

In some cases, if a compute instance is terminated before Kubernetes Engine gives a status of SUCCESS to the associated NPN resource, the NPN resource remains in a BACKOFF or IN_PROGRESS status indefinitely. The existence of such 'stale' resources can delay the provisioning of new worker nodes. Resolution

The issue is fixed in clusters created after 2023-06-26. To resolve the issue in clusters created before 2023-06-26, take a one-time action to delete the stale resources by following the instructions in this section.

Before you start, make sure that your system meets the following prerequisites:
- the OCI CLI is installed (see[Installing the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm))
- the OCI CLI is configured (see[Configuring the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliconfigure.htm))
- jq has been downloaded and installed (see[https://jqlang.github.io/jq/download/](https://jqlang.github.io/jq/download/))
- an IAM policy exists that grants at least the INSTANCE_READ permission, such as`Allow group <group-name> to manage instance-family in <location>`(see[Create Required Policy for Groups](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Concepts/contengpolicyconfig.htm#policyforgroupsrequired))
- the appropriate kubeconfig files are accessible to enable you to use kubectl to manage clusters that use the OCI VCN-Native Pod Networking CNI plugin (see[Accessing a Cluster Using Kubectl](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Tasks/contengaccessingclusterkubectl.htm))

Identify and delete the stale resources as follows:
- Validate that your system meets all the prerequisites:
- Save the following script in a file named`pre-req-check.sh`:

```

```

- Run the`pre-req-check.sh`script by entering:

```

```

- Identify NPN resources that are possible candidates for deletion because they do not have a status of SUCCESS:
- Output a list of NPN resources that do not have a status of SUCCESS to a text file named`potential_stale_resources.txt`by entering:

```

```

- Optionally view the list of candidate NPN resources in`potential_stale_resources.txt`by entering:

```

```

For example,`potential_stale_resources.txt`might contain:
```

```

- Identify the stale NPN resources to delete by determining which candidate NPN resources are associated with compute instances that are not available or have been terminated:
- Save the following script in a file named`get_stale_resources.sh`:

```

```

- Run the`get_stale_resources.sh`script by entering:

```

```

The`get_stale_resources.sh`script identifies the stale NPN resources to delete, outputs processing messages to the screen, and writes the names of stale NPN resources to a file named`stale_resources.txt`. For example:
```

```

- Optionally view the list of stale NPN resources in`stale_resources.txt`by entering:

```

```

For example,`stale_resources.txt`might contain:
```

```

- Delete the stale NPN resources listed in the`stale_resources.txt`file:
- Save the following script in a file named`delete_stale_resources.sh`:

```

```

- Run the`delete_stale_resources.sh`script by entering:

```

```

The`delete_stale_resources.sh`script deletes the stale NPN resources listed in the`stale_resources.txt`file and outputs processing messages to the screen. For example:
```

```

- As good housekeeping practice, delete the`stale_resources.txt`and`potential_stale_resources.txt`files you created previously.

## Virtual node Architecture shown as AMD64 when pods scheduled to run on Arm processors
Details

When you specify an Arm shape for a virtual node, pods scheduled on the node run on Arm processors as intended. However, if you examine the virtual node using the`kubectl describe node`command or the Kubernetes API, the node's Architecture property indicates`AMD64`, even though pods scheduled on the node run on Arm processors. Workaround

We are aware of the issue and working on a resolution.

In the meantime, if you encounter this issue, ignore the value of the virtual node's Architecture property.

## OCI Load Balancers cannot be updated when delete protection is enabled
Details

When Kubernetes Engine provisions an OCI load balancer for a Kubernetes service of type LoadBalancer, the load balancer does not have delete protection enabled.

If you subsequently use the Console, the CLI, or the API to enable delete protection for the load balancer, the cloud-controller-manager is not only prevented from deleting the load balancer, but is also unable to update any of the load balancer's properties. Workaround

We are aware of the issue and working on a resolution.

In the meantime, do not use the Console, the CLI, or the API to enable delete protection for a load balancer.

Note that using the Console, the CLI, or the API to modify OCI load balancers provisioned by Kubernetes Engine is not recommended (for more information, see[Defining Kubernetes Services of Type LoadBalancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Tasks/contengcreatingloadbalancer.htm)).

## Clusters in OC2 and OC3 are not using the latest version of the OCI VCN-Native Pod Networking CNI plugin
Details

New versions of the OCI VCN-Native Pod Networking CNI plugin are normally released in the OC1, OC2, and OC3 realms.

However, on September 3, 2024, OCI VCN-Native Pod Networking CNI plugin version 2.2.0, containing security and performance enhancements, was released in the OC1 realm only.

On October 4, 2024, OCI VCN-Native Pod Networking CNI plugin version 2.2.2 was released in the OC1, OC2, and OC3 realms, containing further enhancements.

Therefore, between September 3, 2024 and October 4, 2024:
- New clusters you created in the OC2 and OC3 realms used the earlier version of the OCI VCN-Native Pod Networking CNI plugin, namely version 2.1.0.
- In the case of existing clusters in the OC2 and OC3 realms, even if you had specified that you wanted Oracle to deploy updates to the OCI VCN-Native Pod Networking CNI plugin on a cluster automatically, version 2.2.0 was not deployed on those clusters.

Regardless of whether you or Oracle is responsible for deploying updates to the OCI VCN-Native Pod Networking CNI plugin, the updates are only applied when worker nodes are next rebooted.

As a result, you might have clusters in the OC2 and OC3 realms that are still running OCI VCN-Native Pod Networking CNI plugin version 2.1.0. Workaround

To benefit from the enhancements in OCI VCN-Native Pod Networking CNI plugin versions 2.2.0 and 2.2.2, we strongly recommend that you update any cluster in OC2 or OC3 to use version 2.2.2.

OCI VCN-Native Pod Networking CNI plugin version 2.2.0 will not be released in the OC2 and OC3 realms, even though you can select version 2.2.0 in the Console.

If you enable the OCI VCN-Native Pod Networking CNI plugin for an enhanced cluster in the OC2 or OC3 realm, and specify that you want to choose the version of the add-on to deploy, do not select version 2.2.0. Instead, select version 2.2.2 (or later). If you do select version 2.2.0 for an enhanced cluster in the OC2 and OC3 realms, be aware that worker nodes will not come up and the cluster will not function.

For more information, see[Using the OCI VCN-Native Pod Networking CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm).

## Clusters exhibit unexpected delays when interacting with the Kubernetes API server (also known as kube-apiserver latency)
Details

When you work with a Kubernetes cluster created by Kubernetes Engine, you might notice unexpected delays when the cluster interacts with the Kubernetes API server (such as slow responses to kubectl commands).

If you are using a client machine with an older version of the OCI CLI and/or Python installed, these intermittent spikes in kube-apiserver latency might be due to a known OCI CLI performance issue. This performance issue has been observed with Python version 3.6 specifically.

By default, the kubeconfig file that Kubernetes Engine creates for a cluster contains an OCI CLI command to generate a token (the[oci ce cluster generate-token](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/generate-token.html)command). The token is used to authenticate requests to the kube-apiserver. Currently, each kube-apiserver request triggers an invocation of the OCI CLI to run the command to generate the token. It is this OCI CLI invocation that might be impacted by the known OCI CLI performance issue.

To confirm that kube-apiserver latency is caused by the known OCI CLI performance issue, locate and view the kubeconfig file being used by the client. In the`users`section of the kubeconfig file, locate the user associated with the cluster in question. Assuming that no modifications have been made to the kubeconfig file to use a service account (see[Adding a Service Account Authentication Token to a Kubeconfig File](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Tasks/contengaddingserviceaccttoken.htm)), the`user`section contains the OCI CLI token generation command in the following yaml format:
```

```

To confirm that kube-apiserver latency is caused by the known performance issue, use the following command to return the time that the OCI CLI takes to run the token generation command:
```

```

If the time taken to run the command is close to the kube-apiserver latency that you have observed, you might be experiencing the known performance issue. Workaround

Make sure that you are using the latest stable version of the OCI CLI, along with a supported version of Python (see[Manual Installation](https://docs.oracle.com/iaas/Content/API/SDKDocs/climanualinst.htm#climanualinst_intro)in the OCI CLI documentation).

If you are using Python version 3.6, we recommend that you upgrade to a newer Python version.

If you cannot upgrade to a newer Python version, disable the importing of all services (the default behavior) and instead selectively import only those individual services and modules that are required. Selectively importing services is known to improve the performance of Python version 3.6. For more information, see[Enable Selective Service Imports for Python 3.6](https://docs.oracle.com/iaas/tools/python/latest/sdk_behaviors/enable_selective_service_imports.html).

## Upgrade to Kubernetes 1.33.1 might reduce container open file limits
Details

When you upgrade an existing node pool to Kubernetes version 1.33.1 in a cluster you have created using Kubernetes Engine, you might notice that workloads that previously ran successfully now encounter issues and return error messages such as`Too many open files`.

A possible cause is that in node pools running Kubernetes version 1.33.1, the default soft limit for open files (`ulimit nofile`) within containers has been reduced to 1024. Workloads that implicitly depended on a previously higher default limit might therefore encounter issues.

The default soft limit for open files (`ulimit nofile`) within containers has been reduced to 1024 due to a change in the CRI-O container runtime. Kubernetes version 1.33.1 uses CRI-O version 1.33. In CRI-O version 1.33, the`LimitNOFILE`parameter is no longer explicitly set in the CRI-O systemd service file. As a result, the systemd default soft limit (typically 1024) now applies for open files within containers. For more information, see[https://github.com/cri-o/cri-o/pull/8962](https://github.com/cri-o/cri-o/pull/8962). Workaround

We are are aware of the issue and working on a resolution. In the meantime, there are two possible workarounds:
- Workaround 1: Create a custom cloud-init script to increase`ulimit nofile`. For example:
```

```

Note that`nofile=262144:262144`is an example. Set`nofile`to a value appropriate for the workload. For more information about creating custom cloud-init scripts, see[Using Custom Cloud-init Initialization Scripts to Set Up Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Tasks/contengusingcustomcloudinitscripts.htm).
- Workaround 2: Temporarily downgrade the version of Kubernetes running on the node pool to Kubernetes version 1.32, until a permanent resolution is available.

## Provisioning load balancers or volume claims might fail due to network misconfiguration
Details

When you define a Kubernetes service of type LoadBalancer or a persistent volume claim (PVC) for a Kubernetes cluster created by Kubernetes Engine, provisioning of the corresponding load balancer or volume might fail if the Kubernetes API endpoint subnet or the worker node subnet cannot reach the required OCI service endpoints. This issue is frequently caused by incorrect or incomplete VCN configuration, such as misconfigured route tables, security lists, or gateways (internet gateways, NAT gateways, service gateways).

In a cluster created by Kubernetes Engine, access to the Kubernetes API is provided through a Kubernetes API endpoint, which resides in a subnet you specify when creating the cluster. This endpoint can be configured as public (with a public IP address, making it accessible from the internet) or private (without a public IP address, making it accessible only from within the VCN or connected networks).

Workloads affected by network misconfiguration might display events like:
```

```

or
```

```

Other symptoms can include:
- Failure to provision an external load balancer for a service of type LoadBalancer.
- Failure to provision a persistent volume for a PVC using the CSI volume plugin.
- Cloud-controller-manager (CCM) container startup failures, or persistent taints remaining on nodes (which might prevent workloads from being scheduled).

Examine the relevant service logs for more information (see[Viewing Kubernetes Engine (OKE) Service Logs](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Tasks/contengviewingservicelogs.htm)). Background

Every VCN requires the correct gateway configuration to enable communication between worker nodes (compute instances) and other networks or services. In the context of Kubernetes Engine, proper gateway selection ensures that both the Kubernetes API endpoint and the worker nodes have network access for cluster provisioning, node operations, and integration with other OCI services.

The Kubernetes API endpoint for a Kubernetes cluster resides in a subnet that you specify during cluster creation, enabling you to control network access to the endpoint. The underlying Kubernetes control plane is managed and hosted by Oracle outside the tenancy. In OCI, a subnet is considered public when the associated route table contains a rule that directs traffic destined for 0.0.0.0/0 to an internet gateway. If the route table does not include such a rule, the subnet is considered private.

The primary gateway options in a VCN are:
- Internet Gateway (IGW): Allows compute instances in public subnets to access the public internet. The instance must have a public IP address, and the subnet’s route table must include a rule directing`0.0.0.0/0`to the internet gateway.
- NAT Gateway: Enables compute instances in private subnets to initiate outbound internet connections (for example, for operating system updates or package installations) without exposing themselves to inbound internet traffic. Instances using the NAT gateway do not require public IP addresses.
- Service Gateway (SGW): Allows compute instances in private subnets to access other OCI services (such as Object Storage, Container Registry, Autonomous AI Database, Streaming, and other selected services) over Oracle’s internal network, without traversing the public internet.

Do not use an internet gateway and a service gateway together for the same target OCI services. Mixing an internet gateway and a service gateway as routing options to the same OCI service in a VCN can cause traffic to be sent over the wrong network path. For example, requests intended for private OCI services might be routed over the public internet via the internet gateway instead of through the service gateway. Having both an internet gateway and a service gateway as possible routes can prevent the Kubernetes API endpoint or worker nodes from establishing the necessary private, secure connections to OCI endpoints, leading to provisioning failures, persistent taints, or other connectivity issues within a cluster.

Therefore, ensure that route tables for subnets used by worker nodes and the Kubernetes API endpoint unambiguously direct traffic to the appropriate gateway based on the destination. For access to OCI services from private subnets, make sure that routes send traffic explicitly through a service gateway, not an internet gateway.

For example, if you create a cluster and specify a subnet for the Kubernetes API endpoint and do not assign a public IP address to the endpoint, you might encounter connectivity problems. If the route table relies on an internet gateway, worker nodes might not access essential OCI services. As a result, the cloud-controller-manager container might fail to initialize, and taints might remain on the nodes. You can resolve the issue by configuring a NAT gateway or a service gateway to ensure proper access to OCI services. Workaround

To resolve network misconfiguration issues, ensure that worker nodes can communicate with OCI service endpoints by checking the following:
- 

Review network configuration. Check that the VCN, subnets, route tables, and security lists follow the requirements for the deployment scenario. Refer to[Example Network Resource Configurations](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Concepts/contengnetworkconfigexample.htm).
- Review gateway configuration:
- For public Kubernetes API endpoints (Kubernetes API endpoints with a public IP address): Check that public IP addresses are assigned, and that required routes to the internet gateway are present.
- For private Kubernetes API endpoints (Kubernetes API endpoints without a public IP address): Check that a service gateway is used to connect to OCI services. If internet access is needed from private subnets, configure a NAT gateway (not an internet gateway).
- Avoid dual paths: Do not route the same OCI service traffic via both an internet gateway and a service gateway.
- Review route table configuration:
- Check that the correct route tables are associated with worker node and Kubernetes API endpoint subnets.
- Check that all required route rules to gateways are present.
- Review security list configuration:
- Check that rules permit necessary traffic.
- Recommended: Use stateful rather than stateless rules for endpoint subnets.
- Review DHCP options. When using custom DNS resolvers, check that`169.254.169.254`is included as an entry in the DHCP options. For more information, see[DHCP Options](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm).

If configuration changes do not resolve the issue, further review the network against[Network Resource Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Concepts/contengnetworkconfig.htm).

## Upstream issues in Kubernetes version 1.34.1 are addressed in Kubernetes version 1.34.2, so plan upgrades accordingly

A number of upstream issues have been identified in Kubernetes version 1.34.1, as described in this section. These upstream issues are addressed in Kubernetes version 1.34.2.

Before upgrading Kubernetes clusters to version 1.34.1 from an earlier version, we recommend you consider whether your Kubernetes environment will be impacted by the upstream issues:
- If your Kubernetes environment runs workloads running StatefulSets, review[Kube-Controller-Manager: StatefulSet spurious rollout triggered during control plane upgrades](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/conteng-known-issues.htm#knownissues_topic_oke_upstream-k8s-1_34_1-issues__section_statefulset-spurious-rollout).
- If your Kubernetes environment relies on kubelet metrics, review[Missing kubelet_volume_stats_* metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/conteng-known-issues.htm#knownissues_topic_oke_upstream-k8s-1_34_1-issues__section_missing-kubelet_volume_stats-metrics).
- If your Kubernetes environment uses DRA resources, review[Kubelet deadlock when DRA driver connection is idle](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/conteng-known-issues.htm#knownissues_topic_oke_upstream-k8s-1_34_1-issues__section_kubelet-dra-driver-deadlock).

If upgrading your Kubernetes environment would be impacted by these upstream issues in Kubernetes version 1.34.1, in some cases we recommend that you do not perform the upgrade. Instead, keep clusters running Kubernetes version 1.33 (or earlier) until we announce the production release of Kubernetes Engine supporting Kubernetes version 1.34.2, and then upgrade clusters to Kubernetes version 1.34.2.

### Kube-Controller-Manager: StatefulSet spurious rollout triggered during control plane upgradesDetails

A regression introduced in Kubernetes version 1.34.1 caused unnecessary rollouts of existing StatefulSets during control plane upgrades from version 1.33 to version 1.34. The issue stemmed from a change in the semantic comparison logic used to determine whether a StatefulSet update was required.

As a result of this issue, the kube-controller-manager could incorrectly interpret unchanged StatefulSet specifications as modified, causing:
- 

Unnecessary one-time restarts of StatefulSet pods during the upgrade.
- 

Disruption to stateful workloads (the affected workloads should automatically recover after the restart).

For more information about the upstream issue, see[https://github.com/kubernetes/kubernetes/pull/135087](https://github.com/kubernetes/kubernetes/pull/135087). Workaround

If this issue will impact your Kubernetes environment, we recommend that you do not upgrade control plane nodes to Kubernetes version 1.34.1. Instead, keep control plane nodes running Kubernetes version 1.33 (or earlier) until we announce the production release of Kubernetes Engine supporting Kubernetes version 1.34.2, and only then upgrade control plane nodes to version 1.34.2.

### Missing`kubelet_volume_stats_*`metricsDetails

In Kubernetes version 1.34.1, several Prometheus metrics related to volume statistics (specifically the`kubelet_volume_stats_*`family of metrics) were unintentionally omitted due to a regression in metric registration within the kubelet.

The omitted metrics (`kubelet_volume_stats_available_bytes`,`kubelet_volume_stats_capacity_bytes`,`kubelet_volume_stats_used_bytes`) are commonly used for:
- Storage capacity monitoring.
- Alerting based on volume usage thresholds.

As a result of this issue:
- Monitoring systems (such as Prometheus, Grafana dashboards, and any system dependent on kubelet volume metrics) might show gaps or missing values for volume usage.
- Alerts dependent on these metrics (such as low disk space warnings, and persistent volume claim (PVC) usage alerts) might not trigger.
- PVC-backed workloads face the potential risk of unmonitored storage exhaustion.

For more information about the upstream issue, see[https://github.com/kubernetes/kubernetes/pull/133905](https://github.com/kubernetes/kubernetes/pull/133905). Workaround

If this issue will impact your Kubernetes environment, you can upgrade control plane nodes to Kubernetes version 1.34.1. However, we recommend that you do not upgrade worker nodes to Kubernetes version 1.34.1. Instead, keep worker nodes running Kubernetes version 1.33 (or earlier) until we announce the production release of Kubernetes Engine supporting Kubernetes version 1.34.2, and only then upgrade worker nodes to version 1.34.2.

### Kubelet deadlock when DRA driver connection is idleDetails

In Kubernetes version 1.34.1, the kubelet contained a latent deadlock condition affecting communication with Dynamic Resource Allocation (DRA) drivers. If a connection between the kubelet and the DRA driver remained idle for approximately 30 minutes, an internal lock could prevent the connection from becoming usable again.

As a result of this issue, the kubelet could wait indefinitely for driver responses, causing:
- Failure to allocate or free DRA-managed resources.
- Failure to successfully schedule or start workloads requiring DRA devices.

For more information about the upstream issue, see[https://github.com/kubernetes/kubernetes/pull/133934](https://github.com/kubernetes/kubernetes/pull/133934). Workaround

If you have already upgraded worker nodes to Kubernetes version 1.34.1 and encounter this issue, you can temporarily restore normal operation by restarting the kubelet on the affected worker nodes. Since the issue is fully resolved in Kubernetes version 1.34.2, we recommend that you upgrade the worker nodes when we announce the production release of Kubernetes Engine supporting Kubernetes version 1.34.2.

If you have not yet upgraded worker nodes to Kubernetes version 1.34.1, we recommend that you upgrade to Kubernetes version 1.34.2 when we announce the production release of Kubernetes Engine supporting Kubernetes version 1.34.2.

## Unintended boot volume expansion occurs when additional storage is attached to a worker node before first boot (affects OKE image versions 760, 764, 804, and 967 only)
Details

OKE image names include an image version number. For example,`967`is the version number of the`Oracle-Linux-8.10-aarch64-2025.07.21-0-OKE-1.33.1-967`image.

Unintended boot volume expansion behavior occurs in worker nodes based on OKE images with version numbers`760`,`764`,`804`, and`967`. For example, in a worker node based on the`Oracle-Linux-7.9-Gen2-GPU-2025.01.31-0-OKE-1.33.1-764`image, or based on the`Oracle-Linux-8.10-aarch64-2025.07.21-0-OKE-1.33.1-967`image.

If additional storage is attached to a worker node based on such an image before the node is started for the first time, the worker node's boot volume is automatically expanded to use the extra storage.

Such automatic boot volume expansion is not an intended feature. Instead, boot volume expansion should be performed explicitly in a cloud-init script using the`[](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-growfs)oci-growfs`utility. Workaround

No workaround is required when using image versions`1130`or later. Starting with OKE image version`1130`, the unintended automatic boot volume expansion has been disabled.

For workloads that require the same boot volume expansion behavior as earlier image versions, add the following command to the cloud-init script:
```

```

Adding this command to the cloud-init script ensures that any additional storage attached before the first boot is incorporated into the boot volume, matching the previous functionality. For an example of such a cloud-init script, see[Example 5: Using a Custom Cloud-init Script and oci-growfs to Increase the Size of the Boot Volume Partition](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Tasks/contengusingcustomcloudinitscripts.htm#contengusingcustomcloudinitscripts_topic_Examplecloudinitscriptusecases__CustomCloudinitScriptExampleIncreaseBootPartitionSize).

## Loss of Kubernetes Service Backends When Using cilium-agent with kubeProxyReplacement=true
Details

If you use Cilium CNI with`kubeProxyReplacement=true`(as described in the[Cilium documentation](https://docs.cilium.io/en/stable/network/kubernetes/kubeproxy-free/)), you might encounter a loss of backends for the Kubernetes service. When the backends are removed,`cilium-agent`stops routing pod traffic to the Kubernetes API server.

This issue appears when you run the following command:
```

```

Example output before and after backends are removed:

Before removal:
```

```

After removal:
```

```

This issue occurs because`cilium-agent`tracks endpointslices by IP address and port, and does not handle cases when multiple endpointslices use the same combination. When a DELETE event is received for one endpointslice,`cilium-agent`removes the backend, even if other endpointslices with the same IP address and port remain.

The standard kube-proxy implementation in Kubernetes is not affected by this issue. Workaround

Set up a liveness probe to monitor the Kubernetes backend in the`cilium-agent`container. The backend should remain stable for nearly the entire cluster lifecycle. If you notice that the service is missing a backend for a long period, this issue has likely occurred.

Restart the`cilium-agent`container. Restarting forces a resync of the in-memory state with Kubernetes. The agent then detects the existing endpointslices and restores the backend entry, allowing pod traffic to flow to the Kubernetes API server again.

## OKE worker nodes require kernel updates for CVE-2026-31431
Details

CVE-2026-31431 is a Linux kernel local privilege escalation vulnerability in`algif_aead`. Because OKE worker nodes run customer workloads, update affected Oracle Linux worker nodes to a fixed UEK kernel as soon as possible.

Fixed kernel versions include:
- UEK8:`6.12.0-201.74.2.2`
- UEK7:`5.15.0-319.201.4.4`
- UEK6:`5.4.17-2136.354.4.2`

For more information, see the[NVD entry for CVE-2026-31431](https://nvd.nist.gov/vuln/detail/CVE-2026-31431). Workaround

Use one of the following approaches:
- Recommended resolution: Resolve the issue by applying a kernel patch using Oracle Ksplice.
- Temporary mitigation: If you cannot apply the kernel patch immediately, mitigate the issue by disabling`algif_aead`initialization.

Method 1: Apply a kernel patch using Oracle Ksplice

We recommend that you resolve the issue by patching the kernel and restarting workloads on affected nodes. You can apply the patch to new managed nodes in a node pool using a custom cloud-init script. To apply the patch to existing managed nodes, use node pool cycling.

To resolve the issue using Ksplice:
- 

In a managed node pool, specify the following custom cloud-init script:

```

```

The Ksplice cloud-init script validates that the patch has been successfully installed. The script fails if the patch installation was unsuccessful.

For more information about custom cloud-init scripts, see[Using Custom Cloud-init Initialization Scripts to Set Up Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Tasks/contengusingcustomcloudinitscripts.htm).
- 

Cycle the node pool to apply the patch to existing managed nodes.

When cycling node pools, OKE automatically cordons, drains, and terminates existing worker nodes, and creates new worker nodes.

For more information about node pool cycling, see[Performing an In-Place Worker Node Update by Cycling Nodes in an Existing Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Tasks/contengupgradingimageworkernode_topic-Performing_an_InPlace_Worker_Node_Update_By_Cycling_an_Existing_Node_Pool.htm).

Method 2: Temporarily disable`algif_aead`initialization

Note that we recommend that you resolve the issue by applying a kernel patch using Oracle Ksplice (see[Method 1: Apply a kernel patch using Oracle Ksplice](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/conteng-known-issues.htm#knownissues_topic_kernel-updates-for-CVE-2026-31431__paragraph_ksplice-kernal-patch)).

Use this temporary mitigation only if you cannot apply the kernel patch immediately. This mitigation prevents`algif_aead`from initializing by adding`initcall_blacklist=algif_aead_init`to the kernel boot arguments. Use a custom cloud-init script to apply the mitigation to newly provisioned managed nodes. To apply the mitigation to existing managed nodes, use node pool cycling.

To apply the temporary mitigation:
- 

In a managed node pool, specify the following custom cloud-init script:

```

```

For more information about custom cloud-init scripts, see[Using Custom Cloud-init Initialization Scripts to Set Up Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Tasks/contengusingcustomcloudinitscripts.htm).
- 

Cycle the node pool to apply the mitigation to existing managed nodes.

When cycling node pools, OKE automatically cordons, drains, and terminates existing worker nodes, and creates new worker nodes.

For more information about node pool cycling, see[Performing an In-Place Worker Node Update by Cycling Nodes in an Existing Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Tasks/contengupgradingimageworkernode_topic-Performing_an_InPlace_Worker_Node_Update_By_Cycling_an_Existing_Node_Pool.htm).

## Outbound TLS connections from Kubernetes components can fail with some custom HTTPS endpoints
Details

When a Kubernetes component built with Go 1.25 or later runs with Go FIPS 140-3 mode enabled, outbound TLS connections to some custom HTTPS endpoints can fail if the endpoint, or a load balancer or proxy in front of it, negotiates TLS 1.2 without Extended Master Secret (EMS). In this case, the component can return an error similar to`tls: FIPS 140-3 requires the use of Extended Master Secret`. This is a generic TLS compatibility issue and, depending on which component initiates the connection, it can affect paths such as custom registry access, custom webhooks, and other external HTTPS integrations. This specific EMS-related failure does not apply when the endpoint negotiates TLS 1.3 or TLS 1.2 with EMS enabled. For more information, see[FIPS 140-3 Compliance](https://go.dev/doc/security/fips140).

In OKE version 1.35.2 (and later versions), the cluster control plane components and the cri-o runtime are on the Go 1.25 FIPS-enabled build path. The most likely customer-visible paths that can be impacted are kube-apiserver connections to custom webhooks and other HTTPS integrations, and cri-o connections to custom image registries. Workaround

Update the remote endpoint, or any TLS termination point in front of it, so that it presents a TLS profile compatible with FIPS-enabled clients. Note that TLS 1.3 is preferred. However, TLS 1.2 can also be used if EMS is enabled end-to-end. If the endpoint is fronted by an OCI Load Balancer, configure the listener (and the backend set, if applicable) to use TLS 1.3 or a TLS 1.2/TLS 1.3 profile using the appropriate SSL configuration options. Both listener and backend SSL configuration examples for TLSv1.3 and mixed TLSv1.2/TLSv1.3 profiles are shown in[Provisioning OCI Load Balancers for Kubernetes Services of Type LoadBalancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/../Tasks/contengcreatingloadbalancers-subtopic.htm). Server-side TLS remediation is the preferred long-term fix because it resolves the incompatibility at the endpoint the Kubernetes component actually reaches.

## AMD GPU Operator cluster add-on might not work in mixed-architecture clusters
Details

If the AMD GPU Operator cluster add-on pod is scheduled on an ARM architecture node, then it will encounter issues. Workaround

To prevent the AMD GPU Operator pods from being scheduled on ARM nodes, cordon all ARM architecture nodes before installing the add-on, and uncordon the nodes afterwards.
