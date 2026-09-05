# Token-based Authentication for the CLI
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clitoken.htm
- Fetched: 2026-09-05 01:36 CDT

# Token-based Authentication for the CLI

Token-based authentication for the CLI allows you to create a temporary session token which can be used to authenticate a CLI command request. You can generate this token with or without using a web browser.

## Requirements

The requirements are the same as those listed for the CLI in[Requirements](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/cliconcepts.htm#Requirements).

## Creating a CLI Session with a Browser

To use token-based authentication for the CLI on a computer with a web browser:
- In the terminal, run the following command:

```

```

- Select a region.
- In the browser, enter your user credentials.
- After successful authentication, close the browser and follow interactive prompt on the terminal. A configuration file will be created.

Optional argument

You can directly select a configured IdP by specifying the name of an identity provider (IdP) for creating a session token with a browser using the`--identity-provider-name`parameter.
For example:

```

```

If an invalid IdP name is provided, authentication falls back to the default method, and you're prompted to provide your credentials in the browser.

## Creating a CLI Session without a Browser

To generate a user token without a browser, you must first authenticate with one of the following methods:

- 

API key based authentication (oci setup config)
- 

Session token based authentication (oci session authenticate)

API key-based authentication

To use token-based authentication for the CLI without a web browser, run the following command:

```

```

This command creates a public/private key pair and updates the private key file location in`.config`file.

Session token-based authentication
If you're using a session token:

```

```

Optional arguments

For both the API key-based and session token-based authentication, you can provide a path to a public key as an argument. This provides a session token which can be signed by corresponding private key while using the generated token.
In the CLI, run the following command:

```

```

You can control the time for which the token persists. The minimum time for which token persists is 5 minutes and the maximum time for token persistence is 60 minutes (the default value). To setup a custom session expiration for the token, use the parameter`--session-expiration-in-minutes.`For example:

```

```

Note  
  
If you require multiple user tokens, run the no-browser token based authentication again with`oci session authenticate --no-browser`.

## Validating a Token

To verify that a token is valid, run the following command:

```

```

You must receive a message showing the expiration date for the session. If you receive an error, check your profile settings.
Note  
  
You must use the`--auth security_token`or set the`OCI_CLI_AUTH`environment variable to`security_token`to authenticate CLI commands using the session token.

## Refreshing a Token

The default token expiration time is set to 1 hour, and can be refreshed within the validity period up to 24 hours.
Note  
  
For sessions authenticated using`oci session authenticate --no-browser`, the maximum value is 60 minutes.

To refresh the token, run the following command:

```

```

Note  
  
You must use the`--auth security_token`or set the`OCI_CLI_AUTH`environment variable to`security_token`to authenticate CLI commands using the session token.

## Copying a CLI Session Token to Another Machine

To use token-based authentication for the CLI on a computer without a web browser, you must export a session from a web-enabled computer, then import it to the computer without a web browser.

### Exporting from Source Computer

On the source computer with the browser:
- In the CLI, run the following command:

```

```

- Enter the user credentials you wish to use on the target computer.
- To export a zip file, run the following command:

```

```

To verify the export, see[Validating a Token](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clitoken.htm#Validati).

### Importing to Target Computer

On the target computer without the browser, run the following command in the CLI,:

```

```

You can test the import by running the following:

```

```

It should return a list of regions. Successful execution of this command verifies that the token authentication is working as expected.

## Running Scripts on a Computer without a Browser

After importing the authentication to the target computer, you can run the CLI and SDKs by using the following settings.

### For CLI

To run scripts on the CLI, append the following suffix:

```

```

### For SDKs

To run SDKs on the target computer, you must read in the token file, then use it to initialize the`SecurityTokenSigner.`

After creating a token file as shown in[Creating a CLI Session with a Browser](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clitoken.htm#Starting), use the following process.
Note  
  
This method only works for the OCI SDKs for Go and Python. The following example is for the Oracle Cloud Infrastructure SDK for Python:
- Read the token file from the`security_token_file`parameter of the`.config`file. The parameter is automatically created and managed by the OCI CLI. The token file is saved under your default OCI config directory, for example,`~/.oci/`. The profile in your`~/.oci/config`file is updated with the`security_token_file`location, for example,`security_token_file=/Users/your-username/.oci/<generated-token-filename>`.

```

```

- Read the private key specified by the`.config`file.

```

```

- Create the initial SDK client which targets the user-specified region.

```

```

- Make the identity request.

```

```
