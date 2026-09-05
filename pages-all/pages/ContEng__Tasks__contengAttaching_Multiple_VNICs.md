# Attaching Multiple Secondary VNICs for Pod Networking
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengAttaching_Multiple_VNICs.htm
- Fetched: 2026-09-05 01:53 CDT

# Attaching Multiple Secondary VNICs for Pod Networking

Find out how to attach and configure multiple secondary VNICs on worker nodes for pod networking using Kubernetes Engine (OKE). You can pin a pod to a single secondary VNIC profile using an Application Resource, or attach multiple pod interfaces using Multus and NetworkAttachmentDefinitions (NADs).

Attaching multiple secondary VNICs to worker nodes enables you to segment pod networking across different subnets and security controls (for example, front-end pods on one secondary VNIC/subnet/NSG, and back-end pods on another). Each secondary VNIC profile is configured with its own pool of pod IP addresses (controlled by`ipCount`) and network settings (such as subnet and NSGs). Optionally, you can associate a secondary VNIC profile with an Application Resource name so that workloads can select that profile explicitly.

If you define Application Resources on secondary VNIC profiles, Kubernetes Engine exposes those Application Resources on each node as Kubernetes Extended Resources (for example,`oke-application-resource.oci.oraclecloud.com/<resource-name>`), with node capacity reflecting how many pod IPs are available on the corresponding secondary VNIC profile.

Pods can use Application Resources in the following way:
- 

A pod can request a single Application Resource (via an Extended Resource request/limit) when you want that pod to select one secondary VNIC profile/interface.
- 

Nodes that expose Application Resources are tainted (with the`oci.oraclecloud.com/application-resource-only:NoSchedule`taint) so that pods that do not explicitly request an Application Resource do not schedule onto these nodes. Pods must include a matching toleration.
- 

Scheduling must satisfy the requested Application Resource (the node must have sufficient capacity for the requested Extended Resource).
- 

If you do not need scheduler-enforced pinning to a specific secondary VNIC profile, do not define an Application Resource on the VNIC profiles. Pods that require additional interfaces must use Multus and NetworkAttachmentDefinitions (NADs) to attach those interfaces.

Using multiple secondary VNICs for pod networking is supported only with the OCI VCN-Native Pod Networking CNI plugin. Multiple secondary VNICs for pod networking are not supported when using the flannel CNI plugin for pod networking. Compute shape VNIC limits, subnet/IP availability, and NSG rule limits still apply.

When a pod requests an Application Resource, pod scheduling proceeds as follows:
- 

You create a pod that requests a single Application Resource (optional: only if you want the pod pinned to one selectable secondary VNIC profile).
- 

Admission validation checks the pod specification, including whether the requested Application Resource and requested quantity are valid.
- 

The Kubernetes scheduler selects a node that has capacity for the requested Application Resource and available IPs on the corresponding secondary VNIC profile.
- 

The OCI VCN-Native Pod Networking CNI plugin assigns an IP address to the pod from the selected secondary VNIC profile.
- 

The pod uses that selected profile/interface as its primary network path in this scheduling model.

Before attaching multiple secondary VNICs for pod networking, ensure:
- 

The cluster uses VCN-native pod networking.
- 

The VCN, subnets, and NSGs are planned for the segmentation you want (because each secondary VNIC profile can point to a different subnet and security policy).
- 

If you want to assign ZPR security attributes to secondary VNICs, make sure the ZPR security attributes and ZPR policies have been created. You must also have permission to use the security attribute namespaces. See[Adding Security Attributes to Cluster-Related Resources and Applying ZPR Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm).
- 

The compute shape used for worker nodes supports the required number of VNIC attachments and the expected pod density.
- 

If you require multi-interface pods, confirm that Multus is deployed and that the required CNI plugins are present on worker nodes, and confirm the required OCI VCN-Native CNI plugin version for multi-interface support in your environment.
Note  
  

Do not combine Multus pod network annotations with pod-level Application Resource requests in the same pod spec, because that can create scheduling and interface-selection conflicts. If a multi-interface pod needs to select specific secondary VNIC profiles, define that selection in the NAD configuration instead of using a pod-level Application Resource request. For example, use a`deviceSelector`field such as`deviceSelector.appResource`or`deviceSelector.interfaceName`.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengAttaching_Multiple_VNICs.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengAttaching_Multiple_VNICs.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengAttaching_Multiple_VNICs.htm#)
- 

