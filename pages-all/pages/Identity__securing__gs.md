# Getting Started
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/securing/gs.htm
- Fetched: 2026-09-05 02:28 CDT

# Getting Started

Get started with Identity Verification Providers and Identity Assurance.

## Before You Begin

Before you configure this feature, ensure you have the following:
- Third-party Identity Verification Provider Subscription: You must have an active commercial relationship and license with a supported third-party Identity Verification provider. IAM supports identity verification with providers using OpenID Connect (OIDC) integration. You will need to obtain a license from a configured third-party identity verification provider (for example, Daon or CLEAR) before you can begin the identity verification provider configuration.
- From your IDV provider, you will need the following credentials for configuration:
- Client ID
- Client Secret
- Discovery URL
- Feature availability: Identity Verification and Identity Assurance features are available in the OCI IAM Premium domain type only. If you have a Free domain type, you must upgrade to the Premium domain type.
- Admin Access: You need permissions to manage identity verification providers and domain policies.
- User Prerequisites: Ensure your users are aware of the requirements for enrollment:
- A mobile device with a camera and the ability to install the IDV provider's application.
- A government-issued ID with NFC capabilities (for example, a modern passport).
- A computer with a webcam for facial biometric enrollment and verification.
- A passkey configured as an authentication factor, as it's a prerequisite for Identity Assurance.

## Required IAM Policies

To manage Identity Domain security settings and Identity Assurance policies, you must have one of the following grants:
- Be a member of the Administrators group
- Be granted the Identity Domain Administrator role or the Security Administrator role
-
