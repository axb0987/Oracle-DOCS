# Authorizing Pods to Access Non-OCI Resources Using OpenID Connect (OIDC) Discovery
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengOpenIDConnect-Discovery.htm
- Fetched: 2026-09-05 01:54 CDT

# Authorizing Pods to Access Non-OCI Resources Using OpenID Connect (OIDC) Discovery

Find out about using OpenID Connect (OIDC) Discovery to authenticate application pods running on clusters you create with Container Engine for Kubernetes (OKE), so that the pods can call service APIs on external cloud providers.

You might want application pods running on a Kubernetes cluster you've created with Kubernetes Engine to communicate with cloud service APIs hosted on external cloud providers (such as GCP, AWS, and Azure). To ensure the security of the resources hosted by an external cloud provider, the application running on the cluster must authenticate and manage identity. However, managing credentials directly can be a cumbersome process for applications, and key rotation is a manual process with considerable overhead.

OpenID Connect (OIDC) is an industry standard to make such integrations more straightforward. OpenID Connect is an identity layer built on top of OAuth 2.0. OpenID Connect supports a discovery protocol (often referred to as "OIDC Discovery") that uses an OpenID Provider Configuration document (known as the "discovery document") to authenticate applications.

Kubernetes Engine provides support for OIDC Discovery, enabling you to build applications that interact with other cloud services without the need to hard code and manually rotate API authentication keys. You can optionally enable OIDC Discovery when you create or update an enhanced cluster with Kubernetes Engine.

At a high level, when you enable OIDC Discovery for a cluster, the application's service account token is authenticated and (if valid) exchanged for an access token. The access token is then used to authenticate the application with the API on the external cloud provider.

For more information, see[Service account issuer discovery](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-issuer-discovery)in the Kubernetes documentation.

## OIDC Discovery in more detail

Kubernetes gives a service account to every application pod running on a cluster, and creates a service account token for each service account. Kubernetes manages the lifecycle of service account tokens. The service account token is a bearer token that the application attaches to API requests, and is structured as a JSON Web Token (JWT).

