diff --git a/lab/scripts/build_case.py b/lab/scripts/build_case.py
new file mode 100644
index 0000000000000000000000000000000000000000..d602cfcd6e040cea77de3d116c8264feb8276761
--- /dev/null
+++ b/lab/scripts/build_case.py
@@ -0,0 +1,89 @@
+#!/usr/bin/env python3
+"""Build a ready-to-use lab case directory with evidence and hashes."""
+from __future__ import annotations
+
+import csv
+import hashlib
+from datetime import datetime, timezone
+from pathlib import Path
+import shutil
+
+ROOT = Path(__file__).resolve().parents[2]
+EVIDENCE_SRC = ROOT / "lab" / "evidence"
+CASE_DIR = ROOT / "cases" / "case-001"
+EVIDENCE_DST = CASE_DIR / "evidence"
+REPORTS_DIR = CASE_DIR / "reports"
+HASHES_PATH = CASE_DIR / "hashes.csv"
+TIMELINE_PATH = CASE_DIR / "timeline.csv"
+
+
+def sha256sum(path: Path) -> str:
+    hasher = hashlib.sha256()
+    with path.open("rb") as handle:
+        for chunk in iter(lambda: handle.read(8192), b""):
+            hasher.update(chunk)
+    return hasher.hexdigest()
+
+
+def build_case() -> None:
+    if CASE_DIR.exists():
+        shutil.rmtree(CASE_DIR)
+
+    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
+    shutil.copytree(EVIDENCE_SRC, EVIDENCE_DST)
+
+    hashes = []
+    for artifact in sorted(EVIDENCE_DST.rglob("*")):
+        if artifact.is_file():
+            rel_path = artifact.relative_to(CASE_DIR)
+            hashes.append((str(rel_path), sha256sum(artifact)))
+
+    with HASHES_PATH.open("w", newline="") as handle:
+        writer = csv.writer(handle)
+        writer.writerow(["path", "sha256"])
+        writer.writerows(hashes)
+
+    timeline_rows = [
+        (
+            "2024-09-17T08:12:14Z",
+            "AUTH_SUCCESS",
+            "alex authenticated from 10.0.5.23",
+        ),
+        (
+            "2024-09-17T08:18:10Z",
+            "WEB_DOWNLOAD",
+            "alex visited update-checker.example download page",
+        ),
+        (
+            "2024-09-17T08:18:40Z",
+            "PROCESS_START",
+            "update_checker.exe launched by outlook.exe",
+        ),
+        (
+            "2024-09-17T08:21:55Z",
+            "FILE_WRITE",
+            "sync.ps1 written to AppData\\Roaming",
+        ),
+        (
+            "2024-09-17T08:21:59Z",
+            "EXFIL",
+            "powershell.exe posted data to 203.0.113.77",
+        ),
+    ]
+
+    with TIMELINE_PATH.open("w", newline="") as handle:
+        writer = csv.writer(handle)
+        writer.writerow(["timestamp", "event", "details"])
+        writer.writerows(timeline_rows)
+
+    summary_path = REPORTS_DIR / "case_summary.txt"
+    with summary_path.open("w") as handle:
+        now = datetime.now(timezone.utc).isoformat()
+        handle.write("Case: Suspicious Update Checker\n")
+        handle.write(f"Generated: {now}\n")
+        handle.write("Artifacts stored in evidence/\n")
+
+
+if __name__ == "__main__":
+    build_case()
+    print(f"Case created at {CASE_DIR}")
