# Threat Intelligence
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/threatintel.htm
- Fetched: 2026-09-05 03:11 CDT

# Threat Intelligence

Learn how WAF has several sources of known IP address threats that are updated daily.

WAF has several sources of known IP address threats that are updated daily. The IP address threats are displayed in the following table:

Source Description
Webroot BotNets Botnet C&amp;C channels and infected zombie machines controlled by Botmaster.
Webroot Denial of Service Includes DOS, DDOS, anomalous sync flood, and anomalous traffic detection.
Webroot Mobile Threats IP addresses of malicious and unwanted mobile applications. This category leverages data from the Webroot mobile threat research tea.
Webroot Phishing IP addresses hosting phishing sites and other kinds of illicit activities such as ad-click or gaming fraud.
Webroot Proxy IP addresses providing proxy and def services.
Webroot Reputation IP addresses currently known to be infected with malware. This category also includes IP addresses with an average low Webroot Reputation Index score.
Webroot Scanners Includes all reconnaissance such as probes, host scan, domain scan and password brute force attacks.
Webroot Spam Sources Includes tunneling spam messages through proxy, anomalous SMTP activities, and forum spam activities.
Webroot Tor Proxy Includes IP addresses acting as exit nodes for the Tor Network. Exit nodes are the last point along the proxy chain and make a direct connection to the originator's intended destination.
Webroot Web Attacks Includes known IP addresses involved in cross-site scripting, iFrame injection, SQL injection, cross-domain injection, or domain password brute force attacks.
Webroot Windows Exploits Includes active IP addresses offering or distributing malware, shell code, rootkits, worms, or viruses.

- [Console](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/threatintel.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/threatintel.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/WAF/Tasks/threatintel.htm#)
- 

This task can't be performed using the Console.
- 

You can use the CLI to enable threat intelligence sources to block.

Open a command prompt and run the following command to list the keys for all of the threat intelligence:
```

```

Then parse the keys to block and add them to the JSON:
```

```

For example:
```

```

- 

Enabling Threat Intelligence can only be performed by using the API at this time.

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

To return a set of keys for the threat intelligence:
- 

[ListThreatFeeds](https://docs.oracle.com/iaas/api/#/en/waas/latest/ThreatFeed/ListThreatFeeds)
Note  
  

Do not use the keys in the example below, as keys are unique across each policy.
```

```

To set all threats to DETECT:
- 

[UpdateThreatFeeds](https://docs.oracle.com/iaas/api/#/en/waas/latest/ThreatFeed/UpdateThreatFeeds)

With body:
```

```
