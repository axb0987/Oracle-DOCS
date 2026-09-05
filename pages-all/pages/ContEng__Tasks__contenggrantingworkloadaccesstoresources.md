# Granting Workloads Access to OCI Resources
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contenggrantingworkloadaccesstoresources.htm
- Fetched: 2026-09-05 01:55 CDT

# Granting Workloads Access to OCI Resources

Find out how to use the identity of a workload running on a Kubernetes cluster to grant the workload fine-grained access to other OCI resources using Kubernetes Engine (OKE).
Note  
  
You can only use workload identities to grant access to OCI resources when using enhanced clusters. See[Enhanced Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingenhancedwithbasicclusters_topic.htm#contengcomparingenhancedwithbasicclusters_topic-enhancedclusters).

In Kubernetes, a workload is an application running on a Kubernetes cluster. A workload can be one application component running inside a single pod, or several application components running inside a set of pods that work together. All the pods in the workload run in the same namespace.

To grant all the pods in a workload access to Kubernetes resources, you can specify that every pod in the workload is to use the same Kubernetes service account. You can then grant Kubernetes cluster role permissions to the service account. It is the service account that binds the pods in the workload to cluster role permissions, and grants the pods access to Kubernetes resources.

In Oracle Cloud Infrastructure, a workload running on a Kubernetes cluster is considered a resource in its own right. A workload resource is identified by the unique combination of cluster, namespace, and service account. This unique combination is referred to as the workload identity. You can use the workload identity when defining IAM policies to grant fine-grained access to other OCI resources (such as Object Storage buckets). In addition, you can use Oracle Cloud Infrastructure Audit to satisfy compliance requirements by tracking requests made by the workload identity, enabling you to monitor and report unauthorized access and suspicious activity.

To grant all the pods in a workload access to OCI resources:
- Create a namespace for a service account.
- Create a service account for the application to use.
- Define an IAM policy to grant the workload resource access to other OCI resources.
- Download and configure the appropriate OCI SDK for the language in which the application is written.
- Edit the application to specify:
- 
- that workload requests are to be authenticated using the Kubernetes Engine workload identity provider
- the OCI resources that are to be accessed
- Update the application's deployment spec to specify that every pod in the workload is to use the service account.

Note the following when using workload identities:
- You cannot currently use workload identities with dynamic groups.
- You can only use workload identities with an OCI SDK, not with the Console or the API.
- The following OCI SDKs currently support workload identities:
- Go SDK v65.32.0 (and later)
- Java SDK v2.93.0 (and later) for legacy SDK and v3.88.0 (and later) for standard SDK
- Python SDK v2.111.0 (and later)
- .NET SDK v87.3.0 (and later)
- Ruby SDK v2.19.0 (and later)
- 

To ensure efficient token reuse and reduce unnecessary token generation, create only one instance of the Kubernetes Engine workload identity provider and reuse this instance across all parts of the application that require authentication. Each instance maintains its own cached token, so creating multiple instances will result in multiple tokens being fetched and managed independently, leading to duplicate token fetches, unnecessary load on the authentication service, inefficient resource usage, and degraded system response times.
Note  
  

Note for Java SDK Users

Behavior Change: Starting with Java SDK v2.93.0 (Legacy) and v3.88.0 (Standard), service account-level token caching is enabled by default to improve resource optimization.

Key Impact: When enabled, service account-level token caching automatically overrides any custom`SessionKeySupplier`provided while building the`OkeWorkloadIdentityAuthenticationDetailsProvider`.

Action Required (Opt-Out): If you need to continue supplying a custom`SessionKeySupplier`, you must explicitly opt out of the service account-level token caching feature. For an example of how to opt out, refer to the following code:
```

```

## Example: Using the Go SDK to Grant Application Workloads Access to OCI Resources

To grant Go application workloads running on a Kubernetes cluster access to other OCI resources:
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- Obtain the OCID of the cluster (for example, using the Cluster details tab in the Console).
- 

Create a namespace for the Kubernetes service account to use by entering:

```

```

For example:

```

```

- Create a Kubernetes service account for the application to use by entering:

```

```

For example:

```

```

- Define an IAM policy to enable the workload to access the necessary OCI resources:
- Follow the instructions in[To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy)in the IAM documentation, and give the new policy a name (for example,`acme-oke-finance-workload-policy`).
- 

Enter a policy statement to enable the workload to access the necessary OCI resources, in the format:

```

```

where:
- `<namespace-name>`is the name of the namespace that you created previously.
- `<service-account-name>`is the name of the service account that you created previously.
- `<cluster-ocid>`is the cluster's OCID that you obtained previously.

For example:

```

```

- Select Create to create the new policy.
- Install the OCI SDK for Go (see[SDK for Go](https://docs.oracle.com/iaas/Content/API/SDKDocs/gosdk.htm#SDK_for_Go)).
- 

In your Go application code, add:
- the Kubernetes Engine workload identity provider (`OkeWorkloadIdentityConfigurationProvider`)
- the OCI resource to access

For example, the following code snippet uses the workload identity for authentication, creates a bucket in the Object Storage service in the Phoenix (PHX) region, and uploads a file to the bucket:
```

```

- Open the application's deployment spec in a text editor and:
- Add`serviceAccountName`and set it to the name of the service account you created earlier. For example,`serviceAccountName: financeserviceaccount`.
- Add`automountServiceAccountToken`and set it to`true`.

For example:

```

```

- Deploy the application by entering:
```

```

For example:
```

```

## Example: Using the Java SDK to Grant Application Workloads Access to OCI Resources

To grant Java application workloads running on a Kubernetes cluster access to other OCI resources:
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- Obtain the OCID of the cluster (for example, using the Cluster details tab in the Console).
- 

Create a namespace for the Kubernetes service account to use by entering:

```

```

For example:

```

```

- Create a Kubernetes service account for the application to use by entering:

```

```

For example:

```

```

- Define an IAM policy to enable the workload to access the necessary OCI resources:
- Follow the instructions in[To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy)in the IAM documentation, and give the new policy a name (for example,`acme-oke-finance-workload-policy`).
- 

Enter a policy statement to enable the workload to access the necessary OCI resources, in the format:

```

```

where:
- `<namespace-name>`is the name of the namespace that you created previously.
- `<service-account-name>`is the name of the service account that you created previously.
- `<cluster-ocid>`is the cluster's OCID that you obtained previously.

For example:

```

```

- Select Create to create the new policy.
- Install the OCI SDK for Java (see[SDK for Java](https://docs.oracle.com/iaas/Content/API/SDKDocs/javasdk.htm#SDK_for_Java)).
- In the application's pom.xml, add the`oci-java-sdk-addons-oke-workload-identity`artifact as a dependency:
```

```
Note the SDK version must be 2.93.0 (or later) for legacy SDK and 3.88.0 (or later) for standard SDK.
- In your Java application code, add:
- the Kubernetes Engine workload identity provider (`OkeWorkloadIdentityAuthenticationDetailsProvider`)
- the OCI resource to access

For example, the following code snippet uses the workload identity for authentication, creates a bucket in the Object Storage service in the Phoenix (PHX) region, and uploads a file to the bucket:

```

```

- Open the application's deployment spec in a text editor and:
- Add`serviceAccountName`and set it to the name of the service account you created earlier. For example,`serviceAccountName: financeserviceaccount`.
- Add`automountServiceAccountToken`and set it to`true`.

For example:

```

```

- Deploy the application by entering:
```

```

For example:
```

```

## Example: Using the Java SDK to Grant Application Workloads Access to OCI Resources in a Different Compartment

To grant Java application workloads running on a Kubernetes cluster in one compartment access to other OCI resources in a different compartment:
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- Obtain the OCID of the cluster (for example, using the Cluster details tab in the Console).
- As the cluster administrator, create a namespace for the Kubernetes service account to use by entering:

```

```

For example:

```

```

- 

As the cluster administrator, create a Kubernetes service account for the application to use by entering:

```

```

For example:

```

```

- 

As the tenancy administrator, define an IAM policy to allow a cluster administrator to bind workloads running on a cluster in one compartment, to other OCI resources in a different compartment:
- Follow the instructions in[To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy)in the IAM documentation, and give the new policy a name (for example,`acme-oke-finance-workload-policy`).
- 

Enter policy statements to allow a cluster administrator to bind workloads running on a cluster in one compartment, to other OCI resources in a different compartment, in the format:

```

```

where:
- `<compartment-one>`is the compartment to which the cluster belongs
- `<compartment-two>`is the compartment to which the other OCI resources belong

For example:

```

```
Note that if a group is not in the default identity domain, prefix the group name with the identity domain name, in the format`group '<identity-domain-name>'/'group-name'`. You can also specify a group using its OCID, in the format`group id <group-ocid>`.
- Select Create to create the new policy.
- 

As the cluster administrator, in the compartment to which the cluster belongs, create a workload mapping that maps workloads running on the cluster to the compartment that the other OCI resources belong to:
```

```

For example:
```

```

Note that a workload mapping applies to all workloads in the specified namespace on the cluster. Use IAM policy conditions such as`request.principal.service_account`for finer-grained access to OCI resources.
- 

As the administrator of the resource in the second compartment, define an IAM policy to enable the workload to access the OCI resources in the compartment:
- Follow the instructions in[To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy)in the IAM documentation, and give the new policy a name (for example,`acme-oke-finance-workload-policy`).
- 

Enter a policy statement to enable the workload to access the necessary OCI resources, in the format:

```

```

where:
- `<namespace-name>`is the name of the namespace that you created previously.
- `<service-account-name>`is the name of the service account that you created previously.
- `<cluster-ocid>`is the cluster's OCID that you obtained previously.

For example:

```

```

- Select Create to create the new policy.
- Install the OCI SDK for Java (see[SDK for Java](https://docs.oracle.com/iaas/Content/API/SDKDocs/javasdk.htm#SDK_for_Java)). Note the SDK version must be 2.66.0 or later (or 3.18.0 or later).
- In the application's pom.xml, add the`oci-java-sdk-addons-oke-workload-identity`artifact as a dependency:
```

```
Note the SDK version must be 2.93.0 (or later) for legacy SDK and 3.88.0 (or later) for standard SDK.
- In your Java application code, add:
- the Kubernetes Engine workload identity provider (`OkeWorkloadIdentityAuthenticationDetailsProvider`)
- the OCI resource to access

For example, the following code snippet uses the workload identity for authentication, creates a bucket in the Object Storage service in the Phoenix (PHX) region, and uploads a file to the bucket:

```

```

- Open the application's deployment spec in a text editor and:
- Add`namespace`and set it to the name of the namespace you created earlier. For example,`namespace: finance`.
- Add`serviceAccountName`and set it to the name of the service account you created earlier. For example,`serviceAccountName: financeserviceaccount`.
- Add`automountServiceAccountToken`and set it to`true`.

For example:

```

```

- Deploy the application by entering:
```

```

For example:
```

```
