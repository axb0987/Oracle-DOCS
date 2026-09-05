# Securing Kubernetes Engine
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/oke_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Kubernetes Engine

This topic provides security recommendations for using Oracle Cloud Infrastructure's Kubernetes Engine (also known as OKE).

## Multi-Tenant Clusters

### Mutually Distrusted Workloads

At this time, it is not recommended to run mutually distrusted workloads in the same cluster. For example, you should not run the following workloads in the same cluster:
- Development workloads and production workloads
- Control plane and data plane
- Workloads that run arbitrary customer code

### Workloads with Different Levels of Trust

Consider having separate clusters if you have multiple tenants, teams, or users accessing the same cluster with differing levels of trust. As mentioned in subsequent sections, Kubernetes and OKE offer methods to isolate workloads. However, these methods are not currently sufficient for hard multi-tenancy.

### Kubelets have Read Access to Resources

A kubelet running on a worker node in a cluster created by OKE cannot modify resources that do not belong to the kubelet's node. For more information, see details about the[NodeRestriction admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#noderestriction)in the Kubernetes documentation.

Note, particularly when running multi-tenant workloads, that even though a kubelet cannot modify resources that do not belong to its node, the kubelet can still read those resources. Such resources can include:
- services
- endpoints
- nodes
- pods
- secrets, configmaps, and persistent volumes bound to the kubelet's node

