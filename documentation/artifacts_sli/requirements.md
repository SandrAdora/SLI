# Requirements and Specification

* We assume there is stable Internet (WLAN or MobilFunk)
* The device used has a working camera and display


## Requirements

### Functional Requirements

* The system must provide real‑time text‑based communication between users.
* The system must support video‑based communication for sign‑language conversations.
* The system must include an AI‑assisted sign‑language recognition feature to translate sign language into written text.
* The system must include an AI‑assisted text‑to‑sign‑language avatar for users who prefer sign‑language output.
* The system must allow users to switch between communication modes (text,  sign‑language translation) at any time.
* The system must support API access for third‑party accessibility tools.

### Non-Functional Requirements

* Real‑time video communication must maintain a latency of under 300 ms under normal network conditions.
* Sign‑language recognition must process gestures with at least 85% accuracy at launch, improving over time.

## Specification

* Text chat: real‑time messaging via WebSockets.
* Video communication: WebRTC for P2P video
* Latency target for video calls: < 300 ms under typical conditions.
* Translation response time: < 1–2 seconds for short utterances.
* Fallback to pure text if video/AI fails or network is weak.
* Constrains: The system will only work on Computers and Laptops with webcams
* The Sign-Language used will be the ameridan Sign-Lang. (ASL)
