# Provisioning OCI Load Balancers for Kubernetes Services of Type LoadBalancer
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm
- Fetched: 2026-09-05 01:54 CDT

# Provisioning OCI Load Balancers for Kubernetes Services of Type LoadBalancer

Find out how to provision an OCI load balancer for a Kubernetes service of type LoadBalancer using Kubernetes Engine (OKE).

An Oracle Cloud Infrastructure (OCI) load balancer is an OSI layer 4 (TCP) and layer 7 (HTTP) proxy, which supports features such as SSL termination and advanced HTTP routing policies. It provides the utmost flexibility, with responsive scaling up and down. You choose a custom minimum bandwidth and an optional maximum bandwidth, both between 10 Mbps and 8,000 Mbps. The minimum bandwidth is always available and provides instant readiness for your workloads.

For more information about OCI load balancers, see[Overview of Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm).

Provisioning an OCI load balancer for a Kubernetes service of type LoadBalancer enables you to:
- load balance transport Layer 4 and Layer 7 (TCP and HTTP) traffic
- terminate SSL/TLS at the load balancer

Note that when Kubernetes Engine provisions an OCI load balancer for a Kubernetes service of type LoadBalancer, security rules to allow inbound and outbound traffic to and from the load balancer's subnet are created automatically by default. See[Security Rules for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#securitylistconfig__security_rules_for_load_balancers).

