# Getting Started with Edge Policies
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm
- Fetched: 2026-09-05 03:10 CDT

# Getting Started with Edge Policies

Use the Web Application Firewall to manage edge policies.

## Before You Begin

Refer to the[Overview of Web Application Firewall](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/overview.htm#Overview_of_the_Web_Application_Firewall_Service)for important concepts about the WAF service.

To begin using the WAF service, you must have the following available:
- Ensure that you have the[Required IAM Service Policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/../Policies/getting_started_with_waf-policies.htm#iam)permissions.
- We recommended that you use a separate[compartment](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm)for the WAF policy so that management is easier and more secure.
- A main webapp domain.
- IP address of the LBaaS or other public facing endpoint of the application.
- Ability to update DNS records for the domain.
- The WAF service only supports traffic on ports 80/443; however, after requests reach the WAF on ports 80/443, we're able to send the requests to your origin server on any port necessary. The following is an example:

End User → Port 80/443 → WAF → Port 443/8000/555/*** → Origin Server Ensure that your application isn't running on other ports.
Note  
  
You can't use WAF for traffic like SSH, FTP, or SMTP.

Also, if you plan to run your site on HTTPS/443, you need:
- Public certificate for the fully qualified domain name (FQDN) of the application.
- Corresponding private key for the site.
- Certificate in PEM format.
- Full chain certificate (Root, Intermediate, Origin Server)
Note  
  
SSL certificates can only be applied to the main application of the policy.

Changes to Edge policies generally take 10 to 30 minutes to propagate, depending on the change. It takes that long to propagate because we have hundreds of nodes that new configurations are pushed to. The following feature changes typically propagate within 10 to 15 minutes:
- Bots policies
- Human Interaction Challenge (HIC)
- Device Fingerprint Challenge
- Javascript Challenge
- CAPTCHA Challenge
- Good Bot Whitelist
- Access Rules
- Thread Intelligence
- IP Lists
- IP Whitelist

Consider the following information when you work with Edge policies:
- 

IPv6 isn't currently supported.
- WAF inspects, but doesn't alter the response body.
- The caching limit is 1 GB per policy.
- For file size upload limitations, the limit is 1 GB. For file size limitations, consider:
- The limit doesn't depend on the type of upload, such as images, videos, binaries, and so on.
- The Content-Type header doesn't affect the limit. Only different protection rules are applied based on the Content-Type header.
- Uploads using chunked or streams don't affect the limit. In buffering mode, the limit is 1 GB for uploads and downloads. However, some other modes, including streaming the response body, disregard the 1 GB limit.
- WAF connections are rarely cancelled. A cancellation can occur because of large uploads or slow connections. After edge node reloads, a connection can be cancelled when a "cleanup" process is run, if the request or response cycle takes too long.
- When using the WAF with content streaming services, the content streaming services might be affected because our protection rules require buffering of the full HTML content before analysis. The entire content needs to be buffered within our protection rules core engine, which might lead to slow responses or events not displaying the streaming content.
- You can create or restore WAF policy backups with the OCI CLI. Extract the full JSON file of the web application and then re-create it in parts. We recommend that you recreate the main settings first, and then the security challenges and features of the web application.
- You can enable WebSocket for a specific URL through the CLI by using the following command:

`oci waas policy-config update --waas-policy-id ocid1.waaspolicy.oc1..[WAAS POLICY OCID] --websocket-path-prefixes '["/url/url/websocket"]'`
Note  
  
WebSocket support prevents WAF processing in the specified paths. This means that if a WAF rule is enabled, it doesn't analyze the requests going to the URL excluded in the configuration. However, other countermeasures, such as Human Interaction Challenge and JavaScript Challenge, can be enabled to provide an extra layer of security for WebSocket URL.
- The "key" in the Threat Intelligence Feed generated is different for each WAF policy.
- 

You can make changes to Edge policies only when the policy status is ACTIVE.

## Estimate cost for using WAF

Use this information to estimate costs for using the WAF service.
You can estimate the cost as follows:
- Go to:[https://www.oracle.com/cloud/cost-estimator.html](https://www.oracle.com/cloud/cost-estimator.html).
- Select Search and search for Networking - WAF .
- Select Add .
- Under Add Configuration , select the menu next to the service name, select Add by SKU, and then enter the SKU.
- Select Add .

In the cost estimator, "Instance" represents the WAF policy.

## Initial Setup of Your WAF Policy

### 1. Create an Edge Policy to Route Traffic Through the WAF

To begin, create an edge policy to route traffic through the WAF without rules enabled. Creating a policy without rules enabled ensures that there are no regressions by having a reverse proxy in front of the application.

[To create an edge policy](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- 

Select Create edge policy .
- 

Look at the bottom of the Basic Information page for the following:

Use legacy workflow here if you need to secure your non-OCI web applications.
- Select the link to display the Create Edge Policy dialog box.
- Complete the following:
- Name: A unique name for the policy.
- Domains:
- Primary Domain : The fully qualified domain name (FQDN) of the application where the policy will be applied.
- Additional Domains : (Optional) Subdomains where the policy will be applied.
Note  
  

Wildcard domains are accepted, however, only as additional domains and only through the API and CLI.
- WAF Origin: The host or IP address of the public internet facing application that is being protected.
- Origin Name : A unique name for the origin.
- URI : Enter the public facing endpoint (IPv4 or FQDN) of the application.
- HTTPS Port : The port used for secure HTTP connection. The default port is 443.
- HTTP Port : The HTTP port the origin listens on. The default port is 80.
- Headers: (Optional)
- Header Name : The name displayed in the HTTP request header and the header value that can be added and passed to the origin server with all requests.
- Header Value : Specifies the data requested by the header.
- Tags : If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create WAF Policy . The WAF Policy overview appears. Expect the policy to become active within 15 minutes of creation.

See[Managing Edge Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/../Tasks/managingwaf.htm#Managing_WAF_Policies)for more information.

### 2. Update Origin Keep Alive Timeout

The edge policy requires that your origin's (load balancer or web server) keep alive timeouts are maintained for 301 seconds or more, as our upstream timeout value is 300 seconds. The additional second is to ensure that the connection has enough time to renegotiate when our nodes create connections and avoid connectivity issues. This applies to API calls, as we use our OCI Network Multiplexing technology that helps to reduce network bottlenecks and improve performance by optimizing TCP protocol.

[To test the upstream keep alive timeout](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

HTTP check:
- Make the request against the origin or upstream server. Run the following command:
```

```

Example output:
```

```

- Make a GET request by entering the following HTTP headers:
```

```

- Press ENTER twice and wait for the session to close or disconnect.

HTTPS check:
- Initiate the request against the Origin or Upstream Server. Run the following command:
```

```

- Make a GET request by entering the following HTTP headers:
```

```

- Press ENTER twice and wait for the session to close or disconnect.
You will receive the following output. In this example, the real section shows the actual time the session was alive (5.1 minutes (301 seconds)):
```

```

See[Origin Management](https://docs.oracle.com/iaas/Content/WAF/Tasks/originmanagement.htm)for more information.

### 3. Upload Your Certificate and Key

This step assumes that your site runs on HTTPS/443.

[To upload your certificate and key](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Policies .

Alternatively, open the Web Application Firewall page and select Policies under Resources .

The WAF Policies page appears.
- Select the Compartment from the list.

All the WAF policies in that compartment are listed in tabular form.
- (Optional) Apply one or more of the following Filters to limit the WAF policies displayed:

- 

State
- 

Name
- 

Policy Type : Select Edge Policy .
- Select the edge policy for which you want to upload the certificate and key.

The Edge Policy Details dialog box appears.
- Select Settings under WAF Policy .
The Settings list appears.
- Select General Settings .
- Select Edit .
The Edit Settings dialog box appears.
- Complete the following:

- Enable HTTPS Support : Select this check box to enable all communications between the browser and web application to be encrypted.
- Certificate Source : Choose one of the following methods:
- Choose Certificate : Select an existing certificate from the drop-down menu. Select Change Compartment to select a certificate from another compartment.
- Upload or Paste Certificate and Private Key
- 

Drag and drop, select, or paste a valid SSL certificate in PEM format. You must also include intermediate certificates (the website certificate must be first). The following is an example:
```

```

- 

Private Key: Drag and drop, select, or paste a valid private key in PEM format in this field. The private key cannot be protected by a passphrase. The following is an example:
```

```

- Self Signed Certificate : Enable this field when using a self-signed certificate to show an SSL warning in the browser.
- HTTP to HTTPS Redirect : When enabled, all HTTP traffic is automatically redirected to HTTPS.
- TLS Protocols Support : Select a TLS protocol from the drop-down list.
Caution  
  
TLS versions 1 and 1.1 have been deprecated and cannot be used in policy configurations. If you use these versions, a validation error might occur. Use versions 1.2 or 1.3 instead.
- Enable SNI : Server Name Indication (SNI) is an extension of the TLS protocol, which allows multiple secure hostnames to be served from a single IP address.
- Advanced Options
- Enable Response Buffering : Enable or disable buffering of the response from the origin.
- Cache Control Respected : Enable or disable automatic content caching based on the response cache-control header.
- Behind CDN: Enable this to allow the collection of IP addresses from the client request if WAF is connected to a CDN.
- Select Save Changes .
You must publish your changes for them to take effect. See[Publishing Changes](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/../Bot/publishing_changes.htm#PublishChanges).

### 4. Test Your Application (Before Deploying it to Production)

In this step, you ensure that requests are being routed to the WAF and that your application continues to function normally with a reverse proxy in the topology.

[Test your application through a terminal command](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

- Open a terminal.

Run the following command for HTTP:
```

```

Run the following command for HTTPS:
```

```

- You can also run a DNS query against the`<OCI_WAF_CNAME>`for your WAF policy and copy one of the IP addresses from the resulting output.
- 
To run a DNS query you can use one of the following commands:
```

```

```

```

- Copy any of the IP addresses from the output.
- Run the following command. Replace`<WEBAPP_DOMAIN>`with your WAF policy domain. Use port 80 or 443. Replace`<OCI_NODE_IP>`with the IP address from`OCI_WAF_CNAME`.
```

```

A 200, 301, 302, or any other expected HTTP response code is returned.

Note  
  
If you receive a 5XX HTTP error, ensure that you have updated your firewall setting to allow our IP addresses. If you are still experiencing an issue, open a service request with My Oracle Support. In the support request, provide your compartment OCID, policy OCID, explanation about the issue you are experiencing, a HAR file, and a time when the issue started.

[Test your application through a web browser](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

To test your application using a hosts file, you need an IP address where you could point your application. Under the policy, you should see the CNAME which is assigned to you. You can get the IP address where you can point your application.
- Open a terminal.
- Run a DNS query using any of the following commands:
```

```

```

```

- Copy one of three IP addresses from a dig command output Answer section and paste it to a hosts file with your domain name.
- After you save your hosts file, open your application in a browser and verify it is working as expected.

A 200, 301, 302, or any other expected HTTP response code is returned.

Note  
  
If you receive a 5XX HTTP error, ensure that you have updated your firewall setting to allow our IP addresses. If you are still experiencing an issue, open a service request with My Oracle Support. In the support request, provide your compartment OCID, policy OCID, explanation about the issue you are experiencing, a HAR file, and a time when the issue started.

[Test your SSL](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

The following useful command line tools can be used to validate certificates on a given web application:
```

```

Pay special attention to the certificate validity dates and expiration dates that might cause connection issues:
```

```

You can also check the certificate from third-party websites such as SSL Shooper or SSL labs and perform the validation there.

### 5. Update DNS to Enable WAF

After confirming your web application works flawless through WAF, you can now proceed to update the DNS globally.

In this step, you update the CNAME for your zone to route requests from internet clients to WAF. Use the following instructions to make this DNS change in the Console. If your DNS setup resides with another provider, refer to their documentation for instructions.

[To update the CNAME for your zone](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

- In the Policy Information tab of the WAF Policy overview, select the CNAME Target.
- Copy the CNAME target to your clipboard.
- Open the navigation menu and select Networking . Under DNS management , select Public Zones .
- 

Select the Zone Name of the primary domain where you want to update the record. Zone details and a list of records appear.
- Select the check box for the CNAME record and select Edit from the Actions drop-down menu.
- In the Edit Record dialog box, update the Target field with the CNAME Target from your clipboard.
- Select Submit .
- Select Publish Changes .
- In the confirmation dialog box, Select Publish Changes .

### 6. Securing Your WAF

To secure your WAF, you must configure your servers to accept traffic from the WAF servers. Configure your origin's ingress rules to only accept connections from the following CIDR ranges.

[CIDR Ranges](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

- 129.146.12.128/25
- 129.146.13.128/25
- 129.146.14.128/25
- 129.148.156.0/22
- 129.213.0.128/25
- 129.213.2.128/25
- 129.213.4.128/25
- 130.35.0.0/20
- 130.35.112.0/22
- 130.35.116.0/25
- 130.35.120.0/21
- 130.35.128.0/20
- 130.35.144.0/20
- 130.35.16.0/20
- 130.35.176.0/20
- 130.35.192.0/19
- 130.35.224.0/22
- 130.35.232.0/21
- 130.35.240.0/20
- 130.35.48.0/20
- 130.35.64.0/19
- 130.35.96.0/20
- 130.35.228.0/22
- 132.145.0.128/25
- 132.145.2.128/25
- 132.145.4.128/25
- 134.70.16.0/22
- 134.70.24.0/21
- 134.70.32.0/22
- 134.70.56.0/21
- 134.70.64.0/22
- 134.70.72.0/22
- 134.70.76.0/22
- 134.70.8.0/21
- 134.70.80.0/22
- 134.70.84.0/22
- 134.70.88.0/22
- 134.70.92.0/22
- 134.70.96.0/22
- 138.1.0.0/20
- 138.1.104.0/22
- 138.1.128.0/19
- 138.1.16.0/20
- 138.1.160.0/19
- 138.1.192.0/20
- 138.1.208.0/20
- 138.1.224.0/19
- 138.1.32.0/21
- 138.1.40.0/21
- 138.1.48.0/21
- 138.1.64.0/20
- 138.1.80.0/20
- 138.1.96.0/21
- 138.1.112.0/20
- 140.204.0.128/25
- 140.204.12.128/25
- 140.204.16.128/25
- 140.204.20.128/25
- 140.204.24.128/25
- 140.204.4.128/25
- 140.204.8.128/25
- 140.91.10.0/23
- 140.91.12.0/22
- 140.91.22.0/23
- 140.91.24.0/22
- 140.91.28.0/23
- 140.91.30.0/23
- 140.91.32.0/23
- 140.91.34.0/23
- 140.91.36.0/23
- 140.91.38.0/23
- 140.91.4.0/22
- 140.91.40.0/23
- 140.91.8.0/23
- 147.154.0.0/18
- 147.154.128.0/18
- 147.154.192.0/20
- 147.154.208.0/21
- 147.154.224.0/19
- 147.154.64.0/20
- 147.154.80.0/21
- 147.154.96.0/19
- 192.157.18.0/24
- 192.157.19.0/24
- 192.29.0.0/20
- 192.29.128.0/21
- 192.29.138.0/23
- 192.29.144.0/21
- 192.29.152.0/22
- 192.29.16.0/20
- 192.29.160.0/21
- 192.29.168.0/22
- 192.29.172.0/25
- 192.29.178.0/25
- 192.29.180.0/22
- 192.29.32.0/21
- 192.29.40.0/22
- 192.29.44.0/25
- 192.29.48.0/21
- 192.29.56.0/21
- 192.29.60.0/23
- 192.29.64.0/20
- 192.29.96.0/20
- 192.29.140.0/22
- 192.69.118.0/23
- 198.181.48.0/21
- 199.195.6.0/23
- 205.147.88.0/21

## Enable WAF to Passively Detect Rules

WAF protection rules add extra CPU cycles to each transaction, therefore, we recommended enabling only the rules designed for your web application topology. WAF offers a set of recommended rules that will not harm your site performance and work with most of the web application. The WAF bot protection feature makes your web application fully secured to threats.

If you need help with setting up WAF, you can open a service request with[My Oracle Support](http://support.oracle.com/)requesting OCI WAF tuning help. An expert will guide you through the process.

[To view Protection Rule Recommendations](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select the name of the WAF Policy you want to view protection rule recommendations for. The WAF Policy overview appears.
- Select Protection Rules .
- Select the Recommendations tab. This list is generated based on the traffic the WAF detects flowing through the WAF. If nothing appears in this list, keep testing the FQDN of your application and check back later.
- Select the protection rules with a Detect recommended action and then select Accept Recommendations .
Tip  
  
You can use the Recommended Action filter to locate a recommendation by Detect .

[To enable WAF Protection Rules to detect mode](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select the name of the WAF Policy you want to configure rule settings for. The WAF Policy overview appears.
- Select Protection Rules .
- Use the[Protection Rules table](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/../Reference/protectionruleids.htm#Supported_Protection_Rules)to locate the rules you want to detect.
- Enter the Rule IDs you located from the table into the Rule ID filter. For this example, enter 941110 (Cross-Site Scripting) in the Rule ID filter.
- Select Detect from the Actions drop-down menu for the protection rules you filtered.

See[WAF Protection Rules](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/../Tasks/wafprotectionrules.htm#WAF_Protection_Rules)for more information.

[To enable WAF Access Rules to detect mode](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select the name of the WAF Policy you want to configure access rules for. The WAF Policy overview appears.
- Select Access Control .
- Select Add Access Rule .
- In the Add Access Rule dialog box, enter the following:
- Name: DetectRequestsFromMySpecificBrowser
- Rule Action: Select Detect Only .
- Conditions: Select IP Address is from the menu and enter the IP address you copied to your clipboard while testing your application in the IP Address field.
- Select +Additional Condition .
- Condition: Select User Agent is from the menu and enter the agent value you copied to your clipboard while testing your application in the User Agent Header field.
Note  
  

Both the IP Address and the User Agent in the preceding example must match for the rule to be triggered. If a different User Agent is used to test your application, the request will not be detected.
- Select Add Access Rule .
- Select Unpublished Changes .
- Select Publish All .

See[Access Control for Edge Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/../Tasks/wafaccesscontrol.htm#Access_Control)for more information.

[To enable WAF BOT rules to detect mode (JavaScript Challenge)](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select the name of the WAF Policy you want to configure JavaScript Challenge settings for. The WAF Policy overview appears.
- Select Bot Management .
- Select Edit JavaScript Challenge .
- In the JavaScript Challenge dialog box, select the Enable JavaScript Challenge check box.
- 

In the JavaScript Challenge Action section, select Detect Only .
- 

Enter the following information:
- Enable Conditions: When enabled, conditions must match for a set action to be taken. See[Access Control for Edge Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/../Tasks/wafaccesscontrol.htm#Access_Control)for more information about conditions and rules.
- Action Threshold (number of requests) : Specify the number of failed requests before taking action. Because of the asynchronous request from the browser during page loading, it is recommended to set a threshold of 10 for web applications with basic ajax usage, and 100 for apps with heavy ajax usage.
- Action Expire Time (seconds) : Enter the number of seconds between challenges to the same IP address. Because of client IP address changes, it is recommended that the expiry time is set to 120 seconds for apps with mobile users and 3,600 seconds for apps with desktop users only.
- Follow Redirects: When enabled, redirect responses from the origin will also be challenged.
- Enable NAT Support: When enabled, the user is identified not only by the IP address but also by a unique additional hash, which prevents blocking visitors with shared IP addresses. It is recommended that this NAT support is disabled for high-load apps (200+RPS).
- Select Save Changes .

The JavaScript Challenge is added to the list of changes to be published.

See[Bot Management](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/../Tasks/botmanagement.htm#BotManagement)for more information.

[To enable WAF BOT rules to detect mode (Human Interaction Challenge)](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select the name of the WAF Policy you want to configure JavaScript Challenge settings for. The WAF Policy overview appears.
- Select Bot Management .
- Select the Human Interaction Challenge tab.
- Select Edit Human Interaction Challenge .
- In the Edit Human Interaction Challenge dialog box, select the Enable Human Interaction Challenge check box.
- In the Human Interaction Action section, select Detect Only .
- Enter the following information:
- Action Threshold (number of requests): Specify the number of failed requests before taking action. Because of the asynchronous request from the browser during page loading, it is recommended to set a threshold of 10 for web applications with basic ajax usage, and 100 for apps with heavy ajax usage.
- Threshold Expiry Period (seconds) : The number of seconds before the threshold expires.
- Action Expire Time (seconds): Enter the number of seconds between challenges to the same IP address. Because of the client IP address changes, it is recommended that the expiry time is set to 120 seconds for apps with mobile users and 3,600 seconds for apps with desktop users only.
- Interaction Threshold (number of interactions): Number of interactions before the threshold expires.
- Recording Period (seconds): The period of time to record the user's events.
- NAT Support: When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking visitors with shared IP addresses. It's recommended to disable the support for the high-load apps (200+ RPS).
- Select Save Changes .

The Human Interaction Challenge is added to the list of changes to be published.

See[Bot Management](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/../Tasks/botmanagement.htm#BotManagement)for more information.

See[Managing Edge Policies](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/../Tasks/managingwaf.htm#Managing_WAF_Policies)for the order of processing of WAF.

## Test the Rules

When the policy is active, you can test that your rules are detected by WAF.

[To initiate requests](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

- Use the same browser you used when you tested your application to do the following:
- Request the FQDN of your application with the following query parameter appended:
```

```

- Use a different browser on the same machine and repeat the preceding requests. All requests should go through the application.

[To verify that WAF is detecting requests](https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/gettingstarted.htm#)

To verify that WAF is detecting requests identified as a risk:
- Open the navigation menu and select Identity &amp; Security . Under Web Application Firewall , select Edge Policy Resources .

The Policies list opens. All edge policies are listed in a table.
- Select the name of the WAF Policy you want to view logs for. The WAF Policy overview appears.
- Select Logs . Logs for the WAF policy appear.
- Select the Detect check box from the Actions filter.
-
