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


## 直接拿 Windows 的 EXE（推荐）

你可以不装 Python，直接下载 `exam_reminder.exe`：

1. 打开仓库的 **Actions**。
2. 进入 **Build Exam Reminder Executables**。
3. 点击 **Run workflow** 并等待完成。
4. 在 Artifacts 下载 `exam-reminder-windows` 压缩包。
5. 解压后即可得到 `exam_reminder.exe`，双击或命令行运行都可以。

如果你想在 Windows 本地自行打包，也可以执行：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/build_windows_exe.ps1
```

打包结果：`release/exam-reminder-windows.zip`。

## 双击 EXE 提示 `the following arguments are required: command` 怎么办？

这是旧版本行为（需要命令行参数 `add/list/remind`）。  
新版本已支持 **无参数进入交互模式**，双击后会出现菜单：

- `1` 添加考试
- `2` 查看考试清单
- `3` 查看今日提醒
- `0` 退出

如果你仍看到该报错，请重新下载最新构建产物（Artifacts 里的 `exam-reminder-windows`）。


### 如果 Actions 里看不到 `Build Exam Reminder Executables`


> 你截图里的关键点：仓库默认分支是 `main`，你当前查看的是 `codex` 分支。
> GitHub Actions 左侧工作流列表默认按“默认分支中的 workflow 文件”显示，
> 所以如果 `build-executable.yml` 只在 `codex` 分支，还没合并到 `main`，就只会看到 `Auto Update Worker`。

### 按你当前仓库的正确操作（最短路径）

1. 打开 `Pull requests`，把 `codex -> main` 的 PR 合并。
2. 合并后切回 `main` 分支刷新 Actions 页面。
3. 这时会出现 **Build Exam Reminder Executables**。
4. 点进该工作流后，点击 **Run workflow**。
5. 完成后到 Artifacts 下载 Windows 的 `exam-reminder-windows`（里面有 `.exe`）。

通常是下面几种原因：

1. 这个工作流文件还没在 **默认分支**（main/master）上。
2. 仓库的 **Actions 被禁用**（Settings -> Actions）。
3. 你在 Fork 仓库里，未开启 Workflow 权限。

快速处理：

```bash
# 1) 确认 workflow 文件在当前分支
ls .github/workflows/build-executable.yml

# 2) 推送到默认分支（main 或 master）
git push origin main
# 或
# git push origin master
```

然后刷新 GitHub 的 Actions 页面即可看到。

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
