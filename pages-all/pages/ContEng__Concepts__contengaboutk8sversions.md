# Supported Versions of Kubernetes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm
- Fetched: 2026-09-05 01:52 CDT

# Supported Versions of Kubernetes

Find out about the Kubernetes versions that Kubernetes Engine (OKE) currently supports, along with details of previously supported versions and planned support for future versions.

When Kubernetes Engine support for a new version of Kubernetes is announced, an older Kubernetes version will subsequently cease to be supported. Oracle recommends that you upgrade existing clusters to use the most recent Kubernetes version that Kubernetes Engine supports.

This topic lists:
- [Currently Supported Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm#supportedk8sversions)
- [Planned Support for Future Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm#contengaboutk8sversions_topic-Planned_Kubernetes_Versions_Support)
- [Previously Supported Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm#previouslysupportedk8sversions)

## Currently Supported Kubernetes Versions

Kubernetes Engine supports three versions of Kubernetes for new clusters. For a minimum of 30 days after the announcement of support for a new Kubernetes version, Kubernetes Engine continues to support the fourth oldest available Kubernetes version. After that time, the older Kubernetes version ceases to be supported.

When creating a new cluster with Kubernetes Engine, Oracle recommends that you use the most recent Kubernetes version that Kubernetes Engine supports. When Oracle announces Kubernetes Engine support for a new Kubernetes version, Oracle recommends you upgrade existing clusters to use that new Kubernetes version as soon as possible.

### Release Calendar

Kubernetes Engine (OKE) supports the following Kubernetes versions for new clusters:

Kubernetes Minor Version Kubernetes Patch Version Supported by OKE Upstream Minor Version Release Date Upstream Minor Version End-of-life date OKE Release Date OKE End-of-life Date
`1.36``1.36.1`2026-04-22 2027-06-28 2026-07-07 1.36 is supported for 30 days after 1.39.1 OKE Release Date (planned)
`1.36``1.36.0`2026-04-22 2027-06-28 2026-05-20

(Preview release only. See[Notes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm#supportedk8sversions__notes-1-36-0)) 1.36 is supported for 30 days after 1.39.1 OKE Release Date (planned)
`1.35``1.35.2`2025-12-17 2027-02-28 2026-04-28 1.35 is supported for 30 days after 1.38.1 OKE Release Date (planned)
`1.35``1.35.0`2025-12-17 2027-02-28 2026-03-17

(Preview release only. See[Notes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm#supportedk8sversions__notes-1-35-0)) 1.35 is supported for 30 days after 1.38.1 OKE Release Date (planned)
`1.34``1.34.10`2025-08-27 2026-10-27 2026-08-20 1.34 is supported for 30 days after 1.37.1 OKE Release Date (planned)
`1.34``1.34.2`2025-08-27 2026-10-27 2026-02-03 2026-09-22
`1.34``1.34.1`2025-08-27 2026-10-27 2025-10-07 (See[Notes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm#supportedk8sversions__notes-1-34-1)) 2026-03-09
`1.34``1.34.0`2025-08-27 2026-10-27 2025-10-07

(Preview release only. See[Notes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm#supportedk8sversions__notes-1-34-0)) 2026-03-09

Legal Disclaimer: The table is intended to outline our general product direction. It is intended for information purposes only, and may not be incorporated into any contract. It is not a commitment to deliver any material, code, or functionality, and should not be relied upon in making purchasing decisions. The development, release, timing, and pricing of any features or functionality described for Oracle's products may change and remains at the sole discretion of Oracle Corporation.

### Notes about Kubernetes Engine Support for Kubernetes Version 1.36.1

New clusters that you create with Kubernetes Engine to run Kubernetes version 1.36.1 or later use Kubernetes Key Management Service (KMS) provider version 2 for Kubernetes secret objects from the time the cluster is created.

When you upgrade an existing cluster that uses a master encryption key you manage from an earlier Kubernetes version to Kubernetes version 1.36.1 or later, Kubernetes Engine starts using KMS provider version 2. New Kubernetes secret objects use KMS provider version 2, as do existing secret objects that are subsequently updated. Existing unchanged secret objects can remain encrypted using KMS provider version 1.

Kubernetes Engine retains KMS provider version 1 as a read fallback, so secret objects that have not been migrated remain readable. Kubernetes Engine does not automatically migrate all existing secret objects when you upgrade the cluster control plane.

To re-encrypt all existing unchanged Kubernetes secret objects using KMS provider version 2, see[Migrating Kubernetes Secrets to KMS v2](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengmigratingsecretstokmsv2.htm).

### Notes about Kubernetes Engine Support for Kubernetes Version 1.36.0

Note that Kubernetes Engine support for Kubernetes version 1.36.0 is a preview release of Kubernetes Engine. This preview release of Kubernetes Engine is only intended for early access and for testing with Kubernetes version 1.36.0.

In particular, note the following:
- This preview release of Kubernetes Engine has limited support, and is only available in the OC1 realm.
- For production environments, we recommend that you do not use this preview release of Kubernetes Engine.
- For production environments, we recommend that you wait for the production release of Kubernetes Engine supporting Kubernetes version 1.36.1, which we plan to make available in a timely fashion after the upstream launch of Kubernetes version 1.36.1.

For more information about the introduction of support for Kubernetes version 1.36, see[Kubernetes v1.36 is now available on OCI Kubernetes Engine (OKE)](https://blogs.oracle.com/cloud-infrastructure/kubernetes-v1-36-is-now-available-on-oke).

### Notes about Kubernetes Engine Support for Kubernetes Version 1.35

Starting with Kubernetes version 1.35, Kubernetes requires cgroups v2 for container resource management.

Control Groups (cgroups) is a Linux kernel feature that provides a mechanism for managing and controlling resource allocation for processes or groups of processes. Control groups version 2 (cgroups v2) groups provide a single control group hierarchy against which all resource controllers are mounted. In this hierarchy, you can coordinate resource use across different resource controllers.

Oracle Linux 7 (OL7) supports cgroups v1, but does not support cgroups v2. Oracle Linux 8 (OL8) and later versions support both cgroups v1 and cgroups v2, but cgroups v2 is not always enabled by default in OL8.

In summary, Kubernetes version 1.35 therefore requires OL8 (or later) with cgroups v2 enabled.

Cgroups v2 is enabled by default in OKE OL8 images that have a build number of 1367 or greater. However, in OKE OL8 images that have a build number lower than 1367 (and in OL8 platform images), cgroups v1 is enabled by default.

For worker nodes on clusters running Kubernetes version 1.35 (and later), Kubernetes Engine supports the following images:
- OKE OL8 images, and custom images based on OKE OL8 images, that have a build number of 1367 or greater.
- OKE OL8 images, and custom images based on OKE OL8 images, that have a build number lower than 1367, but only if you enable cgroups v2 (see[Enabling Cgroups v2 on OL8 Worker Nodes Using Custom Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengcreatingcgroupv2enabledworkernodes.htm)).
- Custom images based on OL8 platform images, but only if you enable cgroups v2 (see[Enabling Cgroups v2 on OL8 Worker Nodes Using Custom Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengcreatingcgroupv2enabledworkernodes.htm)).

In clusters running Kubernetes version 1.35 (and later), the use of platform images (both OL7 platform images and OL8 platform images) is not recommended. We strongly recommend the use of OKE images for all new deployments and upgrades. If you want to continue to use a platform image, create a custom image based on the platform image and specify the custom image's OCID when creating or updating a node pool (note that we do not recommend this approach).

When upgrading worker nodes that currently use an OKE OL7 image to Kubernetes version 1.35, you cannot perform an in-place upgrade. Instead, you have to perform an out-of-place upgrade and specify a supported OKE OL8 image or custom OL8 image. For specific upgrade instructions, see[Upgrading Managed Nodes to Kubernetes version 1.35 (or later)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengupgradingk8sworkernode_topic-Upgrading_managed_nodes_to_k8s_135.htm).

For more information about the introduction of support for Kubernetes version 1.35, see[OKE Welcomes Kubernetes 1.35: What’s new, what’s changing, and what to do next](https://blogs.oracle.com/cloud-infrastructure/oke-welcomes-kubernetes-1-35).

### Notes about Kubernetes Engine Support for Kubernetes Version 1.35.0

Note that Kubernetes Engine support for Kubernetes version 1.35.0 is a preview release of Kubernetes Engine. This preview release of Kubernetes Engine is only intended for early access and for testing with Kubernetes version 1.35.0.

In particular, note the following:
- This preview release of Kubernetes Engine has limited support, and is only available in the OC1 realm.
- For production environments, we recommend that you do not use this preview release of Kubernetes Engine.
- For production environments, we recommend that you wait for the production release of Kubernetes Engine supporting Kubernetes version 1.35.1, which we plan to make available in a timely fashion after the upstream launch of Kubernetes version 1.35.1.

### Notes about Kubernetes Engine Support for Kubernetes Version 1.34.1
Note  
  
A number of upstream issues have been identified in Kubernetes 1.34.1. These upstream issues are addressed in Kubernetes version 1.34.2.

Before upgrading Kubernetes clusters to version 1.34.1 from an earlier version, we recommend you consider whether your Kubernetes environment will be impacted by the upstream issues. The upstream issues are described in[Upstream issues in Kubernetes version 1.34.1 are addressed in Kubernetes version 1.34.2, so plan upgrades accordingly](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../known-issues/conteng-known-issues.htm#knownissues_topic_oke_upstream-k8s-1_34_1-issues).

If upgrading your Kubernetes environment would be impacted by the upstream issues in Kubernetes version 1.34.1, in some cases we recommend that you do not perform the upgrade. Instead, keep clusters running Kubernetes version 1.33 (or earlier) until we announce the production release of Kubernetes Engine supporting Kubernetes version 1.34.2, and then upgrade clusters to Kubernetes version 1.34.2.

Starting with Kubernetes 1.34.1, the container runtime interface (CRI-O) enforces fully qualified image names by default. This upstream change improves supply chain security and helps prevent the risk of pulling unintended or malicious images.

When you specify container images in your deployments, use the full registry path. For example,`docker.io/nginx`instead of`nginx`.

If you specify a short image name that matches multiple registries (as defined in the node’s`/etc/containers/registries.conf`file), the image pull fails. You might see errors similar to the following:
```

```

If you need to use short image names, disable this enforcement by creating a custom cloud-init script for worker nodes (for more information, see[Using Custom Cloud-init Initialization Scripts to Set Up Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengusingcustomcloudinitscripts.htm)). For example:
```

```

For more information about the CRI-O change, see[https://github.com/cri-o/cri-o/pull/9401](https://github.com/cri-o/cri-o/pull/9401)

### Notes about Kubernetes Engine Support for Kubernetes Version 1.34.0

Note that Kubernetes Engine support for Kubernetes version 1.34.0 is a preview release of Kubernetes Engine. This preview release of Kubernetes Engine is only intended for early access and for testing with Kubernetes version 1.34.0.

In particular, note the following:
- This preview release of Kubernetes Engine has limited support, and is only available in the OC1 realm.
- For production environments, we recommend that you do not use this preview release of Kubernetes Engine.
- For production environments, we recommend that you wait for the production release of Kubernetes Engine supporting Kubernetes version 1.34.1, which we plan to make available in a timely fashion after the upstream launch of Kubernetes version 1.34.1.

### Notes about Kubernetes Engine Support for Kubernetes Version 1.33.0

Note that Kubernetes Engine support for Kubernetes version 1.33.0 is a preview release of Kubernetes Engine. This preview release of Kubernetes Engine is only intended for early access and for testing with Kubernetes version 1.33.0.

In particular, note the following:
- This preview release of Kubernetes Engine has limited support, and is only available in the OC1 realm.
- For production environments, we recommend that you do not use this preview release of Kubernetes Engine.
- For production environments, we recommend that you wait for the production release of Kubernetes Engine supporting Kubernetes version 1.33.1, which we plan to make available in a timely fashion after the upstream launch of Kubernetes version 1.33.1.

### Notes about Kubernetes Engine Support for Kubernetes Version 1.30

Note that Kubernetes Engine support for Kubernetes version 1.30 also introduces changes to default Kubernetes Engine behavior with regards CPU and memory reservation. On clusters running Kubernetes version 1.30 and later, CPU and memory resources for managed nodes are reserved by default, using the`--kube-reserved`and`--system-reserved`kubelet flags respectively (as recommended in[Best Practice: Reserve resources for Kubernetes and OS system daemons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengbestpractices_topic-Cluster-Management-best-practices.htm#contengbestpractices_topic-Cluster-Management-best-practices__ManagingOKEClusters-Reserveresourcesforkubernetesandossystemdaemons)). As a result, on clusters running Kubernetes version 1.30 and later, there is a difference between a node's total resources, and the resources that are available for workloads to request. For more information, see[Best Practice: Reserve resources for Kubernetes and OS system daemons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/../Tasks/contengbestpractices_topic-Cluster-Management-best-practices.htm#contengbestpractices_topic-Cluster-Management-best-practices__ManagingOKEClusters-Reserveresourcesforkubernetesandossystemdaemons).

### Notes about Kubernetes Engine Support for Kubernetes Version 1.28

Note that in Kubernetes version 1.28, the Kubernetes skew policy has expanded. Prior to Kubernetes version 1.28, the skew policy required a cluster's control plane nodes to be no more than two versions ahead of worker nodes. Starting from Kubernetes version 1.28, the Kubernetes skew policy allows control plane nodes to be up to three versions ahead of worker nodes. See the[Kubernetes version skew support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/).

Kubernetes Engine applies the expanded skew policy to clusters running Kubernetes version 1.28 and later.

### Notes about Kubernetes Engine Support for Kubernetes Version 1.27

Note that Kubernetes version 1.27 stopped serving the following deprecated Kubernetes API:
- CSIStorageCapacity (storage.k8s.io/v1beta1 API version)

For more information about migrating from the deprecated APIs, see the[Kubernetes Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-27).

### Notes about Kubernetes Engine Support for Kubernetes Version 1.26

Note that Kubernetes version 1.26 stopped serving a number of deprecated Kubernetes APIs, including:
- FlowSchema (flowcontrol.apiserver.k8s.io/v1beta1 API version)
- HorizontalPodAutoscaler (autoscaling/v2beta2 API version)
- PriorityLevelConfiguration (flowcontrol.apiserver.k8s.io/v1beta1 API version)

For more information about migrating from the deprecated APIs, see the[Kubernetes Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-26).

Support for Kubernetes version 1.26.7 was released to address the following upstream issues with Kubernetes version 1.26.2:
- [https://github.com/opencontainers/runc/issues/3849](https://github.com/opencontainers/runc/issues/3849): A bug in kubelet causes a memory leak on nodes using cgroup v1 on the 5.15 Linux kernel. Oracle Linux 8.7 images use the 5.15 Linux kernel, so Oracle Linux 8.7 images are impacted by the bug.
- [https://github.com/cri-o/cri-o/issues/6805](https://github.com/cri-o/cri-o/issues/6805): Metrics are missing after a crio restart.

### Notes about Kubernetes Engine Support for Kubernetes Version 1.25

Note that Kubernetes version 1.25 stopped serving a number of deprecated Kubernetes APIs, including:
- CronJob (batch/v1beta1 API version)
- EndpointSlice (discovery.k8s.io/v1beta1 API version)
- Event (events.k8s.io/v1beta1 API version)
- HorizontalPodAutoscaler (autoscaling/v2beta1 API version)
- PodDisruptionBudget (policy/v1beta1 API version)
- PodSecurityPolicy (policy/v1beta1 API version)
- RuntimeClass (node.k8s.io/v1beta1 API version)

For more information about migrating from the deprecated APIs, see the[Kubernetes Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-25).

Support for Kubernetes version 1.25.12 was released to address the following upstream issues with Kubernetes version 1.25.4:
- [https://github.com/opencontainers/runc/issues/3849](https://github.com/opencontainers/runc/issues/3849): A bug in kubelet causes a memory leak on nodes using cgroup v1 on the 5.15 Linux kernel. Oracle Linux 8.7 images use the 5.15 Linux kernel, so Oracle Linux 8.7 images are impacted by the bug.
- [https://github.com/cri-o/cri-o/issues/6805](https://github.com/cri-o/cri-o/issues/6805): Metrics are missing after a crio restart.

Note  
  

The upstream Kubernetes project deprecated pod security policies in Kubernetes version 1.21, and removed the feature in Kubernetes version 1.25. Consequently, Kubernetes Engine does not support pod security policies and the PodSecurityPolicy admission controller in clusters running Kubernetes version 1.25 and later.

If you require similar functionality, consider using Kubernetes pod security standards and the PodSecurity admission controller instead (along with the Privileged, Baseline, and Restricted policies). By default, Kubernetes Engine enables the PodSecurity admission controller in clusters running Kubernetes version 1.23 and later, in order to support pod security standards. For more information about Kubernetes pod security standards, and the PodSecurity admission controller, see[Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)in the Kubernetes documentation.

Alternatively, consider using other alternatives that are being developed in the Kubernetes ecosystem to enforce policies.

If you do decide to move from using pod security policies and the PodSecurityPolicy admission controller to using pod security standards and the PodSecurity admission controller, see[Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller](https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/)in the Kubernetes documentation. Note that it is important to complete the migration before creating a new cluster running Kubernetes version 1.25, or before upgrading an existing Kubernetes version 1.24 cluster to run Kubernetes version 1.25. Also note that the Console provides a convenient way to disable the use of the PodSecurityPolicy admission controller in existing Kubernetes clusters created and managed by Kubernetes Engine (see[Using the Console to Disable the PodSecurityPolicy Admission Controller](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengusingpspswithoke.htm#contengusingpspswithoke_topic-Using_the_Console_to_Disable_the_PodSecurityPolicy_Admission_Controller)).

### Notes about Kubernetes Engine Support for Kubernetes Version 1.22

Note that Kubernetes version 1.22 stopped serving a number of deprecated Kubernetes APIs, including:
- Webhook resources
- CustomResourceDefinition
- APIService
- TokenReview
- SubjectAccessReview resources
- CertificateSigningRequest
- Lease
- Ingress
- IngressClass
- RBAC resources
- PriorityClass
- Storage resources

For more information about migrating from the deprecated APIs, see the[Kubernetes Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-22).

## Planned Support for Future Kubernetes Versions

Kubernetes Engine support is currently planned for the following future versions of Kubernetes. Note that future dates are subject to change without notice. In addition, note the Legal Disclaimer following the table.

Kubernetes Minor Version Kubernetes Patch Version Supported by OKE Upstream Minor Version Release Date Upstream Minor Version End-of-life date OKE Release Date
`1.37`To Be Confirmed To Be Confirmed To Be Confirmed To Be Confirmed
`1.38`To Be Confirmed To Be Confirmed To Be Confirmed To Be Confirmed
`1.39`To Be Confirmed To Be Confirmed To Be Confirmed To Be Confirmed

Legal Disclaimer: The table is intended to outline our general product direction. It is intended for information purposes only, and may not be incorporated into any contract. It is not a commitment to deliver any material, code, or functionality, and should not be relied upon in making purchasing decisions. The development, release, timing, and pricing of any features or functionality described for Oracle's products may change and remains at the sole discretion of Oracle Corporation.

## Previously Supported Kubernetes Versions

Kubernetes Engine previously supported the following versions of Kubernetes:

Kubernetes Version Support Ended
`1.33.10`August 10, 2026
`1.33.1`August 10, 2026
`1.33.0`August 10, 2026
`1.32.10`May 28, 2026
`1.32.1`May 28, 2026
`1.31.10`November 25, 2025
`1.31.1`September 1, 2025
`1.30.10`July 21, 2025
`1.30.1`May 13, 2025
`1.29.10`April 17, 2025
`1.29.1`February 21, 2025
`1.28.10`January 27, 2025
`1.28.2`October 8, 2024
`1.27.10`August 27, 2024
`1.27.2`May 21, 2024
`1.26.7`April 29, 2024
`1.26.2`October 13, 2023
`1.25.12`February 15, 2024
`1.25.4`October 13, 2023
`1.24.1`September 26, 2023
`1.23.4`June 22, 2023
`1.22.5`February 22, 2023
`1.21.5`October 13, 2022
`1.20.11`July 19, 2022
`1.20.8`November 7, 2021
`1.19.15`April 22, 2022
`1.19.12`November 7, 2021
`1.19.7`August 13, 2021
`1.18.10`February 9, 2022
`1.17.13`September 8, 2021
`1.17.9`April 17, 2021
`1.16.15`April 17, 2021
`1.15.12`February 2, 2021
`1.15.7`February 2, 2021
`1.14.8`December 15, 2020
`1.13.x`March 21, 2020
`1.12.7`January 29, 2020
`1.12.6`April 15, 2019
`1.11.9`September 9, 2019
`1.11.8`April 15, 2019
`1.11.x`versions prior to`1.11.8`March 13, 2019
`1.10.x`April 12, 2019
`1.9.x`December 11, 2019
`1.8.x`September 7, 2018

### Notes about Kubernetes Engine Support for Kubernetes Version 1.20

With the announcement of support for Kubernetes version 1.20.8, the container runtime used by Kubernetes Engine changes from Docker to CRI-O. However, you don't have to change any of your existing Docker images because Docker images are Open Container Initiative (OCI) compliant. As far as Kubernetes is concerned, all OCI-compliant images look the same.

Note the following:
- CRI-O is an implementation of the Kubernetes Container Runtime Interface (CRI), which enables the use of OCI-compatible runtimes. CRI-O can pull your existing Docker images and run them on your Kubernetes version 1.20.8 clusters.
- When using the Docker runtime, the default configuration captures the standard output and standard error streams of containers using the JSON format. In contrast, CRI-O uses the Logrus format. If you use a logging tool such as Fluentd or Fluent Bit, update the tool's configuration to use a new parser to parse CRI logs. For example:
- If you use Fluentd, use the[fluent-plugin-parser-cri parser](https://github.com/fluent/fluent-plugin-parser-cri#fluent-plugin-parser-cri).
- If you use Fluent Bit, use the[Container Runtime Interface (CRI) parser](https://docs.fluentbit.io/manual/installation/kubernetes#container-runtime-interface-cri-parser).
- You might have a workflow in a cluster that relies on the underlying docker socket /var/run/docker.sock (a pattern often referred to as Docker in Docker). Starting with Kubernetes version 1.20.8, such a workflow no longer functions.
- If you previously used the Docker CLI to run commands on a host, you have to use crictl (a CLI for CRI-compatible container runtimes) instead.
- The upstream Kubernetes project is deprecating Docker as a container runtime after Kubernetes version 1.20.

To find out more:
- See the[Kubernetes 1.20.8 Changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#v1208)for more information about Kubernetes 1.20.8
- See the[Dockershim Deprecation FAQ](https://kubernetes.io/blog/2020/12/02/dockershim-faq/)
