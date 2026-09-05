# Layer 7 DDoS Mitigation
- Source: https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/ddos.htm
- Fetched: 2026-09-05 03:10 CDT

# Layer 7 DDoS Mitigation

## Distributed Denial of Service (DDoS) Overview

A DDoS attack is an often intentional attack that consumes an entity's resources, usually using a large number of distributed sources. DDoS can be categorized into either Layer 7 or Layer 3/4 (L3/4), as defined by the[Open Systems Interconnection (OSI)](https://en.wikipedia.org/wiki/OSI_model)model. L3/4 DDoS attacks are DDoS attacks that occur at lower levels of the OSI stack than layer 7. Examples of such attacks include UDP, CharGen, and NTP Floods. L3/4 DDoS mitigation is inherently provided by Oracle Cloud Infrastructure.

A layer 7 DDoS attack is a DDoS attack that sends HTTP/S traffic to consume resources and hamper a website's ability to deliver content or to harm the owner of the site. The Web Application Firewall (WAF) service can protect layer 7 HTTP-based resources from layer 7 DDoS and other web application attack vectors.

## Layer 7 DDoS Mitigation Services

Oracle provides a Layer 7 DDoS Mitigation service to help mitigate layer 7 DDoS attacks. DDoS Mitigation Specialists are trained members of our Cloud Customer Support team who help onboard you to WAF if you are not already using it. At the conclusion of the DDoS mitigation effort of a layer 7 DDoS attack, you may seek to receive credits for services that incurred additional Cloud Service fees. Details of this claim are available in the[Oracle PaaS and IaaS Public Cloud Services Pillar Document](https://www.oracle.com/us/corporate/contracts/paas-iaas-pub-cld-srvs-pillar-4021422.pdf).

### Requesting Help

It is your responsibility to report an attack through My Oracle Support. You can use monitoring and alarm definitions based on telemetry to receive notifications of thresholds exceeded. For more information about setting up alarms, see[Managing Alarms](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/managingalarms.htm). All changes will be audited in the Audit service.

To request help, go to[My Oracle Support](http://support.oracle.com/)and select the WAF product.

### Price Insurance Program

You may be eligible for credits due to excessive consumption due to a DDoS attack. Refer to the[Oracle PaaS and IaaS Public Cloud Services Pillar Document](https://www.oracle.com/us/corporate/contracts/paas-iaas-pub-cld-srvs-pillar-4021422.pdf)for details. Contact your customer success manager for details on how to apply for credits.

### Monitoring

For future monitoring, you can create an alarm definition in the Monitoring service that will alert you of high activity levels of HTTP traffic that could indicate another layer 7 DDoS attack. For more information, see[Managing Alarms](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/managingalarms.htm). Oracle Cloud Infrastructure automatically scrubs layer 3 and 4 attacks. If you suspect malicious activity that is not being properly remediated, go to[My Oracle Support](http://support.oracle.com/)
