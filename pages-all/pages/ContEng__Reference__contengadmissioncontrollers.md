# Supported Admission Controllers
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengadmissioncontrollers.htm
- Fetched: 2026-09-05 01:53 CDT

# Supported Admission Controllers

Find out about the admission controllers that are turned on in Kubernetes clusters you create using Kubernetes Engine (OKE).

The Kubernetes version you select when you create a cluster using Kubernetes Engine determines the default set of admission controllers that are turned on in the created cluster. The set follows the recommendation given in the[Kubernetes documentation](https://kubernetes.io/docs/admin/admission-controllers/#is-there-a-recommended-set-of-admission-controllers-to-use)for that version. This topic shows the supported admission controllers, the Kubernetes versions in which they are supported, and the order in which they run in the Kubernetes API server.

Note that if you install other admission controllers in a way that mutates or rejects requests in the`kube-system`namespace, the Kubernetes control plane components might stop functioning or behave unexpectedly. For more information, see[Avoiding operating on the kube-system namespace](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#avoiding-operating-on-the-kube-system-namespace)in the Kubernetes documentation.

## Admission Controllers (sorted alphabetically)

The tables list, in alphabetical order, the admission controllers that are turned on in the Kubernetes clusters you create using Kubernetes Engine. For each admission controller, the tables show the Kubernetes version in which it is supported.

### Mutating Admission Controllers (sorted alphabetically)

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
PodSecurityPolicy (optional, see[Using Pod Security Polices with Kubernetes Engine](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/../Tasks/contengusingpspswithoke.htm)) No No No
PodTopologyLabels Yes Yes Yes
Priority Yes Yes Yes
RuntimeClass Yes Yes Yes
ServiceAccount Yes Yes Yes
StorageObjectInUseProtection Yes Yes Yes
TaintNodesByCondition Yes Yes Yes

### Validating Admission Controllers (sorted alphabetically)

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
PodSecurityPolicy (optional, see[Using Pod Security Polices with Kubernetes Engine](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/../Tasks/contengusingpspswithoke.htm)) No No No
Priority Yes Yes Yes
ResourceQuota Yes Yes Yes
RuntimeClass Yes Yes Yes
ServiceAccount Yes Yes Yes
ValidatingAdmissionPolicy Yes Yes Yes
ValidatingAdmissionWebhook Yes Yes Yes

## Admission Controllers (sorted by run order)

The tables list the admission controllers that are turned on in the Kubernetes clusters you create using Kubernetes Engine. The tables show the order in which supported admission controllers run in the Kubernetes API server. Note that the run order can be different in different Kubernetes versions.

### Mutating Admission Controllers (sorted by run order)

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

### Validating Admission Controllers (sorted by run order)

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
