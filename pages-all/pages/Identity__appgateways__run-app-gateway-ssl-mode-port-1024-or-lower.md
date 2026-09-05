# Run App Gateway in SSL mode on port 1024 or lower
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/run-app-gateway-ssl-mode-port-1024-or-lower.htm
- Fetched: 2026-09-05 02:18 CDT

# Run App Gateway in SSL mode on port`1024`or lower

You can configure App Gateway to run in SSL mode on port number`1024`or lower.
Note  
  
To run your App Gateway server in Secure Sockets Layer (SSL) mode, you need to have a valid certificate.

## Configuring App Gateways in the IAM Console

Update your App Gateway configuration to enable the server to listen on port number 443 and in Secure Sockets Layer (SSL) mode.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select Security and then App gateways .
- Select the name of the App gateway you want.
- In Hosts select the name of the host you created.
- in the Edit Hosts window, update the following parameters as in the example below:

Parameter Value
Port`443`
SSL Enabled Selected.
Additional Properties
```

```

Note  
  
Generate a valid certificate to be used as the SSL certificate. The certificate file (`myappgateway.example.com.cert`) and the certificate key file (`myappgateway.example.com.key`) are referenced as an example.
- Select Save .

## Configuring the App Gateway Server

Enable your App Gateway server to run on port 443 in SSL mode.
Note  
  
Generate a valid certificate to your App Gateway to run on SSL mode, and copy the certificate file and the certificate key file to your desktop.

- Use an SSH client such as`PuTTY`to sign in to the App Gateway server.
- Run the following script.

```

```

Note  
  
The`setup-runasroot`is available from OVA version 25.4.3-10.0.0
- Edit the`/scratch/oracle/cloudgate/ova/bin/setup/cloudgate-env`file. You can use the following command or any other text editor of your choice:`vi /scratch/oracle/cloudgate/ova/bin/setup/cloudgate-env`
- Replace the value of the`CG_CALLBACK_PREFIX`parameter with the following`https://%hostid%`
- Save the`/scratch/oracle/cloudgate/ova/bin/setup/cloudgate-env`file.
- Run the following`sed`commands to enable running the server with`sudo`command:

```

```

- Confirm the`setup-cloudgate`file is configured with the values of your IAM tenant, and the values of the Client ID and Client Secret of the App Gateway you registered in the IAM Console.
- Run the following command to reconfigure App Gateway according to the parameters registered in the IAM Console (in this case, port number`443`and SSL Enabled .

```

```

After the`setup-cloudgate`script finishes, the App Gateway server starts automatically. You can access any application protected by your App Gateway using HTTPs, App Gateway domain, and port number`443`(default HTTPs port). For example,`https://myappgateway.example.com/myapp/index`

## Log Rotation

On OVA version 25.4.3-10.0.0, please run the following commands to ensure log rotation works as expected:
- `sudo chown root:root /usr/local/nginx/conf/logrotate_conf/logrotate.conf`
- `sudo chmod 755 /usr/local/nginx/logs/agent_logs`

## Starting and Stopping App Gateway Server Using`sudo`

Because you set up your App Gateway server to run on port`443`, you need to start and stop App Gateway server and agent using`sudo`command.

- To stop the App Gateway server and agent use the following command:

```

```

- To start the App Gateway server and agent use the following command:

```

```
