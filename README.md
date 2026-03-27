# 考试提醒程序（Exam Reminder）

这是一个命令行版考试倒计时提醒工具。

## 你在哪里可以找到这个程序

程序主文件在仓库根目录：

- `exam_reminder.py`（可直接运行）
- `exam_reminder_project.md`（项目设计说明）

如果你当前就在本仓库目录 `/workspace/6900chw`，完整路径就是：

- `/workspace/6900chw/exam_reminder.py`

## 如何使用（有 Python）

> 先确保你的环境有 Python 3。

### 1) 查看帮助

```bash
python3 exam_reminder.py --help
```

### 2) 添加一门考试

```bash
python3 exam_reminder.py add --name "高等数学期末" --date 2026-06-20 --remind-before 14
```

参数说明：
- `--name`：考试名称
- `--date`：开考日期，格式 `YYYY-MM-DD`
- `--remind-before`：提前多少天提醒（默认 7 天）

### 3) 查看所有考试与剩余天数

```bash
python3 exam_reminder.py list
```

### 4) 查看今天需要提醒的考试

```bash
python3 exam_reminder.py remind
```

## 我没有安装 Python，怎么下载可执行程序？

本仓库已提供 GitHub Actions 打包流程：

- 工作流文件：`.github/workflows/build-executable.yml`
- 支持平台：Windows / macOS / Linux

下载步骤：
1. 在 GitHub 仓库页面打开 **Actions**。
2. 选择 **Build Exam Reminder Executables**。
3. 点击 **Run workflow** 运行一次（或推送 `v*` tag 自动触发）。
4. 运行结束后在该次任务页面的 **Artifacts** 下载：
   - `exam-reminder-windows`（含 `exam_reminder.exe`）
   - `exam-reminder-macos`
   - `exam-reminder-linux`

> 这样你不用安装 Python，也可以直接运行打包后的程序。

## 为什么你在 GitHub 看不到我这里改的代码（同步问题）

最常见原因是“本地提交没有推到你的远端仓库”。

请在你的本地仓库执行：

```bash
git remote -v
git branch --show-current
git log --oneline -n 5
git push origin <你的分支名>
```

排查建议：
- `git remote -v` 没有输出：说明没配置远端。
- 推送到错误分支：检查当前分支与 GitHub 页面分支是否一致。
- 权限失败：检查 GitHub Token/SSH Key 是否有效。

## 数据保存位置

程序会在当前运行目录生成 `exams.json` 文件，用来保存你添加的考试数据。

- 例如在仓库根目录运行时，文件会是：`/workspace/6900chw/exams.json`

## 常见问题

### Q1: 为什么提示“暂无考试数据”？
你还没执行 `add` 添加考试，先添加至少一门即可。

### Q2: 为什么 `remind` 没有输出考试？
说明当前日期不在“提前提醒天数”窗口内，或考试已经结束。

### Q3: 日期怎么填？
必须是 `YYYY-MM-DD`，例如：`2026-12-20`。
