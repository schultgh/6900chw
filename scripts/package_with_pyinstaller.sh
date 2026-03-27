#!/usr/bin/env bash
set -euo pipefail

# Local packaging helper (requires pyinstaller)
# Usage: bash scripts/package_with_pyinstaller.sh

if ! command -v pyinstaller >/dev/null 2>&1; then
  echo "pyinstaller 未安装。请先执行: python3 -m pip install pyinstaller"
  exit 1
fi

pyinstaller --onefile --name exam_reminder exam_reminder.py
mkdir -p release
cp dist/exam_reminder release/
cp README.md exam_reminder_project.md release/

tar -C release -czf release/exam-reminder-linux.tar.gz exam_reminder README.md exam_reminder_project.md
echo "打包完成: release/exam-reminder-linux.tar.gz"
