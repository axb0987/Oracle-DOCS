# Prerequisites for deploying the OCI Native Ingress Controller as a Standalone Program
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm
- Fetched: 2026-09-05 01:56 CDT

# Prerequisites for deploying the OCI Native Ingress Controller as a Standalone Program

Find out what you have to do before you can deploy the OCI native ingress controller as a standalone program to load balance and route incoming traffic to service pods running on worker nodes in a Kubernetes cluster.

Before deploying the OCI native ingress controller as a standalone program:
- Create a new cluster, or identify an existing cluster, that has either VCN-native pod networking or Flannel overlay as the network type. The cluster can be an enhanced cluster or a basic cluster. The cluster must be running Kubernetes version 1.26 or later. See[Creating a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-cluster.htm).
- Configure load balancer security rules to allow inbound and outbound traffic to and from the load balancer's subnet. See[Load Balancer Subnet Configuration](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#subnetconfig__section_loadbalancersubnetconfig).
- Set up an instance principal, user principal, or workload identity principal to enable the OCI native ingress controller to access other Oracle Cloud Infrastructure services and resources. See[Setting Up an Instance Principal, User Principal, or Workload Identity Principal to Enable Access to OCI Services and Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-auth).
- Grant permissions to the instance principal, user principal, or workload identity principal to allow the OCI native ingress controller to access resources. See[Granting Permissions to the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-permissions).
- Install cert-manager to generate and manage the TLS certificates required by the webhook server that supports the pod readiness gates feature. See[Installing cert-manager](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-certmanagerinstall).
- Install the Helm CLI, to enable you to install the OCI native ingress controller in one of two ways. See[Installing the Helm CLI to Install the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-helminstall).
- Clone the OCI native ingress controller repository from GitHub to a local repository, to enable you to deploy the OCI native ingress controller and specify parameter values for the deployment. See[Cloning the OCI Native Ingress Controller Repository and Setting Parameters in values.yaml](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-clone).

## Setting Up an Instance Principal, User Principal, or Workload Identity Principal to Enable Access to OCI Services and Resources

To create a load balancer and route incoming traffic, the OCI native ingress controller, whether installed as a standalone program or as a cluster add-on, performs actions on other Oracle Cloud Infrastructure service resources (including the Load Balancer service and the Certificates service). To perform those actions on OCI service resources, the OCI native ingress controller pod uses the credentials of an authorized actor (or principal). You can currently set up the following types of principal to enable the OCI native ingress controller to perform actions on OCI service resources:
- Instance principal: The OCI native ingress controller uses the identity of the instance on which it is running. See[Using instance principals to enable access to OCI services and resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-auth__section_instanceprincipalauthenticaton).
- User principal: The OCI native ingress controller uses an OCI user's identity. See[Using user principals to enable access to OCI services and resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-auth__section_userprincipalauthenticaton).
- Workload identity principal: The OCI native ingress controller uses the identity of a workload resource running on a Kubernetes cluster. See[Using workload identity principals to enable access to OCI services and resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-auth__section_workloadidentityauthenticaton).

Note:
- The use of instance principals to enable the OCI native ingress controller to access OCI services and resources is not supported in clusters with virtual nodes.
- The use of workload identity principals to enable the OCI native ingress controller to access OCI services and resources is supported with enhanced clusters, but not with basic clusters.

### Using instance principals to enable access to OCI services and resources

You can set up an instance principal to enable the OCI native ingress controller to perform actions on OCI service resources. Note that you can only use instance principals with managed nodes.

To set up an instance principal:
- Create a new dynamic group in the compartment to which the compute instances belong, containing the compute instances hosting the cluster's worker nodes:
- 

