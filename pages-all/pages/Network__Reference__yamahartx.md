# Yamaha RTX Series
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Reference/yamahartx.htm
- Fetched: 2026-09-05 02:42 CDT

# Yamaha RTX Series

This configuration was validated using an RTX1210 running Firmware Rev.14.01.28 and RTX830 running Firmware Rev.15.02.03.
Important  
  

Oracle provides configuration instructions for a tested set of[vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/CPElist.htm). Use the correct configuration for the vendor and software version.

If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes.

If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of[supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/supportedIPsecparams.htm)and consult the vendor's documentation for help.
Important  
  
Oracle uses asymmetric routing across the tunnels that make up the IPSec connection. Even if you configure one tunnel as primary and another as backup, traffic from a VCN to an on-premises network can use any tunnel that's "up" on a device. Configure firewalls as appropriate. Otherwise, ping tests or application traffic across the connection don't work reliably.

## Before Starting

Before configuring the CPE:
- Configure the internet provider settings.
- Configure firewall rules to open UDP port 500, UDP port 4500, and ESP.

### Supported Encryption Domain or Proxy ID

The values for the encryption domain (also known as a proxy ID, security parameter index (SPI), or traffic selector) depend on whether a CPE supports route-based tunnels or policy-based tunnels. For more information about the correct encryption domain values to use, see[Supported Encryption Domain or Proxy ID](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Tasks/ipsecencryptiondomains.htm).

## Parameters from API or Console

Get the following parameters from the Oracle Cloud Infrastructure Console or API.

${ipAddress#}
- Oracle VPN headend IPSec tunnel endpoints. One value per tunnel.
- Example value: 129.146.12.52

${sharedSecret#}
- The IPSec IKE pre-shared-key. One value per tunnel.
- Example value: EXAMPLEDPfAMkD7nTH3SWr6OFabdT6exXn6enSlsKbE

${cpePublicIpAddress}
- The public IP address for the CPE (already made available to Oracle through the Console).

${VcnCidrBlock}
- When creating the VCN, your company selected this CIDR to represent the IP aggregate network for all VCN hosts.
- Example Value: 10.0.0.0/20

## Parameters Based on Current CPE Configuration and State

The following parameters are based on the current CPE configuration.

${tunnelInterface#}
- An interface number to identify the specific tunnel.
- Example value: 1

${ipsecPolicy#}
- The SA policy to be used for the selected inline interface.
- Example value: 1

${localAddress}
- The public IP address of the CPE.
- Example value: 146.56.2.52

## Config Template Parameter Summary

Each region has several Oracle IPSec headends. The following template helps you to set up several tunnels on a CPE, each to a corresponding headend. In the table, "User" is you or your company.

Parameter Source Example Value
`${ipAddress1}`Console/API 129.146.12.52
`${sharedSecret1}`Console/API (long string)
`${ipAddress2}`Console/API 129.146.13.52
`${sharedSecret2}`Console/API (long string)
`${cpePublicIpAddress``}`User 1.2.3.4
`${VcnCidrBlock}`User 10.0.0.0/20

Important  
  
The following ISAKMP and IPSec policy parameter values are applicable to Site-to-Site VPN in the commercial cloud. For the[Government Cloud](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm), you must use the values listed in[Required Site-to-Site VPN Parameters for Government Cloud](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#vpn_params).

## ISAKMP Policy Options

Parameter Recommended Value
ISAKMP protocol version Version 1
Exchange type Main mode
Authentication method Pre-shared keys
Encryption AES-256-cbc
Authentication algorithm SHA-256
Diffie-Hellman Group Group 5
IKE session key lifetime 28800 seconds (8 hours)

## IPSec Policy Options

Parameter Recommended Value
IPSec protocol ESP, tunnel-mode
Encryption AES-256-cbc
Authentication algorithm HMAC-SHA1-96
Diffie-Hellman Group Group 5
Perfect Forward Secrecy Enabled
IPSec session key lifetime 3600 seconds (1 hour)

## CPE Configuration

### ISAKMP and IPSec Configuration

```

```

### Static Routes Configuration

```

```
