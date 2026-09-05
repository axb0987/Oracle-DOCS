# Observing Worker Node and Add-On Health
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengobservingworkernodeaddonhealth.htm
- Fetched: 2026-09-05 01:55 CDT

# Observing Worker Node and Add-On Health

Find out how to observe the health and resource usage of worker nodes and core Kubernetes add-ons with Kubernetes Engine (OKE).

Kubernetes Engine enables you to observe the health and resource usage of worker nodes and key Kubernetes add-ons, such as CoreDNS and KubeProxy. You can observe health and resource usage in any cluster that supports managed add-ons. By collecting operational and resource metrics, you can proactively detect and troubleshoot potential issues and anomalies before workloads are affected.

To enable you to observe health and resource usage, Kubernetes Engine deploys the following two managed add-ons on each worker node:
- ObservabilityAgent: The ObservabilityAgent add-on collects infrastructure metrics from sources including kubelet, cAdvisor, CoreDNS, and KubeProxy.
- NodeProblemDetector: The NodeProblemDetector add-on identifies and surfaces issues such as resource saturation and network problems at the worker node level. The managed NodeProblemDetector configuration is designed to avoid conflicts with any existing deployments of this tool, or similar tools.

The observability add-ons are pre-configured to use minimal resources, and do not require extensive custom configuration. They are assigned a low scheduling priority, ensuring that system and user workloads remain the primary focus of worker node resources. Resources for the two observability add-ons are added to the kube-system namespace.

When observing health and resource usage, Kubernetes Engine collects the following metrics:
- Container and pod CPU, memory, and network usage (from kubelet and cAdvisor).
- CoreDNS DNS requests, error rates, and response times.
- KubeProxy service network statistics.
- Worker node health information, events, and conditions (from the NodeProblemDetector add-on).

Collected data is aggregated and made accessible using industry-standard endpoints and tools, such as those compatible with Prometheus.

Note that only metrics data for infrastructure and platform components is collected. More specifically, note that no identifiable workload or application data is collected.

Note also that an egress rule must have been defined for the Kubernetes API endpoint subnet to specify a port on which to allow traffic for observability and enhanced customer support (by default, port 9995).

## Enabling and Disabling Health Observation Functionality

Find out how to enable and disable health observation functionality with Kubernetes Engine (OKE).

You can enable and disable health observation functionality using the Console, the CLI, and the API.

- [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengobservingworkernodeaddonhealth.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengobservingworkernodeaddonhealth.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengobservingworkernodeaddonhealth.htm#)
- 

- On the Clusters list page, select the name of the cluster for which you want to enable health observation functionality. If you need help finding the list page or the cluster, see[Listing Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm).
- On the Add-ons tab, select Manage add-ons .
- Select the Edit option beside ObservabilityAgent or NodeProblemDetector .
- Select the Enable &lt;add-on name&gt; option to deploy and enable the cluster add-on if it hasn't been enabled on this cluster before, or to enable the cluster add-on if it has been deployed previously but is currently disabled.
- Configure the cluster add-on by specifying the following details:
- Automatic updates: Choose this option when you want Oracle to automatically update the add-on when a new version becomes available.
- Choose a version: Choose this option when you want to control the version of the add-on that Oracle deploys on the cluster. A warning indicates that you have taken responsibility for updating the add-on. If you choose this option, select the version of the add-on to deploy on the cluster from the Version list. See[Cluster Add-on Supported Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-supportedversions.htm).
- Option: and Value: (Optional) Select Add configuration to specify one or more key/value pairs to pass as arguments to the cluster add-on. See[Cluster Add-on Configuration Arguments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons-configurationarguments.htm).
- Select Save changes .

To disable the ObservabilityAgent or NodeProblemDetector add-on, select the Edit option beside the add-on, de-select the Enable &lt;add-on name&gt; option, and select Save changes .
- 

Use the[oci ce cluster install-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/install-addon.html)command and required parameters to deploy the ObservabilityAgent or NodeProblemDetector add-on:
```

```

```

```

Use the[oci ce cluster disable-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/disable-addon.html)command and required parameters to disable (and optionally remove) the ObservabilityAgent or NodeProblemDetector add-on deployed on a cluster:

```

```

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[InstallAddon](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/InstallAddon)operation or[DisableAddon](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/DisableAddon)operation to install or to disable (and optionally remove) the ObservabilityAgent or NodeProblemDetector add-on deployed on a cluster.

## Using Labels to Enable and Disable Health Observation Functionality on Specific Worker Nodes or on All Worker Nodes

Find out how to use labels to enable and disable health observation functionality on worker nodes with Kubernetes Engine (OKE).

To collect metrics from a specific worker node, apply labels to the worker node as follows:
```

```

```

```

To collect metrics from all worker nodes, apply labels as follows:
```

```

```

```

To disable health observation functionality on a specific worker node, apply labels to the worker node as follows:
```

```

```

```

## Observing the Health of Worker Nodes and Add-Ons

Find out how to observe worker node and add-on health after installing and enabling the ObservabilityAgent and NodeProblemDetector add-ons.

After installing and enabling the ObservabilityAgent and NodeProblemDetector add-ons, use standard Kubernetes and monitoring tools to observe worker node and add-on health.

For example, to query and visualize the metrics collected for worker node and add-ons, use monitoring solutions compatible with Prometheus or OpenMetrics. These metrics include container and pod resource usage, CoreDNS and KubeProxy statistics, and worker node health events.

### Obtaining metrics directly from a worker node (mTLS endpoint)

The ObservabilityAgent add-on exposes a metrics endpoint on each worker node and secures it with mutual TLS (mTLS). The metrics endpoint can only be accessed by a client presenting a valid client certificate issued by a trusted Certificate Authority (CA). A CA is a trusted issuer that signs certificates so other components can verify identity and establish encrypted connections. The client certificate must be signed by the cluster’s CA. The required certificates are available on the worker node after provisioning.

To fetch metrics from a worker node, connect to the node (for example, using SSH) and run a command similar to the following:
```

```

where:
- `--cert /var/lib/kubelet/pki/kubelet-client-current.pem`specifies the kubelet client certificate, which is trusted by the cluster CA.
- `--key /var/lib/kubelet/pki/kubelet-client-current.pem`specifies the private key for the client certificate (in this configuration, it is stored in the same PEM file).
- `--cacert /etc/kubernetes/ca.crt`specifies the cluster’s root CA certificate used to verify the server certificate presented by the metrics endpoint.
- `<node-private-ip>`is the worker node’s private IP address (for example,`10.0.10.121`).
- `https://<node-private-ip>:9995/metrics`is the ObservabilityAgent metrics endpoint on the node.

You can use the same certificates and endpoint when configuring your own metrics pipeline (for example, a Prometheus-compatible scraper) to collect and visualize ObservabilityAgent metrics.

### Checking the health of the add-ons

You can observe the health of the ObservabilityAgent and NodeProblemDetector add-ons themselves, as follows:
- 

To check DaemonSet status for the deployed observability add-ons, enter:
```

```

Confirm that the`oke-dataplane-observability-agent`and`oke-node-problem-detector`DaemonSets are running and that the desired and ready pod counts match the number of observed worker nodes.
- 

If you encounter unexpected results or issues with the observability add-ons, inspect pod logs for the ObservabilityAgent and NodeProblemDetector in the kube-system namespace by entering:
```

```

Also double-check that worker nodes have the required labels.

For more information about managing cluster add-ons, see[Cluster Add-on Management](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddonmanagement_topic.htm)
