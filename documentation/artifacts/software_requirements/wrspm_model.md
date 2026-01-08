# Requirements and Specification Using the **WRSPM**-Model

**World Requirments Specification Program Machine**

### World

* We assume the users are literate (can read and write)
* The device used has a working camera and display
* We assume there is stable Internet (WLAN or Hotspot)
* There is a domain available

## Requirements

### Functional Requirements

* The system must allow users to register or sign to access an account
* The system must provide real‑time text‑based communication between users.
* The system must support video‑based communication for sign‑language conversations.
* The system must include an AI‑assisted *sign‑language* recognition feature to translate sign language into written text.
* The system must include an AI‑assisted *text‑to‑sign‑language* **avatar** for deaf users who prefer sign‑language output.
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
* Constrains:
  * The system will only work on Computers and Laptops with webcams
  * The Sign-Language used will be the American-Sign-Language. (ASL)
  * Fallback to pure text if video/AI fails or network is weak.

## Program

* Programing language used:
  * Code:
    * (backend) Python
    * (frontend) HTML/CSS/JS
* IDE: Visual Studio Code
* Versionsystem control: Git / GitHub

## Machine

* Hardware:
  * Developer: HP 660 G11 with 32 GB RAM & 1 TB SSD Intel Core Ultra 7
  * Developer:
* Server:
