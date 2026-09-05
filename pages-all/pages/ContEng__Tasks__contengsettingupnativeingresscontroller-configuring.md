# Configuring the OCI Native Ingress Controller
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm
- Fetched: 2026-09-05 01:56 CDT

# Configuring the OCI Native Ingress Controller

Find out how to configure and customize the OCI native ingress controller to load balance and route incoming traffic to service pods running on worker nodes in a Kubernetes cluster.

When you have installed the OCI native ingress controller (either as a standalone program or as a cluster add-on) and created the necessary Kubernetes ingress-related resources to use it, you can configure the OCI native ingress controller by:
- [Specifying Route Rules for the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-specifyingrouterules)
- [Customizing OCI Native Ingress Controller Behavior Using Annotations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-annotationcustomization)
- [Setting Up a Pod Readiness Gate](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-podreadinessgate)
- [Setting up TCP Listeners](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_tcplistener)
- [Setting up gRPC Listeners](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_grpclistener)
- [Adding Support for HTTPS/TLS Requests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-https_tls)
- [Aggregating HTTP/HTTPS Listener Ports](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-aggregatinghttplistenerports)
- [Preserving the Load Balancer After IngressClass Deletion](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_preservinglb)
- [Applying Tags to the Load Balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_addingtags)
- [Configuring Cookie-Based Session Persistence](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_configuringcookie-basedsessionpersistence)
- [Specifying ZPR Security Attributes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_addingzprsecurityattributes)

## Specifying Route Rules for the OCI Native Ingress Controller

To specify how the OCI load balancer created by the OCI native ingress controller (installed either as a standalone program or as a cluster add-on) routes incoming requests, you specify route rules in the`Ingress`manifest.

### Route requests based on host

You can configure the OCI native ingress controller to route an incoming request based on the domain name in the request's Host header (the host to which the request was originally sent).

To route a request to a particular backend service and port based on the host, create a route rule in the`Ingress`manifest. If the host matches the route rule, the OCI native ingress controller routes the request to the associated backend service and port.

For example, you might define the following rule to route requests originally sent to`http://foo.bar.com`to a backend service named ServiceA on port 80. All incoming traffic originally sent to`http://foo.bar.com`is routed to ServiceA on port 80.
```

```

### Route requests to different backend services based on path

You can configure the OCI native ingress controller to route incoming requests to different backend services, based on elements in the path to which the requests were originally sent.

To route a request to a particular backend service and port based on the path, create a route rule in the`Ingress`manifest. If the path matches the route rule, the OCI native ingress controller routes the request to the associated backend service and port. You can specify multiple paths in the same rule, to route requests to different backends.

For example, you might define the following rule to route requests based on the path to which the request was originally sent:
- If the path starts with /app1, the OCI native ingress controller routes the request to a backend service named ServiceA on port 80.
- If the path starts with /app2, the OCI native ingress controller routes the request to a backend service named ServiceB on port 443.

Since the rule does not specify a host, the rule applies to all incoming traffic.
```

```

### Route requests based on host and path

You can configure the OCI native ingress controller to route an incoming request based on both the domain name in the request's Host header (the host to which the request was originally sent) and elements in the path to which the original request was sent.

To route a request to a particular backend service and port based on the host and path, create a route rule in the`Ingress`manifest. If the host and path match the route rule, the OCI native ingress controller routes the request to the associated backend service and port.

For example, you might define the following rule to route requests originally sent to`http://foo.bar.com/app1`to a backend service named foo on port 80:
```

```

### Route requests to a default backend

You can configure the OCI native ingress controller to route incoming requests to a default backend. You might configure a default backend to handle requests that do not match any route rules.

For example, you might define the following`defaultBackend`to route requests that do not match other rules in the`Ingress`manifest to a backend service named ServiceC on port 8080.

Note that if you do not specify any other rules in an`Ingress`manifest, you must specify a`defaultBackend`.
```

```

## Customizing OCI Native Ingress Controller Behavior Using Annotations

You can add annotations to the`IngressClass`or the`Ingress`resource manifests to customize the behavior of the OCI native ingress controller (installed either as a standalone program or as a cluster add-on).

### Customizing general behavior using annotations

You can add annotations to the`IngressClass`or the`Ingress`resource manifests to customize general behavior of the OCI native ingress controller.

Annotation Description Add annotation to this resource manifest Example
`oci-native-ingress.oraclecloud.com/id`OCID of an existing OCI load balancer to use, rather than creating a new one.

Note that if you do specify an existing load balancer, the OCI native ingress controller manages the load balancer and updates its properties as necessary to align with values in the IngressClassParameters, IngressClass, and Ingress resource manifests.`IngressClass``oci-native-ingress.oraclecloud.com/id: ocid1.loadbalancer.oc1.iad.aaaaaaaan___u7a`
`oci-native-ingress.oraclecloud.com/defined-tags`One or more defined tags to apply to the load balancer, in JSON format.

See[Applying defined tags to the load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_addingtags__native-ingress-controller-lb-defined-tags).`IngressClass``oci-native-ingress.oraclecloud.com/defined-tags: '{"tag-namespace-1": {"key1": "value1", "key2": "value2"}, "tag-namespace-2": {"key1": "value1"}}'`
`oci-native-ingress.oraclecloud.com/freeform-tags`One or more free-form tags to apply to the load balancer, in JSON format.

See[Applying free-form tags to the load balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_addingtags__native-ingress-controller-lb-freeform-tags).`IngressClass``oci-native-ingress.oraclecloud.com/freeform-tags: '{"key1": "value1", "key2": "value2"}'`
`oci-native-ingress.oraclecloud.com/delete-protection-enabled: "true"`Whether to preserve the load balancer if the IngressClass is deleted.

If set to`true`, the load balancer is preserved. If not specified,`false`is the default and the load balancer is deleted if the IngressClass is deleted.

