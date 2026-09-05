# Kubernetes Versions and Kubernetes Engine (OKE)
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengupgradeoverview.htm
- Fetched: 2026-09-05 01:53 CDT

# Kubernetes Versions and Kubernetes Engine (OKE)

Find out about the Kubernetes versioning scheme and Kubernetes Engine (OKE) support for different Kubernetes versions.

Kubernetes version numbers have the format`x.y.z`where`x`is a major version,`y`is a minor version, and`z`is a patch version. For example, 1.35.2.

The Kubernetes project supports the most recent three minor versions of Kubernetes.

When you create a new Kubernetes cluster using Kubernetes Engine, you specify:
- The version of Kubernetes to run on the control plane nodes in the cluster.
- The version of Kubernetes to run on the worker nodes in the cluster. Different worker nodes in the same node pool can run different versions of Kubernetes. Different node pools in a cluster can run different versions of Kubernetes.

The version of Kubernetes that you specify for the worker nodes in a cluster must be either the same Kubernetes version as that running on the control plane nodes, or an earlier Kubernetes version that is still compatible. As described in the[Kubernetes version skew support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/), a certain amount of version variation is permissible between control plane nodes and worker nodes in a cluster:
- The control plane nodes must run the same version of Kubernetes as the version running on worker nodes, or must be no more than two versions (or three versions, starting from Kubernetes version 1.28) ahead.
- The worker nodes can run a version of Kubernetes that lags behind the version on the control plane nodes by up to two versions (or three versions, starting from Kubernetes version 1.28), but no more. If the version on the worker nodes is more than two versions (or three versions, starting from Kubernetes version 1.28) behind the version on the control plane nodes, the Kubernetes versions on the worker nodes and the control plane nodes are incompatible.
- The worker nodes in a cluster must not run a more recent version of Kubernetes than the associated control plane nodes.

The restrictions ensure that the oldest supported minor version of the kubelet and kube-proxy components running on a cluster's worker nodes are always compatible with the newest supported minor version of the kube-apiserver, kube-scheduler, kube-controller-manager, and cloud-controller-manager components running on the cluster's control plane nodes.

For more information, see the[Kubernetes version skew support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/).

## Kubernetes Minor Version Support

Note  
  
Starting with Kubernetes version 1.33, a preview release of Kubernetes Engine supports the initial patch version of each Kubernetes minor version. The initial patch version of a Kubernetes minor version has an x.y.0 version number, such as 1.33.0. We plan to make available a preview release of Kubernetes Engine within 30 days of the upstream launch of the initial Kubernetes patch version. Note that the preview release of Kubernetes Engine is only intended for early access and for testing with the initial Kubernetes patch version. In particular, note the following:
- A preview release of Kubernetes Engine has limited support.
- For production environments, we recommend that you do not use a preview release of Kubernetes Engine.
- For production environments, we recommend that you wait for the production release of Kubernetes Engine supporting Kubernetes version x.y.1, which we plan to make available in a timely fashion after the upstream launch of Kubernetes version x.y.1. Kubernetes minor versions typically introduce new features and other improvements. The Kubernetes project regularly releases minor versions, three times a year.

Oracle monitors and validates the minor versions released by the Kubernetes project, and releases Kubernetes Engine support for minor versions in a timely fashion.

Kubernetes Engine supports three minor versions of Kubernetes for new clusters. For a minimum of 30 days after the announcement of support for a new Kubernetes version, Kubernetes Engine continues to support the fourth oldest available Kubernetes minor version. After that time, the older Kubernetes version ceases to be supported.

When a minor version is no longer supported, you cannot:
- Create new clusters running that minor version.
- Add new node pools running that minor version.

Oracle therefore recommends that you upgrade any existing clusters that are currently running a soon-to-be unsupported minor version to run a minor version that Kubernetes Engine does support. Clusters that are not upgraded will continue to function as expected. However, they will no longer be supported.

You can upgrade control plane nodes through unsupported minor versions.

### Skipping versions when upgrading

