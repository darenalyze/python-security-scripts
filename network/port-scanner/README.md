# Port Scanner Script

A multi-threaded Python tool designed to scan network ports and detect active services across target IP addresses.

---

## Features

* **High-Speed Scanning:** Probes ports 1 through 65,535 in ~6 seconds using concurrent execution via `ThreadPoolExecutor`.
* **WSA Error Mapping:** Decodes Windows socket return codes to accurately determine port status.
* **Thread-Safe Logging:** Utilizes `threading.Lock()` to prevent log corruption when multiple threads write simultaneously.
* **Automated File Output:** Automatically exports scan summaries to `scan_results.txt`.

---

## WSA Error Code Mapping

Special socket return codes are captured and categorized to determine port states:

| Return Code | Code Name | Port Status | Description |
| :--- | :--- | :--- | :--- |
| **0** | `SUCCESS` | **Open** | Connection established. |
| **10035** | `WSAEWOULDBLOCK` | **Closed** | No response within timeout. |
| **10061** | `WSAECONNREFUSED` | **Closed** | Connection actively refused by host. |
| **10038** | `WSAENOTSOCK` | **Error** | Invalid socket operation. |
| **10060** | `WSAETIMEDOUT` | **Timeout** | Connection attempt timed out. |
| **10013** | `WSAEACCES` | **Denied** | Permission denied by network rules/firewall. |

---

## Installation & Setup

### 1. Set Up Virtual Environment
From the repository root folder, run:

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Tool
Navigate to the directory and launch the script:

```bash
cd network/port-scanner
python main.py
```

---

## Changelog

### [v1.1.0] - 2026-06-11
* **Added:** Migrated execution model to `ThreadPoolExecutor` for concurrent scanning.
* **Added:** Implemented `threading.Lock()` to prevent race conditions during file writing.
* **Improved:** Expanded scan range from `1–1024` to `1–65535` (~6 seconds execution time).

### [v1.0.1] - 2026-06-06
* **Added:** Support for return code `10061` (`WSAECONNREFUSED`) to classify closed ports.
* **Added:** File output export targeting `scan_results.txt`.
* **Changed:** Renamed `port-scanner.py` to `main.py` for repository consistency.

### [v1.0.0] - 2026-06-03
* **Initial Release:** Core port scanning engine using standard `socket.connect_ex()`.