When you enable OIDC Discovery for a cluster, Kubernetes Engine exposes an OIDC Issuer, and adds the URL of the OIDC Issuer (including the cluster's`OpenIDConnectDiscoveryKey`) to the service account token as the value of the`iss`claim.

The location of an OIDC discovery document is relative to the OIDC Issuer's URL, and is a publicly accessible and unauthenticated well-known endpoint (known as the "OIDC discovery endpoint"). Note that you can derive a cluster's OIDC discovery endpoint before OIDC Discovery is enabled for the cluster (see[Notes on OIDC Discovery](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengOpenIDConnect-Discovery.htm#contengOpenIDConnect-Discovery__section-oidc-discovery-notes)).

The OIDC discovery document includes the publicly accessible and unauthenticated location of a JSON Web Key Set (JWKS) that contains the public keys to verify the service account token. The external cloud provider's identity provider uses the OIDC discovery document to locate the JWKS, and uses the JWKS to verify the service account token.

For additional security, the cloud service API called by an application pod might require a particular audience to be present in the service account token that Kubernetes creates. If the cloud service API does require a particular audience, you can specify that audience by setting the`audience`property of a projected volume in the pod manifest. The audience you specify is included as the value of the`aud`claim in the service account token, and can then be verified by the external cloud provider. You can also specify a validity period for the service account token by setting the value of the`expirationSeconds`property of the projected volume in the pod manifest. For more information see[ServiceAccount token volume projection](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#serviceaccount-token-volume-projection)in the Kubernetes documentation.

If the external cloud provider's identity provider successfully verifies the service account token using the JWKS, the identity provider exchanges the service account token for an access token. The access token is then used to authenticate the application, and authorize the application to use the API on the external cloud provider.

## OIDC Discovery token exchange process
When you enable OIDC Discovery for a cluster so that an application pod can make a request to an external API, Kubernetes Engine exposes:
- An OIDC Issuer. The OIDC issuer is exposed over HTTPS with a publicly trusted TLS/SSL certificate.
- An OIDC discovery document (in JSON format) that includes the location of the JWKS. The discovery document is stored in a publicly accessible and unauthenticated bucket in the Object Storage service (the OIDC discovery endpoint). See[Discovery Document Example](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengOpenIDConnect-Discovery.htm#contengOpenIDConnect-Discovery_topic-Defining-a-pod-for-OIDC-Discovery__discovery-document-example).
- A JSON Web Key Set (JWKS), containing the public keys used to verify the service account token. The JWKS is stored in a publicly accessible and unauthenticated bucket in the Object Storage service. See[JWKS Example](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengOpenIDConnect-Discovery.htm#contengOpenIDConnect-Discovery_topic-Defining-a-pod-for-OIDC-Discovery__jwks-example).

When defining an application pod that sends requests to an external API, if the external cloud provider's identity provider expects a specific audience in the service account token, specify a projected`serviceAccountToken`in the pod manifest and set its`audience`property accordingly. See[Pod Manifest Example](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengOpenIDConnect-Discovery.htm#contengOpenIDConnect-Discovery_topic-Defining-a-pod-for-OIDC-Discovery__pod-manifest-example).

The following is an overview of the token exchange process:
- 

When you create the application pod on the cluster, Kubernetes gives the pod a service account token. The service account token includes the URL of the Kubernetes Engine OIDC Issuer as the value of the`iss`claim in the JWT. If you specified an audience in the pod manifest, the audience is included in the JWT as the value of the`aud`claim. See[Service Account Token Example](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengOpenIDConnect-Discovery.htm#contengOpenIDConnect-Discovery_topic-Defining-a-pod-for-OIDC-Discovery__service-account-token-example).
- The application pod makes a request to an API on an external cloud provider and presents the encoded service account token to the external cloud provider in the Authorization header of the API request.
- The external cloud provider's identity provider decodes the service account token, extracts the URL of the Kubernetes Engine OIDC Issuer from the`iss`claim, appends`/.well-known/openid-configuration`to the URL as the location of the OIDC discovery document (the OIDC discovery endpoint). The identity provider sends a request to that URL to obtain the discovery document.
- The Kubernetes Engine OIDC Issuer returns the OIDC discovery document, which contains the URL of the location of the JWKS in the`jwks_uri`field. See[Discovery Document Example](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengOpenIDConnect-Discovery.htm#contengOpenIDConnect-Discovery_topic-Defining-a-pod-for-OIDC-Discovery__discovery-document-example).
- The external cloud provider's identity provider extracts the URL from the OIDC discovery document and sends a request to that URL to get the JWKS. See[JWKS Example](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengOpenIDConnect-Discovery.htm#contengOpenIDConnect-Discovery_topic-Defining-a-pod-for-OIDC-Discovery__jwks-example).
- The external cloud provider's identity provider uses the JWKS to validate the service account token originally presented by the application pod.
- Assuming the service account token is valid, the external cloud provider's identity provider returns an access token to the application pod.
- The application pod presents the access token to the API on the external cloud provider to prove its identity, and successfully makes API requests.

The token exchange process is shown in the following diagram:

[

## Notes on OIDC Discovery

Note the following points when using OIDC Discovery:
- OIDC Discovery is supported on clusters running Kubernetes version 1.21 or later.
- OIDC Discovery is only supported on VCN-native clusters (clusters with Kubernetes API endpoints in a subnet in your own VCN). See[Migrating to VCN-Native Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm).
- OIDC Discovery is supported on managed nodes, virtual nodes, and self-managed nodes.
- OIDC Discovery is supported on enhanced clusters (but not on basic clusters).
- 

If you want to configure external systems to use a cluster's OIDC discovery endpoint before you have enabled the cluster for OIDC Discovery, send a request to the cluster's[GetCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/GetCluster)endpoint to obtain the cluster's`OpenIDConnectDiscoveryKey`value. You can then construct the cluster's future OIDC discovery endpoint as follows:
```

```

where`<discoveryUUID>`is the cluster's`OpenIDConnectDiscoveryKey`value. Every cluster is assigned a unique`OpenIDConnectDiscoveryKey`value, regardless of whether OIDC Discovery is enabled for that cluster. Note that the above endpoint assumes the cluster is in the OC1 realm, and therefore specifies the namespace as`id9y6mi8tcky`. If the cluster is in a different realm, specify the`okecustprod`namespace instead of the`id9y6mi8tcky`namespace.

## Example Pod Manifest, Service Account Token, Discovery Document, and JWKS for OIDC Discovery

### Pod Manifest Example

An example manifest for an application pod calling a cloud service API. In this example the external cloud provider's identity provider expects the service account token to specify an audience named`vault`:
```

```

### Service Account Token Example

An example service account token that Kubernetes might create for the pod in[Pod Manifest Example](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengOpenIDConnect-Discovery.htm#contengOpenIDConnect-Discovery_topic-Defining-a-pod-for-OIDC-Discovery__pod-manifest-example):
```

```

In the above example,`{discoveryUUID}`is the cluster's`OpenIDConnectDiscoveryKey`.

### Discovery Document Example

An example discovery document that Kubernetes Engine might issue, including the location of the JWKS specified by the`jwks_uri`field:
```

```

### JWKS Example

An example JWKS to authenticate the service account token:
```

```

## Enabling a Cluster for OIDC Discovery

To enable application pods running on a cluster you create with Kubernetes Engine to authenticate using OIDC Discovery when accessing APIs hosted on an external cloud provider, you must set the cluster's Enable OIDC Discovery property.

### Using the Console to Enable a Cluster for OIDC Discovery

#### Creating a new cluster enabled for OIDC Discovery

To create a cluster and enable application pods running on the cluster to authenticate using OIDC Discovery when accessing APIs hosted on an external cloud provider:
- Follow the instructions to create a cluster using the 'Custom Create' workflow. See[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm).
- 

On the Create cluster page, either accept the default configuration details for the new cluster, or specify alternatives as follows:
- Name: The name of the new cluster. Either accept the default name or enter a name of your choice. Avoid entering confidential information.
- Compartment: The compartment in which to create the new cluster.
- 

Kubernetes version: The version of Kubernetes to run on the cluster's control plane nodes. Either accept the default version or select a version of your choice. Amongst other things, the Kubernetes version you select determines the default set of admission controllers that are turned on in the created cluster (see[Supported Admission Controllers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Reference/contengadmissioncontrollers.htm)).

Available Kubernetes version numbers are shown in`x.y`format, where`x`is a major version, and`y`is a minor version. Having selected a Kubernetes version in`x.y`format, you can optionally select Show patch versions and specify a supported patch version for the major.minor version you selected. However, we recommend you simply select a Kubernetes version in`x.y`format, to enable Kubernetes Engine to automatically select the most recent supported patch version for the minor version. For more information, see[Kubernetes Versions and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengupgradeoverview.htm).

Note the list of Kubernetes versions includes preview versions provided for early access testing and validation purposes only. These preview versions have ".0" as the patch version number (for example, 1.34.0). Preview versions are not intended for production workloads, and might contain issues without known workarounds. We do not recommend using preview versions for production workloads.
- 

Select Advanced options and in the OpenID Connect (OIDC) discovery panel, select the Enable OIDC discovery option.
- Enter other configuration details for the new cluster as described in[Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm).
- 

Select Create cluster to create the new cluster now.

#### Editing an existing cluster to enable OIDC Discovery

To update an existing cluster to enable application pods running on the cluster to authenticate using OIDC Discovery when accessing APIs hosted on an external cloud provider:
- Follow the instructions to update an existing cluster using the Console. See[Updating a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-cluster.htm).
- 

On the cluster details page, select Edit from the Actions menu.
- 

In the Edit cluster dialog, in the OpenID Connect (OIDC) discovery panel, select the Enable OIDC discovery option.
- 

Select Update to save your changes.

### Using the CLI to Enable a Cluster for OIDC Discovery

For information about using the CLI, see[Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the[Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

#### Creating A Cluster and Enabling OIDC Discovery

To use the CLI to create an enhanced cluster that uses OIDC Discovery to authenticate application pods when accessing APIs hosted on an external cloud provider, include the`--open-id-connect-discovery-enabled`parameter in the`oci ce cluster create`command.

For example:

```

```

#### Editing A Cluster To Enable OIDC Discovery

To use the CLI to update an enhanced cluster to use OIDC Discovery to authenticate application pods when accessing APIs hosted on an external cloud provider, set the`isOpenIdConnectDiscoveryEnabled`attribute to true:
- In a suitable editor, create a JSON file with a name of your choice (these instructions assume the file is called`cluster-enable-oidc.json`) containing the following:
```

```

- Save and close the`cluster-enable-oidc.json`file.
- 

Update the cluster by entering:
```

```

where:
- `--cluster-id <cluster-ocid>`is the OCID of the cluster in which you want to enable OIDC Discovery.
- `--from-json file://<path-to-file>`specifies the location of the file to use when updating the cluster.

For example:
```

```

### Using the API to Enable a Cluster for OIDC Discovery

Run the[CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster)operation to create a cluster, or the[UpdateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster)operation to edit a cluster, and specify`true`as the value of the`isOpenIdConnectDiscoveryEnabled`
