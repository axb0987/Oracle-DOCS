# CLI Environment Variables
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clienvironmentvariables.htm
- Fetched: 2026-09-05 01:36 CDT

# CLI Environment Variables

The Oracle Cloud Infrastructure CLI supports the use of environment variables to specify default values for some options.

## Environment Variables

The following table lists the available environment variables and their corresponding CLI options or`~/.oci/config`entries.

Environment Variable CLI option OCI config entry Description
`OCI_CLI_PROFILE``--profile`Specified by`[DEFAULT]`The profile in the OCI config file to load. This profile will also be used to locate any default parameter values which have been specified in the OCI CLI-specific configuration file.
`OCI_CLI_USER`n/a`user`

The OCID of the user calling the API. To get the value, see[Required Keys and OCIDs](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm).

Example:`ocid1 . user . oc1 ..<unique_ID>`
`OCI_CLI_REGION``--region``region`

An Oracle Cloud Infrastructure region. See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).

Example:`us-ashburn-1`
`OCI_CLI_FINGERPRINT`n/a`fingerprint`

The fingerprint for the public key that was added to this user. To get the value, see[Required Keys and OCIDs](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm).

Example:`20:3b:97:13:55 : 1c:5b:0d:d3:37 : d8:50:4e:c5:3a :34`
`OCI_CLI_KEY_FILE`n/a`key_file`

The full path and filename of the private key.

Important: The key pair must be in PEM format. For instructions on generating a key pair in PEM format, see[Required Keys and OCIDs](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm).

If you encrypted the key with a passphrase, you must also include the`pass_phrase`entry in the config file.

Example:`~/.oci / oci_api_key.pem`
`OCI_CLI_KEY_CONTENT`n/a`n/a`The full content of the private key enclosed in single quotes. Important: The key pair must be in PEM format.

Example:`$ export OCI_CLI_KEY_CONTENT="$(</path/to/oci_api_key.pem)"`
`OCI_CLI_TENANCY`n/a`tenancy`

The OCID of your tenancy. To get the value, see[Required Keys and OCIDs](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/apisigningkey.htm).

Example:`ocid1 . tenancy . oc1 ..<unique_ID>`
`OCI_CLI_PASSPHRASE`n/a`pass_phrase`

Passphrase used for the key, if it's encrypted.
`OCI_CLI_ENDPOINT``--endpoint`

This value can be set in the OCI CLI-specific configuration file. See[Configuring the CLI](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliconfigure.htm).

The value to use as the service endpoint, including any required API version path.

Example:`https://iaas.us-phoenix-1.oracle.com/20160918`

Note: The`--region`parameter is the recommended way of targeting different regions.
`OCI_CLI_CONFIG_FILE``--config-file`n/a The path to the[OCI config file](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm).
`OCI_CLI_RC_FILE``--cli-rc-file`n/a The path to the OCI CLI-specific configuration file, containing parameter default values and other configuration information such as command aliases and predefined queries. See[Configuring the CLI](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliconfigure.htm)for more information.
`OCI_CLI_CERT_BUNDLE``--cert-bundle`n/a The full path to a CA certificate bundle to be used for SSL verification.
`OCI_CLI_AUTH``--auth`n/a

The type of auth to use for the API request. By default the API key in your config file will be used.

Accepted values are:`api_key, instance_obo_user, instance_principal, resource_principal, security_token`
`OCI_CLI_SECURITY_TOKEN_FILE`n/a`security_token_file`The location of the file used for[token-based authentication for the CLI](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clitoken.htm).
`HTTP_PROXY``--proxy`This value can be set in the OCI CLI-specific config file. See[Specifying a Proxy Server](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliconfigure.htm#cliconfigure_topic_Proxy_Server). The URL of the HTTP proxy server to use for outgoing CLI requests.
`HTTPS_PROXY``--proxy`This value can be set in the OCI CLI-specific config file. See[Specifying a Proxy Server](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliconfigure.htm#cliconfigure_topic_Proxy_Server). The URL of the HTTPS proxy server to use for outgoing CLI requests.

## Order of precedence

The CLI respects and applies configurations specified by option, environment variable, or OCI config file entry in the following order of precedence:
- The value specified in the command option.
- The value specified in the environment variable.
-
