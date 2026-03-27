# 考试提醒程序项目设计（可直接落地）

## 1. 项目目标
做一个“输入考试日期后，自动计算距离开考还有多少天，并按规则提醒”的小型项目。

核心价值：
- 学生能看到每门考试的剩余天数。
- 可以在“提前 N 天”收到提醒，避免错过复习节奏。
- 支持多门考试管理。

## 2. MVP（最小可用版本）

### 必做功能
1. 新增考试：考试名称、开考日期、提醒提前天数。
2. 查看清单：显示每门考试距离开考还有多少天。
3. 今日提醒：显示“今天应该提醒”的考试。
4. 本地持久化：将数据保存到 `exams.json`。

### 可选增强功能
- 每天固定时间自动提醒（系统计划任务 + 脚本）。
- 邮件/企业微信/钉钉通知。
- 支持导入 iCal/课程表。

## 3. 技术方案

### 方案 A（推荐新手）
- 语言：Python 3
- 交互：命令行（CLI）
- 存储：JSON 文件

优点：
- 开发快，依赖少。
- 易于理解“日期计算 + 任务提醒”的核心逻辑。

### 方案 B（进阶）
- 前端：Vue/React
- 后端：FastAPI/Node.js
- 存储：SQLite/PostgreSQL
- 通知：消息推送服务

## 4. 数据模型

```json
{
  "name": "研究生入学考试",
  "exam_date": "2026-12-20",
  "remind_before_days": 30
}
```

字段说明：
- `name`：考试名称
- `exam_date`：开考日期，格式 `YYYY-MM-DD`
- `remind_before_days`：提前提醒天数

## 5. 关键逻辑

### 剩余天数
`days_left = (exam_date - today).days`

### 提醒条件
当 `0 <= days_left <= remind_before_days` 时，触发提醒。

## 6. 项目结构建议

```text
exam-reminder/
├─ exam_reminder.py        # 主程序（CLI）
├─ exams.json              # 本地数据文件（运行后生成）
└─ exam_reminder_project.md
```

## 7. 运行方式

```bash
# 添加考试
python3 exam_reminder.py add --name "高等数学期末" --date 2026-06-20 --remind-before 14

# 查看清单
python3 exam_reminder.py list

# 查看今天提醒
python3 exam_reminder.py remind
```

## 8. 验收标准
- 能新增至少 2 门考试。
- `list` 命令能显示每门考试剩余天数。
- `remind` 命令能正确过滤“今天应该提醒”的考试。
- 数据重启后不丢失。

## 9. 迭代路线图
1. **v1**：CLI + JSON（当前版本）
2. **v2**：Web 页面 + SQLite
3. **v3**：消息推送 + 账号体系 + 多端同步