Follow the instructions in[To create a dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#To)in the IAM documentation, and give the new dynamic group a name (for example,`acme-oke-native-ingress-controller-dyn-grp`).
- Enter a rule that includes the compute instances in the compartment, in the format:

```

```

where`<compartment-ocid>`is the OCID of the compartment in which cluster node pools are created.

For example:
```

```

Before you deploy the OCI native ingress controller, you will:
- Grant permissions to the instance on which the OCI native ingress controller is running via the dynamic group. See[Granting Permissions to the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-permissions).
- Indicate you want to use instance principals with the OCI native ingress controller by specifying the following in the values.yaml file:

```

```

See[Cloning the OCI Native Ingress Controller Repository and Setting Parameters in values.yaml](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-clone).

### Using user principals to enable access to OCI services and resources

You can set up a user principal to enable the OCI native ingress controller to perform actions on OCI service resources.

To set up a user principal:
- If a suitable user does not exist already, create a user in IAM (see[To create a user](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingusers.htm#create_user)).
- If a suitable group does not exist already, create a group in IAM (see[To create a group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm#To)).
- Add the user to the group (see[To add a user to a group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingusers.htm#add_user)).
- 

Get these items:
- RSA key pair in PEM format (minimum 2048 bits). See[How to Generate an API Signing Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#two).
- Fingerprint of the public key. See[How to Get the Key's Fingerprint](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#four).
- Tenancy's OCID and user's OCID. See[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).
- Upload the public key from the key pair in the Console. See[How to Upload the Public Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#three).
- Create a config file as a .yaml file containing credential information, in the following format:

```

```

where:
- `region: <region-identifier>`is the region where the cluster resides. For example,`us-ashburn-1`
- `passphrase: <passphrase>`specifies the passphrase used for the key if it is encrypted.
- `user: <user-ocid>`is the OCID of the user that the OCI native ingress controller is to use.
- `fingerprint: <fingerprint>`is the fingerprint of the public key.
- `tenancy: <tenancy-ocid>`is the OCID of the tenancy containing the cluster.

For example:
```

```

- Create a Kubernetes secret resource in the cluster by entering:

```

```

where:
- `<secret-name>`specifies the name of the secret to create. For example,`oci-config`
- `--from-file=config=<config-file>.yaml`specifies the name and path of the .yaml file containing the credential information that you created previously. For example,`user-auth-config.yaml`
- `--from-file=private-key=./oci/oci_api_key.pem`specifies the name and path of the downloaded private key file. For example,`./oci/oci_api_key.pem`
- `--namespace <namespace>`specifies the namespace containing the OCI native ingress controller

For example:
```

```

Before you deploy the OCI native ingress controller you will:
- Grant permissions to the user via the group to which the user belongs. See[Granting Permissions to the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-permissions).
- Indicate you want to use user principals with the OCI native ingress controller by specifying the following in the values.yaml file:

```

```

where`<secret-name>`is the name of the Kubernetes secret you created previously. For example:
```

```

See[Cloning the OCI Native Ingress Controller Repository and Setting Parameters in values.yaml](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-clone).

### Using workload identity principals to enable access to OCI services and resources

You can set up a workload identity principal to enable the OCI native ingress controller to perform actions on OCI service resources. Note that you can only use workload identity principals with enhanced clusters.

To set up a workload identity principal:
- Obtain the OCID of the cluster (for example, using the Cluster details tab in the Console).

Before you deploy the OCI native ingress controller, you will:
- Grant permissions to the OCI native ingress controller workload identity. See[Granting Permissions to the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-permissions).
- Indicate you want to use workload identity principals with the OCI native ingress controller by specifying the following in the values.yaml file:

```

```

See[Cloning the OCI Native Ingress Controller Repository and Setting Parameters in values.yaml](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-clone).
- 

Set the`OCI_RESOURCE_PRINCIPAL_VERSION`and`OCI_RESOURCE_PRINCIPAL_REGION`environment variables in the deployment.yaml file.

See[Cloning the OCI Native Ingress Controller Repository and Setting Parameters in values.yaml](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-clone).

## Granting Permissions to the OCI Native Ingress Controller as a Standalone Program

The OCI native ingress controller requires permissions to access resources created by other Oracle Cloud Infrastructure services (such as the Load Balancer service and the Certificates service). The permissions you grant are the same, regardless of whether you install the OCI native ingress controller as a standalone program or as a cluster add-on. And the permissions are the same, regardless of whether you have set up an instance principal, a user principal, or a workload identity principal for the OCI native ingress controller. However, the way in which you grant those permissions does depend on the type of principal you have set up:
- When using instance principals, the OCI native ingress controller inherits the permissions granted to the instance on which it is running via a dynamic group to which the instance belongs. For information about creating the dynamic group for instance principals, see[Using instance principals to enable access to OCI services and resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengsettingupnativeingresscontroller-addon-prereqs.htm#contengsettingupnativeingresscontroller-addon-auth__section_instanceprincipalauthenticaton).
- When using user principals, the OCI native ingress controller inherits the permissions granted to a user via a group to which the user belongs. For information about creating the user and the group for user principals, see[Using user principals to enable access to OCI services and resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengsettingupnativeingresscontroller-addon-prereqs.htm#contengsettingupnativeingresscontroller-addon-auth__section_userprincipalauthenticaton).
- When using workload identity principals, the OCI native ingress controller inherits the permissions granted to a workload running on a specified cluster, in the Kubernetes service account and namespace created for the OCI native ingress controller during installation. For more information, see[Using workload identity principals to enable access to OCI services and resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengsettingupnativeingresscontroller-addon-prereqs.htm#contengsettingupnativeingresscontroller-addon-auth__section_workloadidentityauthenticaton).

To set up permissions for the OCI native ingress controller, create a policy for the group (in the case of user principals), for the dynamic group (in the case of instance principals), or for the workload (in the case of workload identity principals), with policy statements to access OCI services and resources:
- Follow the instructions in[To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy)in the IAM documentation, and give the new policy a name (for example,`acme-oke-native-ingress-controller-policy`).
- 

If you are using instance principals or user principals, enter policy statements to allow access to the OCI services and resources used by the OCI native ingress controller, in the format:

```

```

where:
- `<group|dynamic-group>`is either`group`(in the case of user principals) or`dynamic-group`(in the case of instance principals)
- `<subject-name>`is either the name of the group (in the case of user principals) or the name of the dynamic group (in the case of instance principals). For example,`acme-oke-nat-ing-cont-dyn-grp`. Note that if a group or dynamic group is not in the default identity domain, prefix the group or dynamic group name with the identity domain name, in the format`<group|dynamic-group> '<identity-domain-name>'/'<group-name|dynamic-group-name>'`. You can also specify a group or dynamic group using its OCID, in the format`group id <group-ocid>`or`dynamic-group id <dynamic-group-ocid>`.
- `<verb> <resource>`is one of the following (all of these are required, in separate policy statements):
- `manage load-balancers`
- `use virtual-network-family`
- `manage cabundles`
- `manage cabundle-associations`
- `manage leaf-certificates`
- `read leaf-certificate-bundles`
- `manage leaf-certificate-versions`
- `manage certificate-associations`
- `read certificate-authorities`
- `manage certificate-authority-associations`
- `read certificate-authority-bundles`
- `read public-ips`
- `manage floating-ips`
- `manage waf-family`
- `read cluster-family`
- `use tag-namespaces`(only required if you want the OCI native ingress controller to apply defined tags to load balancers, see[Applying defined tags to the load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_addingtags__native-ingress-controller-lb-defined-tags))
- `<location>`is one of:
- `tenancy`, if you want the OCI native ingress controller to have access to resources in the entire tenancy.
- `compartment <compartment-name>`if you only want the OCI native ingress controller to have access to resources in the compartment with the name you specify as`compartment <compartment-name>`.

For example:
```

```

The syntax for the complete list of policy statements is as follows:

```

```

Example of the complete list of policy statements:
```

```

- If you are using workload identity principals, enter policy statements to allow access to the OCI services and resources used by the OCI native ingress controller, in the format:
```

```

where:
- `<verb> <resource>`is one of the following (all of these are required, in separate policy statements):
- `manage load-balancers`
- `use virtual-network-family`
- `manage cabundles`
- `manage cabundle-associations`
- `manage leaf-certificates`
- `read leaf-certificate-bundles`
- `manage leaf-certificate-versions`
- `manage certificate-associations`
- `read certificate-authorities`
- `manage certificate-authority-associations`
- `read certificate-authority-bundles`
- `read public-ips`
- `manage floating-ips`
- `manage waf-family`
- `read cluster-family`
- `use tag-namespaces`(only required if you want the OCI native ingress controller to apply defined tags to load balancers, see[Applying defined tags to the load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_addingtags__native-ingress-controller-lb-defined-tags))
- `<location>`is one of:
- `tenancy`, if you want the OCI native ingress controller to have access to resources in the entire tenancy.
- `compartment <compartment-name>`if you only want the OCI native ingress controller to have access to resources in the compartment with the name you specify as`compartment <compartment-name>`.
- `request.principal.namespace = 'native-ingress-controller-system'`is the name of the namespace created for the OCI native ingress controller during installation.
- `request.principal.service_account = 'oci-native-ingress-controller'`is the name of the service account created for the OCI native ingress controller during installation.
- `<cluster-ocid>`is the cluster's OCID that you obtained previously.

For example:
```

```

The syntax for the complete list of policy statements is:

```

```

## Installing cert-manager

The OCI native ingress controller, whether installed as a standalone program or as a cluster add-on, uses webhooks to inject pod readiness gates into pod specifications. To ensure security, the webhook server has to run in HTTPS mode, which requires a pair of certificates and keys. The OCI native ingress controller uses Certificate Manager (also known as cert-manager) to generate and manage the certificates and keys for the webhook server, so you have to install cert-manager on the cluster to use pod readiness gates.

Regardless of whether you install the OCI native ingress controller as a standalone program or as a cluster add-on, you can install and run cert-manager in two ways:
- 

You can install and run cert-manager as an open-source product, by entering:

```

```

- 

You can install and run cert-manager as a cluster add-on. For more information about installing cert-manager as a cluster add-on, see[Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/install-add-on.htm).

For more information about cert-manager, see the[cert-manager.io documentation](https://cert-manager.io/docs/).

## Installing the Helm CLI to Install the OCI Native Ingress Controller as a Standalone Program

Helm is a package manager for Kubernetes. Helm is commonly used for creating, packaging, configuring, and deploying Kubernetes applications by combining configuration files into a single reusable package called a Helm chart. Charts are packaged and distributed in an archive format known as a chart archive. A chart contains the necessary information to install a set of Kubernetes resources on a Kubernetes cluster. A chart includes:
- a chart.yaml file, describing the application,
- a values.yaml file, providing default values for application parameters
- templates of files used by the application
- other dependencies

Helm also has a command line client, the Helm CLI (sometimes referred to as helm, all lowercase)

To install the OCI native ingress controller as a standalone program, the OCI native ingress controller is made available as a Helm chart. Before you can install the OCI native ingress controller chart, you have to first install the Helm CLI.

To install the Helm CLI, follow the instructions in the[Helm installation documentation](https://helm.sh/docs/intro/install/)to download and extract the appropriate tar.gz or zip archive file.

## Cloning the OCI Native Ingress Controller Repository and Setting Parameters in values.yaml

To clone the OCI native ingress controller and set parameters in values.yaml in readiness for installing the OCI native ingress controller as a standalone program:
- Clone the OCI native ingress controller repository from GitHub by entering:

```

```

- In the local Git repository, navigate to the`oci-native-ingress-controller`directory and open the`values.yaml`file in a text editor.
- In the`values.yaml`file, set the`compartment_id`parameter to the OCID of the compartment in which the OCI native ingress controller is to create the OCI load balancer and certificate. For example:
```

```

- In the`values.yaml`file, set the`subnet_id`parameter to the OCID of the load balancer's subnet. For example:
```

```

- In the`values.yaml`file, set the`cluster_id`parameter to the OCID of the cluster. For example:
```

```

- In the`values.yaml`file, specify how the OCI native ingress controller is to access OCI services and resources as follows:
- To specify that you want the OCI native ingress controller to access OCI services and resources using an instance principal, set the`authType`parameter as follows:

```

```

See[Using instance principals to enable access to OCI services and resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-auth__section_instanceprincipalauthenticaton).
- To specify that you want the OCI native ingress controller to access OCI services and resources using a user principal, set the`authType`and`authSecretName`parameters as follows:

```

```

where`<secret-name>`is the name of the Kubernetes secret you created previously. For example:
```

```

See[Using user principals to enable access to OCI services and resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-auth__section_userprincipalauthenticaton).
- To specify that you want the OCI native ingress controller to access OCI services and resources using a workload identity principal, set the`authType`parameters as follows:

```

```

See[Using workload identity principals to enable access to OCI services and resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-auth__section_workloadidentityauthenticaton).
- (optional) If you want to run multiple instances of the OCI native ingress controller for availability reasons, change the value of`replicaCount`in the`values.yaml`file. For example:
```

```
By default,`replicaCount`is set to`1`, meaning one instance of the OCI native ingress controller runs as a single pod. To ensure availability, you might want to increase`replicaCount`(typically to`2`or`3`) to run multiple OCI native ingress controller instances as different pods. One pod is nominated as the leader and acts as the OCI native ingress controller, while the remaining pods wait in a passive state. If the leader subsequently becomes unavailable, one of the other pods is nominated as the leader and acts as the OCI native ingress controller.
- Save the changes you have made in the`values.yaml`file and close the file.
- If you want the OCI native ingress controller to access OCI services and resources using a workload identity principal, you have to set additional environment variables as follows:
- In the local Git repository, navigate to the`oci-native-ingress-controller/templates`directory and open the`deployment.yaml`file in a text editor.
- In the`deployment.yaml`file, set the following environment variables as shown:

```

```

- Save the changes you have made in the`deployment.yaml`
