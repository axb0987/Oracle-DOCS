# Using Karpenter Provider for OCI (KPO)
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm
- Fetched: 2026-09-05 01:53 CDT

# Using Karpenter Provider for OCI (KPO)

Find out how Karpenter Provider for OCI (KPO) works with Kubernetes Engine (OKE) to provision, scale, and manage worker nodes.

Read about how to use the Karpenter Provider for OCI (KPO) to integrate Karpenter into clusters you create with Kubernetes Engine to provision and scale worker nodes:
- 

[Using Karpenter Provider for OCI (KPO) with Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-overview)
- 

[Installing Karpenter Provider for OCI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-installation)
- 

[Granting IAM Permissions to Karpenter Provider for OCI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-iam)
- 

[Enabling Node Registration for KPO-Launched Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-enable-node-registration)
- 

[Creating OCINodeClass Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-create-ocinodeclass)
- 

[Creating NodePool Resources that Reference OCINodeClass Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-create-nodepool)
- 

[OCINodeClass Reference](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass)
- 

[Scheduling, Labels, and Taints](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-scheduling)
- 

[Validating Node Provisioning](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-validating-node-provisioniing)
- 

[NodePool and OCINodeClass Examples](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-examples)
- 

[Resource Discovery and Cleanup](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-cleanup)
- 

[Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ops-troubleshooting)
- 

[Frequently Asked Questions (FAQs) about KPO](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-faq)

## Using Karpenter Provider for OCI (KPO) with Kubernetes Engine (OKE)

Karpenter is an open source Kubernetes node provisioning and scaling tool. You use Karpenter to add and remove worker nodes automatically based on scheduling demand. When pods can’t be scheduled, Karpenter provisions worker nodes that meet the pods’ requirements. You also configure disruption settings so Karpenter consolidates capacity and replaces worker nodes in a controlled way.

You can use Karpenter to:
- 

Scale worker nodes based on workload demand.
- 

Select instance types based on scheduling requirements, such as CPU, memory, architecture, and availability domain.
- 

Control node lifecycle behavior, such as consolidation and disruption budgets.
- 

Reduce the operational work of managing fixed-size node pools.

