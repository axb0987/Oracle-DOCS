# Client Parameters
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_configure_client_component_parameters.htm
- Fetched: 2026-09-05 02:34 CDT

# Client Parameters

Learn about Dedicated KMS client parameters.

Use the information in the table that follows to set the client parameters in Linux or Windows:

SSL Parameter Description
`certificate`Absolute or relative file path to the user certificate signed by the Partition Owner using the PO key and`partitionOwnerCert.pem`(cert-c).
`pkey`Absolute or relative file path to the private key file used in SSL connections to the HSM server (pkey-c).
`CApath`Absolute or relative file path to the CA certs that are used by the`oci hsm`client to verify the HSM partition SSL connection. These certificates are bundled in the client RPM package.
`owner_cert_path`Absolute or relative file path of the`partitionOwnerCert.pem`.
Note  
  

Windows Users: See[Setting up the HSM Cluster Client in Windows](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dkms_installation_user_sll_config_win.htm)for instructions on generating and signing a private key (`pkey-c`) and a CSR (`pkeycsr.csr`). Use the`data`directory of the Windows client installation for the`pkey-c`operations. By default, the directory is at`C:\Program Files\Oracle\DedicatedKms\data`.

Use the information in the table that follows to set the HSM client parameters:

Client Parameter Description
`daemon_id`Provides identification (ID) to the clients, if you're running many clients on the same host.
`reconnect_attempts`

Number of reconnection attempts made by the client after connectivity is lost between client and server.

Using the value "-1" makes the server retry connection an infinite number of times.

Supported values:`-1`to`3`
`reconnect_interval`Time interval (in seconds) taken by the client to reconnect with the disconnected server.

Supported values:`1`to`10`
`reconnect_interval_count`

Optional. Number of times the client attempts to execute a command . Default value is`3`.

Supported values:`0`to`3`
`command_retry_attempt_time`

Optional. Duration of attempts for the client to run a command. Default value is`3`.

Supported values:`0`to`10`

Use the information in the table that follows to set the OCI HSM mutual authentication parameters:

Mutual Authentication Parameter Description
`e2e_mutual_auth_cert_path`Path to the certificate used to establish an end-to-end connection.
`e2e_mutual_auth_cert_pkey`

Path to the private key used to establish an end-to-end connection.

Use the information in the table that follows to set the OCI HSM server parameters:

Server Parameter Description
`hostname`DNS of the HSM Cluster.
`port`Port of the HSM Cluster.

Use the information in the table that follows to set the OCI HSM logging parameters:

Logging Parameter Description
`log_level`Defines the log severity in the log file. Logs become more detailed as the level setting goes from ERROR to INFO to DEBUG.
`logfiles_location`
