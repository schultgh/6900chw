$ErrorActionPreference = "Stop"

Write-Host "[1/3] Installing dependencies..."
python -m pip install --upgrade pip pyinstaller

Write-Host "[2/3] Building exam_reminder.exe ..."
pyinstaller --clean --onefile --name exam_reminder exam_reminder.py

Write-Host "[3/3] Packaging zip ..."
New-Item -ItemType Directory -Force -Path release | Out-Null
Copy-Item dist/exam_reminder.exe release/
Copy-Item README.md release/
Copy-Item exam_reminder_project.md release/
Compress-Archive -Path release/* -DestinationPath release/exam-reminder-windows.zip -Force

Write-Host "Done: release/exam-reminder-windows.zip"