See[Preserving the Load Balancer After IngressClass Deletion](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_preservinglb).`IngressClass``oci-native-ingress.oraclecloud.com/delete-protection-enabled: "true"`
`oci-native-ingress.oraclecloud.com/network-security-group-ids`One or more OCIDs of network security groups (NSGs) to which to add the load balancer, in a comma-delimited list. If not specified, the load balancer is not added to any NSGs.`IngressClass``oci-native-ingress.oraclecloud.com/network-security-group-ids: 'ocid1.networksecuritygroup.oc1.iad.agx___kby, ocid1.networksecuritygroup.oc1.iad.ahr___mlo'`
`oci-native-ingress.oraclecloud.com/waf-policy-ocid`OCID of an existing web application firewall (WAF) policy. See[Web Application Firewall Policies](https://docs.oracle.com/iaas/Content/WAF/Policies/waf-policy_management.htm).`IngressClass``oci-native-ingress.oraclecloud.com/waf-policy-ocid: ocid1.webappfirewallpolicy.oc1.iad.ama___aqq`
`oci-native-ingress.oraclecloud.com/protocol`Protocol to use for listener on the load balancer.

Valid values are`HTTP2`,`GRPC`, and`TCP`.

Note that HTTP2 and GRPC listeners require TLS configuration.`Ingress``oci-native-ingress.oraclecloud.com/protocol: "GRPC"`
`oci-native-ingress.oraclecloud.com/backend-tls-enabled`Whether backend service pods can receive TLS requests.

If set to`false`, TLS requests terminate at the load balancer listener, and requests between the backend set and the backends are exchanged in plain text.`Ingress``oci-native-ingress.oraclecloud.com/backend-tls-enabled: "false"`
`oci-native-ingress.oraclecloud.com/listener-ssl-config`TLS policy for listeners that have TLS enabled. Specify`cipherSuiteName`,`protocols`, or both as a JSON object. This annotation does not enable TLS. See[Configuring TLS Policies for Listeners and Backend Sets](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-https_tls__section_configuring-tls-policies).`Ingress``oci-native-ingress.oraclecloud.com/listener-ssl-config: '{"cipherSuiteName":"oci-tls-12-13-ssl-cipher-suite-v3","protocols":["TLSv1.2","TLSv1.3"]}'`
`oci-native-ingress.oraclecloud.com/backendset-ssl-config`TLS policy for backend sets that have TLS enabled. Specify`cipherSuiteName`,`protocols`, or both as a JSON object. This annotation does not enable TLS. See[Configuring TLS Policies for Listeners and Backend Sets](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-https_tls__section_configuring-tls-policies).`Ingress``oci-native-ingress.oraclecloud.com/backendset-ssl-config: '{"cipherSuiteName":"oci-default-http2-tls-12-13-ssl-cipher-suite-v1","protocols":["TLSv1.2","TLSv1.3"]}'`
`oci-native-ingress.oraclecloud.com/http-listener-port`

Create a single listener port for all HTTP paths under this ingress, rather than creating a listener port for each service port. The routing policies are configured accordingly.`Ingress``oci-native-ingress.oraclecloud.com/http-listener-port: "100"`
`oci-native-ingress.oraclecloud.com/https-listener-port`Create a single listener port for all HTTPS paths under this ingress, rather than creating a listener port for each service port. The routing policies are configured accordingly.`Ingress``oci-native-ingress.oraclecloud.com/https-listener-port: "500"`
`oci-native-ingress.oraclecloud.com/policy`Policy to be used by the load balancer backend set for traffic distribution.`Ingress``oci-native-ingress.oraclecloud.com/policy: "ROUND_ROBIN"`
`oci-native-ingress.oraclecloud.com/reserved-private-ip-address-id`OCID of reserved private IPv4 address to assign to the load balancer (native ingress controller version 1.4.4 and later).`IngressClass``oci-native-ingress.oraclecloud.com/reserved-private-ip-address-id: <reserved-private-ip-ocid>`
`oci-native-ingress.oraclecloud.com/lb-cookie-session-persistence-config`How to configure load balancer cookie persistence.

See[Configuring load balancer cookie persistence](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_configuringcookie-basedsessionpersistence__section_configuring-load-balancer-cookie-persistence).`Ingress`
```

```

`oci-native-ingress.oraclecloud.com/session-persistence-config`How to configure application cookie persistence.

See[Configuring application cookie persistence](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_configuringcookie-basedsessionpersistence__section_configuring-application-cookie-persistence).`Ingress`
```

```

`oci-native-ingress.oraclecloud.com/security-attributes`ZPR security attributes to add to the load balancer.

See[Specifying ZPR Security Attributes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_addingzprsecurityattributes)`IngressClass`
```

```

### Customizing health check behavior using annotations

You can add annotations to the`Ingress`resource manifest to customize the health checks performed by the load balancer created by the OCI native ingress controller. For more information about load balancer health checks, see[Health Checks for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/load_balancer_health_management.htm).

Annotation Description Add annotation to this resource manifest Example
`oci-native-ingress.oraclecloud.com/healthcheck-protocol`Protocol to use for the load balancer backend set health checks.`Ingress``oci-native-ingress.oraclecloud.com/healthcheck-protocol: "HTTP"`
`oci-native-ingress.oraclecloud.com/healthcheck-port`Port to use for the load balancer backend set health checks.`Ingress``oci-native-ingress.oraclecloud.com/healthcheck-port: "80"`
`oci-native-ingress.oraclecloud.com/healthcheck-path`Path to use for the load balancer backend set health checks.`Ingress``oci-native-ingress.oraclecloud.com/healthcheck-path: "/test"`
`oci-native-ingress.oraclecloud.com/healthcheck-interval-milliseconds`Interval between the load balancer backend set health checks.`Ingress``oci-native-ingress.oraclecloud.com/healthcheck-interval-milliseconds: "1000"`
`oci-native-ingress.oraclecloud.com/healthcheck-timeout-milliseconds`Period of time after which the load balancer backend set health check is considered to have failed.`Ingress``oci-native-ingress.oraclecloud.com/healthcheck-timeout-milliseconds: "750"`
`oci-native-ingress.oraclecloud.com/healthcheck-retries`Number of retries after which the load balancer backend set health check is considered to have failed.`Ingress``oci-native-ingress.oraclecloud.com/healthcheck-retries: "5"`
`oci-native-ingress.oraclecloud.com/healthcheck-return-code`Status code the load balancer backend set must return in response to a health check to be considered healthy.`Ingress``oci-native-ingress.oraclecloud.com/healthcheck-return-code: "200"`
`oci-native-ingress.oraclecloud.com/healthcheck-response-regex`Regular expression for parsing the response body from the load balancer backend set. You can specify any regex value (such as * or / ), or an empty value.`Ingress``oci-native-ingress.oraclecloud.com/healthcheck-response-regex: "*"`
`oci-native-ingress.oraclecloud.com/healthcheck-force-plaintext`Whether to send a health check to the load balancer backend without SSL (HTTP only). If not specified,`false`is the default.`Ingress``oci-native-ingress.oraclecloud.com/healthcheck-force-plaintext: "true"`

## Setting Up a Pod Readiness Gate

Pod readiness gates are additional conditions included in a pod manifest to indicate that a pod is ready to receive traffic. Pod readiness gates enable you to implement complex custom readiness checks, and can help to achieve zero downtime during rolling deployments. For more information, see[pod readiness details in the Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate).

When using the OCI native ingress controller (either as a standalone program or as a cluster add-on) with a cluster that has VCN-native pod networking as the network type, you can specify that the OCI native ingress controller is to inject a pod readiness gate into the pod spec of every pod created in a particular namespace. Note that you cannot use the OCI native ingress controller to inject pod readiness gates into pod specs if the cluster has Flannel overlay as the network type.

Specify that the OCI native ingress controller is to inject a pod readiness gate into the pod spec of every pod created in a particular namespace by entering:

```

```

The OCI native ingress controller injects a condition into the pod spec of every pod created in the namespace. For example:
```

```

You can verify the status of pod readiness gates by entering:

```

```

Example output:
```

```

## Setting up TCP Listeners

You can use the OCI native ingress controller (either as a standalone program or as a cluster add-on) to set up load balancer listeners as TCP listeners. Each TCP listener simply forwards TCP traffic received on a particular port to the backend service specified for that port in an`Ingress`resource manifest, without performing any transport layer 7 routing.

You set the`oci-native-ingress.oraclecloud.com/protocol`annotation to specify that the OCI native ingress controller is to create a TCP listener for each unique port that is included in routing rules in an`Ingress`resource manifest.

To specify that the OCI native ingress controller is to create TCP listeners:
- Define a new ingress resource in a .yaml file. See[Create Ingress resource](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-createresources.htm#contengsettingupnativeingresscontroller-createresources__section_ingress).
- In the`metadata:`section, add an`annotations:`element and set the`oci-native-ingress.oraclecloud.com/protocol`annotation to`TCP`, in the format:

```

```

where`name: <i-name>`is your choice of name for the ingress resource.

For example:

```

```

- In the`rules:`section of the`Ingress`resource manifest, add a rule for each listener that is to receive TCP traffic:
- (recommended) Set`paths.pathType`to`ImplementationSpecific`.
- Set`paths.backend.service.name`to the name of the backend service.
- Set`paths.backend.service.port.number`to the port on which to listen for TCP traffic, and to which to forward the TCP traffic.

For example, if you want a TCP listener listening on port 8080 to forward TCP traffic to`my-first-svc:8080`, and a TCP listener listening on port 8081 to forward TCP traffic to`my-second-svc:8081`, you might set up an`Ingress`resource manifest as follows:
```

```

- 

Create the resource by entering`kubectl create -f <filename>.yaml`

## Setting up gRPC Listeners

You can use the OCI native ingress controller (either as a standalone program or as a cluster add-on) to set up OCI load balancer listeners for gRPC traffic. A gRPC listener uses HTTP/2 and requires TLS configuration on the listener.

To create a gRPC listener:
- Configure TLS on the listener in one of the following ways:
- By specifying a Kubernetes TLS secret in the`spec.tls`section of the`Ingress`manifest (see[Adding Support for HTTPS/TLS Requests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-https_tls)).
- By specifying a certificate OCID using the`oci-native-ingress.oraclecloud.com/certificate-ocid`annotation.
- Set the`oci-native-ingress.oraclecloud.com/protocol`annotation to`GRPC`.

For example, if you want a gRPC listener listening on port 443 to forward gRPC traffic to`grpc-service:443`, you might set up an`Ingress`resource manifest as follows:
```

```

- 

Create the resource by entering`kubectl create -f <filename>.yaml`

The OCI native ingress controller configures the load balancer listener with the GRPC protocol and associates the configured certificate with the listener. Backend TLS remains enabled by default. To terminate TLS at the load balancer and send plain text traffic to backend pods, set`oci-native-ingress.oraclecloud.com/backend-tls-enabled: "false"`on the`Ingress`resource.

To configure the cipher suite and supported TLS protocols for the gRPC listener or backend set, use the`oci-native-ingress.oraclecloud.com/listener-ssl-config`and`oci-native-ingress.oraclecloud.com/backendset-ssl-config`annotations. See[Configuring TLS Policies for Listeners and Backend Sets](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-https_tls__section_configuring-tls-policies).

Do not configure different listener protocols for the same listener port across`Ingress`resources that use the same`IngressClass`. If you do so, the OCI native ingress controller reports a protocol conflict.

## Adding Support for HTTPS/TLS Requests

You can use the OCI native ingress controller (either as a standalone program or as a cluster add-on) to support secure HTTPS communication. Using the OCI native ingress controller, you can set up OCI load balancer listeners and backend sets to handle traffic encrypted using TLS (formerly SSL).

When using the OCI native ingress controller to support HTTPS communication, you have two options:
- [Option 1: OCI Native Ingress Controller obtains certificate from the Certificates service using a Kubernetes secret](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-https_tls__section_certificate_using_secret): You create a Kubernetes secret and specify the name of the secret in an`Ingress`resource manifest. The OCI native ingress controller uses the Kubernetes secret to obtain a certificate and a CA bundle (Certificate Authority bundle) from the OCI Certificates service. The OCI native ingress controller associates the certificate and the CA bundle with the listener and the backend set.
- [Option 2: You obtain certificate from the Certificates service](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-https_tls__section_certificate_yourself): You manually create a certificate in the OCI Certificates service yourself. You then specify the certificate's OCID in the`Ingress`resource manifest as an annotation. The OCI native ingress controller associates the certificate with the listener and the backend set.

When handling HTTPS traffic, the OCI load balancer created by the OCI native ingress controller implements end-to-end TLS by default. The load balancer uses certificates to accept a TLS encrypted request from a client, and then uses routing rules to forward the request to the appropriate backend set. The backend set creates a new TLS connection with backends running on the cluster (using the CA bundle as the trust authority for the new connection).

Note the following:
- If you delete an`IngressClass`resource, the OCI native ingress controller deletes the load balancer it created, or deletes the existing load balancer specified by the`oci-native-ingress.oraclecloud.com/id`annotation (unless you have set`oci-native-ingress.oraclecloud.com/delete-protection-enabled: "true"`). However, note that the ingress controller does not delete resources created in the OCI Certificates service. You are responsible for deleting any such Certificates service resources. In particular, if you specified a Kubernetes secret in the`Ingress`resource manifest, note that you are responsible for deleting any Certificates service resources that the OCI native ingress controller has created for you.
- Certificates obtained from the OCI Certificates service of type Imported cannot be automatically rotated. If you want certificates rotated automatically, manually obtain a certificate in the OCI Certificates service yourself by specifying that you want the certificate to be issued by a Certificates service internal CA (the certificates are of type Issued by internal CA ). You can configure certificates of type Issued by internal CA to be automatically rotated.
- If you specify a Kubernetes secret in the`Ingress`resource manifest, the certificates the OCI native ingress controller obtains from the Certificates service are of type Imported and therefore are not rotated automatically. However, you can manually renew the certificate obtained from the Certificates service by changing the details of the current server certificate specified in the existing Kubernetes secret. When you change the server certificate details, the OCI native ingress controller updates corresponding details of the certificate obtained from the Certificates service.

Note that changing subject information in the current server certificate (Common Name, Organization Name, Subject Alternative Names) is not supported by the Certificates service. If you do want to change subject information, delete the original Kubernetes secret and create a new secret with the same name. The OCI native ingress controller obtains a new certificate of type Imported and a new CA bundle from the Certificates service and associates them with the listener and the backend set (replacing the previous certificate and CA bundle).
- A listener can only be associated with one certificate. Therefore, do not create multiple ingress resources that each have rules specifying the same backend service/port combination, but where the ingress resources use different certificates.
- By default, the OCI load balancer created by the OCI native ingress controller implements end-to-end TLS. The load balancer terminates the TLS request on the listener, and a new TLS connection is established between the backend set and backends. However, if the backends are not running an HTTPS server and you therefore want the connection between the backend set and the backends to be in plain text, set the`oci-native-ingress.oraclecloud.com/backend-tls-enabled`annotation to`"false"`. When the`oci-native-ingress.oraclecloud.com/backend-tls-enabled`annotation is set to`"false"`, the load balancer can accept encrypted traffic from a client but traffic between the load balancer and the backends is not encrypted.

### Configuring TLS Policies for Listeners and Backend Sets

You can specify the cipher suite and TLS protocols that the OCI native ingress controller configures for load balancer listeners and backend sets.

Use the following annotations in an`Ingress`resource manifest:
- 

`oci-native-ingress.oraclecloud.com/listener-ssl-config`: Specifies the TLS policy for listeners.
- 

`oci-native-ingress.oraclecloud.com/backendset-ssl-config`: Specifies the TLS policy for backend sets.

Each annotation accepts a JSON object containing one or both of the following fields:
- 

`cipherSuiteName`: The name of an OCI predefined cipher suite.
- 

`protocols`: An array containing the TLS protocol versions to enable. You can specify`TLSv1.2`,`TLSv1.3`, or both.

For example:
```

```

You can omit either`cipherSuiteName`or`protocols`. You must specify at least one field. If you specify only`cipherSuiteName`, the OCI native ingress controller uses`TLSv1.2`and`TLSv1.3`as the default protocols. If you specify only`protocols`, the controller selects a default cipher suite that is compatible with the specified protocols and with the listener or backend set.

For example, the following annotation specifies TLS 1.3 for an HTTP listener. Because`cipherSuiteName`is omitted, the OCI native ingress controller uses`oci-tls-13-ssl-cipher-suite-v3`:
```

```

If TLS is enabled and you do not specify a TLS policy annotation, the OCI native ingress controller uses the following default TLS policies when it creates TLS configuration:

TLS configuration Default cipher suite Default protocols
HTTP listener with TLS enabled`oci-tls-12-13-ssl-cipher-suite-v3``TLSv1.2`,`TLSv1.3`
HTTP/2 or gRPC listener`oci-default-http2-tls-12-13-ssl-cipher-suite-v1``TLSv1.2`,`TLSv1.3`
Backend set`oci-default-http2-tls-12-13-ssl-cipher-suite-v1``TLSv1.2`,`TLSv1.3`

If you specify only one field in a TLS policy annotation, the OCI native ingress controller applies the default value shown in the following table for the omitted field:

TLS target Specified annotation field Specified value Default value applied
HTTP listener`protocols``["TLSv1.2"]``cipherSuiteName: "oci-tls-12-ssl-cipher-suite-v3"`
HTTP listener`protocols``["TLSv1.3"]``cipherSuiteName: "oci-tls-13-ssl-cipher-suite-v3"`
HTTP listener`protocols``["TLSv1.2","TLSv1.3"]``cipherSuiteName: "oci-tls-12-13-ssl-cipher-suite-v3"`
HTTP/2 or gRPC listener`protocols``["TLSv1.2"]``cipherSuiteName: "oci-default-http2-ssl-cipher-suite-v1"`
HTTP/2 or gRPC listener`protocols``["TLSv1.3"]``cipherSuiteName: "oci-default-http2-tls-13-ssl-cipher-suite-v1"`
HTTP/2 or gRPC listener`protocols``["TLSv1.2","TLSv1.3"]``cipherSuiteName: "oci-default-http2-tls-12-13-ssl-cipher-suite-v1"`
Backend set`protocols``["TLSv1.2"]``cipherSuiteName: "oci-default-http2-ssl-cipher-suite-v1"`
Backend set`protocols``["TLSv1.3"]``cipherSuiteName: "oci-default-http2-tls-13-ssl-cipher-suite-v1"`
Backend set`protocols``["TLSv1.2","TLSv1.3"]``cipherSuiteName: "oci-default-http2-tls-12-13-ssl-cipher-suite-v1"`
HTTP, HTTP/2, or gRPC listener`cipherSuiteName`User-specified cipher suite`protocols: ["TLSv1.2","TLSv1.3"]`
Backend set`cipherSuiteName`User-specified cipher suite`protocols: ["TLSv1.2","TLSv1.3"]`
Note the following points:
- 

The TLS policy annotations do not enable TLS. Configure listener TLS by specifying a Kubernetes TLS secret in`spec.tls`, or by specifying a certificate using the`oci-native-ingress.oraclecloud.com/certificate-ocid`annotation.
- 

The`backendset-ssl-config`annotation applies only when backend TLS is enabled. Backend TLS is enabled by default for HTTPS and gRPC traffic. To disable backend TLS, set`oci-native-ingress.oraclecloud.com/backend-tls-enabled`to`"false"`.
- 

If TLS is enabled and you do not specify a TLS policy annotation when the OCI native ingress controller creates TLS configuration, the controller uses the applicable default policy.
- 

If TLS configuration already exists, the listener protocol is unchanged, and you do not specify a TLS policy annotation, the OCI native ingress controller preserves the existing cipher suite and protocols.

If you change the listener protocol and the existing policy is a default previously applied by the controller, the controller applies the default policy for the new listener protocol. The controller preserves a custom policy.
- 

If you remove a TLS policy annotation, the OCI native ingress controller preserves the currently configured cipher suite and protocols during subsequent updates.
- 

If multiple`Ingress`resources share a listener or backend set, their TLS policy annotations must not conflict. If the annotations conflict, the OCI native ingress controller does not apply the configuration and reports a warning event.
- 

The OCI native ingress controller rejects an annotation that contains malformed JSON, unknown fields, empty values, unsupported protocol versions, or an unsupported cipher suite.
- 

You cannot specify TLS 1.0 or TLS 1.1. Specify TLS 1.2, TLS 1.3, or both.
- 

To view validation or conflict errors, describe the`Ingress`resource and review its events by entering:
```

```

Look for`TLSPolicyInvalidAnnotation`or`TLSPolicyConflict`.
- 

For information about OCI predefined cipher suites and the protocols that they support, see[Cipher Suites for Load Balancers](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingciphersuites.htm).

### Option 1: OCI Native Ingress Controller obtains certificate from the Certificates service using a Kubernetes secret

To configure the OCI native ingress controller to obtain a certificate from the OCI Certificates service:
- Obtain a TLS public and private key pair, and a certificate.

In production environments, you obtain a TLS certificate from your chosen Certificate Authority by submitting a certificate signing request. During the certificate request process, a public key and corresponding private key are generated.

In development and test environments, you can create a self-signed certificate and generate a private key yourself using a tool such as OpenSSL. For example (using OpenSSL 3.0 or later):
- 

Generate a public and private key pair by entering the following commands:

```

```

```

```

- 

Generate a certificate by entering the following commands:

```

```

```

```

```

```

In this example:
- `rootCA.key`contains the key pair for the root CA.
- `rootCA.crt`contains the root CA certificate.
- `server.key`contains the key pair for generating the server certificate.
- `server.csr`contains the certificate signing request for the server certificate.
- `server.crt`contains the generated server certificate.
- Create a Kubernetes secret resource in either of the following ways:
- 

Using the`kubectl create secret generic`command, by entering:

```

```

where:
- `<k8s-secret-name>`is your choice of name for the Kubernetes secret
- `--from-file=ca.crt=<path-and-filename>.crt`specifies the path to the file containing the root CA certificate. For example,`--from-file=ca.crt=rootCA.crt`
- `--from-file=tls.crt=<path-and-filename>.crt`specifies the path to the file containing the generated server certificate. For example,`--from-file=tls.crt=server.crt`
- `--from-file=tls.key=<path-and-filename>.key`specifies the path to the file containing the generated private key. For example,`--from-file=tls.key=server.key`

For example:
```

```

- Using a`Secret`resource manifest file:
- 

Define the Kubernetes secret in a .yaml file, in the format:

```

```

where:
- `name: <k8s-secret-name>`is your choice of name for the Kubernetes secret resource.
- `ca.crt: <base64-encoded-certificate-chain>`is the contents of the file (or files) containing intermediate certificates that form a certificate chain from the leaf certificate back to the Certificate Authority. Note that you can omit`ca.cert`, provided you include the entire certificate chain as the value of`tls.cert`(in which case, start the certificate chain with the contents of the file containing the generated server certificate, followed by the remaining certificates).
- `tls.crt: <base64-encoded-server-certificate>`is the contents of the file containing the generated server certificate.
- `tls.key: <base64-encoded-private-key>`is the contents of the file containing the generated private key.

For example:
```

```

- 

Create the secret resource by entering`kubectl create -f <filename>.yaml`
- Add the Kubernetes secret to an`Ingress`resource manifest:
- Define a new ingress resource in a .yaml file. See[Create Ingress resource](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-createresources.htm#contengsettingupnativeingresscontroller-createresources__section_ingress).
- In the`spec:`section of the manifest, add a`tls:`element that specifies both the host that is to receive HTTPS traffic and the name of the Kubernetes secret, in the format:

```

```

For example:
```

```

- In the`rules:`section of the manifest, add a rule for the host that is to receive HTTPS traffic, and specify 443 as the port on which to listen for HTTPS traffic.

For example:
```

```

- 

Create the resource by entering`kubectl create -f <filename>.yaml`

When you create the ingress resource, the OCI native ingress controller uses the Kubernetes secret to obtain a certificate of type Imported , and a CA bundle (Certificate Authority bundle), from the OCI Certificates service. The OCI native ingress controller associates the certificate with the listener, and the CA bundle with the backend set.

When the listener listening on port 443 receives an HTTPS request to the specified host, the listener uses the certificate for TLS termination. The listener then uses the routing rule to forward the request to the backend set. The backend set creates a new TLS connection with the backends running on the cluster (using the CA bundle as the trust authority for the new connection).

### Option 2: You obtain certificate from the Certificates service

To configure the OCI native ingress controller to use a certificate that you have obtained from the OCI Certificates service:
- Create a certificate in the OCI Certificates service in one of the following ways:
- by importing a certificate issued by a third-party CA (the certificate will be of type Imported )
- by issuing the certificate internally from a Certificates service CA (the certificate will be of type Issued by internal CA )

Do not create a certificate to manage externally (of type Issued by internal CA, managed externally ). For more information, see[Creating a Certificate](https://docs.oracle.com/iaas/Content/certificates/creating-certificate.htm).
- Make a note of the certificate's OCID.
- Add the certificate's OCID to an`Ingress`resource manifest:
- Define a new ingress resource in a .yaml file. See[Create Ingress resource](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-createresources.htm#contengsettingupnativeingresscontroller-createresources__section_ingress).
- In the`metadata:`section, add an`annotations:`element that specifies the OCID of the certificate you created in the OCI Certificates service, in the format:

```

```

where:
- `name: <i-name>`is your choice of name for the ingress resource.
- `oci-native-ingress.oraclecloud.com/certificate-ocid: <certificate-ocid>`is the OCID of the certificate you created in the OCI Certificates service

For example:
```

```

- In the`rules:`section of the`Ingress`resource manifest, add a rule for the host that is to receive HTTPS traffic, and specify 443 as the port on which to listen for HTTPS traffic.

For example:
```

```

- 

Create the resource by entering`kubectl create -f <filename>.yaml`

What happens when you create the ingress resource depends on how you created the certificate in the OCI Certificates service:
- If you created the certificate by importing a certificate issued by a third-party CA, the certificate is of type Imported . The OCI native ingress controller associates the certificate with the listener, creates a CA bundle from the certificate chain, and associates the CA bundle with the backend set. Note that you cannot configure certificates of type Imported to be automatically rotated.
- If you created the certificate by issuing the certificate internally from a Certificates service CA, the certificate is of type Issued by internal CA . The OCI native ingress controller associates the certificate with the listener, obtains the OCID of the CA, and associates that OCID with the backend set. Note that you can configure certificates of type Issued by internal CA to be automatically rotated.

When the listener listening on port 443 receives an HTTPS request to the specified host, the listener uses the certificate for TLS termination. The listener then uses the routing rule to forward the request to the backend set. The backend set creates a new TLS connection with the backends running on the cluster (using the CA bundle, or the CA identified by its OCID, as the trust authority for the new connection).

## Aggregating HTTP/HTTPS Listener Ports

When using the OCI native ingress controller (either as a standalone program or as a cluster add-on) you can aggregate all HTTP traffic into a single listener port, and similarly you can aggregate all HTTPS traffic into a single port.

By default, the OCI native ingress controller creates an OCI load balancer listener for each backend service port defined in an`Ingress`manifest. The OCI native ingress controller also creates a routing policy for each listener port. However, you can use the`oci-native-ingress.oraclecloud.com/http-listener-port`annotation and/or the`oci-native-ingress.oraclecloud.com/https-listener-port`annotation to create a single listener and routing policy for all HTTP requests, and/or a single listener and routing policy for all HTTPS requests.

For example, you might define an ingress with rules for four backend services, each service listening on a different port, as follows:
```

```

In this example, the`Ingress`manifest defines four services:
- testecho1, listening on port 80 for HTTP traffic
- testecho2, listening on port 81 for HTTP traffic
- testecho3, listening on port 443 for HTTPS traffic
- testecho4, listening on port 444 for HTTPS traffic

By default, the OCI native ingress controller creates:
- Four listeners in the load balancer (two listeners listening on ports 80 and 81 for HTTP traffic, and two listeners listening on ports 443 and 444 for HTTPS traffic).
- Four routing policies (one for each listener port).

To simplify administration, you might decide to have a single listener listening for HTTP traffic, and a single listener listening for HTTPS traffic, by setting annotations as follows:
```

```

With the annotations set as shown, the OCI native ingress controller creates:
- a single listener listening for HTTP traffic on port 100, and a single routing policy for port 100 with paths for backends on ports testecho1:80 and testecho2:81
- a single listener listening for HTTPS traffic on port 500, and a single routing policy for port 500 with paths for backends on ports testecho3:443 and testecho4:444

Note the following:
- 

You can set the`oci-native-ingress.oraclecloud.com/http-listener-port`and`oci-native-ingress.oraclecloud.com/https-listener-port`annotations independently of each other, so you do not have to set both annotations.
- 

If the`Ingress`resource manifest includes the`oci-native-ingress.oraclecloud.com/certificate-ocid`annotation, the OCI native ingress controller considers all hosts to be configured for TLS. In this case, the OCI native ingress controller:
- ignores the`oci-native-ingress.oraclecloud.com/http-listener-port`annotation (if present in the`Ingress`resource manifest)
- applies the`oci-native-ingress.oraclecloud.com/https-listener-port`annotation (if present in the`Ingress`resource manifest) to create a single listener for all traffic
- Regardless of the`oci-native-ingress.oraclecloud.com/http-listener-port`and`oci-native-ingress.oraclecloud.com/https-listener-port`annotations, the OCI native ingress controller only creates HTTP and/or HTTPS listeners (and corresponding routing policies) if required for backend services that are defined in the Ingress resource manifest. For example:
- If you include the`oci-native-ingress.oraclecloud.com/http-listener-port`annotation in an`Ingress`resource manifest that does not define an HTTP backend, then the OCI native ingress controller does not create an HTTP listener.
- If you include the`oci-native-ingress.oraclecloud.com/https-listener-port`annotation in an`Ingress`resource manifest that does not define an HTTPS backend, then the OCI native ingress controller does not create an HTTPS listener.
- If you include both`oci-native-ingress.oraclecloud.com/http-listener-port`and`oci-native-ingress.oraclecloud.com/https-listener-port`annotations in an`Ingress`resource manifest that only defines HTTP backends, then the OCI native ingress controller ignores the`oci-native-ingress.oraclecloud.com/https-listener-port`annotation and does not create an HTTPS listener.
- If you include both`oci-native-ingress.oraclecloud.com/http-listener-port`and`oci-native-ingress.oraclecloud.com/https-listener-port`annotations in an`Ingress`resource manifest that only defines HTTPS backends, then the OCI native ingress controller ignores the`oci-native-ingress.oraclecloud.com/http-listener-port`annotation and does not create an HTTP listener.

## Preserving the Load Balancer After IngressClass Deletion

You can specify that you want the OCI native ingress controller to preserve the load balancer for an`IngressClass`resource if you delete the`IngressClass`itself.

You use the`oci-native-ingress.oraclecloud.com/delete-protection-enabled`annotation in the`IngressClass`manifest to specify whether the load balancer is deleted. Set the annotation to`true`to preserve the load balancer if you delete the`IngressClass`. Set the annotation to`false`(or do not include the annotation in the manifest) to delete the load balancer if you delete the`IngressClass`. For example:

```

```

If you delete an`IngressClass`resource and use the annotation to preserve the load balancer, the OCI native ingress controller retains the load balancer itself, but clears associations with other supporting resources (such as network security groups, tags, a web application firewall). The OCI native ingress controller also deletes the`default_ingress BackendSet`backend set that it created.

However, note that the OCI native ingress controller does not delete OCI load balancer resources (listeners, backend sets) that it created for`Ingress`resources that currently reference the deleted`IngressClass`. Therefore, before you delete an`IngressClass`resource, first delete any`Ingress`resource that references the`IngressClass`in its manifest. If you do not delete such`Ingress`resources first, the OCI resources created for them will continue to exist in the load balancer.

## Applying Tags to the Load Balancer

You can specify that you want the OCI native ingress controller to apply defined tags and free-form tags to a load balancer it creates (for an`IngressClass`resource) or manages (if specified by the`oci-native-ingress.oraclecloud.com/id`annotation). Tagging enables you to group disparate resources across compartments, and also enables you to annotate resources with your own metadata. For more information about tags, see[Tagging Kubernetes Cluster-Related Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources.htm).

### Applying defined tags to the load balancer

Defined tags are set up and managed by a tag administrator. A defined tag consists of a tag namespace, a key, and a value. The tag namespace and tag key definition must be set up in a tenancy before you can apply a defined tag to a resource.

To specify that the OCI native ingress controller is to apply defined tags to the load balancer, use the`oci-native-ingress.oraclecloud.com/defined-tags`annotation in the`IngressClass`manifest, in the following format:

```

```

where:
- `<tag-namespace>`is the tag namespace to which the tag belongs.
- `<tag-key>`is the name of a defined tag to apply to the load balancer.
- `<tag-value>`is either a value for the tag from a pre-defined list of values, or a new value, or blank (depending on how the defined tag has been set up).

The value of the`oci-native-ingress.oraclecloud.com/defined-tags`annotation is a JSON string, enabling you to specify multiple tag namespaces, tag keys, and tag values in JSON format.

For example:

```

```

Changing one of the tags in the`oci-native-ingress.oraclecloud.com/defined-tags`annotation of the`IngressClass`manifest causes the OCI native ingress controller to reapply to the load balancer all of the defined tags specified by the annotation. However, if a defined tag contains a tag variable, the OCI native ingress controller only reapplies the defined tag to the load balancer if the tag is not already present.

Note that to enable the OCI native ingress controller to apply defined tags to a load balancer, a suitable IAM policy must exist to enable the OCI native ingress controller to use the appropriate tag namespace. For more information, see:
- [Granting Permissions to the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-permissions)
- [Granting Permissions to the OCI Native Ingress Controller Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-prereqs.htm#contengsettingupnativeingresscontroller-addon-permissions)

### Applying free-form tags to the load balancer

Free-form tags are not managed by a tag administrator. A free-form tag consists of a key and a value. Unlike defined tags, free-form tags do not belong to a tag namespace.

To specify that the OCI native ingress controller is to apply free-form tags to the load balancer, use the`oci-native-ingress.oraclecloud.com/freeform-tags`annotation in the`IngressClass`manifest, in the following format:

```

```

where:
- `<tag-key>`is a name for the free-form tag to apply to the load balancer.
- `<tag-value>`is a value for the free-form tag to apply to the load balancer.

The value of the`oci-native-ingress.oraclecloud.com/freeform-tags`annotation is a JSON string, enabling you to specify multiple tag keys and tag values in JSON format.

For example:

```

```

Changing one of the tags in the`oci-native-ingress.oraclecloud.com/freeform-tags`annotation of the`IngressClass`manifest causes the OCI native ingress controller to reapply to the load balancer all of the free-form tags specified by the annotation.

### Applying tag defaults to the load balancer

Tag defaults are set up for a specific compartment. Tag defaults are compartment-specific. Tag defaults specify defined tags that are applied automatically to all resources created in a specific compartment at the time of creation.

When using the OCI native ingress controller version 1.4.0 (or later), tag defaults are automatically applied to load balancers that the OCI native ingress controller creates. Subsequently, the OCI native ingress controller retains a tag default applied to a load balancer unless one of the following conditions is met:
- You manually remove a tag default that has been automatically applied to a load balancer.
- You specify a tag default as a defined tag, using the`oci-native-ingress.oraclecloud.com/defined-tags`annotation (in which case, the OCI native ingress controller treats the tag default as any other defined tag).

Note that tag defaults with user-applied values are not supported. If a tag default with a user-applied value has been set up for a compartment in which the OCI native ingress controller is to create or manage a load balancer, you must use the`oci-native-ingress.oraclecloud.com/defined-tags`annotation to specify the tag default as a defined tag.

For load balancers created using an OCI native ingress controller version earlier than version 1.4.0, or when using the`oci-native-ingress.oraclecloud.com/id`annotation to specify that the OCI native ingress controller is to manage an existing load balancer, note that tag defaults are not supported. In both cases, to apply or retain a tag default, use the`oci-native-ingress.oraclecloud.com/defined-tags`annotation to specify the tag default as a defined tag instead.

## Configuring Cookie-Based Session Persistence

When using the OCI native ingress controller (either as a standalone program or as a cluster add-on), you can configure session persistence ("sticky sessions") to ensure that requests from the same client are consistently routed to the same backend in a backend set.

Session persistence is configured using annotations in the`Ingress`resource manifest.

OCI load balancers created by the OCI native ingress controller support two types of cookie-based session persistence:
- Application cookie persistence : The backend application sets and manages the cookie.
- Load balancer cookie persistence : The load balancer sets and manages the cookie.

For more information about OCI load balancer support for cookie-based session persistence, see[Load Balancer Session Persistence](https://docs.oracle.com/iaas/Content/Balance/Reference/sessionpersistence.htm).

You configure session persistence by adding one of two persistence annotations to the`metadata:`section of the`Ingress`resource manifest.

Note the following:
- You must configure only one persistence mode for a backend set.
- If both persistence annotations are specified, the ingress resource fails to reconcile.
- If no persistence annotation is specified, session persistence is disabled.

### Configuring application cookie persistence

To configure application cookie persistence, add the following annotation in the`metadata:`section of the`Ingress`resource manifest:
```

```

where`<json>`defines the application cookie persistence configuration.

For example:
```

```

Optional fields you can include to control cookie behavior include:
- `cookieName`to specify the name of the cookie set by the application.
- `disableFallback`to specify whether fallback behavior is disabled if the cookie is not present.

Note the following:
- If`cookieName`is omitted or empty, the default value`"*"`is used.
- In application cookie mode, session persistence only takes effect after the backend sends a matching`Set-Cookie`header.

For more information about OCI load balancer support for application cookie persistence, see[Application Cookie Stickiness](https://docs.oracle.com/iaas/Content/Balance/Reference/sessionpersistence.htm#app-cookie-stickiness).

### Configuring load balancer cookie persistence

To configure load balancer cookie persistence, add the following annotation in the`metadata:`section of the`Ingress`resource manifest:
```

```

where`<json>`defines the load balancer cookie persistence configuration.

For example:
```

```

In this example, the load balancer manages the cookie used to maintain session persistence.

Optional fields you can include to control cookie behavior include:
- `cookieName`
- `disableFallback`
- `domain`
- `path`
- `maxAgeInSeconds`
- `isSecure`
- `isHttpOnly`

If you set`"isSecure": true`, ensure the ingress resource is configured to use HTTPS/TLS listeners. Secure cookies are not accepted on HTTP-only listeners.

For more information about OCI load balancer support for load balancer cookie persistence, see[Load Balancer Cookie Stickiness](https://docs.oracle.com/iaas/Content/Balance/Reference/sessionpersistence.htm#lb-cookie-stickeiness).

### Disabling session persistence

To disable session persistence, remove the annotation from the ingress resource. For example:
```

```

or:
```

```

After the ingress resource is reconciled, session persistence is no longer applied to backend sets.

## Specifying ZPR Security Attributes

When using the OCI native ingress controller (either as a standalone program or as a cluster add-on), you can specify that you want the OCI native ingress controller to apply Zero Trust Packet Routing (ZPR) security attributes to a load balancer it creates for an`IngressClass`resource.

To specify ZPR security attributes to apply to the load balancer, use the`oci-native-ingress.oraclecloud.com/security-attributes`annotation in the`IngressClass`manifest, in the following format:
```

```

where:
- `<security-attribute-namespace>`is the security attribute namespace to which the security attribute belongs.
- `<security-attribute-key>`is the name of the security attribute to apply to the load balancer.
- `<security-attribute-value>`is the value of the security attribute to apply to the load balancer.

The value of the`oci-native-ingress.oraclecloud.com/security-attributes`annotation is a JSON string, enabling you to specify multiple security attribute namespaces, security attribute keys, and security attribute values in JSON format.

For example:
```

```

Changing one of the security attributes in the`oci-native-ingress.oraclecloud.com/security-attributes`annotation of the`IngressClass`manifest causes the OCI native ingress controller to reapply to the load balancer all of the security attributes specified by the annotation.

Note that to enable the OCI native ingress controller to apply ZPR security attributes to a load balancer, a suitable IAM policy must exist to enable the OCI native ingress controller to use the appropriate security attribute namespace. For example:

```

```

Note  
  
Assigning ZPR security attributes to a load balancer does not, by itself, allow traffic. You must also create ZPR policies that allow the required traffic. Existing network security groups and security lists continue to apply.

For more information about adding ZPR security attributes, see[Adding Security Attributes to Cluster-Related Resources and Applying ZPR Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingzpr.htm)