Use OCI load balancer metrics to monitor the health of an OCI load balancer provisioned for a Kubernetes service of type LoadBalancer (see[Load Balancer Metrics](https://docs.oracle.com/iaas/Content/Balance/Reference/loadbalancermetrics.htm)).

## Specifying the Annotation for an OCI Load Balancer

To provision an Oracle Cloud Infrastructure load balancer for a Kubernetes service of type LoadBalancer, define a service of type LoadBalancer that includes the following annotation in the metadata section of the manifest file:
```

```

Note that`lb`is the default value of the`oci.oraclecloud.com/load-balancer-type`annotation. If you do not explicitly include the annotation in the service definition, the default value of the annotation is used.

For example, consider the following configuration file,`nginx_lb.yaml`. It defines a deployment (`kind: Deployment`) for the`nginx`app, followed by a definition of a service of type of LoadBalancer (`type: LoadBalancer`) that balances http traffic on port 80 for the`nginx`app.

```

```

The first part of the configuration file defines an Nginx deployment, requesting that it be hosted on 3 pods running the`nginx:latest`image, and accept traffic to the containers on port 80.

The second part of the configuration file defines the Nginx service, which uses type LoadBalancer to balance Nginx traffic on port 80 amongst the available pods.

To create the deployment and service defined in`nginx_lb.yaml`while connected to your Kubernetes cluster, enter the command:

```

```

This command outputs the following upon successful creation of the deployment and the load balancer:
```

```

The load balancer may take a few minutes to go from a pending state to being fully operational. You can view the current state of your cluster by entering:

```

```

The output from the above command shows the current state:

```

```

The output shows that the`my-nginx`deployment is running on 3 pods (the po/my-nginx entries), that the load balancer is running (svc/my-nginx-svc) and has an external IP (192.0.2.22) that clients can use to connect to the app that's deployed on the pods.

## Terminating SSL/TLS at the Load Balancer (Frontend SSL)

When you provision an Oracle Cloud Infrastructure (OCI) load balancer for a Kubernetes service of type LoadBalancer, you can configure it to terminate SSL/TLS traffic. This configuration, often referred to as frontend SSL , ensures that encrypted traffic from the internet is decrypted at the load balancer before being forwarded to worker nodes.

Implementing SSL termination at the load balancer level offloads the intensive decryption process from application pods, simplifying certificate management and improving backend performance.

Note that you can implement full point-to-point SSL encryption between clients and application pods running on worker nodes. To do so, configure SSL termination at the load balancer (as described in this section) and also implement backend SSL between the load balancer and worker nodes (see[Implementing SSL/TLS between the Load Balancer and Worker Nodes (Backend SSL)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-SSLbetweenLBandbackend)).

### Choose a Certificate Management Method for Frontend SSL

Depending on your security requirements and how you manage your certificate lifecycle, choose one of the following methods to implement frontend SSL:
- 

Kubernetes Secrets: Best for certificates managed within the cluster or by third-party providers (such as Let's Encrypt). For detailed implementation steps, see[Terminating SSL/TLS at the Load Balancer using Kubernetes secrets](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#creatinglbhttps-K8ssecrets).
- 

OCI Certificates service: Recommended for production environments, this method leverages OCI’s native certificate management to enable features like automatic certificate rotation without requiring manifest updates. For more information, see[Terminating SSL/TLS at the Load Balancer using OCI Certificates service](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#creatinglbhttps-OCICertificates).

Note that these methods are mutually exclusive for a given service of type LoadBalancer. You must choose either a Kubernetes secret or a native OCI certificate mapping to avoid configuration conflicts.

### Configuring Cipher Suites and Protocols for Listeners

Regardless of the certificate management method you choose, you can specify the cipher suite and SSL protocols the load balancer uses for the frontend listener.

Cipher suites determine the security, compatibility, and speed of HTTPS traffic (for more information, see[Cipher Suites for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingciphersuites.htm)).

To specify the cipher suite and TLS protocol versions to use with the load balancer's frontend listener, add the following annotation in the metadata section of the manifest file:

```

```

where:
- `"CipherSuiteName":"<cipher-suite-name>"`is the name of a predefined cipher suite preconfigured by Oracle Cloud Infrastructure (see[Predefined Load Balancer Cipher Suites](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingciphersuites_topic-Predefined_Cipher_Suites.htm)), or a cipher suite you have created yourself. For example,`"CipherSuiteName":"oci-default-http2-tls-12-13-ssl-cipher-suite-v1"`
- `"Protocols":["<tls-version>"]`specifies one or more TLS versions, in a comma-delimited list. For example,`"Protocols":["TLSv1.2", "TLSv1.3"]`

For example:
```

```

If you don't include the`oci.oraclecloud.com/oci-load-balancer-listener-ssl-config`annotation but you do include the`service.beta.kubernetes.io/oci-load-balancer-tls-secret`annotation, Kubernetes Engine uses a default cipher suite.

The default cipher suite depends on the listener protocol:
- For`HTTP2`listeners, Kubernetes Engine uses`oci-default-http2-ssl-cipher-suite-v1`.
- For all other listener protocols, Kubernetes Engine uses`oci-default-ssl-cipher-suite-v1`.

### Terminating SSL/TLS at the Load Balancer using Kubernetes secrets

Kubernetes secrets provide a way to manage SSL/TLS certificates locally within the cluster. This method is standard for certificates managed manually or by third-party providers (such as Let's Encrypt). While this method offers direct control over the certificate data within Kubernetes, it requires manual updates to the secret whenever a certificate expires.

This example provides a walkthrough of the configuration and creation of a load balancer with SSL support.

Consider the following configuration file,`nginx-demo-svc-ssl.yaml`, which defines an Nginx deployment and exposes it via a load balancer that serves http on port 80, and https on port 443. This sample creates an Oracle Cloud Infrastructure load balancer, by defining a service with a type of LoadBalancer (`type: LoadBalancer`).

```

```

The load balancer's annotations are of particular importance, as described here.

The ports on which to support https traffic are defined by the value of the`service.beta.kubernetes.io/oci-load-balancer-ssl-ports`annotation. You can declare multiple SSL ports by using a comma-separated list for the annotation's value. For example, you could set the annotation's value to "443, 3000" to support SSL on ports 443 and 3000.

The cipher suite to use with the load balancer is defined by the value of the`oci.oraclecloud.com/oci-load-balancer-listener-ssl-config`annotation.

The required TLS secret,`ssl-certificate-secret`, needs to be created in Kubernetes. This example creates and uses a self-signed certificate. However, in a production environment, the most common scenario is to use a public certificate that's been signed by a certificate authority.

The following command creates a self-signed certificate,`tls.crt`, with its corresponding key,`tls.key`:

```

```

Now that you created the certificate, you need to store both it and its key as a secret in Kubernetes. The name of the secret must match the name from the`service.beta.kubernetes.io/oci-load-balancer-tls-secret`annotation of the load balancer's definition. Use the following command to create a TLS secret in Kubernetes, whose key and certificate values are set by`--key`and`--cert`, respectively.

```

```

You must create the Kubernetes secret before you can create the service, since the service references the secret in its definition. Create the service using the following command:

```

```

Watch the service and wait for a public IP address (EXTERNAL-IP) to be assigned to the Nginx service (nginx-service) by entering:

```

```

The output from the above command shows the load balancer IP to use to connect to the service.

```

```

The load balancer is now running, which means the service can now be accessed as follows:
- using http, by entering:

```

```

- using https, by entering:

```

```

The "`--insecure`" flag is used to access the service using https due to the use of self-signed certificates in this example. Do not use this flag in a production environment where the public certificate was signed by a certificate authority.

Note: When a cluster is deleted, a load balancer that's dynamically created when a service is created will not be removed. Before deleting a cluster, delete the service, which in turn will result in the removal of the load balancer. The syntax for this command is:

```

```

For example, to delete the service from the previous example, enter:

```

```

#### Updating the TLS Certificates of Existing Load Balancers using Kubernetes secrets

To update the TLS certificate of an existing load balancer:
- Obtain a new TLS certificate. In a production environment, the most common scenario is to use a public certificate that's been signed by a certificate authority.
- 

Create a new Kubernetes secret. For example, by entering:

```

```

- Modify the service definition to reference the new Kubernetes secret by changing the`service.beta.kubernetes.io/oci-load-balancer-tls-secret`annotation in the service configuration. For example:

```

```

- Update the service. For example, by entering:

```

```

### Terminating SSL/TLS at the Load Balancer using OCI Certificates service

The OCI Certificates service provides a way to manage SSL/TLS certificates natively within Oracle Cloud Infrastructure. This method is recommended for production environments as it allows the OCI load balancer to automatically consume renewed certificates, offering several enterprise-grade benefits:
- Zero-Downtime Rotation: When a certificate is renewed in OCI, the load balancer automatically picks up the new version without requiring a manifest application.
- Centralized Management: Manage all frontend certificates from a single OCI dashboard rather than across multiple Kubernetes namespaces.
- Enhanced Security: Private keys are stored securely within OCI and are never exposed as plaintext within the Kubernetes cluster.

#### Prerequisites for OCI Certificates Integration

To use this native integration, you must ensure the following are in place:
- 

IAM Policy: Grant the cluster's resource principal permission to manage certificates in the compartment:
```

```

- 

Certificate OCID: You must have the OCID of the leaf certificate that you want the load balancer to present to clients. The certificate must be in the same region as the load balancer.
- Resource State: The certificate must be created or imported into the OCI Certificates service and must be in an Active state.

#### Configuring the Certificate Mapping

Because an OCI load balancer can support multiple certificates for different listeners, you must use a`ConfigMap`to map listener ports to their respective OCI Certificates certificate resources. When you apply the`ConfigMap`, an update of the OCI load balancer is triggered immediately.
- 

Create the ConfigMap: Create a`ConfigMap`in the same namespace as the service of type LoadBalancer, and define a mapping where the key is the listener port and the value is a JSON array containing the OCID of the leaf certificate. For example:
```

```

- 

Annotate the Service: Add the`oci-load-balancer.oraclecloud.com/tls-certificate-map`annotation to the manifest of the service of type LoadBalancer, to link it to the`ConfigMap`.

Note: The`tls-certificate-map`and`oci-load-balancer-tls-secret`annotations are mutually exclusive. If both are provided, the load balancer will fail to provision with an`sslConfiguration violation`error.

#### Example Frontend SSL Manifest
```

```

## Implementing SSL/TLS between the Load Balancer and Worker Nodes (Backend SSL)

When Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, you can specify that you want to implement SSL between the load balancer and the backend servers (worker nodes) in the backend set. This configuration is known as backend SSL . To implement backend SSL, you associate an SSL certificate with the load balancer's backend set.

Note that you can implement full point-to-point SSL encryption between clients and application pods running on worker nodes. To do so, associate an SSL certificate with the load balancer's backend set (as described in this section), and also create a load balancer with SSL termination (see[Terminating SSL/TLS at the Load Balancer (Frontend SSL)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#creatinglbhttps)).

While frontend SSL termination secures the connection between the client and the load balancer, backend SSL secures the connection between the load balancer and worker nodes. This configuration ensures that traffic remains encrypted even as it travels through the internal Virtual Cloud Network (VCN), providing an additional layer of defense-in-depth.

When you implement backend SSL, the load balancer decrypts incoming traffic using a frontend certificate, performs any necessary Layer 7 inspections or routing, and then re-encrypts the traffic before sending it to the destination pods. This is a common requirement for high-security environments, where cleartext traffic is restricted at every hop.

### Certificate Management Method for Backend SSL

When you implement backend SSL, you use Kubernetes secrets to manage backend encryption using certificates stored within the cluster. This method requires manual updates to the secret and manifest when certificates expire. For implementation details, see[Implementing SSL/TLS between the Load Balancer and Worker Nodes using Kubernetes secrets](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-SSLbetweenLBandbackend-K8ssecrets).

Note that application pods must be configured to accept and terminate SSL/TLS connections on their target ports.

### Configuring Cipher Suites and Protocols for Backend Sets

You can specify the cipher suite and SSL protocols the load balancer uses for the backend set.

Cipher suites determine the security, compatibility, and speed of HTTPS traffic (for more information, see[Cipher Suites for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingciphersuites.htm)). To specify the cipher suite to use with the load balancer's backend set, add the following annotation in the metadata section of the manifest file:

```

```

where:
- `"CipherSuiteName":"<cipher-suite-name>"`is the name of a predefined cipher suite preconfigured by Oracle Cloud Infrastructure (see[Predefined Load Balancer Cipher Suites](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingciphersuites_topic-Predefined_Cipher_Suites.htm)), or a cipher suite you have created yourself. For example,`"CipherSuiteName":"oci-default-http2-tls-12-13-ssl-cipher-suite-v1"`
- `"Protocols":["<tls-version>"]`specifies one or more TLS versions, in a comma-delimited list. For example,`"Protocols":["TLSv1.2", "TLSv1.3"]`

For example:
```

```

If you don't include the`oci.oraclecloud.com/oci-load-balancer-backendset-ssl-config`annotation but you do include the`service.beta.kubernetes.io/oci-load-balancer-tls-backendset-secret`annotation, the oci-wider-compatible-ssl-cipher-suite-v1 cipher suite is used.

### Implementing SSL/TLS between the Load Balancer and Worker Nodes using Kubernetes secrets

Kubernetes secrets provide a way to manage SSL/TLS certificates locally within the cluster for backend communication. This method is used when you manage your own certificates or use a third-party certificate authority to secure the link between the load balancer and worker nodes. It ensures internal traffic is encrypted but requires manual rotation of the CA certificate stored in the secret.

To specify the certificate to associate with the backend set, add the following annotation in the metadata section of the manifest file:

```

```

where`<value>`is the name of a Kubernetes secret you've created to contain a signed certificate and the private key to the certificate. Note that you must create the Kubernetes secret before you can create the service, since the service references the secret in its definition.

The following example creates and uses a self-signed certificate, which is usually acceptable for internal communication between the load balancer and the backend set. However, if you prefer, you could use a public certificate that's been signed by a certificate authority.

For example:
- 

Generate a private key by entering:`openssl genrsa -out ca.key 2048`
- 

Generate a certificate by entering:`openssl req -x509 -new -nodes -key ca.key -subj "/CN=nginxsvc/O=nginxsvc" -days 10000 -out ca.crt`
- 

Store the certificate and the key as a secret in Kubernetes by entering:`kubectl create secret generic ca-ser-secret --from-file=tls.crt=tls.crt --from-file=tls.key=tls.key --from-file=ca.crt=ca.crt`
- Define an Nginx deployment and expose it via a load balancer that serves http on port 80, and https on port 443.
This example creates an Oracle Cloud Infrastructure load balancer, by defining a service with a type of LoadBalancer`(type: LoadBalancer`).
```

```

Communication between the load balancer and the worker nodes in the backend set is encrypted using the key and certificate stored in the`ca-ser-secret`Kubernetes secret that you created earlier.

## Specifying Alternative Load Balancer Shapes

The shape of an Oracle Cloud Infrastructure load balancer specifies its maximum total bandwidth (that is, ingress plus egress). By default, load balancers are created with a shape of 100Mbps. Other shapes are available, including 400Mbps and 8000Mbps.

To specify an alternative shape for a load balancer, add the following annotation in the metadata section of the manifest file:

```

```

where`value`is the bandwidth of the shape (for example, 100Mbps, 400Mbps, 8000Mbps).

For example:

```

```

Sufficient load balancer quota must be available in the region for the shape you specify. Enter the following kubectl command to confirm that load balancer creation did not fail due to lack of quota:

```

```

Note that Oracle recommends you implement Kubernetes services of type LoadBalancer as cost-efficient flexible load balancers rather than as fixed-shape (dynamic) load balancers (see[Specifying Flexible Load Balancer Shapes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#flexible)).

## Specifying Flexible Load Balancer Shapes

The shape of an Oracle Cloud Infrastructure load balancer specifies its maximum total bandwidth (that is, ingress plus egress). As described in[Specifying Alternative Load Balancer Shapes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#Specifyi), you can specify different load balancer shapes.

In addition, you can also specify a flexible shape for an Oracle Cloud Infrastructure load balancer, by defining a minimum and a maximum bandwidth for the load balancer.

To specify a flexible shape for a load balancer, add the following annotations in the metadata section of the manifest file:

```

```

where:
- `"<min-value>"`is the minimum bandwidth for the load balancer, in Mbps (for example, "10")
- `"<max-value>"`is the maximum bandwidth for the load balancer, in Mbps (for example, "100")

Note that you do not include a unit of measurement when specifying bandwidth values for flexible load balancer shapes (unlike for pre-defined shapes). For example, specify the minimum bandwidth as`10`rather than as`10Mbps`.

For example:

```

```

## Specifying Load Balancer Connection Timeout

When provisioning an Oracle Cloud Infrastructure load balancer for a Kubernetes service of type LoadBalancer, you can specify the maximum idle time (in seconds) allowed between two successive receive or two successive send operations between the client and backend servers.

To explicitly specify a maximum idle time, add the following annotation in the metadata section of the manifest file:

```

```

where`value`is the number of seconds.

For example:

```

```

Note that if you don't explicitly specify a maximum idle time, a default value is used. The default value depends on the type of listener:
- for TCP listeners, the default maximum idle time is 300 seconds
- for HTTP listeners, the default maximum idle time is 60 seconds
- for HTTP2 listeners, the default maximum idle time is 60 seconds

## Specifying the Maximum Number of Allowed Load Balancer Connections to Backend Servers

When provisioning an Oracle Cloud Infrastructure load balancer for a Kubernetes service of type LoadBalancer, you can specify the maximum number of simultaneous connections that the load balancer is allowed to make to backend servers (worker nodes) in the backend set.

To explicitly specify the maximum number of simultaneous connections that are allowed between the load balancer and each individual backend server in the backend set, add the following annotation in the metadata section of the manifest file:

```

```

where`<value>`is a valid value for the number of allowed connections, as follows:
- A number between`"256"`and`"65535"`(inclusive). If you specify a number outside of this range (apart from`0`), an error is returned.
- `"0"`. If you specify 0 as the maximum number of allowed connections, an infinite number of connections between the load balancer and each individual backend server in the backend set are allowed.

For example:

```

```

Note the following:
- The number you specify for the annotation is not only used as the value of the backend set's`backendMaxConnections`property, but is also inherited by each individual backend server as the value of its`maxConnections`property. As a result, the number you specify is used as the number of connections that are allowed between the load balancer and each individual backend server in the backend set, and not as the overall total number of connections that are allowed between the load balancer and the backend set.
- If you do not include the annotation in the manifest (or subsequently remove the annotation), an infinite number of connections between the load balancer and each backend server are allowed.
- For related information about specifying the maximum number of concurrent connections to the load balancer's listener that are allowed from the same originating IP address, see[Specifying Max Listener Connection Rules](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic_Specifying_Max_Listener_Connection_Rule_Set).

## Specifying Max Listener Connection Rules

When Kubernetes Engine provisions an Oracle Cloud Infrastructure load balancer for a Kubernetes service of type LoadBalancer, you can specify the maximum number of concurrent connections to the load balancer's listener that are allowed from the same originating IP address. You use an annotation to define a default maximum listener connections value that applies to all IP addresses. The annotation defines a maximum listener connection rule for the load balancer. If you don't set this default maximum value, there's no limit to the number of connections that an IP address can make to the listener.

For more information about maximum listener connection rules, see[Max Listener Connection Rules](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrulesets.htm#max-listener-connection-rules)in the OCI Load Balancer documentation.

To specify the maximum number of concurrent listener connections that are allowed from the same originating IP address, add the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation in the metadata section of the manifest file. Note that you specify the value of the annotation as formatted JSON, as follows:

```

```

where:
- `<rule-set-name>`is your choice of name for the rule set (between 1 and 32 characters in length). For example,`IpLimitRuleSet`.
- `<value>`is the maximum number of simultaneous listener connections that are allowed from the same originating IP address.

For example:

```

```

This configuration creates a maximum listener connection rule set named`IpLimitRuleSet`that restricts each originating IP address to a maximum of 20 concurrent connections.

To subsequently change the maximum number of concurrent connections, update the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation and re-apply the manifest.

When using the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation, keep in mind the following:
- 

When you apply a manifest containing the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation, note that Kubernetes Engine assumes management of all of the load balancer's rule sets. Kubernetes Engine not only adds the rule set specified by the annotation, but also deletes any other rule sets currently associated with the load balancer.
- 

If you later want to delete a rule set, then specify an empty JSON object as the value of the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation as follows:
```

```

When you specify an empty JSON object as the value of the annotation, Kubernetes Engine deletes all of the rule sets that are associated with the load balancer, and gives up management of the load balancer's rule sets.
- 

If you simply remove the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation from the manifest and apply the manifest, Kubernetes Engine gives up management of the load balancer's rule sets. Note that if you remove the annotation, Kubernetes Engine does not delete any of the rule sets that are associated with the load balancer.
- 

If you make direct changes to the load balancer's rule sets (which is not recommended) rather than using the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation, note the following point. If you subsequently apply a manifest that contains the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation, Kubernetes Engine adds the rule set specified by the annotation, and deletes any other rule sets associated with the load balancer. Therefore, if you want to keep direct changes you have made to the load balancer's rule sets, do not include the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation in the manifest.

## Specifying HTTP Header Rules

When Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, you can specify the maximum size of the HTTP header that is accepted by the load balancer's listeners. You specify the maximum size of the HTTP header by using an annotation to specify the size (in KB) of the buffer used to read the header. The allowed values for the buffer size are 8, 16, 32 and 64. The annotation defines an HTTP header rule for the load balancer. The HTTP header rule applies to all of the load balancer's listeners, on all ports.

For more information about HTTP header rules, see[HTTP Header Rules](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingrulesets.htm#HTTPHeaderRules)in the OCI Load Balancer documentation.

To specify the maximum size of the HTTP header accepted by the load balancer's listeners, add the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation in the metadata section of the manifest file. Note that you specify the value of the annotation as formatted JSON, as follows:

```

```

where:
- `<rule-set-name>`is your choice of name for the rule set (between 1 and 32 characters in length). For example,`header-size`.
- `<value>`is the maximum size of the HTTP header in KB, and is one of`8`,`16`,`32`, or`64`.

For example:

```

```

To subsequently change the maximum size of the HTTP header, update the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation and re-apply the manifest.

When using the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation, keep in mind the following:
- 

When you apply a manifest containing the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation, note that Kubernetes Engine assumes management of all of the load balancer's rule sets. Kubernetes Engine not only adds the rule set specified by the annotation, but also deletes any other rule sets currently associated with the load balancer.
- 

If you later want to delete a rule set, then specify an empty JSON object as the value of the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation as follows:
```

```

When you specify an empty JSON object as the value of the annotation, Kubernetes Engine deletes all of the rule sets that are associated with the load balancer, and gives up management of the load balancer's rule sets.
- 

If you simply remove the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation from the manifest and apply the manifest, Kubernetes Engine gives up management of the load balancer's rule sets. Note that if you remove the annotation, Kubernetes Engine does not delete any of the rule sets that are associated with the load balancer.
- 

If you make direct changes to the load balancer's rule sets (which is not recommended) rather than using the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation, note the following point. If you subsequently apply a manifest that contains the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation, Kubernetes Engine adds the rule set specified by the annotation, and deletes any other rule sets associated with the load balancer. Therefore, if you want to keep direct changes you have made to the load balancer's rule sets, do not include the`oci.oraclecloud.com/oci-load-balancer-rule-sets`annotation in the manifest.

## Specifying Listener Protocols

When Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, you can define the type of traffic accepted by the listener by specifying the protocol on which the listener accepts connection requests.

Note that if you don't explicitly specify a protocol, "TCP" is used as the default value.

To explicitly specify the load balancer listener protocol when Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, add the following annotation in the metadata section of the manifest file:

```

```

where`<value>`is the protocol that defines the type of traffic accepted by the listener. For example, "HTTP". Valid protocols include "HTTP", "HTTP2", "TCP", and "GRPC". HTTP2 is supported in clusters running Kubernetes version 1.32 and later. Protocol values are case-insensitive.

For example:

```

```

Note that if you specify HTTP2 as the protocol, you must configure frontend SSL/TLS using the`service.beta.kubernetes.io/oci-load-balancer-ssl-ports`and`service.beta.kubernetes.io/oci-load-balancer-tls-secret`annotations. Backend SSL/TLS is optional, unless you want to encrypt traffic between the load balancer and worker nodes.

For example:
```

```

Note that if you specify GRPC as the protocol, you must configure both of the following:
- Frontend SSL, using the`service.beta.kubernetes.io/oci-load-balancer-ssl-ports`,`oci.oraclecloud.com/oci-load-balancer-listener-ssl-config`, and`service.beta.kubernetes.io/oci-load-balancer-tls-secret`annotations. For more information, see[Terminating SSL/TLS at the Load Balancer (Frontend SSL)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#creatinglbhttps).
- Backend SSL, using the`oci.oraclecloud.com/oci-load-balancer-backendset-ssl-config`and`service.beta.kubernetes.io/oci-load-balancer-tls-backendset-secret`annotations. For more information, see[Implementing SSL/TLS between the Load Balancer and Worker Nodes (Backend SSL)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-SSLbetweenLBandbackend).

For example:

```

```

## Specifying Security List Management Options When Provisioning an OCI Load Balancer

Note  
  

You might encounter scalability and other issues if you use the Kubernetes security list management feature in complex deployments, and with tools like Terraform. For these reasons, Oracle does not recommend using the Kubernetes security list management feature in production environments.

Also note that the ability to use security lists to manage security rules will be deprecated in a future release. For this reason, Oracle recommends the use of network security groups (NSGs) and the`oci.oraclecloud.com/security-rule-management-mode`annotation (see[Specifying Security Rule Management Options for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Specifying_Load_Balancer_Security_Rule_Management_Options)).

You can use the security list management feature to configure how security list rules are managed for an Oracle Cloud Infrastructure load balancer that Kubernetes Engine provisions for a Kubernetes service of type LoadBalancer. This feature is useful if you are new to Kubernetes, or for basic deployments.

To specify how the Kubernetes security list management feature manages security lists when Kubernetes Engine provisions a load balancer for a Kubernetes service of type LoadBalancer, add the following annotation in the metadata section of the manifest file:

```

```

where`<value>`is one of:
- `"None"`: (recommended) No security list management is enabled. You have to set up a security rule that allows inbound traffic to the appropriate ports for node port ranges, the kube-proxy health port, and the health check port ranges. Additionally, you have to set up security rules to allow inbound traffic to load balancers (see[Security Rules for Load Balancers and Network Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Concepts/contengnetworkconfig.htm#securitylistconfig__security_rules_for_load_balancers)).
- `"All"`: (default) All required security list rules for load balancer services are managed.
- `"Frontend"`: Only security list rules for ingress to load balancer services are managed. You have to set up a security rule that allows inbound traffic to the appropriate ports for node port ranges, the kube-proxy health port, and the health check port ranges.

Oracle recommends that you explicitly set`service.beta.kubernetes.io/oci-load-balancer-security-list-management-mode`to`None`.

In clusters with managed nodes, if you don't explicitly specify a management mode or you specify an invalid value, all security list rules are managed (equivalent to`"All"`). Be aware that in this case, Kubernetes Engine creates a security rule that allows inbound traffic from 0.0.0.0/0 (or from the source port ranges specified in the manifest file) to listener ports. In clusters with virtual nodes, security list management is never enabled and you always have to manually configure security rules (equivalent to`"None"`).

Note that there are limits to the number of ingress and egress rules that are allowed in a security list (see[Security List Limits](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm#sec_list_limits)). If the number of ingress or egress rules exceeds the limit, and`<value>`is set to`"All"`or`"Frontend"`, creating or updating the load balancer fails.

For example:

```

```
