diff --git a/lab/README.md b/lab/README.md
new file mode 100644
index 0000000000000000000000000000000000000000..ecbb49567161fe0aeb8a32550f9c0e81dfd63180
--- /dev/null
+++ b/lab/README.md
@@ -0,0 +1,43 @@
+# DFIR Lab: Suspicious Update Checker
+
+This lab provides a lightweight, self-contained case with disk, memory, and network artifacts so you can practice triage, analysis, and reporting without external data downloads.
+
+## Scenario
+
+A helpdesk ticket reports that a user "Alex" saw an update prompt and clicked a link. Shortly after, the workstation started making outbound traffic. You are asked to identify what happened, build a timeline, and propose remediation steps.
+
+## Objectives
+
+1. Validate evidence integrity using hashes.
+2. Identify initial access, execution, and persistence artifacts.
+3. Correlate disk, memory, and network evidence into a timeline.
+4. Draft an incident report with indicators of compromise (IOCs).
+
+## Quick Start
+
+1. Build (or rebuild) the case directory.
+
+   ```bash
+   python3 lab/scripts/build_case.py
+   ```
+
+2. Review evidence in `cases/case-001/evidence`. A pre-built case is checked into the repository so the lab works out of the box.
+3. Use your preferred tools (Autopsy, Sleuth Kit, Volatility, Wireshark) or manual analysis to answer the investigation questions below.
+
+## Investigation Questions
+
+- Which process initiated the suspicious outbound connections?
+- What file or script was written to establish persistence?
+- Which IP addresses and domains should be added to block lists?
+- What user actions preceded the execution of the malicious chain?
+
+## Reporting Deliverables
+
+- A short incident summary (2-3 paragraphs).
+- A timeline of key events.
+- IOCs (hashes, IPs, domains, filenames).
+- Recommendations for containment and remediation.
+
+## Notes
+
+The artifacts in this lab are synthetic and intended for training only.
