# Integrating Swaks with Email Delivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/swaks.htm
- Fetched: 2026-09-05 02:01 CDT

# Integrating Swaks with Email Delivery

Use Swaks to send emails through the Email Delivery service.

Swaks (Swiss Army Knife SMTP) is a transaction-based tool you can use to test SMTP configurations in Email Delivery. Before you use Swaks, you must configure Email Delivery and take note of your SMTP sending information and SMTP credentials.

Important  
  
These instructions contain sample code for your convenience and should be used as a reference. For client support, you must contact Swaks customer support. These steps were tested on an Oracle Linux Server release 7.9 compute instance and Swaks version 20201014.0.
Note  
  

Many options and parameters can be used to test various scenarios with Swaks. When Swaks evaluates an option (that is, a flag with parameters), it does so in three steps:
- First, it looks for a configuration file (default location or specified with`--config`).
- Next, it looks for options in environment variables.
- Finally, it looks at command line options. At each step, any options set earlier are overridden.

## Assumptions

The following procedures assume the following:
- The following example supplies options to Swaks via the command line in long form, for example,`--server`as opposed to the short form,`-s`.
- The following example assumes the default behavior to connect through network sockets.
- A local certificate is not required for a TLS connection to be negotiated. The following example assumes the default behavior where Swaks does not attempt certificate verification.
- Swaks is primarily intended for use on UNIX-like operating systems with functionality based on known standards so it should work on most modern mail servers.

## Configure Swaks to Send Email Through Email Delivery

To enable Swaks to test the configuration of Email Delivery:
- 

Ensure Email Delivery is configured to send email. See[Getting Started](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted.htm).
Note  
  

The SMTP credentials are required to configure Swaks to use Email Delivery. Be sure to note the user name and password when you generate the SMTP credentials.
- 

Ensure Swaks is installed. The installation process differs depending on which operating system you are using. For example, run the following command to install Swaks on Oracle Linux:
```

```

- 

To send a test email with Swaks, run the following command:

```

```

For example:

```

```

Note  
  

When sending email with Swaks:
- The`-tls`parameter is required when using port 25 or 587. If using port 465, use the`--tls-on-connect`parameter.
- The`--pipeline`parameter is supported to make use of SMTP pipelining.
- The`--port <number>`parameter or`:<port number>`syntax can be used to specify the port.
- The SMTP password is prompted after running this command

## More Information

- See the[Swaks documentation](https://linux.die.net/man/1/swaks)