For more information, see[Using Node Authorization](https://kubernetes.io/docs/reference/access-authn-authz/node/)in the Kubernetes documentation.

## Encrypt Secrets at Rest in Etcd

Please review[Encrypting Kubernetes Secrets at Rest in Etcd](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengencryptingdata.htm)for information on configuring secret encryption.

## Role-Based Access Control (RBAC)

Kubernetes ships an integrated[Role-Based Access Control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)component that matches an incoming user or group to a set of permissions which are bundled into roles. These permissions combine verbs (get, create, delete) with resources (pods, services, nodes) and can be scoped to a namespace or cluster. A set of preconfigured roles are provided which offer reasonable default separation of responsibility, depending on what actions a client might want to perform.

It is important to understand how updates on one object may cause actions in other places. For example, a user may not be able to create pods directly, but allowing them to create a deployment, which creates pods on their behalf, will let them create those pods indirectly. Likewise, deleting a node from the API will result in the pods scheduled to that node being terminated and recreated on other nodes. The preconfigured roles represent a balance between flexibility and the common use cases, but more limited roles should be carefully reviewed to prevent accidental privilege escalation. You can make roles specific to your use case if the preconfigured roles don’t meet your needs.

You should always follow the principle of least privilege to ensure users and Kubernetes Service Accounts have the minimal set of privileges required. By default, any user with USE CLUSTER access in Oracle Cloud Infrastructure IAM or any Kubernetes Service Account will have no access to the Kubernetes API, except to the[discovery roles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#discovery-roles). See[About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm)﻿ to learn how IAM integrates with OKE.

You must use the OCID of the Principal when creating RBAC bindings (for example, user OCID, instance OCID, and service name).

## Cluster Security

You can control the operations that pods are allowed to perform on a cluster you've created with Kubernetes Engine by setting up pod security policies for the cluster. Pod security policies are a way to ensure that pods meet security-related conditions before they can be accepted by a cluster. For example, you can use pod security polices to:
- limit the storage choices available to pods
- restrict the host networking and ports that pods can access
- prevent pods from running as the root user
- prevent pods from running in privileged mode

Having defined a pod security policy for a cluster, you have to authorize the requesting user or pod to use the policy by creating roles and bindings. You can then specify whether a cluster enforces the pod security policies defined for it by enabling the cluster's PodSecurityPolicy admission controller.

For more information, see[Using Pod Security Policies with Kubernetes Engine (OKE)](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengusingpspswithoke.htm).

Note  
  

The upstream Kubernetes project deprecated pod security policies in Kubernetes version 1.21, and removed the feature in Kubernetes version 1.25. Consequently, Kubernetes Engine does not support pod security policies and the PodSecurityPolicy admission controller in clusters running Kubernetes version 1.25 and later.

If you require similar functionality, consider using Kubernetes pod security standards and the PodSecurity admission controller instead (along with the Privileged, Baseline, and Restricted policies). By default, Kubernetes Engine enables the PodSecurity admission controller in clusters running Kubernetes version 1.23 and later, in order to support pod security standards. For more information about Kubernetes pod security standards, and the PodSecurity admission controller, see[Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)in the Kubernetes documentation.

Alternatively, consider using other alternatives that are being developed in the Kubernetes ecosystem to enforce policies.

If you do decide to move from using pod security policies and the PodSecurityPolicy admission controller to using pod security standards and the PodSecurity admission controller, see[Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller](https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/)in the Kubernetes documentation. Note that it is important to complete the migration before creating a new cluster running Kubernetes version 1.25, or before upgrading an existing Kubernetes version 1.24 cluster to run Kubernetes version 1.25. Also note that the Console provides a convenient way to disable the use of the PodSecurityPolicy admission controller in existing Kubernetes clusters created and managed by Kubernetes Engine (see[Using the Console to Disable the PodSecurityPolicy Admission Controller](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengusingpspswithoke.htm#contengusingpspswithoke_topic-Using_the_Console_to_Disable_the_PodSecurityPolicy_Admission_Controller)).

## Node Pool Security

### Node Pool Compartments

Node pools in a cluster can span compartments. However, while using multiple compartments provides a convenient way to group and manage worker nodes, it does not provide any isolation between the worker nodes in the cluster. Any workload can be scheduled across any node pool regardless of the compartment. A valid use case for using more than one compartment for a node pool would be to easily create dynamic groups and IAM policies for worker nodes. An invalid use case for multiple compartments would be putting each node pool running a customer workload in a separate compartment under the assumption that the compartments are providing some type of security boundary or isolation.

### Node Pool Subnets

We recommend only using private subnets for node pools. A service gateway should be configured to provide access to Oracle Cloud Infrastructure services. A service gateway cannot be used if the subnets are public with an internet gateway . If your private subnets require access to the internet, use a NAT gateway .

### Controlling Which Nodes Pods May Access

By default, a pod may be scheduled on any node in the cluster. Kubernetes offers a[rich set of policies for controlling placement of pods onto nodes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/)and the[taint based pod placement and eviction](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)that are available to end users. For many clusters, the use of these policies to separate workloads can be a convention that authors adopt or enforce via tooling. These placement controls are not adequate in a multi-tenant environment when users with deployment capabilities are untrusted. If you have untrusted users deploying code then you should consider a cluster per untrusted group.

When using ZPR, use node placement controls to help schedule workloads onto node pools with the appropriate pod security attributes. These controls are not a security boundary for untrusted users.

### Limit Access Given to Instance Principals

By default, all pods on a node are able to access the instance principal certificates using the instance metadata endpoint. In order to avoid privilege escalation via instance principals, you should isolate workloads across node pools with different dynamic groups so that pods in a given node pool have the minimal set of privileges required to function.

For example, assume you have the following two workloads, which both require different access:
- LogArchiver - requires access to manage buckets and objects in Object Storage
- HostMonitor - requires access to the Compute API to manage Instances

The simplest approach would be to schedule them in the same node pool and provide the instance principal with all the required access. However, this increases the impact in the event one of the workloads becomes compromised. A better approach would be to schedule the workloads on separate node pools with the limited set of access the instance principals require for the applicable workload.

### Block Container Access to Instance Metadata

The preferred way to block access is using a network policy plugin with a default policy of "deny all". Then you would explicitly grant access to pods and networks using NetworkPolicy resources in Kubernetes via label selectors. If you don't have a network policy plugin installed, you can use a IPTables rule to restrict access from all pods on the host. We recommend that you do not use this approach to block a subset of pods on a host.
Important  
  
NetworkPolicy resources and the following IPTable rule only apply to containers in the pod overlay network. Containers and services running in the host network are not impacted by either option:

```

```

## Network Security

Pods running in your OKE Cluster often need to communicate with other pods in the cluster or with services outside the cluster. Kubernetes Engine offers multiple options to secure communication to and from the workloads in your cluster. For the best network security posture, you should evaluate using a combination of network policies (to secure pod-level network communication) and security lists (to secure host-level network communication).

### Zero Trust Packet Routing

Zero Trust Packet Routing (ZPR) provides an additional way to control network access for OKE resources. ZPR enforces layer 4 network access policies in the Oracle Cloud Infrastructure network fabric, based on ZPR security attributes assigned to supported OCI resources used by Kubernetes Engine.

You can use ZPR with existing network security controls, including network security groups, security lists, and Kubernetes network policies. ZPR does not replace these controls and does not enforce traffic between pods on the same worker node. For example, you can use Kubernetes network policies to control pod-to-pod traffic in a cluster, and use ZPR to control traffic between OKE resources and other OCI resources.

When using ZPR with managed node pools, plan workload placement carefully. Pod security attributes are applied at the node pool level. Workloads that require different security profiles should run in different node pools.

ZPR does not provide hard multi-tenancy for mutually distrusted workloads. Continue to follow the recommendations in this topic for multi-tenant clusters, node pool security, and workload isolation.

For more information about Kubernetes Engine and ZPR, see[Adding Security Attributes to Cluster-Related Resources, and Applying ZPR Policies](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengusingzpr.htm).

### Network Policies

[Network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)in Kubernetes allow administrators to define how groups of pods are able to communicate with other pods in the cluster. Also, network policies allow you to define how groups of pods are able to communicate with services outside the cluster (for example, Oracle Cloud Infrastructure services).

To restrict access using network policies, you need to install a network plugin. Network plugins configure and enforce the network policies defined in Kubernetes. Numerous network plugin options are available. You can follow our instructions here to install and configure Calico in your cluster. Network policy plugins work by restricting access on the host. For information on installing Calico into OKE, see[Example: Installing Calico and Setting Up Network Policies](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengsettingupcalico.htm).

ZPR is not an implementation of the Kubernetes NetworkPolicy resource. To enforce Kubernetes network policies, install and configure a network policy plugin, such as Calico.

### Node Pool Security Lists

Network administrators can define security list rules on node pool subnets to restrict access to and from worker nodes. Defining security list rules allows administrators to enforce network restrictions that cannot be overridden on the hosts in your cluster.

Because all pod-to-pod communication occurs in a VXLAN overlay network on the worker nodes, you cannot use security list rules to restrict pod-to-pod communication. However, you can use security lists to restrict access to and from your worker nodes.

Important: A minimum set of security list rules must exist on node pool subnets to ensure that the cluster can function. See[Example Network Resource Configurations](https://docs.oracle.com/iaas/Content/ContEng/Concepts/contengnetworkconfigexample.htm)for information on the minimum set of security list rules before you modify your security list rules.

## Workload Security Best Practices

### Use Image Digests Instead of Tags

We recommend that you only pull images using the image digests, and not pull images using tags (because image tags are mutable). Image digests are the sha256 digest of your image, which allows docker to verify the image it downloaded is what you expected.

Example image digest id:
```

```

Pull the image as shown in the following example:
```

```

You can use the following command to show all the digests for your local images:

```

```

### Limit Resource Utilization

[Resource quota](https://kubernetes.io/docs/concepts/policy/resource-quotas/)limits the number or capacity of resources granted to a namespace. This is most often used to limit the amount of CPU, memory, or persistent disk a namespace can allocate, but can also control how many pods, services, or volumes exist in each namespace.

[Limit ranges](https://kubernetes.io/docs/tasks/administer-cluster/memory-default-namespace/)restrict the maximum or minimum size of some of the resources above, to prevent users from requesting unreasonably high or low values for commonly reserved resources like memory, or to provide default limits when none are specified.

Access to resource quotas can be restricted via RBAC policies in Kubernetes. This can help an administrator ensure that users of a cluster are not able to use resources that they should not have access to. See[Limiting resource usage in the on a cluster](https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/#limiting-resource-usage-on-a-cluster)in the Kubernetes documentation for more information.

## Disabling the Tiller Add-on

OKE offers an optional Tiller add-on. This provides an easy way to install and use Helm+Tiller, allowing you to quickly provision and run Kubernetes. It is not recommended to use this add-on for production clusters because of the security risks associated with Tiller. Clusters provisioned with Tiller do not have authentication or authorization for API calls made to Tiller, which means they cannot provide attribution for requests. Therefore, any operator or service that can reach Tiller can invoke its APIs with Tiller access.

To solve the security problems associated with Tiller, Helm V3 was developed. The Helm V3 release[completely removed Tiller](https://helm.sh/blog/helm-3-released/)from Helm. We recommend that you consider using Helm V3 if you'd like to utilize the functionality offered by Helm+Tiller.
Note  
  
To disable the Tiller add-on on an existing cluster, contact Oracle Support.

## Disabling the Kubernetes Dashboard Add-on

OKE offers an optional Kubernetes Dashboard add-on, providing an easy way to install the Kubernetes Dashboard. The Kubernetes Dashboard is installed by OKE with the minimal set of privileges required to run. You will not be able to use the dashboard without providing additional credentials. See[Accessing a Cluster Using the Kubernetes Dashboard](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengstartingk8sdashboard.htm)for more information.

The dashboard is particularly useful for new Kubernetes users. However, we do not recommend installing this add-on on production clusters due to the lack of extensible authentication support. Consequently, you cannot specify that you want to install the Kubernetes Dashboard when creating a cluster using the Console. If you decide you do want to install the Kubernetes Dashboard, create the cluster using the API and set the isKubernetesDashboardEnabled attribute to true.

If you do install the Kubernetes Dashboard, we recommend that you restrict access within your cluster, instead of exposing it externally via either a load balancer or an ingress controller. The Kubernetes Dashboard is a common attack vector used to gain access to a Kubernetes Cluster.

Note