You can attach multiple secondary VNICs for pod networking:
- When creating a new node pool (either when creating a new cluster, or when scaling up an existing cluster).
- When updating an existing node pool.

In both cases, the cluster's Network type must be VCN-native pod networking . Multi-interface pod networking with Multus also requires the supported OCI VCN-Native CNI plugin version for your environment.
- 

Follow the instructions to create or update a managed node pool (see[Creating a Managed Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-node-pool.htm)or[Updating a Managed Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-node-pool.htm)as appropriate).
- When specifying details for the node pool:
- Optionally use Network Launch Type to select the networking launch type for worker node networking. If you do not select a value, PARAVIRTUALIZED is used as the default.

In most cases, select PARAVIRTUALIZED . Select VFIO only when the selected shape and image support hardware-assisted SR-IOV networking and your workload requires it. Select E1000 only when required for compatibility with an image or workload that does not support paravirtualized networking. Support for each launch type depends on the selected compute shape and image.
- Select Configure Secondary VNICs for nodes and specify details for the first secondary VNIC profile as follows:
- 

VNIC Attachment Display Name : Optional. Specify a display name for the VNIC attachment. The display name helps you identify this VNIC attachment in the node pool configuration.
- 

VNIC Display Name : Optional. Specify a display name for the VNIC. The display name helps you identify the VNIC in Networking and Compute resources.
- 

NIC Index : Optional. Specify the physical NIC to use for this VNIC attachment. This option is typically used on bare metal shapes when you want to place VNICs on specific physical NICs, for example to align workload traffic with available NIC bandwidth. If you do not specify a value, Kubernetes Engine uses the default placement for the selected shape and configuration.
- 

VNIC Subnet compartment : Specify the compartment that contains the subnet for this VNIC.
- 

VNIC Subnet : Specify the subnet for this VNIC. The subnet determines the network, route table, security rules, and IP address family available to the VNIC. For pod networking, choose a subnet that has enough available IP addresses for the number of pod IPs you want to allocate.
- 

Assign public IP to VNIC : Optional. Specify whether to assign a public IPv4 address to this VNIC. This setting applies to the VNIC only. Public IP addresses are not assigned to pods, regardless of whether the VNIC is in a public subnet or a private subnet. In most pod networking designs, leave this option unselected. Select it only if the subnet is public and you have a specific requirement for the VNIC itself to have a public IP address. Ensure that route tables and security rules restrict access appropriately.
- 

Assign IPv6 address to VNIC : Optional. Specify whether to assign an IPv6 address to this VNIC. This option is applicable only if the selected subnet supports IPv6.
- 

Skip source/destination check : Optional. Specify whether to skip source/destination checks for this VNIC. Enable this option only for routing, forwarding, or NAT use cases where the VNIC must send or receive traffic that is not addressed to one of its own IP addresses.
- 

# of IP addresses : Specify the number of pod IP addresses to allocate for this secondary VNIC profile (`ipCount`). The combined`ipCount`across all configured secondary VNIC profiles on a node can be up to 256. Size this value with enough headroom for expected pod density, and consider subnet capacity and compute shape VNIC limits.
- 

Application Resources : Optional. Select Add application resource to add an Application Resource name to this secondary VNIC profile. Use Application Resources when you want workloads to select this VNIC profile explicitly. Kubernetes Engine exposes Application Resources as Kubernetes Extended Resources on nodes, and a pod can request one Application Resource to pin the pod to a selected profile. Each pod can request only one Application Resource in the pod-level scheduling model. If you do not need pods to select a specific profile, do not define Application Resources. For multi-interface pods that use Multus and NetworkAttachmentDefinitions (NADs), define interface selection in the NAD configuration instead of using pod-level Application Resource requests.
- 

Network Security Group : Optional. Select Add network security group to associate one or more NSGs with this VNIC. Use NSGs to control traffic to and from the VNIC. Apply least-privilege rules so that only the traffic required by the workload is allowed.
- 

VNIC Tags : Optional. Select Add tag to add one or more freeform tags or defined tags to the VNIC. Use tags to organize, track, and manage VNIC resources according to your tagging strategy.
- Security attributes: Optional. Specify one or more (up to a maximum of five) ZPR security attributes to add to the secondary VNIC. Note that if you define multiple secondary VNICs for a managed node pool, you must specify the same security attributes for all of the secondary VNICs.

If you have permissions to create a resource, then you might also have permissions to add security attributes to that resource. To add a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.

