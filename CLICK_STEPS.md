# GitHub 点哪里清单（让 Build Exam Reminder Executables 出现并下载 EXE）

> 适用你当前仓库：默认分支是 `main`，开发分支是 `codex`。

## A. 先把 workflow 合并到 main

1. 顶部点击 **Pull requests**。
2. 找到分支为 **codex -> main** 的 PR。
3. 点进 PR 后，点击 **Merge pull request**。
4. 再点击 **Confirm merge**。
5. 回到 **Code** 页面，左上分支下拉切换到 **main**。

## B. 在 Actions 里找到工作流

1. 顶部点击 **Actions**。
2. 左侧列表应该出现 **Build Exam Reminder Executables**。
3. 点击它进入工作流详情。

> 如果仍未出现：按 `Ctrl/Cmd + Shift + R` 强制刷新页面一次。

## C. 手动运行打包

1. 在工作流页面右上点击 **Run workflow**。
2. Branch 选择 **main**。
3. 点击绿色按钮 **Run workflow**。
4. 等待任务结束（约 2~8 分钟）。

## D. 下载 Windows EXE

1. 点击最新一次运行记录。
2. 下拉到页面底部 **Artifacts** 区域。
3. 点击 **exam-reminder-windows** 下载 zip。
4. 解压后得到 `exam_reminder.exe`。
5. 在 Windows 双击运行，或在终端运行：

```powershell
.\exam_reminder.exe --help
```

## E. 你最关心的一键路径（30 秒版）

**Pull requests → Merge codex 到 main → Actions → Build Exam Reminder Executables → Run workflow → Artifacts 下载 exam-reminder-windows**
