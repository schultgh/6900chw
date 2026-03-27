#!/usr/bin/env python3
"""考试倒计时提醒程序（命令行版）

功能：
1) 维护考试清单（名称 + 开考日期 + 提前提醒天数）
2) 计算距离开考还有多少天
3) 在命令行展示“今天需要提醒”的考试
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from datetime import date, datetime
from pathlib import Path
from typing import List

DATA_FILE = Path("exams.json")


@dataclass
class Exam:
    name: str
    exam_date: str  # YYYY-MM-DD
    remind_before_days: int = 7

    def days_left(self, today: date | None = None) -> int:
        today = today or date.today()
        d = datetime.strptime(self.exam_date, "%Y-%m-%d").date()
        return (d - today).days

    def should_remind(self, today: date | None = None) -> bool:
        left = self.days_left(today)
        return 0 <= left <= self.remind_before_days


class ExamStore:
    def __init__(self, file_path: Path = DATA_FILE) -> None:
        self.file_path = file_path

    def load(self) -> List[Exam]:
        if not self.file_path.exists():
            return []
        raw = json.loads(self.file_path.read_text(encoding="utf-8"))
        return [Exam(**item) for item in raw]

    def save(self, exams: List[Exam]) -> None:
        payload = [asdict(e) for e in exams]
        self.file_path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


def add_exam(args: argparse.Namespace) -> None:
    store = ExamStore()
    exams = store.load()
    exams.append(
        Exam(
            name=args.name,
            exam_date=args.date,
            remind_before_days=args.remind_before,
        )
    )
    store.save(exams)
    print(f"已添加考试：{args.name}（{args.date}）")


def list_exams(_: argparse.Namespace) -> None:
    store = ExamStore()
    exams = store.load()

    if not exams:
        print("暂无考试数据。先使用 add 命令添加。")
        return

    print("考试清单：")
    for i, ex in enumerate(exams, 1):
        left = ex.days_left()
        if left > 0:
            status = f"还有 {left} 天"
        elif left == 0:
            status = "今天开考"
        else:
            status = f"已结束 {-left} 天"
        print(f"{i}. {ex.name} | {ex.exam_date} | 提前 {ex.remind_before_days} 天提醒 | {status}")


def remind(_: argparse.Namespace) -> None:
    store = ExamStore()
    exams = store.load()

    due = [ex for ex in exams if ex.should_remind()]
    if not due:
        print("今天没有需要提醒的考试。")
        return

    print("今日提醒：")
    for ex in due:
        left = ex.days_left()
        label = "今天开考" if left == 0 else f"还有 {left} 天开考"
        print(f"- {ex.name}（{ex.exam_date}）{label}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="考试倒计时提醒程序")
    sub = parser.add_subparsers(dest="command", required=False)

    p_add = sub.add_parser("add", help="添加考试")
    p_add.add_argument("--name", required=True, help="考试名称")
    p_add.add_argument("--date", required=True, help="开考日期，格式 YYYY-MM-DD")
    p_add.add_argument("--remind-before", type=int, default=7, help="提前多少天提醒")
    p_add.set_defaults(func=add_exam)

    p_list = sub.add_parser("list", help="查看考试清单")
    p_list.set_defaults(func=list_exams)

    p_remind = sub.add_parser("remind", help="查看今天需要提醒的考试")
    p_remind.set_defaults(func=remind)

    return parser


def interactive_mode() -> None:
    print("欢迎使用考试提醒程序（交互模式）")
    print("提示：直接回车可取消当前输入。")

    while True:
        print("\n请选择操作：")
        print("1) 添加考试")
        print("2) 查看考试清单")
        print("3) 查看今日提醒")
        print("0) 退出")
        choice = input("输入编号: ").strip()

        if choice == "1":
            name = input("考试名称: ").strip()
            if not name:
                print("已取消添加。")
                continue
            exam_date = input("开考日期(YYYY-MM-DD): ").strip()
            if not exam_date:
                print("已取消添加。")
                continue
            remind_before = input("提前提醒天数(默认7): ").strip() or "7"
            try:
                args = argparse.Namespace(
                    name=name,
                    date=exam_date,
                    remind_before=int(remind_before),
                )
                add_exam(args)
            except ValueError:
                print("输入格式错误：提前提醒天数必须是整数。")
        elif choice == "2":
            list_exams(argparse.Namespace())
        elif choice == "3":
            remind(argparse.Namespace())
        elif choice == "0":
            print("已退出。")
            return
        else:
            print("无效选项，请输入 0/1/2/3。")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if not getattr(args, "command", None):
        interactive_mode()
        return
    args.func(args)


if __name__ == "__main__":
    main()