See also[Adding Security Attributes to Cluster-Related Resources and Applying ZPR Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm)
- If you want to use multiple secondary VNIC profiles, select Add VNIC and enter details for one or more additional secondary VNIC profiles.
- 

You can specify multiple secondary VNICs for pod networking when creating or updating managed node pools. For example, using the[oci ce node-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/create.html)command, as follows (abbreviated for readability):
```

```

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

You can specify multiple secondary VNICs for pod networking when creating or updating managed node pools, using the following operations:
- [CreateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/CreateNodePool)
- [UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool)

## Deploying pods that use multiple secondary VNICs

When you attach multiple secondary VNIC profiles to a node pool, you can deploy workloads in different ways depending on whether you want a pod to use a single pinned network path or to use multiple interfaces .

### Option 1: Pin a pod to a single secondary VNIC profile using an Application Resource

Use this option when a node exposes multiple selectable secondary VNIC profiles and a workload must be pinned to exactly one of them.

Step 1: Verify the Extended Resource names and capacity on a node

After the node pool has worker nodes, verify the Extended Resource names and capacity on a node.
- 

Review the node’s advertised Extended Resources:
```

```

- In the`Capacity`section of the output, identify the Extended Resources that correspond to Application Resources (for example`oke-application-resource.oci.oraclecloud.com/frontend`) and confirm they have non-zero capacity.
Step 2: Add the required toleration to the pod spec

Nodes that expose Application Resources are tainted with`oci.oraclecloud.com/application-resource-only:NoSchedule`to prevent pods without explicit Application Resource requests from landing on them.

Add a corresponding toleration to the pod spec (at`spec.tolerations`for a Pod, or at`spec.template.spec.tolerations`in a Deployment):
```

```

Without this toleration, the scheduler will reject placement even if resource capacity exists.
Step 3: Request exactly one Extended Resource (one Application Resource per pod)

In the pod spec, request the Extended Resource that corresponds to the secondary VNIC profile the pod must use (for example, in a Deployment at`spec.template.spec.containers[].resources`). Request and limit exactly one unit so the scheduler reserves capacity consistently.

For example:
```

```

Step 4: (Optional) Target the correct node pools

If your organization uses a node label/selector convention for these nodes (for example,`gva_vnic: "yes"`), include it so pods do not land on node pools that do not have the required resources:
```

```

A nodeSelector is optional when Application Resource requests and tolerations already constrain scheduling. Only use a nodeSelector if you have labeled the target nodes (for example via node pool Kubernetes labels).
Step 5: Verify scheduling

After deployment:
- Enter:
```

```

- For a pod of interest, enter:
```

```

- Confirm the pod is Running and that there are no scheduling errors (for example, insufficient capacity for the requested resource).

### Option 2: Use multiple interfaces in a pod (Multus + NADs)

Use this option when a pod must attach to multiple network interfaces. In this model, Multus attaches additional pod interfaces and the NADs define which host interface (and optionally which secondary VNIC profile) each pod interface should use.
Note  
  

- Do not combine Multus pod network annotations with pod-level Application Resource requests in the same pod spec.
- If you need per-interface selection of secondary VNIC profiles, define that selection in the NAD (for example, using a`deviceSelector`).
Step 1: Install and verify Multus (if not already installed)