For more information about Karpenter, see the[Karpenter documentation](https://karpenter.sh/docs/).

Karpenter Provider for OCI (KPO) integrates Karpenter with OCI Kubernetes Engine (OKE) so you can provision and scale worker nodes by using OCI compute instances. In summary, you configure OCI-specific worker node settings in`OCINodeClass`, then configure scheduling and scaling intent in the Karpenter`NodePool`.

In more detail, KPO uses the following Kubernetes custom resources to configure provisioning and scaling behavior. The resources are defined by custom resource definitions (CRDs) installed with Karpenter and KPO:
- `NodePool`: The CRD is installed with Karpenter. You create`NodePool`resources to define scheduling requirements, disruption behavior, and scaling limits. A`NodePool`describes the kind of capacity that workloads can use, and it references an`OCINodeClass`to supply OCI-specific settings for that capacity.
- `OCINodeClass`: The CRD is installed with Karpenter Provider for OCI. You create`OCINodeClass`resources to define OCI-specific worker node settings such as image selection, boot volume settings, and VNIC settings.
- `NodeClaim`: The CRD is installed with Karpenter. Karpenter creates`NodeClaim`resources when pending pods need capacity, and each`NodeClaim`represents a request for a worker node.

When pods can’t be scheduled, provisioning follows this sequence:
- Karpenter selects a compatible`NodePool`and creates a`NodeClaim`.
- The`NodeClaim`includes a`nodeClassRef`that points to the`OCINodeClass`referenced by the`NodePool`.
- KPO reads the`NodeClaim`and the referenced`OCINodeClass`, then provisions OCI resources such as the compute instance, VNICs, and the boot volume.
- The instance boots and joins the cluster as a worker node.

KPO integrates with the standard Karpenter cloud provider interface. KPO v1.3.0 is aligned with upstream Karpenter version 1.13.0. Configure OCI-specific behavior through`OCINodeClass`, including:
- 

OCI compute shapes (VM and bare metal) and corresponding scheduling labels.
- 

Multiple sizing configurations for flexible shapes.
- 

Burstable configuration for flexible shapes (`baselineOcpuUtilization`).
- 

Preemptible instances (mapped from Karpenter`spot`capacity type).
- 

OKE prebuilt images (Oracle Linux and Ubuntu).
- 

Boot volume customization (KMS key, size, VPUs per GB, PV encryption in transit).
- 

IPv4 and IPv6 addressing options on worker node VNICs.
- 

Network security group (NSG) support on worker node VNICs.
- 

Secondary VNIC configuration (only clusters using the OCI VCN IP Native CNI add-on).
- 

Capacity reservations, cluster placement groups, and compute clusters.
- 

Instance configuration (such as metadata, tags, launch options, SSH authorized keys).
- 

Kubelet configuration overrides.
- 

Image selection by filter to auto-detect a compatible OKE image.
- 

Drift detection so Karpenter can replace nodes that drift from the desired configuration. Note that KPO does not guarantee drift detection for changes made directly in OCI outside Karpenter.
- 

Optional node repair policies (requires Karpenter node repair to be enabled).
- 

Oracle Cloud Agent plugin enablement when KPO launches instances.

KPO also supports upstream Karpenter features such as:
- 

Static node pools for maintaining a fixed number of worker nodes.
- 

NodeOverlay support for influencing scheduling decisions with capacity or pricing overlays.

In addition, KPO supports configurable rate limiting for requests to OCI service APIs (for more information, see the[KPO OCI Rate Limiter documentation on Github](https://github.com/oracle/karpenter-provider-oci/blob/main/docs/guide/rate-limiter.md)).

Complete the following tasks to set up KPO, configure IAM, and start provisioning worker nodes with Karpenter:
- 

Install KPO in the cluster's data plane (see[Installing Karpenter Provider for OCI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-installation)).
- 

Grant IAM permissions so that KPO can manage required OCI resources (see[Granting IAM Permissions to Karpenter Provider for OCI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-iam)).
- 

Grant IAM permissions to enable KPO-launched instances to join the cluster (see[Enabling Node Registration for KPO-Launched Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-enable-node-registration)).
- 

Create one or more`OCINodeClass`resources (see[Creating OCINodeClass Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-create-ocinodeclass)).
- 

Create one or more Karpenter`NodePool`resources that reference the`OCINodeClass`resources (see[Creating NodePool Resources that Reference OCINodeClass Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-create-nodepool)).

## Installing Karpenter Provider for OCI

### Prerequisites

Before you install KPO, confirm that the cluster and networking configuration support Karpenter-provisioned worker nodes. Note that it's possible for installation to succeed, but for subsequent worker node provisioning to fail due to missing prerequisites.
- 

Kubernetes version running on cluster : Use a KPO version that is compatible with the Kubernetes version running on the cluster, as shown in the table:

Kubernetes version KPO version
Kubernetes version 1.31`v1.0.0`or later
Kubernetes version 1.32`v1.0.0`or later
Kubernetes version 1.33`v1.0.0`or later
Kubernetes version 1.34`v1.0.0`or later
Kubernetes version 1.35`v1.1.0`or later
Kubernetes version 1.36`v1.3.0`or later
- 

Worker node capacity : Run at least one existing managed node pool or self-managed worker nodes so KPO can run in the data plane.
- 

OCI VCN-Native Pod Networking CNI plugin cluster add-on (also known as the OCI VCN IP Native CNI add-on) version : If the cluster is using the OCI VCN IP Native CNI add-on, the add-on must be version 3.0.0 or later. We strongly recommend the use of version 3.2.0 or later. If the cluster is using a version of the add-on prior to version 3.2.0, secondary VNICs support a maximum of 16 IP addresses (`ipCount`must not exceed 16).
- 

Helm client installed : Install the Helm client in the environment where you want to run Helm commands.

### Add the KPO Helm Repository

Add the KPO Helm repository by entering:
```

```

Download the latest index for the`karpenter-provider-oci`repository by entering:
```

```

To list the available chart versions, enter:
```

```

### Review and Configure Helm Values

Review the Helm configuration values (often simply referred to as Helm values) for the chart version that is compatible with the Kubernetes version running on the cluster by entering:

```

```

The following table shows the most important Helm values:

Value Required Description
`settings.clusterCompartmentId`Yes Default compartment OCID used to resolve OCI resources referenced in`OCINodeClass`. Use the cluster's compartment OCID in most cases.
`settings.vcnCompartmentId`Yes Default compartment OCID used to resolve network resources referenced in`OCINodeClass`. Use the cluster's VCN compartment OCID in most cases.
`settings.apiserverEndpoint`Yes

API server endpoint (privateIP) that worker nodes use to communicate with the Kubernetes API server. For example,`10.0.0.14`.
`settings.ociVcnIpNative`No Set to`true`if your cluster uses OCI VCN IP Native CNI add-on. Accepted values:`true`or`false`.
`settings.ipFamilies`No IP families allocated to a worker node VNIC. Default:`["IPv4"]`. Accepted values:`"IPv4"`,`"IPv6"`, or both. Ensure the referenced subnets include matching CIDR blocks.
`settings.flexibleShapeConfigs`No Default sizing configurations for flexible shapes. Each entry can specify`ocpu`,`memoryInGbs`, and`baselineOcpuUtilization`. Define this in YAML format (the chart converts YAML to JSON).
`settings.repairPolicies`No A list of Karpenter node repair policies (for more information, see[Karpenter`cloudprovider.RepairPolicy`](https://pkg.go.dev/sigs.k8s.io/karpenter/pkg/cloudprovider#RepairPolicy)). Each entry specifies a node condition type and status plus a duration threshold before Karpenter repairs the node. Define this in YAML format (the chart converts YAML to JSON). Requires the Karpenter node repair feature to be enabled.

For example:
```

```

where`tolerationDuration`is specified in nanoseconds:
`image.registry`No

The container registry in which the the KPO image has been published, Default:`ghcr.io`
`settings.featureGates.staticCapacity`No

Enables upstream static node pools. When enabled, a`NodePool`can set`spec.replicas`to maintain a fixed number of nodes. Default:`false`.
`settings.featureGates.nodeOverlay`No

Enables upstream`NodeOverlay`. When enabled, you can use`NodeOverlay`resources to influence scheduling simulations by applying price overrides, price adjustments, or extended-resource capacity overlays. Default:`false`.
`settings.enableUnavailableOfferingsOnServiceLimitExceeded`No

Enables caching of offerings that are unavailable because of an OCI service limit. While an offering is cached as unavailable, KPO excludes it from scheduling until the cache entry expires. Default:`false`.
`settings.rateLimiter`No

Rate limiter configurations for requests that KPO sends to OCI service APIs (for more information, see[KPO OCI Rate Limiter documentation on Github](https://github.com/oracle/karpenter-provider-oci/blob/main/docs/guide/rate-limiter.md)). Each entry can specify`disable`,`qpsRead`,`burstRead`,`qpsWrite`, and`burstWrite`values. Define this in YAML format (the chart converts YAML to JSON).
`settings.unavailableOfferingsTTLSeconds`No

Time for which KPO treats an offering that returned an out-of-capacity response as unavailable. During this period, Karpenter can consider other eligible offerings. Default: 180 seconds.

You must set the required Helm values to enable KPO to resolve OCI resources and bootstrap worker nodes. You can also set the optional Helm values to match your networking model and your worker node strategy.

You set Helm values in a configuration file (referred to as the Helm values file).

### Install KPO

Deploy the KPO controller into the OKE data plane. Install KPO into a namespace you can manage and monitor with your cluster operations tooling.
- 

Choose the namespace where you want to deploy KPO.
- 

Create a Helm values file in YAML format that includes required values and any optional values you want to override. For example:
```

```

- 

Install the chart by entering:

```

```

If you do not specify a namespace in which to deploy KPO, the`default`namespace is used.

For more information about installing KPO, see the[KPO installation documentation on Github](https://github.com/oracle/karpenter-provider-oci/blob/main/docs/guide/installation-using-helm.md).

### Verify the Installation

Having installed KPO, confirm that the KPO controller starts successfully before you create`OCINodeClass`and`NodePool`resources.
- 

Confirm that the pods are running by entering:

```

```

- 

If the pods are not running, inspect pod events and logs by entering:

```

```

```

```

## Granting IAM Permissions to Karpenter Provider for OCI

To enable KPO to create and manage the OCI resources required for worker nodes, you must grant the KPO workload the necessary IAM permissions. Use the policy pattern shown in[Workload Identity Policy Pattern](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-iam__section_workload_identity_policy_pattern)to add the required policy statements shown in[Basic Policies Required for KPO Operation](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-iam__section_basic-policies-required-for-kpo-operation). Add additional statements for specific features that you enable in`OCINodeClass`, as shown in[Optional Policies (Feature-Specific)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-iam__section_karpenter-optional-features).

### Workload Identity Policy Pattern

Use the following pattern to specify workload identity conditions in IAM policies so OCI permissions apply only to the KPO workload in the cluster:

```

```

where:
- `<verb>`is the action to permit (varies by OCI resource).
- `<location>`is the name of the resource's compartment, or specify`tenancy`for all compartments.
- `<namespace-name>`is the Kubernetes namespace where KPO is deployed (by default, KPO is deployed in the`default`namespace).
- `<service-account-name>`is the service account used by KPO pods (by default, the`karpenter`service account is used by KPO pods).
- `<cluster-ocid>`is the OCID of the cluster.

### Basic Policies Required for KPO Operation

Grant permissions to KPO to manage the compute, storage, and networking resources required for worker nodes by including policy statements similar to the following in an IAM policy (using the pattern shown in[Workload Identity Policy Pattern](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-iam__section_workload_identity_policy_pattern)):

```

```

Note that if you enable optional features in`OCINodeClass`, you also have to define additional policies (see[Optional Policies (Feature-Specific)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-iam__section_karpenter-optional-features)).

### Optional Policies (Feature-Specific)

In addition to the policy statements shown in[Basic Policies Required for KPO Operation](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-iam__section_basic-policies-required-for-kpo-operation), if you enable optional features in`OCINodeClass`, you also have to define additional policies.

Feature Example policy statements
Capacity reservation`Allow any-user to use compute-capacity-reservations in compartment <compartment-name> where all { ... }`
Compute cluster`Allow any-user to use compute-clusters in compartment <compartment-name> where all { ... }`
Cluster placement group`Allow any-user to use cluster-placement-groups in compartment <compartment-name> where all { ... }`
Defined tags`Allow any-user to use tag-namespaces in compartment <compartment-name> where all { ... }`

Only add the policies required by the features you enable in`OCINodeClass`.

## Enabling Node Registration for KPO-Launched Worker Nodes

Worker nodes launched by KPO must join the cluster. Grant`CLUSTER_JOIN`by using a dynamic group for instances. Create a dynamic group (with a rule that includes the compute instances to add to the cluster), and a policy for the dynamic group (with a policy statement to allow members of the dynamic group to join the cluster).
- 

Create a new dynamic group to contain the compute instances in the compartment where KPO launches nodes:
- Follow the instructions in[To create a dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#To)in the IAM documentation, and give the new dynamic group a name (for example,`kpo-nodes-dyn-grp`).
- 

Enter a rule that includes the compute instances in the compartment, in the format:

```

```

where`<compartment-ocid>`is the OCID of the compartment where KPO launches nodes.

For example:

```

```

- Select Create .
- Create a policy for the dynamic group, with a policy statement to allow compute instances in the dynamic group to join the cluster:
- Follow the instructions in[To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy)in the IAM documentation, and give the new policy a name (for example,`kpo-nodes-policy`).
- 

Enter a policy statement to allow compute instances in the dynamic group to join the cluster, in the format:

```

```

where:
- `<dynamic-group-name>`is the name of the dynamic group you created earlier. For example,`kpo-nodes-dyn-grp`. Note that if a dynamic group is not in the default identity domain, prefix the dynamic group name with the identity domain name, in the format`dynamic-group '<identity-domain-name>'/'<dynamic-group-name>'`. You can also specify the dynamic group using its OCID, in the format`dynamic-group id <dynamic-group-ocid>`.
- `<compartment-name>`is the name of the compartment to which the cluster belongs. For example,`oke-cluster-compartment`

For example:

```

```

If you consider this policy statement to be too permissive, you can restrict the permissions to explicitly specify the cluster that you want worker nodes launched by KPO to join, by entering a policy statement in the format:

```

```

- Select Create to create the new policy.

## Creating OCINodeClass Resources

Use`OCINodeClass`to define OCI infrastructure settings for Karpenter-provisioned worker nodes. KPO provisions the OCI compute and networking resources for those nodes. Reference an`OCINodeClass`from a Karpenter`NodePool`by using`nodeClassRef`.

For more information about each`OCINodeClass`field and status value, see[OCINodeClass Reference](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass).

To create an`OCINodeClass`resource:
- Create a YAML file containing an`OCINodeClass`manifest. For example:
```

```

- Apply the manifest by entering:
```

```

- Check the status and conditions of the new`OCINodeClass`resource by entering:
```

```

## Creating NodePool Resources that Reference OCINodeClass Resources

Create one or more Karpenter`NodePool`resources to define the worker node capacity that Karpenter can provision, including instance shape requirements, taints, disruption settings, and scaling limits.

In each`NodePool`, set`spec.template.spec.nodeClassRef`to reference an`OCINodeClass`so Karpenter Provider for OCI can apply the OCI-specific settings (such as image selection, boot volume settings, and VNIC settings) when it provisions nodes. Create separate`NodePool`resources when workloads require different scheduling rules or different`OCINodeClass`configurations.

To create a`NodePool`resource:
- 

Create a YAML file containing a`NodePool`manifest that references an`OCINodeClass`by using`nodeClassRef`. For example:
```

```

- Apply the manifest by entering:
```

```

- Confirm that the`NodePool`exists by entering:
```

```

## OCINodeClass Reference

Use`OCINodeClass`to define OCI infrastructure settings that KPO uses when it provisions OCI resources for Karpenter-provisioned worker nodes. Reference an`OCINodeClass`from a Karpenter`NodePool`by using`nodeClassRef`.

### OCINodeClassSpec

Field Description Required Example / Notes
`volumeConfig`Boot volume configuration Required See[VolumeConfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_volumeconfig).
`networkConfig`VNIC subnet and optional NSGs for compute instance Required See[NetworkConfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_networkconfig).
`shapeConfigs`Additional shape configs for flexible and burstable shapes. Omitting this excludes flexible shapes from scheduling. Optional See[ShapeConfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_shapeconfig).
`nodeCompartmentId`Launch instance in a different compartment from the cluster Optional Compartment OCID.
`capacityReservationConfigs`Array of capacity reservations Optional See[CapacityReservationConfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_capacityreservationconfig).
`clusterPlacementGroupConfigs`Array of cluster placement groups (CPGs). Only one CPG is allowed at most per availability domain Optional See[ClusterPlacementGroupConfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_clusterplacementgroupconfig).
`computeClusterConfig`Compute cluster configuration. Immutable after creation Optional See[ComputeClusterConfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_computeclusterconfig).
`metadata`User data (key/value) for compute instance Optional`{ "foo": "bar" }`
`freeformTags`Freeform tags to apply to the instance Optional`{ "env": "prod" }`
`definedTags`Defined tags to apply to the instance Optional`{ "Department": { "CostCenter": "42" } }`
`kubeletConfig`Kubelet overrides Optional See[KubeletConfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_kubeletconfig).
`postBootstrapInitScript`Base64 script to run after OKE bootstrap Optional Base64 shell script.
`preBootstrapInitScript`Base64 script to run before OKE bootstrap Optional Base64 shell script.
`sshAuthorizedKeys`List of authorized SSH public keys Optional`[ "<ssh-public-key>" ]`
`launchOptions`Launch options passed into compute instance Optional See[LaunchOptions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_launchoptions).
`agentPlugins`List of Oracle Cloud Agent plugins to enable on launched instance. Optional For more information, see[KPO Oracle Cloud Agent Plugins documentation on Github](https://github.com/oracle/karpenter-provider-oci/blob/main/docs/guide/agent-plugins.md).

### VolumeConfig

Use`volumeConfig`to control how KPO builds the boot volume for each worker node.

Field Description Required Example / Notes
`bootVolumeConfig`Boot volume configuration Required See[BootVolumeConfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_bootvolumeconfig).

### BootVolumeConfig

Use`bootVolumeConfig`to select the image and to configure boot volume sizing and performance.

Field Description Required Example / Notes
`imageConfig`Reference to image(s) via OCID or filter Required See[ImageConfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_imageconfig).
`sizeInGBs`Size in GB (min 50) Optional`50`
`vpusPerGB`Volume performance units (VPUs) per GB Optional`20`
`kmsKeyConfig`Reference to a KMS key for encryption Optional See[KmsKeyConfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_kmskeyconfig).
`pvEncryptionInTransit`Enable PV encryption in transit. Accepted values:`true`or`false`. Default:`false`Optional`true`

### ImageConfig

Use`imageConfig`to select the OKE image for worker nodes. Select an image by OCID or by filter. For more information about OKE images, see[OKE Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengimagesshapes.htm#images__oke-images).

Field Description Required Example / Notes
`imageType`Type of image Required Accepted:`OKEImage`.
`imageFilter`Filter for selecting image Required if`imageId`empty See[ImageSelectorTerm](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_imageselectorterm).
`imageId`Image OCID Required if`imageFilter`empty`ocid1.image.oc1..xxxx`

### KmsKeyConfig

Use`kmsKeyConfig`to encrypt boot volumes with your own key.

Field Description Required Example / Notes
`kmsKeyId`KMS key OCID Optional`ocid1.key.oc1..xxxx`

### ImageSelectorTerm

Use`ImageSelectorTerm`to select an image by OS, version, compartment, and tags.

Field Description Required Example / Notes
`osFilter`OS name filter Optional`Oracle Linux`
`osVersionFilter`OS version filter Optional`8`
`compartmentId`Image compartment OCID Optional`ocid1.compartment...`
`freeformTags`Match freeform tags Optional`{ "key": "val" }`
`definedTags`Match defined tags Optional`{ "namespace": { "key": "val" } }`

### NetworkConfig

Use`networkConfig`to place worker node VNICs in the correct subnets and attach NSGs when needed.

Field Description Required Example / Notes
`primaryVnicConfig`Primary VNIC subnet and NSGs Required See[PrimaryVnicConfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_primaryvnicconfig).
`secondaryVnicConfigs`Secondary VNIC configs Optional See[SecondaryVnicConfigs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_secondaryvnicconfigs).

### PrimaryVnicConfig

Use`primaryVnicConfig`to define the primary subnet and optional NSGs for the worker node.

Field Description Required Example / Notes
`subnetConfig`Subnet configuration Required See[SubnetConfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_subnetconfig).
`networkSecurityGroupConfigs`NSG configurations Optional See[NetworkSecurityGroupConfigs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_networksecuritygroupconfigs).
`assignIpV6Ip`Assign IPv6 IP address Optional`false`
`assignPublicIp`Assign public IP address Optional`false`
`vnicDisplayname`VNIC display name Optional`my-vnic`
`ipv6AddressIpv6SubnetCidrPairDetails`IPv6 subnet-CIDR and address pairs Optional See[Ipv6AddressIpv6SubnetCidrPairDetails](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_ipv6addressipv6subnetcidrpairdetails).
`skipSourceDestCheck`Skip source/destination check Optional`false`
`securityAttributes`Security attributes map Optional`{ "s": "v" }`

### SubnetConfig

Select a subnet by OCID or by selector.

Field Description Required Example / Notes
`subnetId`Subnet OCID Required if`subnetFilter`empty`ocid1.subnet...`
`subnetFilter`Subnet selector Required if`subnetId`empty See[OciResourceSelectorTerm](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_ociresourceselectorterm).

### NetworkSecurityGroupConfigs

Select an NSG by OCID or by selector.

Field Description Required Example / Notes
`networkSecurityGroupId`NSG OCID Required if`networkSecurityGroupFilter`empty`ocid1.networksecuritygroup...`
`networkSecurityGroupFilter`NSG selector Required if`networkSecurityGroupId`empty See[OciResourceSelectorTerm](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_ociresourceselectorterm).

### Ipv6AddressIpv6SubnetCidrPairDetails

Use this field when you need to control IPv6 subnet CIDR assignment.

Field Description Required Example / Notes
`ipv6SubnetCidr`IPv6 subnet CIDR Optional`2001:0db8::/64`

### OciResourceSelectorTerm

Use selector fields when you want to choose a subnet or NSG by name or by tags, instead of by OCID.

Field Description Required Example / Notes
`compartmentId`Resource compartment Optional`ocid1.compartment...`
`displayName`Match display name Optional`mysubnet`
`freeformTags`Match freeform tags Optional`{ "key": "val" }`
`definedTags`Match defined tags Optional`{ "namespace": { "key": "val" } }`

### SecondaryVnicConfigs

Use`secondaryVnicConfigs`when the cluster uses the OCI VCN IP Native CNI add-on and you need a secondary VNIC for pod IP addressing. Has all of the`[](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_primaryvnicconfig)PrimaryVnicConfig`fields, and some additional fields.

Field Description Required Example / Notes
(All`[](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_primaryvnicconfig)PrimaryVnicConfig`fields) (Same as`[](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_primaryvnicconfig)PrimaryVnicConfig`) (Varies) (not applicable)
`applicationResource`Application identifier Optional`blue`
`ipCount`Max IPs per VNIC (power-of-2 values between 1 and 16, so allowed values are 1, 2, 4, 8, or 16). See[How do you configure secondary VNICs?](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-faq__section_kpo_faq-secoondary-vnic-config)Optional`8`
`nicIndex`NIC slot index for hosts with multiple cards Optional`0`

### ShapeConfigs

Use`shapeConfigs`to define sizing for flexible shapes and burstable configurations.

Field Description Required Example / Notes
`ocpus`OCPUs for flexible shapes (minimum of 1) Required`4`
`baselineOcpuUtilization`Utilization ratio for burstable shapes. Accepted values:`BASELINE_1_8`,`BASELINE_1_2`,`BASELINE_1_1`Optional`BASELINE_1_8`
`memoryInGbs`Memory for flexible shapes (GB) Optional`16`

### CapacityReservationConfigs

Use`capacityReservationConfigs`when you want worker nodes to run on capacity reserved in OCI.

Field Description Required Example / Notes
`capacityReservationId`Reservation OCID Required if`capacityReservationFilter`empty`ocid1.reservation...`
`capacityReservationFilter`Reservation filter Required if`capacityReservationId`empty See[OciResourceSelectorTerm](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_ociresourceselectorterm).

### ClusterPlacementGroupConfigs

Use`clusterPlacementGroupConfigs`when you need worker nodes placed close together for low-latency networking.

Field Description Required Example / Notes
`clusterPlacementGroupId`Cluster placement group (CPG) OCID Required if`clusterPlacementGroupFilter`empty`ocid1.cpg...`
`clusterPlacementGroupFilter`Filter for placement group Required if`clusterPlacementGroupId`empty See[OciResourceSelectorTerm](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_ociresourceselectorterm).

### ComputeClusterConfig

Use`computeClusterConfig`when you want worker nodes to run in a compute cluster.

Field Description Required Example / Notes
`computeClusterId`Compute cluster OCID Required if`computeClusterFilter`empty`ocid1.cluster...`
`computeClusterFilter`Filter for compute cluster Required if`computeClusterId`empty See[OciResourceSelectorTerm](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_ociresourceselectorterm).

### KubeletConfig

Use`kubeletConfig`to override kubelet settings on Karpenter-provisioned worker nodes. Karpenter Provider for OCI (KPO) applies these settings during node provisioning.

Field Description Required Example / Notes
`clusterDNS`List of cluster DNS IPs Optional`[ "10.0.0.10" ]`
`extraArgs`Kubelet extra args Optional`--fail-swap-on=false`
`nodeLabels`Kubelet node labels Optional`{ "role": "worker" }`
`maxPods`Maximum pods per instance (minimum 1) Optional`110`
`podsPerCore`Pods per CPU core Optional`20`
`systemReserved`System resource reservations Optional`{ "cpu": "1" }`
`kubeReserved`Kubernetes component reservations Optional`{ "cpu": "1" }`
`evictionHard`Hard eviction thresholds Optional`{ "memory.available": "200Mi" }`
`evictionSoft`Soft eviction thresholds Optional`{ "memory.available": "500Mi" }`
`evictionSoftGracePeriod`Grace periods for soft eviction Optional`{ "memory.available": "30s" }`
`evictionMaxPodGracePeriod`Max pod graceful termination (seconds) Optional`60`
`imageGCHighThresholdPercent`High-water disk usage percentage that triggers image garbage collection (GC) Optional`85`
`imageGCLowThresholdPercent`Low-water disk usage percentage as target for image garbage collection (GC) Optional`75`

### LaunchOptions

Use`launchOptions`to set instance launch options.

Field Description Required Example / Notes
`bootVolumeType`Boot volume type (ISCSI, SCSI, IDE, VFIO, PARAVIRTUALIZED) Optional`"ISCSI"`
`remoteDataVolumeType`Remote data volume type Optional`"PARAVIRTUALIZED"`
`firmware`Firmware (BIOS or UEFI_64) Optional`"UEFI_64"`
`networkType`NIC emulation (VFIO, E1000, PARAVIRTUALIZED) Optional`"E1000"`
`consistentVolumeNamingEnabled`Consistent volume naming feature Optional`false`(example shows`true`).

### OCINodeClassStatus

Use`status`fields to troubleshoot validation and resolved configuration.

Field Type Description
`Conditions``[]status.Condition`Conditions for readiness, image, and network. Might include capacityReservation, clusterPlacementGroup, computeCluster
`Volume``Volume`Volume configuration and state
`Network``Network`Network configuration and state
`CapacityReservations``[]CapacityReservation`Capacity reservation details, if present
`ClusterPlacementGroups``[]ClusterPlacementGroup`Cluster placement group details, if present
`ComputeCluster``ComputeCluster`Compute cluster details, if present

## Scheduling, Labels, and Taints

### Scheduling Labels

Use node labels in`NodePool.spec.template.spec.requirements`and in workload scheduling rules (for example, node selectors and node affinity). Use standard Kubernetes labels and OCI-specific labels. KPO adds OCI-specific labels to nodes it provisions.

Label Example value Description
`topology.kubernetes.io/zone``Uocm:PHX-AD-1`Availability domain
`node.kubernetes.io/instance-type``VM.Standard.B1.4`OCI shape name.

For flexible shapes use a name in the following format:
```

```

where`<X>o`is the number of CPUs,`<Y>g`is the memory in GB, and`<burstableRatio>b`is one of`1_1`,`1_2`, or`1_8`. For example:
```

```

`kubernetes.io/os``linux`OS value as defined by Go[GOOS values](https://github.com/golang/go/blob/master/src/internal/syslist/syslist.go)(KnownOS) on the instance
`kubernetes.io/arch``amd64`Architecture value as defined by Go[GOARCH values](https://github.com/golang/go/blob/master/src/internal/syslist/syslist.go)(KnownArch) on the instance
`karpenter.sh/capacity-type``spot`Capacity types include`reserved`,`spot`, and`on-demand`
`oci.oraclecloud.com/instance-shape``[ VM.Standard.E5.Flex, VM.Standard.E6.Flex ]`OCI-specific label available on all shapes
`oci.oraclecloud.com/gpu-shape``true`OCI-specific label available on all GPU shapes
`oci.oraclecloud.com/baremetal-shape``true`OCI-specific label available on all bare metal shapes
`oci.oraclecloud.com/denseio-shape``true`OCI-specific label available on all dense I/O shapes
`oci.oraclecloud.com/flex-shape``true`OCI-specific label available on all flexible shapes
`oci.oraclecloud.com/fault-domain``FAULT-DOMAIN-1`OCI-specific. Fault domain within the selected availability domain. Use this label to constrain placement to a specific fault domain, such as`FAULT-DOMAIN-1`,`FAULT-DOMAIN-2`, or`FAULT-DOMAIN-3`
`oci.oraclecloud.com/capacity-reservation-id`last segment of reservation OCID, including the last dot OCI-specific label for capacity reservation ID. To accommodate the 63 character limit of Kubernetes labels, remove all characters before the last dot of the capacity reservation OCID.

### Required Taints and Tolerations

Use taints and tolerations to control where workloads run. Configure taints in the`NodePool`so Karpenter offers the corresponding capacity, then configure tolerations in workloads that must run on those worker nodes.

Be aware of the following special scenarios:
- 

Preemptible (Spot) Worker Nodes:

Worker nodes launched as spot capacity use the taint`oci.oraclecloud.com/oke-is-preemptible`.

To use spot capacity:
- 

Add the taint to the`NodePool`so Karpenter offers spot shapes.
- 

Add the corresponding toleration to workloads that must run on preemptible nodes.

`NodePool`taint example:
```

```

If the`NodePool`does not include the taint`oci.oraclecloud.com/oke-is-preemptible`, Karpenter does not offer preemptible shapes.
- 

GPU Worker Nodes:

Worker nodes launched with GPU shapes use vendor-specific taints:
- 

NVIDIA GPU shapes:`nvidia.com/gpu`
- 

AMD GPU shapes:`amd.com/gpu`

To use GPU shapes:
- 

Add the appropriate taint to the`NodePool`so Karpenter offers GPU shapes.
- 

Add the corresponding toleration to GPU workloads.

`NodePool`taint example (NVIDIA):
```

```

If the`NodePool`does not include the appropriate taint, Karpenter does not offer the corresponding shapes.

## Validating Node Provisioning

Use Karpenter and KPO custom resources to confirm that Karpenter is creating`NodeClaim`resources and that worker nodes are joining the cluster.
- Confirm that`NodePool`and`OCINodeClass`resources exist by entering:

```

```

```

```

- Confirm that Karpenter is creating`NodeClaim`resources by entering:

```

```

```

```

- Confirm that nodes are created and labeled with the name of the node pool they belong to.
- List all nodes in the cluster and show the value of the`karpenter.sh/nodepool`label for each node by entering:

```

```

- List only nodes that have the`karpenter.sh/nodepool`label by entering:

```

```

- If nodes do not join the cluster, review the KPO controller pods and logs by entering:

```

```

```

```

## NodePool and OCINodeClass Examples

Use the following examples to create`NodePool`and`OCINodeClass`resources for common worker node provisioning scenarios. Each example shows how to combine Karpenter scheduling intent in a`NodePool`with OCI-specific settings in an`OCINodeClass`:
- [Example 1: Flexible Shapes with an Explicit OKE Image OCID](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-examples__section_conteng-kpo-examples-flexible-shape)
- [Example 2: Image Filter Selection with Drift Replacement](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-examples__section_conteng-kpo-examples-image-drift)
- [Example 3: Secondary VNIC for OCI VCN IP Native CNI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-examples__section_conteng-kpo-examples-secondary-vnic)

For more information about mapping common OCI features to`NodePool`requirements or`OCINodeClass`fields, see[Additional Use Cases](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-examples__section_conteng-kpo-examples-additional-usecases).

### Example 1: Flexible Shapes with an Explicit OKE Image OCID

Use this example when you want a`NodePool`that allows specific flexible shapes, and you want an`OCINodeClass`that defines sizing for those flexible shapes and selects an OKE image by OCID.
```

```

### Example 2: Image Filter Selection with Drift Replacement

Use this example when you want KPO to use a filter to select an image automatically, and you want Karpenter to replace worker nodes when they drift from the selected image.

The image that is selected depends on the cluster's Kubernetes version and the available OKE images. When the cluster control plane is upgraded or new OKE images are released, the desired worker node image will also change. Nodes launched with an outdated image are considered to have "drifted". To minimize unexpected disruption during such events, we recommend that you configure an appropriate disruption budget in the Karpenter node pool, specifying reasons, disruption percentage, and schedule (for more information, see[Disruption](https://karpenter.sh/docs/concepts/disruption/)in the Karpenter documentation).
```

```

### Example 3: Secondary VNIC for OCI VCN IP Native CNI

Use this example when your cluster uses the OCI VCN IP Native CNI add-on and pods need IP addresses from a secondary VNIC subnet. Configure`secondaryVnicConfigs`to attach a secondary VNIC and allocate pod IP capacity.
```

```

### Additional Use Cases

Use the following table to map common OCI features to`NodePool`requirements or`OCINodeClass`fields.

Use case What to configure Notes
Spot capacity type support In the`NodePool`, set`karpenter.sh/capacity-type`to`spot`:
```

```

KPO maps the Karpenter`spot`capacity type to OCI preemptible instances. Configure the required preemptible taint in the`NodePool`and tolerations in workloads.

For more information about the support, benefits, and limitations of preemptible instances, see[Preemptible Instances](https://docs.oracle.com/iaas/Content/Compute/Concepts/preemptible.htm).
Reserved capacity type support In the`OCINodeClass`, configure`capacityReservationConfigs`:
```

```

KPO maps the Karpenter reserved capacity type to OCI capacity reservations.

An OCI capacity reservation is an availability domain-level resource that can be configured with multiple instance reservation configurations. Each configuration specifies a shape, optional shape settings, and capacity.

When an`OCINodeClass`is configured with a capacity reservation, KPO filters instance offerings to match reservation availability domain and reservation instance configurations.

For more information about capacity reservations, see[Capacity Reservations](https://docs.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm).
Burstable instance support In the`OCINodeClass.shapeConfigs`, set`baselineOcpuUtilization`:
```

```

Burstable instances are supported on OCI flexible shapes.

An OCI burstable instance is a virtual machine (VM) instance that provides a baseline level of CPU performance with the ability to burst to a higher level to support occasional spikes in usage.

For more information about burstable instances, see[Burstable Instances](https://docs.oracle.com/iaas/Content/Compute/References/burstable-instances.htm).
Cluster placement group support In the`OCINodeClass`, configure`clusterPlacementGroupConfigs`:
```

```

An OCI cluster placement group enables you to create resources in close proximity to one another to support low-latency networking use cases. A cluster placement group is an availability domain-level resource, and only one cluster placement group per availability domain is allowed.

For more information about cluster placement groups, see[Overview of Cluster Placement Groups](https://docs.oracle.com/iaas/Content/cluster-placement-groups/overview.htm).
Compute cluster support In the`OCINodeClass`, configure`computeClusterConfig`:
```

```

A compute cluster is a group of high performance computing (HPC), GPU, or optimized instances that are connected with a high-bandwidth, ultra low-latency network.

Configure at most one compute cluster per`OCINodeClass`. Compute cluster configuration is immutable after creation.

For more information about compute clusters, see[Compute Clusters](https://docs.oracle.com/iaas/Content/Compute/Tasks/compute-clusters.htm).
Customize kubelet In the`OCINodeClass`, configure`kubeletConfig`. Use[KubeletConfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_kubeletconfig)fields to control node-level kubelet behavior. If a kubelet configuration field is not shown for[KubeletConfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ocinodeclass__section_kpo_kubeletconfig), consider using the`extraArgs`field.
Customize compute instance In the`OCINodeClass`, configure`nodeCompartmentId`,`metadata`,`freeformTags`,`definedTags`,`sshAuthorizedKeys`, and`launchOptions`. Use OCI instance fields to control metadata, tags, SSH access, and launch behavior.

For more information about how to configure each field, see[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).

Maintain static worker node capacity

In the`NodePool`, set`spec.replicas`to the number of worker nodes to maintain.
```

```

Static capacity is an alpha feature and is disabled by default. Use it when you want Karpenter to maintain a fixed number of worker nodes, even when there are no pending pods.

In the Helm values file, enable`settings.featureGates.staticCapacity`.

Influence scheduling with NodeOverlay

In`NodeOverlay`, configure`spec.requirements`to select the node pools or instance shapes that the overlay applies to. Configure`spec.price`,`spec.priceAdjustment`, or`spec.capacity`to influence scheduling simulations.
```

```

NodeOverlay is an alpha feature and is disabled by default. Use it to influence Karpenter scheduling simulations for selected node pools or instance shapes by applying a price override, price adjustment, or extended-resource capacity.

In the Helm values file, enable`settings.featureGates.nodeOverlay`.
Enable Oracle Cloud Agent plugins when KPO launches an instance In the`OCINodeClass`, configure`agentPlugins`. For more information, see[KPO Oracle Cloud Agent Plugins documentation on Github](https://github.com/oracle/karpenter-provider-oci/blob/main/docs/guide/agent-plugins.md).

## Resource Discovery and Cleanup

You can identify the resources that Karpenter Provider for OCI (KPO) creates. When you no longer need the capacity, you can remove those resources. Perform the following tasks:
- Identify the worker nodes and`NodeClaim`resources that Karpenter creates so you can scope the capacity you are auditing. For more information, see[Identify Karpenter-managed worker nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-cleanup__section_identify-karpenter-managed-nodes).
- Locate the corresponding OCI instances by using KPO-applied tags so you can verify which infrastructure is associated with that capacity. For more information, see[Identify OCI instances (and related resources) created for Karpenter nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-cleanup__section_identify-oci-instances).
- When resources are no longer required and before you delete a cluster, remove Karpenter-managed capacity so instances and attached resources do not continue running. Confirm that termination and deletion complete successfully, and that no orphaned resources remain. For more information, see[Clean up resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-cleanup__section_clean-up-resources).

### Identify Karpenter-managed worker nodes

Karpenter applies the`karpenter.sh/nodepool`label to the nodes it creates. To list the nodes created by Karpenter, and the`NodePool`resource that each node belongs to, enter:

```

```

To find out whether Karpenter is creating`NodeClaim`resources, or whether`NodeClaim`resources are blocked for some reason (for example, failing to launch, failing to register, or waiting on capacity), enter:

```

```

```

```

### Identify OCI instances (and related resources) created for Karpenter nodes

Use OCI search tools (such as the Resource Explorer) and the following OCI freeform tags to find instances and related resources that KPO created:
- 

`karpenterNodepool`
- 

`orcl-containerengine/cluster-id`(when applicable)

For more information about locating OCI resources, see[Querying Resources](https://docs.oracle.com/iaas/Content/Search/Tasks/queryingresources.htm)

### Clean up resources

Before you delete a cluster, remove Karpenter-managed capacity so that instances do not remain running after the cluster has been deleted.
- 

Delete Karpenter`NodePool`resources that create capacity by using`kubectl delete`and the`NodePool`name as follows:
- List`NodePool`resources by entering:
```

```

- Delete a`NodePool`resource by entering:
```

```

- (Optional) Confirm that the`NodePool`resource is deleted by entering:
```

```

- 

Confirm that`NodeClaim`resources and nodes are removed.
- Watch`NodeClaim`resources until they are deleted by entering:
```

```

- Watch nodes created for Karpenter node pools until they are removed:
```

```

- If a`NodeClaim`does not terminate, check its status, conditions, and events by entering:
```

```

- 

Use the OCI Console, CLI, or SDK to confirm that OCI instances and attached resources are deleted.
- Locate the instances that KPO created using the`karpenterNodepool`freeform tag (and the`orcl-containerengine/cluster-id`tag, when applicable).
- Confirm that no such instances are present, or are in a terminated state and then disappear.
- Confirm that there are no remaining VNIC attachments for the instance, and that any VNICs that were created for the instance no longer exist.
- Confirm that there are no remaining volume attachments for the instance, and that the boot volume that was created for the instance is deleted (or is terminated and then removed).

If any of the resources remain after the instance is terminated, treat them as potential orphaned resources and investigate whether:
- the KPO controller is running and has IAM permissions to clean up resources
- there are any deletion finalizers or errors in the KPO controller logs

## Troubleshooting

### What you can troubleshoot and where to look

When a workload can’t schedule or a worker node doesn’t join the cluster, check resources and log files, and metrics, and increase logging, as follows:
- 

Use kubectl to check Kubernetes resources (see[Check Kubernetes resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ops-troubleshooting__section_check-kubernetes-resources)).
- 

Use the OCI Console, CLI, or SDK to confirm that KPO created the expected instances, VNICs, NSGs, and boot volumes for worker nodes.
- 

Use kubectl to check KPO controller logs (see[Check KPO controller logs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ops-troubleshooting__section_check-kpo-controller-logs)).
- 

Increase logging (see[Enable debug logging](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-ops-troubleshooting__section_enable-debug-logging)).

### Check Kubernetes resources

Use kubectl commands to list key resources, as follows:

```

```

```

```

```

```

```

```

Use kubectl commands to review details and conditions, as follows:

```

```

```

```

### Check KPO controller logs

Use kubectl commands to review the status of KPO pods and to review logs, as follows:

```

```

```

```

### Enable debug logging

Increase logging temporarily when you need more detail in KPO controller output, in one or both of the following ways:
- 

Set`logLevel: debug`in the Helm values file and update the KPO deployment (see[How do you change and reapply Helm values to update the KPO deployment?](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-faq__section_reapply-helm-values)). By default, logging is at the`info`level.
- 

Set`OCI_GO_SDK_DEBUG=1`as an environment variable in the KPO deployment to enable OCI Go SDK debug logging.

## Frequently Asked Questions (FAQs) about KPO

### Do special taints added by OKE bootstrapping apply to Karpenter-managed nodes?

Yes. Some worker node types require specific taints. Configure the taints in the`NodePool`so Karpenter offers the corresponding capacity. Then configure tolerations in workloads that must run on those worker nodes.

For more information about special taints, see[Required Taints and Tolerations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-scheduling__section_conteng-kpo-taints_and_tolerations).

### How do you configure secondary VNICs?

When a cluster uses the OCI VCN IP Native CNI add-on, you can attach secondary VNICs to worker nodes so pods receive VCN-routable IP addresses from the pod subnet. Plan subnet capacity carefully so you don’t exhaust available addresses.

If the cluster is using the OCI VCN IP Native CNI add-on, the add-on must be version 3.0.0 or later. We strongly recommend the use of version 3.2.0 or later. In OCI VCN IP Native CNI add-on version 3.2.0 (and later), secondary VNICs support a maximum of 256 IP addresses. If the cluster is using a version of the add-on prior to version 3.2.0, secondary VNICs support a maximum of 16 IP addresses. If the cluster has to use a version of the add-on prior to version 3.2.0, you must explicitly set`ipCount`to a value no greater than 16.

In addition to the maximum number of supported IP addresses, secondary VNICs are subject to the following restrictions:
- 

The number of assigned IP addresses must be a power of two, so set`ipCount`to a power of two.
- 

For IPv6-only (single stack) secondary VNICs, only 1, 16, or 256 assigned IP addresses are supported, so set`ipCount`to 1, 16, or 256.
- 

The aggregate total of all assigned IP addresses across all secondary VNICs within a node must not exceed 256.
- If`ipCount`is not set for a secondary VNIC, it defaults to 32 for IPv4 clusters and IPv6 dual stack clusters, and to 256 for IPv6 single stack clusters.

Note the following recommendations and guidelines:
- We recommend that you configure two CIDR blocks for the pod subnet used by secondary VNICs.
- If the pod subnet used by secondary VNICs has a single CIDR block, make sure that the subnet has a sufficient number of contiguous IP addresses to accommodate the required number of IP assignments.

### How do you schedule workloads on a specific Karpenter node pool?

To force workloads onto a specific Karpenter node pool, target the node pool label`karpenter.sh/nodepool`. Use either node affinity or a node selector, depending on how strict you want placement to be.
- 

Node affinity example:
```

```

For more information about node affinity, see[Node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity)in the Kubernetes documentation.
- 

Node selector example:
```

```

For more information about node selectors, see[nodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector)in the Kubernetes documentation.

### How do you spread workloads across availability domains and fault domains with Karpenter Provider for OCI?

Karpenter Provider for OCI (KPO) honors pod-level`topologySpreadConstraints`when the`topologyKey`matches a scheduling label that KPO supports. Typically, you'll use these topology keys most often in OCI:
- `topology.kubernetes.io/zone`to spread across availability domains (ADs)
- `oci.oraclecloud.com/fault-domain`to spread across fault domains (FDs) within an AD

To spread Karpenter-provisioned capacity, target the intended node pool by using the`karpenter.sh/nodepool`label, and ensure that the selected`NodePool`allows the ADs or FDs that you want the scheduler to use. If you set`whenUnsatisfiable`to`DoNotSchedule`, pods that can’t satisfy the spread constraint remain pending, which gives Karpenter an opportunity to provision nodes that meet the spread requirement:

We recommend the following practices:
- Set`replicas`to a value equal to or greater than the number of topology domains you want to use.
- Use AD spreading when the workload must remain available across multiple ADs.
- Use FD spreading in a single-AD region.
- Ensure that`NodePool`requirements include all topology values that`topologySpreadConstraints`uses.

Example: Configure a`NodePool`to allow three ADs
```

```

Example: Spread a`Deployment`across those three ADs
```

```

Example: Configure a`NodePool`to allow three FDs in a single AD
```

```

Example: Spread a`Deployment`across those three FDs
```

```

Notes
- Use`whenUnsatisfiable: DoNotSchedule`when you want Karpenter to provision capacity that satisfies the spread constraint.
- Ensure that`labelSelector`matches the pod labels. If it does not match, the scheduler does not calculate skew for the intended pod set.
- For more information about supported scheduling labels, see[Scheduling, Labels, and Taints](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-scheduling).

### What happens when an OCI offering is unavailable?

When OCI reports that an offering (a combination of compute shape, availability domain, and capacity type) is unavailable because of insufficient capacity, KPO temporarily excludes the offering from scheduling. Karpenter can then try another compatible offering or select another compatible`NodePool`. Use`settings.unavailableOfferingsTTLSeconds`to specify how long KPO excludes the offering before considering it again. The default is 180 seconds.

By default, when an OCI service limit or compartment quota is exceeded, KPO returns the`LimitExceeded`or`QuotaExceeded`launch failure immediately. To have KPO temporarily treat the failed offering as unavailable, enable the following Helm setting:
```

```

Karpenter can then try another compatible offering or select another compatible`NodePool`.

Adjust the value of`settings.unavailableOfferingsTTLSeconds`to have KPO retry failed offerings sooner or later (we recommend avoiding low values). To completely disable the unavailable-offerings cache feature, set`settings.unavailableOfferingsTTLSeconds`to zero.

These settings do not increase OCI service limits or compartment quotas. Review and raise the applicable limit or quota when necessary.

### How do you list compatible OKE images for a cluster?

Use the OCI CLI to retrieve node pool options and filter the returned image sources. This approach enables you to identify image OCIDs that are compatible with the cluster Kubernetes version.
- 

Set environment variables that specify the region and cluster OCID, and that define filters for the Kubernetes version, OS major version, and any architectures or image types to exclude:
```

```

where:
- `<cluster-ocid>`is the OCID of the cluster.
- `<kubernetes-version>`is the Kubernetes minor version string to match in the image source name (for example,`1.31`).
- `<os-major-version>`is the OS major version to match in the image source name (for example,`8`for Oracle Linux 8). Set this to an empty string to avoid filtering by OS version.
- `<architecture-pattern>`is a regular expression pattern used to exclude image source names (for example,`aarch64|arm64|GPU`to exclude ARM or GPU images). Set this to an empty string to avoid exclusions.

For example:

```

```

- 

Run the following OCI CLI command to obtain the OCIDs of compatible images:

```

```

### What to do if a flexible shape node pool does not provision, and you see: “skipping, nodepool requirements filtered out all instance types.”

Flexible shapes require a sizing configuration so that KPO can translate shape requirements into a concrete offering. Fix this by defining`shapeConfigs`in the referenced`OCINodeClass`or by defining defaults in the Helm values file under`settings.flexibleShapeConfigs`.
- 

Example: Defining`shapeConfigs`in the referenced`OCINodeClass`:
```

```

- 

Example: Setting default`shapeConfigs`values globally in the Helm values file:
```

```

You can override a default in the Helm values file by setting`shapeConfigs`in the`OCINodeClass`.

If you’re using a capacity reservation and facing this issue, confirm that`flexibleShapeConfigs`in the Helm values file (or`shapeConfigs`in the`OCINodeClass`, if present) matches the reservation exactly, with the same values for`ocpus`,`memoryInGbs`, and`baselineOcpuUtilization`.

### How do you run the KPO controller with debug logging?

Increase log output to troubleshoot provisioning and OCI API calls in one or both of the following ways:
- 

Set`logLevel: debug`in the Helm values file and update the KPO deployment (see[How do you change and reapply Helm values to update the KPO deployment?](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-faq__section_reapply-helm-values)).
- 

Set`OCI_GO_SDK_DEBUG=1`as an environment variable in the KPO deployment to enable OCI Go SDK debug logging.

### How do you pass a custom cloud-init script?

You can execute specific commands or configurations during a node's startup process by injecting custom cloud-init scripts using the`OCINodeClass`resource.

Thoroughly test custom cloud-init scripts before deploying them, to ensure the scripts execute as expected and do not interfere with the standard node initialization process.

There are two primary methods:
- 

Option 1: Use`preBootstrapInitScript`and`postBootstrapInitScript`in`OCINodeClass`(recommended)

You can run custom scripts before and after the default cloud-init script by using`preBootstrapInitScript`and`postBootstrapInitScript`in the`OCINodeClass`to specify the custom scripts, as follows:
- Prepare the custom cloud-init scripts:
- Create the scripts you want to run before and after the default node initialisation.
- Base64-encode each script.
- 

Add the base64-encoded scripts to the`preBootstrapInitScript`and/or`postBootstrapInitScript`fields in the`OCINodeClass`resource.

For example:
```

```

- 

Option 2: Specify a full base64-encoded cloud-init script in`metadata.user_data`(advanced workflow)

You can provide a complete custom cloud-init script by setting the`user_data`field in the`metadata`section of the`OCINodeClass`. This method gives you full control of the initialization process, but requires careful management to ensure compatibility with Kubernetes Engine.
- 

Prepare the custom cloud-init script:
- Create the custom cloud-init script, and include both the custom configurations and the necessary commands that join the node to the cluster.

The following example reads configuration values from the OCI Instance Metadata Service (IMDS), which is available only from within the instance, and then runs the commands that join the node to the cluster.
```

```

If you use this example, only insert your custom logic:
- 

between`# BEGIN OF CUSTOM SCRIPT BOOTSTRAP SCRIPT , REPLACE THIS SECTION WITH CUSTOM PRE BOOTSTRAP SCRIPT`and`# END OF CUSTOM SCRIPT BOOTSTRAP SCRIPT`
- 

between`# BEGIN OF POST BOOTSTRAP SCRIPT, IF NEEDED`and`#END OF POST BOOTSTRAP SCRIPT`

Note that the parameters necessary to bootstrap nodes are available in the Instance Metadata Service (IMDS). When creating a custom script, we strongly recommend setting the`CLUSTER_DNS`,`KUBELET_EXTRA_ARGS`,`APISERVER_ENDPOINT`, and`KUBELET_CA_CERT`environment variables by retrieving their values from IMDS, as shown in the example script. Configuring these variables as shown is essential for the correct operation of KPO.
- Base64-encode the script.
- 

Add the base64-encoded script to the`user_data`field in the`metadata`section of the`OCINodeClass`.

For example:
```

```

### What should you consider for KubeletConfig maxPods and podsPerCore?

Use`kubeletConfig`to control the pod density of worker nodes, and keep it aligned with your networking capacity.
- 

Set`podsPerCore`to a value that does not exceed`maxPods`.
- 

For clusters that use the OCI VCN IP Native CNI add-on, set`maxPods`lower than the aggregate sum of`ipCount`values across secondary VNICs.

### How do you configure the OKE prebuilt image compartment OCID in Karpenter Provider for OCI (KPO)?

When you want KPO to use a custom image based on an OKE image (by setting`imageType: OKEImage`), and the image is located in a different compartment, you can enable KPO to discover the image using the`preBakedImageCompartmentId`Helm value or the`imageFilter`of`OCINodeClass`.

If you use only Oracle-published OKE images or you reference images directly by OCID (`imageId`), this configuration is not necessary.

Prerequisites
- 

You know the compartment OCID that contains the images you want KPO to discover.
- A suitable policy exists to enable the KPO controller to read images in the different compartment. For example:
```

```

Option 1: Configure the compartment for all OCINodeClass resources (using a Helm value)
- 

Set the`preBakedImageCompartmentId`Helm value:
```

```

- 

Apply the updated configuration by running`helm upgrade`for the KPO deployment (see[How do you change and reapply Helm values to update the KPO deployment?](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-kpo.htm#conteng-kpo-faq__section_reapply-helm-values)).

Option 2: Configure the compartment for a specific OCINodeClass (using imageFilter)

Set`compartmentId`in`imageFilter`:
```

```

Custom images based on OKE images (k8s_version requirement)

When you use a custom image based on an OKE image, ensure that the image has one or other of the following:
- a`k8s_version`freeform tag
- a`BaseImageId`value that points (directly or indirectly) to an ancestor OKE image that has the`k8s_version`tag

If neither is present, KPO cannot determine the Kubernetes version for the image, and image selection can fail with a`missing k8s_version tag`error.

### How do you change and reapply Helm values to update the KPO deployment?

To change Helm values after installation, update the Helm values file, and then apply the new configuration.
- 

Update the Helm values file (for example, add or change`logLevel: debug`).
- 

Download the latest index for the`karpenter-provider-oci`repository by entering:
```

```

- Apply the updated configuration by entering:
```

```

- Confirm that the updated configuration is applied and that the KPO controller pods restart successfully:
```

```
