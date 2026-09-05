# Managing Identity Assurance
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/securing/configure_idv_providers_and_identity_assurance.htm
- Fetched: 2026-09-05 02:28 CDT

# Managing Identity Assurance

Use Identity Verification and Facial Biometrics to ensure that a user is who they claim to be before accessing enterprise resources.

## Introduction

Identity Verification (IDV) : The one-time process of validating a user's real-world identity by matching a live selfie to a government-issued ID (for example, a passport or driver's license). IDV is performed by a supported third-party identity verification provider and offers a high level of assurance that the user is who they claim to be.

Facial Biometrics : The process leverages the capturing a user's unique facial characteristics to create a secure biometric template. This template is used for initial enrollment and subsequent verification checks. Facial biometrics in OCI IAM is an OCI-native capability.

Identity Assurance : Combines IDV and facial biometrics. After initial identity verification (IDV), the system periodically reverifies a user's identity using facial biometrics. These checks confirm that the person using the credentials is the enrolled user, not someone who obtained the credentials. This process reduces the risk of impersonation and unauthorized access and strengthens your organization's security posture.
This service integrates with third-party identity verification (or identity proofing) providers to perform the initial document and identity check. After a user's identity is verified, their facial biometric data is enrolled with Oracle's native service for ongoing verification checks.
Note  
  
We support third-party verification providers such as Daon and CLEAR.

## Concepts

Identity Verification Provider : We support third-party verification providers such as Daon and CLEAR for the initial identity verification in IAM using government-issued documents.

Liveness Detection : Technology used during facial biometric scans to ensure the user is physically present and not using a photo, video, or mask to spoof the system. This involves prompts such as tilting the head or blinking.

Inline Enrollment : An enrollment process that can be mandated by an administrator and occurs directly within the sign-in flow. Mandated users are typically required to complete it before they can access applications.

### Identity Assurance Process

The process involves two key personas:
- Administrators: Configure Identity Verification providers and set up Identity Assurance policies that define when and how often users must verify their identity.
- Users: Enroll in the service by verifying their identity with a government-issued ID and enrolling their facial biometrics with IAM. Subsequently, they complete periodic facial biometric checks as defined by the administrator.

## Administrators Workflow

- An administrator at Example Inc. first establishes a commercial relationship with a supported third-party identity verification provider.
- In the OCI Console, the administrator navigates to the Identity Domain, configures the third-party identity verification provider using credentials such as client ID and secret, and activates it.
- The administrator then creates an Identity Assurance policy and adds a rule that specifies which user groups are affected.
- Within the rule, the administrator enables facial biometrics and sets the frequency for periodic checks (for example, every 7 to 14 days) and reenrollment (for example, every 6 to 12 months).

We recommend combining Identity Verification and Biometrics for enhanced identity assurance. However, each capability is optional and can be used separately. Administrators have the flexibility to configure Identity Assurance with Identity Verification and Facial Biometrics, or with Facial Biometrics alone according to their organization's specific needs. When both identity verification and facial biometrics are enabled for inline enrollment, the IDV process will be prompted first, followed by Biometric verification.

Identity assurance happens after authentication and can be used for identity verification even if you're federated with an external third-party identity provider, such as Azure.

Administrators also have the option to specify enrollment as a mandatory inline option or a feature that users can skip and define settings such as verification frequency.

## End-User Workflow

- Initial Enrollment : An employee, John, is prompted to enroll inline after authentication (if Identity Assurance policy is configured for inline enrollment), or from My profile. This is a one-time process.
- Identity Verification : A QR code appears on John's computer screen. He scans it with his smartphone to initiate the identity verification process with the configured third-party identity verification provider, for example. He takes a live selfie and then scans his government-issued ID. The configured third-party identity verification provider validates the document's authenticity and confirms that the selfie matches the photo in the document.
- Biometric Enrollment : John is redirected back to his computer's web browser. He is prompted to position his face in a frame and complete randomized liveness prompts, which involves aligning his nose with random dots. The system captures his facial data, creates a biometric template, and stores it securely to complete his enrollment.
- Ongoing Verification : Two weeks later, when John accesses an application, he signs in with his standard credentials. Immediately afterward, Identity Assurance initiates a facial biometric challenge. He positions his face, completes a liveness prompt, and the system validates his identity against the stored template, granting him access.

## Use Case: Example of how Example Inc Leverages IDV and Identity Assurance

This use case uses Daon to highlight how Example Inc leverages the identity verification vendor Daon for Identity Assurance. An administrator configures IAM to integrate with the identity verification provider and creates Identity Assurance policies for periodic verification of users. An employee of Example Inc. verifies identity with a government-issued ID, enrolls in facial biometrics, and is reverified through periodic identity checks.

### Admin Configuration

- An administrator at Example Inc. navigates to the identity domain and configures an identity verification provider, Daon.
- The administrator enters credentials provided by the vendor (client id, client secret, discovery URL), maps the Supported claims with identity domain attributes, and then selects Create . The Identity verification provider is created. Administrator then activates the identity verification provider.
- The administrator creates an Identity Assurance policy and creates a rule. In the rule, administrator sets the prerequisites in the conditions field, with passkey as the first authentication factor and Oracle Mobile Authenticator (OMA) as the second factor and select the user groups that are evaluated by the rule.
- The Example Inc. administrator then enables facial biometrics, schedules facial biometric checks at randomized intervals between 7 and 14 days, and reenrollment frequency between 6 to 12 months.
- The administrator enables identity verification, and selects the provider created in step 2.
- After defined, the policy is enforced across the identity domain for the users who satisfy the conditions specified in the rule.

### User Enrollment

- An employee, John, receives an email informing him of the new requirement. He signs in with his primary and second factor and is prompted to Enroll with Biometrics. If not prompted to enroll in biometrics during sign-in, the user signs in to My Login Profile and selects Enroll with biometrics .
- The user reviews and accepts the terms and conditions.
- 

Identity Verification
- A QR code appears on his computer screen. John scans it with his smartphone, which initiates identity verification with Daon. Depending on Daon configuration, John might be asked to download the Daon app or an app provided by Example Inc. to complete identity verification.
- John takes a live selfie. Daon verifies the user's selfie for liveness.
- He then scans his government-issued ID using his phone. Daon validates the document's authenticity and confirms that the selfie matches the photo in the document.
- A success message indicates that his identity has been verified.
- 

Facial Biometrics Enrollment
- John is redirected back to his computer's web browser.
- The browser requests access to his webcam. He is prompted to position his face in a frame and complete the randomized liveness prompts, such as tilting the user's head up, to the right, and left. These steps protect against spoofing and replay attacks.
- The system captures his facial data, creates a biometric template, and stores it securely. His enrollment is now complete.

### Identity Assurance

- After enrolled, periodic facial biometric verification occurs seamlessly in the background. For example, two weeks later, when accessing an enterprise application, John completes the standard passkey sign-in followed by Oracle Mobile Authenticator (OMA) as the second factor.
- Immediately afterward, Identity Assurance initiates a facial biometric verification challenge. John positions his face within the frame, completes a randomized liveness prompt, and the system validates his identity against the securely stored biometric template.
-
