# FastConnect Public Peering Advertised Routes
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm
- Fetched: 2026-09-05 02:41 CDT

# FastConnect Public Peering Advertised Routes

Learn about how the public IP address ranges (routes) that BGP advertises to an on-premises network over FastConnect public peering (a public virtual circuit). You might need this information when configuring firewall allowlists for an on-premises network.

By default, when you connect with FastConnect to Oracle Cloud Infrastructure (OCI) in a particular region, the routes advertised over the public virtual circuit include routes for other OCI regions in the same market. For more information about regions, see[About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About).

If you don't own a Public ASN or Public IP Address, you might need to review this section:[To use FastConnect if you don't own a Public ASN or Public IP Address](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#public_asn_ip).

Using[route filtering](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering)you can also decide to advertise public routes used by ephemeral IP address ranges, reserved IP address ranges, and Oracle Services Network (OSN) to an on-premises network at the region , market , or global (all regions in all markets) scope. You can also decide to only advertise routes to OSN from the local region. The following map and tables show which regions are in the same[market](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm#markets)group.

You can select route filtering options when you set up a FastConnect virtual circuit. The details vary depending on whether you're using a[FastConnect partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#set_up_vc), a[third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#task_set_up_vc), or[colocation](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#task_set_up_vc).

## Downloading the JSON File

[Use this link to download the current list of all public IP ranges in all commercial regions](https://docs.oracle.com/iaas/tools/public_ip_ranges.json). This list is formatted in JSON, and provides the most current list of the actual public routes advertised by a region. You can concatenate several regional lists into market lists.

You can poll the published file to check for new IP address ranges as often as every 24 hours. We recommend that you poll the published file at least weekly. More information on reading and using this JSON file is at[IP Address Ranges](https://docs.oracle.com/iaas/Content/General/Concepts/addressranges.htm).

## Security considerations for FastConnect public peering

Always consider FastConnect public peering as an untrusted interface, and put in place firewalls and other access controls as you would for any network interface connected to the Internet.

When an on-premises network is connected to OCI using FastConnect public peering without access controls or[route filtering](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering), the on-premises network can receive packets from:
- All VCNs in the same market in the tenancy (or tenancies, if you have more than one) with internet access
- Any VCN resources with internet access operated by other OCI customers in the same market
- OCI public services such as Object Storage, the Console, or APIs

When an on-premises network is connected to OCI using FastConnect public peering without access controls, the on-premises network can't receive packets from:
- Routers used by other OCI customers' on-premises networks that are also connected with FastConnect public peering
- Internet users and resources

## Markets

Markets are groupings of OCI regions that are in the same general part of the world.

The following table shows the OCI regions grouped into the four existing markets. If you use FastConnect public peering to connect to one of the following OCI regions, and you set[route filtering](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering)to the market scope, BGP advertises routes from the region to which you're directly connected and also the other regions in the market to the on-premises network.

Market OCI regions in the market: region keys
Asia Pacific (APAC)

Australia East (Sydney): SYD

Australia Southeast (Melbourne): MEL

India South (Hyderabad): HYD

India West (Mumbai): BOM

Indonesia North (Batam): HSG

Japan Central (Osaka): KIX

Japan East (Tokyo): NRT

Malaysia West 2 (Kulai): JBP

Singapore (Singapore): SIN

Singapore West (Singapore): XSP

South Korea Central (Seoul): ICN

South Korea North (Chuncheon): YNY
Europe, Middle East, Africa (EMEA)

France Central (Paris): CDG

France South (Marseille): MRS

Germany Central (Frankfurt): FRA

Israel Central (Jerusalem): MTZ

Italy North (Turin): NRQ

Italy Northwest (Milan): LIN

Morocco West (Casablanca): LEJ

Netherlands Northwest (Amsterdam): AMS

Saudi Arabia Central (Riyadh): RUH

Saudi Arabia West (Jeddah): JED

South Africa Central (Johannesburg): JNB

Spain Central (Madrid): MAD

Spain Central (Madrid 3): ORF

Sweden Central (Stockholm): ARN

Switzerland North (Zurich): ZRH

UAE Central (Abu Dhabi): AUH

UAE East (Dubai): DXB

UK South (London): LHR

UK West (Newport): CWL
Serbia

Serbia Central (Jovanovac): BEG *
North America (NA)

Canada Southeast (Montreal): YUL

Canada Southeast (Toronto): YYZ

Mexico Central (Queretaro): QRO

Mexico Northeast (Monterrey): MTY

US East (Ashburn): IAD

US Midwest (Chicago): ORD

US West (Phoenix): PHX

US West (San Jose): SJC
Latin America Division (LAD)

Brazil East (Sao Paulo): GRU

Brazil Southeast (Vinhedo): VCP

Chile Central (Santiago): SCL

Chile West (Valparaiso): VAP

Colombia Central (Bogota): BOG
