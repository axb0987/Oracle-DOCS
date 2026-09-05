# Forwarding Client Certificates for a Load Balancer Rule Set
- Source: https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/client-certificate-forwarding.htm
- Fetched: 2026-09-05 01:40 CDT

# Forwarding Client Certificates for a Load Balancer Rule Set

Learn how to forward a client certificate to the backend servers when they create a request to the load balancer and provide the certificate.

You must enable the Verify peer certificate option on the load balancer's listener to make forwarding a client certificate functional. Enable this option when you first create a listener, or when editing your existing listener. For more information on the Verify peer certificate option, see[Creating a Listener](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners_topic-Creating_Listeners.htm).

To forward your client certificate:

- Create a rule set as described in[Creating a Load Balancer Rule Set](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managingrulesets_topic-Creating_Rule_Sets.htm).
- In the Create rule set panel, select Specify Request Header Rules .
- In the Request Header Rules section, complete the following:

- Action : Select Add Request Header .
- Header : Provide a name for the header.
- Value : Enter the header value according to one of the use cases listed in the following table:

Supported Header Rule Types
Header Value Description
{oci_lb_client_cert} Forwarding the client certificate in the PEM format for an established SSL connection, with each line except the first pre-pended with the`tab`character.
{oci_lb_client_cert_apache_compatible} Forwarding the client certificate in the PEM format and removing the`\n`from the certificates for an established SSL connection.
{oci_lb_client_cert_url_encoded} Forwarding the client certificate in the PEM format (url encoded) for an established SSL connection.
- Attach the rule set to the corresponding HTTP listener either when creating a new listener, or editing an existing one, as described in[Listeners for Load Balancers](https://docs.oracle.com/en-us/iaas/Content/Balance/Tasks/managinglisteners.htm).
- Under the Rule Set section of Create listener or Edit listener panel, select the rule set you created earlier.
-