Install Multus before creating NADs or deploying multi-interface pods. For information about installing Multus, see the[Multus-CNI documentation on GitHub](https://github.com/k8snetworkplumbingwg/multus-cni?tab=readme-ov-file#multus-cni).

Follow your organization’s standard process for deploying Multus, then verify it is healthy:
```

```

Step 2: Ensure required CNI plugins are present on worker nodes

The examples in this section use the`ipvlan`CNI plugin for the additional pod interface. Ensure that the`ipvlan`binary is present at`/opt/cni/bin/ipvlan`on every worker node that can run multi-interface pods.

Oracle recommends installing the`ipvlan`plugin using a node pool cloud-init script so that the plugin is installed when nodes are created, replaced, or scaled out. Pin the plugin to a validated release for the target environment, rather than following a floating download path. The following example uses version`v1.9.0`.

For example:
```

```

If worker nodes cannot access GitHub, stage the required CNI plugins archive in OCI Object Storage or another approved internal location, and update the download URL in the cloud-init script.
Step 3: Identify host interface names on a worker node

NADs must target the actual host interface names created by the attached VNICs (for example,`enp1s0`,`enp2s0`). Verify them on a worker node using your organization’s standard access method.
Step 4: Create NADs that select specific interfaces

Create:
- one NAD for the default pod network (to control which host interface backs`eth0`)
- one or more NADs for additional interfaces (for example,`net1`).

Your NAD configuration can select a device using a`deviceSelector`(for example, by`interfaceName`, or by Application Resource name using`appResource`if supported in your environment).

The following NAD examples intentionally use different namespaces.`oci-vcn-native-network`is defined in`kube-system`, while`ipvlan-network`is defined in`default`. If the workload runs in another namespace, create`ipvlan-network`in that namespace or update the pod annotation to reference the fully qualified NAD name.

Default network NAD pinned to`enp1s0`:
```

```

Secondary network NAD pinned to`enp2s0`:
```

```

The default NAD uses the OCI-specific`oci-ipvlan`and`oci-ptp`plugins because that interface participates in the OKE VCN-native default-network path. The additional NAD uses the standard`ipvlan`plugin because Multus is attaching an extra interface on a specific host NIC, while OCI IPAM still provides the subnet-aware IP allocation.

`deviceSelector`can target interfaces with fields such as:
```

```

The`deviceSelector`block lets OCI IPAM choose the target interface or VNIC used for pod IP allocation. It can select a device using one or more of these fields:
- 

`appResource`: Selects the GVA VNIC profile by Application Resource name.
- 

`interfaceName`: Selects a specific host interface, such as`enp1s0`.
- 

`interfaceNamePrefix`: Selects an interface by prefix, such as`enp`.
- 

`macAddress`: Selects an interface by MAC address.

When`appResource`is set in the NAD device selector, the OCI IPAM plugin uses that Application Resource to decide which GVA VNIC profile should provide the pod IP address and act as the parent device for that interface. This allows different NADs in the same pod to map to different VNIC profiles, for example:
- 

`NAD1`-&gt;`Application Resource: vnic-a`
- 

`NAD2`-&gt;`Application Resource: vnic-b`
- 

`NAD3`-&gt;`Application Resource: vnic-c`

If a pod uses all three NADs, each interface can be attached through the corresponding VNIC profile.

In the interface-name examples shown in this document:
- 

The`oci-vcn-native-network`NAD uses`interfaceName: enp1s0`so OCI IPAM allocates the pod's default-network IP from the host's`enp1s0`interface.
- 

The`ipvlan-network`NAD uses`interfaceName: enp2s0`so OCI IPAM allocates the additional interface IP from the host's`enp2s0`interface.

This is also why the pod example sets:
```

```

The`v1.multus-cni.io/default-network`annotation ensures`eth0`uses the`oci-vcn-native-network`NAD. Without explicitly selecting that default network, OCI IPAM can allocate from any eligible host interface, which makes the primary pod interface less predictable. Setting the default NAD ensures`eth0`uses the intended interface and keeps it isolated from the additional network attachment.

Do not combine these Multus pod annotations with pod-level Application Resource requests in the same pod spec. If a multi-interface pod needs GVA VNIC selection, define that selection inside the NAD`deviceSelector.appResource`configuration for each interface instead of using a pod-level Application Resource request.

Apply the NADs:
```

```

```

```

Step 5: Deploy a multi-interface pod using Multus annotations

Annotate the pod to select the default network NAD and attach additional network NADs, for example:
```

```

Step 6: Verify multiple interfaces
- Describe the pod and check Multus network status annotations (if present):
```

```

- If permitted in your environment, exec into the pod and inspect interfaces (for example,`ifconfig`or`ip addr`) to confirm that the pod has the expected interfaces (`eth0`,`net1`, …) and IP addresses.

### Option 3: Use secondary VNIC profiles without Application Resources

If you attach multiple secondary VNIC profiles to a node pool and do not define Application Resources, pods are not pinned to a single secondary VNIC profile by scheduler-enforced resource requests. This option does not require pods to request Extended Resources. Pods that require additional interfaces must use Multus and NetworkAttachmentDefinitions (NADs) to attach those interfaces.

Use this model when the goal is to size overall pod IP capacity, rather than to pin different workloads to different profiles using Application Resources. For multi-interface pods, define interface selection in the NAD configuration, for example by using`deviceSelector.interfaceName`or`deviceSelector.appResource`.

## Configuring kubelet max-pods on worker nodes

In most cases, you do not need to configure kubelet`max-pods`manually for node pools that attach multiple secondary VNIC profiles for pod networking. Kubernetes Engine sets the maximum number of pods per node based on the pod IP capacity available on the node.

Only set a custom`max-pods`value if you have a specific reason to cap pod density manually. When choosing a value, ensure it does not exceed the pod IP capacity available on the node.

To verify the effective pod limit in your cluster, inspect the node’s reported capacity/allocatable values (for example,`kubectl describe node <node-name>`) and confirm that the configured workload density does not exceed available pod IP capacity.

## Troubleshooting

### Pods stuck in Pending status

Pods can remain in a Pending status for a number of reasons. Common causes and solutions include:
- 

Cause: Insufficient capacity.

Occurs when there are no available pod IPs for the selected secondary VNIC profile, or when there is insufficient capacity for the requested Application Resource (if the pod is using an Application Resource to select a specific secondary VNIC profile).

Solution: Scale up the node pool, reduce the number of pods, or (for multi-interface pods) reduce the number of additional pod network attachments.
- 

Cause: Missing toleration.

Occurs when the pod lacks the required toleration for the`oci.oraclecloud.com/application-resource-only:NoSchedule`taint on nodes that expose Application Resources.

Solution: Add the missing toleration.
- 

Cause: Wrong resource name.

Occurs when the pod requests an Application Resource (Extended Resource) that does not exist on the target nodes.

Solution: Verify that the Application Resource names match the node pool configuration (case and spelling matter). Confirm the available resource names on a node by running`kubectl describe node <node-name>`and checking the`Capacity`section.
- 

Cause: Node selection prevents scheduling.

Occurs when the pod includes a`nodeSelector`or other placement constraints that exclude all nodes that have the required capacity.

Solution: Verify that the node labels exist and match exactly, or remove/adjust the node selection constraints.

### Pod rejected at creation time

If pod creation is rejected by admission validation, use the rejection message to correct the pod spec. Common issues include requesting unsupported combinations or quantities of Extended Resources, or specifying requests/limits that do not match the required pattern for the cluster configuration.

### Multi-interface pod does not get the expected interfaces

A multi-interface pod might be created successfully but not have the expected network interfaces, IP addresses, or interface-to-subnet mapping. For example, the pod might not have a`net1`interface, the`eth0`interface might not use the intended default network, or an additional interface might receive an IP address from a different subnet than expected.

Common causes include:
- 

Multus is not running in`kube-system`.
- 

The required CNI plugin, such as`ipvlan`, is not present on the worker nodes.
- 

The NAD references an incorrect host interface name.
- 

The pod annotation references the wrong NAD name or namespace.
- 

Interface selection is split between pod-level Application Resource requests and NAD configuration.

To resolve the issue, check the configuration in the order that Kubernetes and Multus use it: node pool configuration, required CNI components on the worker node, NAD configuration, and pod annotations.

Confirm that Multus is installed and running, and that the required CNI plugins are present on every worker node that can run the workload. Check that the NAD names and namespaces match the pod annotations, and that any`deviceSelector`values in the NAD match the actual worker node interface names or Application Resource names.

Do not combine pod-level Application Resource requests with Multus pod network annotations in the same pod spec. If the pod needs to select specific secondary VNIC profiles, define that selection in the NAD configuration instead.

After correcting the configuration, recreate the pod and inspect the Multus network status annotation and the interfaces inside the pod. Confirm that the pod has the expected interfaces, such as`eth0`and`net1`, and that the IP addresses are allocated from the intended subnets.

## Best practices

When attaching multiple secondary VNICs for pod networking, consider the following best practices:
- 

Decide whether workloads require a single network path or multiple pod interfaces. Use Application Resources to pin pods to a specific secondary VNIC profile when workloads must target exactly one profile. Use Multus and NetworkAttachmentDefinitions (NADs) when pods must attach multiple interfaces.
- 

Plan network segmentation first (subnets/NSGs/security zones). If you use Application Resources, map each Application Resource to the appropriate secondary VNIC profile, subnet, and NSGs.
- 

Right-size`ipCount`allocations and keep headroom to reduce scheduling failures. Review subnet capacity and shape VNIC limits as part of capacity planning.
- 

Use consistent naming for Application Resources and VNIC display names. If you use Multus, also use consistent naming for NADs and document which NAD selects which host interface or VNIC profile.
- 

Monitor capacity and scheduling health. If you use Application Resources, monitor Application Resource utilization and alert on low capacity and scheduling failures (per resource type). If you do not use Application Resources, monitor overall pod IP consumption and pod scheduling failures for the node pool.
-
