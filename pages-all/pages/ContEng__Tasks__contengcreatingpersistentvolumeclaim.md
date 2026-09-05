# Setting Up Storage for Kubernetes Clusters
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim.htm
- Fetched: 2026-09-05 01:54 CDT

# Setting Up Storage for Kubernetes Clusters

Find out how to define and apply persistent volume claims to clusters you've created using Kubernetes Engine (OKE). With Oracle Cloud Infrastructure as the underlying IaaS provider, you can provision persistent volume claims by attaching volumes from the Block Volume service, or by mounting file systems from the File Storage service or the File Storage with Lustre service.

Container storage via a container's root file system is ephemeral, and can disappear upon container deletion and creation. To provide a durable location to prevent data from being lost, you can create and use persistent volumes to store data outside of containers.

A persistent volume offers persistent storage that enables your data to remain intact, regardless of whether the containers to which the storage is connected are terminated.

A persistent volume claim (PVC) is a request for storage, which is met by binding the PVC to a persistent volume (PV). A PVC provides an abstraction layer to the underlying storage.

With Oracle Cloud Infrastructure, you can provision persistent volume claims:
- By attaching volumes from the Oracle Cloud Infrastructure Block Volume service. The volumes are connected to clusters created by Kubernetes Engine using CSI (Container Storage Interface) or FlexVolume volume plugins deployed on the clusters. Oracle recommends the CSI volume plugin since the upstream Kubernetes project deprecates the FlexVolume volume plugin in Kubernetes version 1.23. This method is supported for managed nodes and self-managed nodes, but not for virtual nodes. See[Provisioning PVCs on the Block Volume Service](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm).
- By mounting file systems in the Oracle Cloud Infrastructure File Storage service. The File Storage service file systems are mounted inside containers running on clusters created by Kubernetes Engine using a CSI (Container Storage Interface) volume plugin deployed on the clusters. This method is supported for managed nodes, self-managed nodes, and virtual nodes. See[Provisioning PVCs on the File Storage Service](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm).
- By mounting file systems in the Oracle Cloud Infrastructure File Storage with Lustre service. The File Storage with Lustre service file systems are mounted inside containers running on clusters created by Kubernetes Engine using a CSI (Container Storage Interface) volume plugin deployed on the clusters. This method is supported for managed nodes and self-managed nodes, but not for virtual nodes. See[Provisioning PVCs on the File Storage with Lustre Service](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_Lustre.htm).

By default, Oracle encrypts customer data at rest in persistent storage. Oracle manages this default encryption with no action required on your part.

For more information about persistent volumes, persistent volume claims, and volume plugins, see the[Kubernetes documentation](https://kubernetes.io/docs/concepts/storage/).
Note  
  

Support for persistent storage varies by node type:
- Managed nodes and self-managed nodes can use persistent volumes in the Block Volume service, the File Storage service, and the File Storage with Lustre service.
-
