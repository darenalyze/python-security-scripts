# 🐍 Python Security Tooling & Scripts

A modular, scalable collection of custom Python utilities developed to explore network socket communications, low-level system events, and malware mechanics from an analytical perspective.

---

## 🎯 Purpose & Scope

This repository focuses on understanding **how security tools work under the hood**:
- **Low-Level Socket Programming:** Understanding raw network handshakes, port probing, and connection handling.
- **System-Level Hooks:** Analyzing host event monitoring, logging mechanics, and local execution behaviors.
- **Analytical Defense:** Studying offensive mechanics in order to build better detection strategies and security controls.

---

## 📂 Repository Architecture & Tooling Index

I organize my tools by domain category to ensure scalability as new security utilities are added:

### 📡 Network Security (`network/`)
* **[`network/port-scanner/`](./network/port-scanner/)** — Multi-threaded port scanner for discovering active network services and probing TCP sockets.

### 👁️ Host Monitoring & Endpoint (`monitoring/`)
* **[`monitoring/keylogger/`](./monitoring/keylogger/)** — Educational keystroke event logger examining input hooks, configuration loading, and log handling mechanics.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.x
* **Core Modules:** `socket`, `threading`, `sys`, `json`, `logging`
* **Third-Party Libraries:** `pynput`

---

## ⚠️ Disclaimer

This repository is created strictly for **educational, analytical, and authorized research purposes**. All tools are intended to be executed only within isolated lab environments and target infrastructure you own or have explicit permission to test.