# Port Scanner

A multi-threaded Python tool designed to scan network ports and detect active services across target IP addresses.

## Features
* **Full Range Scanning:** Capable of probing ports 1 through 65,535 in ~6 seconds using multi-threaded execution.
* **WSA Error Handling:** Mapped Windows socket return codes (e.g., 10035, 10061) to differentiate open, closed, and timed-out ports.
* **Thread-Safe Logging:** Uses thread locks to safely record scan results directly to a local log file.
* **File Output:** Exports all scan summaries directly to scan_results.txt.

### WSA Error Code Mapping
Special socket return codes are captured and categorized to determine port status:

| Return Code | Code Name | Port Status |
| :--- | :--- | :--- |
| 0 | SUCCESS | Open |
| 10035 | WSAEWOULDBLOCK | Closed (No response within timeout) |
| 10061 | WSAECONNREFUSED | Closed (Actively refused by host) |
| 10038 | WSAENOTSOCK | Error (Invalid socket state) |
| 10060 | WSAETIMEDOUT | Timeout |
| 10013 | WSAEACCES | Permission Denied |

---

## Installation & Usage

1. **Navigate to the directory:**
  ```bash
    cd network/port-scanner
  ```
2. **Run the script:**
  ```bash
    python main.py
  ```
---

## Update Changelog
- 6/11/2026 — Multi-Threading Performance Upgrade
  -  
  - Migrated from sequential single-thread scanning to ThreadPoolExecutor for concurrent port checks.
  - Added threading.Lock() to prevent race conditions when appending thread results.
  - Expanded scan range from 1–1024 to 1–65535.
  - Improved speed benchmark to scan all 65,535 ports in ~6 seconds.

- 6/06/2026 — WSA Handling & File Export
  - 
  - Added support for return code 10061 (WSAECONNREFUSED) as an explicit closed state.
  - Added scan_results.txt file output instead of terminal-only printing.
  - Renamed port-scanner.py to main.py.

- 6/03/2026 — Initial Implementation
  - 
  - Built initial scanner using Python's standard socket library with socket.connect_ex().