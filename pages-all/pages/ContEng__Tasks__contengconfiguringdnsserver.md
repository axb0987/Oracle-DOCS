# Configuring DNS Servers for Kubernetes Clusters
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringdnsserver.htm
- Fetched: 2026-09-05 01:54 CDT

# Configuring DNS Servers for Kubernetes Clusters

Find out how to configure DNS servers for Kubernetes clusters you've created using Kubernetes Engine (OKE).

## Configuring Built-in DNS Servers (kube-dns, CoreDNS)

Clusters created by Kubernetes Engine include a DNS server as a built-in Kubernetes service that is launched automatically. The kubelet process on each worker node directs individual containers to the DNS server to translate DNS names to IP addresses.

Prior to Kubernetes version 1.14, Kubernetes Engine created clusters with kube-dns as the DNS server. However, from Kubernetes version 1.14 onwards, Kubernetes Engine creates clusters with CoreDNS as the DNS server. CoreDNS is a general-purpose authoritative DNS server that is modular and pluggable.

Default CoreDNS behavior is controlled by a configuration file referred to as a Corefile. The Corefile is a Kubernetes ConfigMap, with a Corefile section that defines CoreDNS behavior. You cannot modify the Corefile directly. If you need to customize CoreDNS behavior, you create and apply your own ConfigMap to override settings in the Corefile (as described in this topic). Note that with basic clusters, if you do customize CoreDNS default behavior, the customizations are periodically deleted during internal updates to the cluster (with enhanced clusters, customizations are not deleted).

When you upgrade a cluster created by Kubernetes Engine from an earlier version to Kubernetes 1.14 or later, the cluster's kube-dns server is automatically replaced with the CoreDNS server. Note that if you customized kube-dns behavior using the original kube-dns ConfigMap, those customizations are not carried forward to the CoreDNS ConfigMap. You will have to create and apply a new ConfigMap containing the customizations to override settings in the CoreDNS Corefile.

For more information about CoreDNS customization and Kubernetes, see the[Kubernetes documentation](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/#coredns)and the[CoreDNS plugin documentation](https://coredns.io/plugins/).

To create a ConfigMap to override the settings in the CoreDNS Corefile:
- 

Define a ConfigMap in a yaml file, in the format:

```

```

For example:

```

```

For more information about the ConfigMap options to use to customize CoreDNS behavior, see the[Kubernetes documentation](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/#coredns)and the[CoreDNS plugin documentation](https://coredns.io/plugins/).
- 

Create the ConfigMap by entering:

```

```

- 

Verify the customizations have been applied by entering:

```

```

- 

Force CoreDNS to reload the ConfigMap by entering:

```

```

## Configuring ExternalDNS to use Oracle Cloud Infrastructure DNS

ExternalDNS is an add-on to Kubernetes that can create DNS records for services in DNS providers external to Kubernetes . It sets up DNS records in an external DNS provider to make Kubernetes services discoverable via that DNS provider, and enables you to control DNS records dynamically. See[ExternalDNS](https://github.com/kubernetes-sigs/external-dns)for more information.

Having deployed ExternalDNS on a cluster, you can expose a service running on the cluster by adding the`external-dns.alpha.kubernetes.io/hostname`annotation to the service. ExternalDNS creates a DNS record for the service in the external DNS provider you've configured for the cluster.

ExternalDNS is not itself a DNS server like CoreDNS, but a way to configure other external DNS providers. Oracle Cloud Infrastructure DNS is one such external DNS provider. See[Overview of DNS](https://docs.oracle.com/iaas/Content/DNS/Concepts/dnszonemanagement.htm).

For convenience, instructions are included below to set up ExternalDNS on a cluster and configure it to use Oracle Cloud Infrastructure DNS. These instructions are a summary based on the[Setting up ExternalDNS for Oracle Cloud Infrastructure (OCI) tutorial](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/oracle.md), which is available on GitHub.

To set up ExternalDNS on a cluster and configure it to use Oracle Cloud Infrastructure DNS:
- Create a new DNS zone in Oracle Cloud Infrastructure DNS to contain the DNS records that ExternalDNS will create for the cluster. See[Creating a Zone](https://docs.oracle.com/iaas/Content/DNS/Concepts/gettingstarted.htm).
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- Create a Kubernetes secret containing the Oracle Cloud Infrastructure user authentication details for ExternalDNS to use when connecting to the Oracle Cloud Infrastructure API to insert and update DNS records in the DNS zone you just created.
- 
In a text editor, create a credentials file containing the Oracle Cloud Infrastructure user credentials to use to access the DNS zone:

```

```

where:
- `<region-identifer>`identifies the user's region. For example,`us-phoenix-1`
- `<tenancy-ocid>`is the OCID of the user's tenancy. For example,`ocid1.tenancy.oc1..aaaaaaaap...keq`(abbreviated for readability).
- `<user-ocid>`is the OCID of the user. For example,`ocid1.user.oc1..aaaaa...zutq`(abbreviated for readability).
- `<private-key>`is an RSA key.
- `passphrase: <passphrase>`optionally provides the passphrase for the key, if one exists
- `<compartment-ocid>`is the OCID of the compartment to which the DNS zone belongs
For example:

```

```

- Save the credentials file with a name of your choosing (for example,`oci-creds.yaml`).
- Create a Kubernetes secret from the credentials file you just created, by entering:

```

```

For example:

```

```

- Deploy ExternalDNS on the cluster.
- In a text editor, create a configuration file (for example, called`external-dns-deployment.yaml`) to create the ExternalDNS deployment, and specify the name of the Kubernetes secret you just created. For example:

```

```

- Save and close the configuration file.
- Apply the configuration file to deploy ExternalDNS by entering:

```

```

where`<filename>`is the name of the file you created earlier. For example:

```

```

The output from the above command confirms the deployment:
```

```

- Verify that ExternalDNS has been deployed successfully and can insert records in the DNS zone you created earlier in Oracle Cloud Infrastructure by creating an nginx deployment and an nginx service:
- In a text editor, create a configuration file (for example, called`nginx-externaldns.yaml`) to create an nginx deployment and an nginx service that includes the`external-dns.alpha.kubernetes.io/hostname`annotation. For example:

```

```

- Apply the configuration file to create the nginx service and deployment by entering:

```

```

where`<filename>`is the name of the file you created earlier. For example:

```

```

The output from the above command confirms the deployment:
```

```

- Wait a couple of minutes, and then verify that a DNS record was created for the nginx service in the Oracle Cloud Infrastructure DNS zone (see[Zones](https://docs.oracle.com/iaas/Content/DNS/Tasks/managingdnszones.htm)
