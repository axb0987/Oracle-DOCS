# Compatibility Matrix
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengCompatibilitymatrix_topic.htm
- Fetched: 2026-09-05 01:52 CDT

# Compatibility Matrix

Find out about the versions of different products and components that are supported on the version of Kubernetes running on clusters you create using Kubernetes Engine.

You can deploy different products and components on the clusters you create using Kubernetes Engine, some of which are compatible with particular versions of Kubernetes and Kubernetes Engine. For more information, see:
- [Calico Compatibility](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengCompatibilitymatrix_topic.htm#contengCompatibilitymatrix_topic-Calico-compatibility-matrix)
- [Cluster Add-on Compatibility](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengCompatibilitymatrix_topic.htm#contengCompatibilitymatrix_topic-Cluster-addon-compatibility-matrix)
- [Admission Controller Compatibility](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengCompatibilitymatrix_topic.htm#contengCompatibilitymatrix_topic-Admission-controller-compatibility-matrix)
- [Ubuntu Node Package Compatibility](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengCompatibilitymatrix_topic.htm#contengCompatibilitymatrix_topic_Ubuntu_compatibility_matrix)
- [Karpenter Provider for OCI (KPO) Compatibility](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengCompatibilitymatrix_topic.htm#contengCompatibilitymatrix_topic_KPO_compatibility_matrix)

## Calico Compatibility

The table lists the versions of the Calico network plugin that Oracle has successfully tested on clusters created using Kubernetes Engine. Oracle only supports Calico versions that have been successfully tested. For each Calico version, the table shows the Kubernetes version that was running on clusters in successful tests.

For more information, see[Example: Installing Calico and Setting Up Network Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengsettingupcalico.htm).

Calico Version Tested (and supported) on clusters running Kubernetes 1.34? Tested (and supported) on clusters running Kubernetes 1.35? Tested (and supported) on clusters running Kubernetes 1.36?
`3.25.1`(not tested) (not tested) (not tested)
`3.26.1`(not tested) (not tested) (not tested)
`3.26.4`(not tested) (not tested) (not tested)
`3.27.2`(not tested) (not tested) (not tested)
`3.28.0`(not tested) (not tested) (not tested)
`3.28.2`(not tested) (not tested) (not tested)
`3.29.2`(not tested) (not tested) (not tested)
`3.30.0`(not tested) (not tested) (not tested)
`3.30.3`Yes (not tested) (not tested)
`3.31.5`(not tested) Yes (not tested)
`3.32.0`(not tested) (not tested) Yes

## Cluster Add-on Compatibility

This table lists the latest versions of essential and optional cluster add-ons for each version of Kubernetes that Kubernetes Engine (OKE) supports.

For more information, see[Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengconfiguringclusteraddons.htm).

Cluster add-on Latest add-on image version supported with Kubernetes 1.34 Latest add-on image version supported with Kubernetes 1.35 Latest add-on image version supported with Kubernetes 1.36
kube-proxy`1.34.10``1.35.2``1.36.1`
CoreDNS`1.12.2``1.12.2``1.12.2`
OCI VCN-Native Pod Networking CNI plugin`3.3.0``3.3.0``3.3.0`
flannel`0.27.3``0.27.3``0.27.3`
ObservabilityAgent`0.135.0``0.135.0``0.135.0`
NodeProblemDetector`0.8.20``0.8.20``0.8.20`
Kubernetes Dashboard`2.7.0``2.7.0``2.7.0`
Tiller (not recommended)`2.16.0``2.16.0``2.16.0`
Oracle Database Operator for Kubernetes`1.2.0``1.2.0``1.2.0`
WebLogic Kubernetes Operator`4.3.10``4.3.10``4.3.10`
Certificate Manager`1.17.1``1.17.1``1.17.1`
Cluster Autoscaler`1.34.3``1.34.3``1.34.3`
Istio`1.29.5``1.29.5``1.29.5`
OCI Native Ingress Controller`1.4.5``1.4.5``1.4.5`
Kubernetes Metrics Server`0.7.2``0.7.2``0.7.2`
NVIDIA GPU Plugin
- `0.17.0`
- `0.16.2`
- `0.15.1`
- `0.14.2`
- `0.17.0`
- `0.16.2`
- `0.15.1`
- `0.14.2`
- `0.17.0`
- `0.16.2`
- `0.15.1`
- `0.14.2`
Node Feature Discovery`0.17.3``0.17.3``0.17.3`
NVIDIA GPU Operator
- `25.3.3-2`
- `25.3.4-2`
- `25.10.0-1`
- `25.10.1-1`
- `25.3.3-2`
- `25.3.4-2`
- `25.10.0-1`
- `25.10.1-1`
- `25.3.3-2`
- `25.3.4-2`
- `25.10.0-1`
- `25.10.1-1`
NVIDIA Network Operator
- `25.4.0`
- `25.7.0`
- `25.10.0-1`
- `25.4.0`
- `25.7.0`
- `25.10.0-1`
- `25.4.0`
- `25.7.0`
- `25.10.0-1`
CSI Driver SMB`1.19.1``1.19.1``1.19.1`
AMD GPU Operator`1.5.0``1.5.0``1.5.0`

## Admission Controller Compatibility

The tables list, in alphabetical order, the admission controllers that are turned on in the Kubernetes clusters you create using Kubernetes Engine. For each admission controller, the tables show the Kubernetes version in which it is supported.

For more information, see[Supported Admission Controllers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Reference/contengadmissioncontrollers.htm).

### Admission Controller Compatibility (sorted alphabetically)

These tables list, in alphabetical order, the admission controllers that are turned on in the Kubernetes clusters you create using Kubernetes Engine. For each admission controller, the tables show the Kubernetes version in which it is supported.

#### Mutating Admission Controllers (sorted alphabetically)

Admission Controllers (in alphabetical order) Supported in 1.34? Supported in 1.35? Supported in 1.36?
DefaultIngressClass Yes Yes Yes
DefaultStorageClass Yes Yes Yes
DefaultTolerationSeconds Yes Yes Yes
ExtendedResourceToleration Yes Yes Yes
LimitRanger Yes Yes Yes
MutatingAdmissionPolicy Yes Yes Yes
MutatingAdmissionWebhook Yes Yes Yes
NamespaceLifecycle Yes Yes Yes
NodeRestriction Yes Yes Yes
PodGroupProtection No No Yes
PodSecurityPolicy (optional, see[Using Pod Security Polices with Kubernetes Engine](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengusingpspswithoke.htm)) No No No
PodTopologyLabels Yes Yes Yes
Priority Yes Yes Yes
RuntimeClass Yes Yes Yes
ServiceAccount Yes Yes Yes
StorageObjectInUseProtection Yes Yes Yes
TaintNodesByCondition Yes Yes Yes

#### Validating Admission Controllers (sorted alphabetically)

Admission Controllers (in alphabetical order) Supported in 1.34? Supported in 1.35? Supported in 1.36?
CertificateApproval Yes Yes Yes
CertificateSigning Yes Yes Yes
CertificateSubjectRestriction Yes Yes Yes
ClusterTrustBundleAttest Yes Yes Yes
ImagePolicyWebhook Yes Yes Yes
JobValidation No No Yes
LimitRanger Yes Yes Yes
NodeDeclaredFeatureValidator No Yes Yes
PersistentVolumeClaimResize Yes Yes Yes
PodGroupWorkloadExists No No Yes
PodResizeValidator No No Yes
PodSecurity Yes Yes Yes
PodSecurityPolicy (optional, see[Using Pod Security Polices with Kubernetes Engine](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengusingpspswithoke.htm)) No No No
Priority Yes Yes Yes
ResourceQuota Yes Yes Yes
RuntimeClass Yes Yes Yes
ServiceAccount Yes Yes Yes
ValidatingAdmissionPolicy Yes Yes Yes
ValidatingAdmissionWebhook Yes Yes Yes

### Admission Controller Compatibility (sorted by run order)

These tables list the admission controllers that are turned on in the Kubernetes clusters you create using Kubernetes Engine. The tables show the order in which supported admission controllers run in the Kubernetes API server. Note that the run order can be different in different Kubernetes versions.

#### Mutating Admission Controllers (sorted by run order)

Run order in Kubernetes 1.34 clusters: Run order in Kubernetes 1.35 clusters: Run order in Kubernetes 1.36 clusters:
NamespaceLifecycle NamespaceLifecycle NamespaceLifecycle
LimitRanger LimitRanger LimitRanger
ServiceAccount ServiceAccount ServiceAccount
NodeRestriction NodeRestriction NodeRestriction
TaintNodesByCondition TaintNodesByCondition TaintNodesByCondition
Priority Priority Priority
DefaultTolerationSeconds DefaultTolerationSeconds DefaultTolerationSeconds
ExtendedResourceToleration ExtendedResourceToleration ExtendedResourceToleration
DefaultStorageClass DefaultStorageClass DefaultStorageClass
StorageObjectInUseProtection StorageObjectInUseProtection StorageObjectInUseProtection
RuntimeClass RuntimeClass PodGroupProtection
DefaultIngressClass DefaultIngressClass RuntimeClass
PodTopologyLabels PodTopologyLabels DefaultIngressClass
MutatingAdmissionPolicy MutatingAdmissionPolicy PodTopologyLabels
MutatingAdmissionWebhook MutatingAdmissionWebhook MutatingAdmissionPolicy
MutatingAdmissionWebhook

#### Validating Admission Controllers (sorted by run order)

Run order in Kubernetes 1.34 clusters: Run order in Kubernetes 1.35 clusters: Run order in Kubernetes 1.36 clusters:
LimitRanger LimitRanger LimitRanger
ServiceAccount ServiceAccount ServiceAccount
ImagePolicyWebhook ImagePolicyWebhook ImagePolicyWebhook
PodSecurity PodSecurity PodSecurity
Priority Priority Priority
PersistentVolumeClaimResize PersistentVolumeClaimResize PersistentVolumeClaimResize
RuntimeClass RuntimeClass RuntimeClass
CertificateApproval CertificateApproval CertificateApproval
CertificateSigning CertificateSigning CertificateSigning
ClusterTrustBundleAttest ClusterTrustBundleAttest ClusterTrustBundleAttest
CertificateSubjectRestriction CertificateSubjectRestriction CertificateSubjectRestriction
ValidatingAdmissionPolicy NodeDeclaredFeatureValidator PodGroupWorkloadExists
ValidatingAdmissionWebhook ValidatingAdmissionPolicy NodeDeclaredFeatureValidator
ResourceQuota ValidatingAdmissionWebhook JobValidation
ResourceQuota PodResizeValidator
ValidatingAdmissionPolicy
ValidatingAdmissionWebhook
ResourceQuota

## Ubuntu Node Package Compatibility

This table lists the Ubuntu releases for which Oracle provides node packages, along with the Kubernetes versions that each node package is compatible with. The node packages that Oracle provides are designed to work on both x86 and ARM architectures.

For more information, see[Running Ubuntu on Worker Nodes Using Custom Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengcreatingubuntubasedworkernodes.htm).

Ubuntu release Package to use with Kubernetes 1.27 Package to use with Kubernetes 1.28 Package to use with Kubernetes 1.29 Package to use with Kubernetes 1.30 Package to use with Kubernetes 1.31 Package to use with Kubernetes 1.32 Package to use with Kubernetes 1.33 Package to use with Kubernetes 1.34 Package to use with Kubernetes 1.35 Package to use with Kubernetes 1.36
Jammy (Ubuntu 22.04)`oci-oke-node-all-1.27.10``oci-oke-node-all-1.28.10``oci-oke-node-all-1.29.1``oci-oke-node-all-1.30.10``oci-oke-node-all-1.31.10``oci-oke-node-all-1.32.10``oci-oke-node-all-1.33.10``oci-oke-node-all-1.34.10``oci-oke-node-all-1.35.2``oci-oke-node-all-1.36.1`
Noble (Ubuntu 24.04)`oci-oke-node-all-1.27.10``oci-oke-node-all-1.28.10``oci-oke-node-all-1.29.1``oci-oke-node-all-1.30.10``oci-oke-node-all-1.31.10``oci-oke-node-all-1.32.10``oci-oke-node-all-1.33.10``oci-oke-node-all-1.34.10``oci-oke-node-all-1.35.2``oci-oke-node-all-1.36.1`

## Karpenter Provider for OCI (KPO) Compatibility

This table lists the versions of the Karpenter Provider for OCI (KPO) that are compatible with versions of Kubernetes running on clusters that you create using Kubernetes Engine.

For more information, see[Using Karpenter Provider for OCI (KPO)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/conteng-kpo.htm).

Kubernetes version KPO version
Kubernetes version 1.31`v1.0.0`or later
Kubernetes version 1.32`v1.0.0`or later
Kubernetes version 1.33`v1.0.0`or later
Kubernetes version 1.34`v1.0.0`or later
Kubernetes version 1.35`v1.1.0`or later
Kubernetes version 1.36`v1.3.0`
