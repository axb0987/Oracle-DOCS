# Roving Edge Infrastructure Device Specifications
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/device_specifications.htm
- Fetched: 2026-09-05 03:02 CDT

# Roving Edge Infrastructure Device Specifications

Describes the hardware and port specifications for Roving Edge Infrastructure devices.

## Hardware

The following table lists the hardware specifications of the Roving Edge Infrastructure devices. Specifications are for the maximum configuration.

Roving Edge Device (no longer shipping)

Roving Edge Device – Compute Shape

Roving Edge Device – GPU Shape

Roving Edge Device – Storage Shape

Roving Edge Ultra
Shape Name

RED.GPU.1.RX1.40 (deprecated) RED.2.56 RED.2.56.GPU RED.2.56.STG ULTRA.USB.1.RX2.12

Raw Storage

8 x 6.9 TB SSDs providing: 55.9 TB

4 x 13.97 TiB SSDs providing 55.88 TiB

4 x 13.97 TiB SSDs providing 55.88 TiB

8 x 13.97 TiB SSDs providing 111.86 TiB
- 7.7 TB
- 

Removable NVMe-based Ignition Key[1 :512 GB

Usable Storage (shared)[2 :

Block Volume Storage (replication) 18.6 TB

27.94 TiB

27.94 TiB

55.88 TiB 7 TB

Usable Storage (shared)[2 :

Object Storage (erasure coding) 41.9 TB

41.91 TiB

41.91 TiB

83.82 TiB 7 TB

Available OCPU

32

48

48

48

8

Usable Memory available for instances

390 GB DDR4-2933

384 GB

384 GB

384 GB

64 GB DDR4-2400

GPU

NVIDIA(R) Tesla(R) T4 GPU 2650 cudas cores, 320 sensor cores

N/A

3x NVIDIA Corporation AD104GL [L4]

N/A

No integrated GPU. Supports up to 2 Intel Movidius VPUs via USB

CPU

2 x Intel(R) Xeon(R) CPUs Gold 6230T @ 2.1Ghz, 40 total cores

1x Intel 8480+ Sapphire Rapids, 56C, 350W

1x Intel 8480+ Sapphire Rapids, 56C, 350W

1x Intel 8480+ Sapphire Rapids, 56C, 350W

Intel(R) Xeon(R) CPU D-1559 @ 1.50GHz, 12 total cores

Networking

2x10GbE (1 active)

3x Quad port Intel Corporation Ethernet Controller X710 for 10GBASE-T

1x Quad port Intel Corporation Ethernet Controller X710 for 10GBASE-T

1x Quad port Intel Corporation Ethernet Controller X710 for 10GBASE-T

2x1GbE (1 active)

Security

TPM, Trenchboot SecureBoot, physical tamper evidence

TPM, Trenchboot SecureBoot, physical tamper evidence, chassis intrusion detection

TPM, Trenchboot SecureBoot, physical tamper evidence, chassis intrusion detection

TPM, Trenchboot SecureBoot, physical tamper evidence, chassis intrusion detection

TPM, Trenchboot SecureBoot, physical tamper evidence

Removable NVMe-based Ignition Key (512 GB) for added security.[1

Dimensions

System: 20" L x 17" W x 3.5" H

Rugged Case: 38" L x 23.6" W x 11.8" H

System: 2U – 18.11" L x 16.93 W x 3.46 H

Rugged Case: 3U – 35.5" L x 23.8" W x 11.4" H

System: 2U – 18.11" L x 16.93 W x 3.46 H

Rugged Case: 3U – 35.5" L x 23.8" W x 11.4" H

System: 2U – 18.11" L x 16.93 W x 3.46 H

Rugged Case: 3U – 35.5" L x 23.8" W x 11.4" H

7.4" L x 6.3" W x 2" H without battery

7.4" L x 7.95" W x 2" H with battery pack

Weight

33.6 lbs (15.24 Kg) without rugged case

82.6 lbs (37.47 Kg) with rugged case combined weight

35 lbs (15.9 Kg) without rugged case

91.1 lbs (41.32 Kg) with rugged case combined weight

35 lbs (15.9 Kg) without rugged case

91.1 lbs (41.32 Kg) with rugged case combined weight

35 lbs (15.9 Kg) without rugged case

91.1 lbs (41.32 Kg) with rugged case combined weight

3.75 lbs (1.7 Kg) without battery

4.80 lbs (2.18 kg) with battery pack

Power Output

850 W

1100 W

1100 W

1100 W

55 W

Input Voltage

100 - 240VAC

100 - 240VAC

100 - 240VAC

100 - 240VAC

9 - 36VDC
Battery Options N/A

N/A

N/A

N/A

Voyager1+ (120 W power output with 65 Wh battery backup power)

80 PLUS Standard

80 PLUS Platinum

80 PLUS Titanium

80 PLUS Titanium

80 PLUS Titanium

Connector Type

C14

C14

C14

C14
Compliance and Certs

FIPS 140-2 Level 2

MIL-STD-810G

MIL-STD-461G

MIL-STD-1472H

MIL-STD-1474E

FIPS 140-3 Level 2

MIL-STD-810H

MIL-STD-461G

FIPS 140-3 Level 2

MIL-STD-810H

MIL-STD-461G

FIPS 140-3 Level 2

MIL-STD-810H

MIL-STD-461G

FIPS 140-2 Level 2

MIL-STD-810G/H

MIL-STD-461F
Operating Temp Range

0 C to 43 C (-5 C to 65 C storage)

0°C to +50°C

0°C to +50°C

0°C to +50°C

-20 C to 50 C (-40 C to 85 C storage)
Noise Level

68.6 - 73.7 dB (at 25 C ambient)

56.2 dbA (at 25C ambient)

56.2 dbA (at 25C ambient)

56.2 dbA (at 25C ambient) &lt; 60 dB

1 The Roving Edge Ultra removable NVMe-based Ignition Key is used for added security. It contains the Roving Edge Infrastructure device OS and the keys to decrypt the data drive.

2 Usable storage (shared) is a device storage pool that's allocated between block volumes and object storage. The total storage available can vary depending on the ratio of storage types used. The values listed in the table assume 100% block or 100% object storage usage.

## Safety and Compliance Resources

For safety and compliance information, refer to the following documents.

[Oracle Engineered System Safety and Compliance Guide](https://docs.oracle.com/en/engineered-systems/safety-and-compliance/es-safety-compliance/)

[Oracle Engineered System Safety and Compliance Guide (Nordic)](https://docs.oracle.com/en/engineered-systems/safety-and-compliance/es-safety-compliance-nordic/)

## Self-Encryption

Flash storage devices used in Roving Edge Device and Roving Edge Ultra are instant secure erase (ISE) drives. ISE drives behave like full disk encryption (FDE) drives in that the data is encrypted with a hardware key when written to disk, and then decrypted when the data is read from the disk. When the Crypto erase command is sent to the drive, the encryption/decryption key is overwritten, preventing the stored data from being decrypted.

The TPM cryptographic modules used in Roving Edge Devices and Roving Edge Ultra devices are FIPS 140-2 certified.

## Tamper-Evident Seals

Oracle applies, maintains, and tracks serialized tamper-evident seals on Roving Edge Device and Roving Edge Ultra. A broken, missing, or damaged label provides a visual indication of a potential hardware breach. Tamper-evident seals aren't FIPS 140-2 certified.

## Ultra Battery Options

The following battery options are available for use with Roving Edge Ultra devices:
- 

Modular stackable form-factor integrated 75Wh module:
- 

Directly attaches to the chassis.
- 

Provides up to 1 hour of operation per battery at its maximum CPU load.
- 

Has a 60W output.

## Service Ports

Each Roving Edge Infrastructure device supports a single IP and exposes its services through the following unique ports:

Service

Port

Identity

12050

Authorization

12060

Object Storage Gateway

8019

Virtual Cloud Network (VCN)

18336

Compute

19060, 19022

Data Sync

21060, 21061
Diagnostic Service

31060
Metric Service

32060

Monitoring

22060

System Upgrade

23060

Block Storage

5012

Roving Edge Device Console

8015

Etcd3