Kubernetes requires that you upgrade control plane nodes one minor version at a time. However, you don't have to upgrade worker nodes one minor version at a time.

## Kubernetes Patch Version Support

Kubernetes patch versions typically address critical bugs or security vulnerabilities that have been recently identified in a Kubernetes minor version. The Kubernetes project frequently releases patch versions, typically once a month, but sometimes more frequently.

Oracle monitors and validates the patch versions released by the Kubernetes project, and releases Kubernetes Engine support for critical patch versions in a timely fashion.

When Oracle notifies you of Kubernetes Engine support for a new Kubernetes patch version, we recommend that you upgrade any clusters running the corresponding minor version of Kubernetes to the latest available patch version as soon as possible. You have thirty days after the announcement of Kubernetes Engine support for a new Kubernetes patch version to upgrade clusters from an older patch version to the new patch version. After thirty days, clusters running the older patch version are no longer supported.

Note that although clusters running an older patch version cease to be supported after thirty days, the older patch version might continue to be available for selection. However, Oracle strongly recommends you select the latest patch version.

## Note about Kubernetes Version Selection

When creating or updating a cluster or a node pool using the Console, the CLI, and the API, you specify the Kubernetes version. You can specify the Kubernetes version in the following ways:
- (Recommended) You can specify the Kubernetes version number using the major.minor format (that is,`x.y`). In this case, Kubernetes Engine automatically uses the latest supported patch version for the specified minor version. Using the`x.y`format is recommended as best practice, because it enables Kubernetes Engine to automatically select the latest, most secure, and most stable patch available for the minor version you select.
- You can specify the Kubernetes version number using the major.minor.patch format (that is,`x.y.z`). In this case, Kubernetes Engine uses the Kubernetes patch version that you specify. Using the`x.y.z`format to specify the Kubernetes version is appropriate when an organization or compatibility policy requires a specific patch version.

When using the Console, the available Kubernetes version numbers are initially shown in`x.y`format. Having selected a Kubernetes version in`x.y`format, you can optionally select Show patch versions and specify a supported patch version for the major.minor version you selected. However, we recommend you simply select a Kubernetes version in`x.y`format, to enable Kubernetes Engine to automatically select the patch version for the minor version.

When using the CLI, you can obtain the available Kubernetes versions in just`x.y`format by including the`--should-list-all-patch-versions false`option when using the`oci ce cluster-options get`or`oci ce node-pool-options get`commands.

When using the API, you can obtain the available Kubernetes versions in just`x.y`format by including`shouldListAllPatchVersions=false`as a query parameter when using the`GetClusterOptions`or`GetNodePoolOptions`operations.

## Rolling Back the Kubernetes Version on Managed Nodes

You can roll back the Kubernetes version running on managed nodes in an existing managed node pool by configuring the node pool with an earlier available Kubernetes version and replacing the existing managed nodes.

The Kubernetes version you select must be available for the managed node pool and compatible with the Kubernetes version running on the cluster control plane. The versions available for a managed node pool can vary by tenancy.

To see the Kubernetes versions available for a managed node pool:
- In the Console, view the Version list when editing the node pool.
- Using the CLI, use the`oci ce node-pool-options get`command.
- Using the API, use the`GetNodePoolOptions`operation.

Changing the Kubernetes version configured for a managed node pool does not change the Kubernetes version running on existing managed nodes. Until you replace the existing nodes, the Kubernetes version configured for the node pool can differ from the versions running on its nodes.

To complete the rollback, replace the existing managed nodes. In an enhanced cluster, you can cycle the node pool. In a basic cluster, manually delete and replace the managed nodes.

When subsequently upgrading the Kubernetes version of the cluster control plane, Kubernetes Engine validates both the Kubernetes version configured for each managed node pool and the Kubernetes versions running on the worker nodes. The control plane upgrade fails if either is outside the permitted version skew for the target control plane version.

For instructions, see[Rolling Back Managed Nodes to an Earlier Kubernetes Version](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengupgradingimageworkernode_Rolling-Back.htm)
