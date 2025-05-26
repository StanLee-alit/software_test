#!/usr/bin/env python
from tabulate import tabulate


def coverage_circle(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        return "请输入整数"
    if x <= 0 or y <= 0:
        return "输入不符合要求"
    abs_value = abs(x - y)
    if x == y:
        return "可以构建圆形或正方形"
    elif 2 < abs_value <= 5:
        return "可以构建椭圆"
    elif abs_value > 5:
        return "可以构建矩形"
    elif 0 < abs_value <= 2:
        return "可以构建长方形"
    else:
        return "无法构建图形"


test_case = [
    {"x": 0, "y": 0, "expected": "输入不符合要求"},
    {"x": 1, "y": 1, "expected": "可以构建圆形或正方形"},
    {"x": 3, "y": 4, "expected": "可以构建长方形"},
    {"x": 6, "y": 10, "expected": "可以构建矩形"},
    {"x": 10, "y": 10, "expected": "可以构建圆形或正方形"},
    {"x": 10, "y": 12, "expected": "可以构建椭圆"},
    {"x": 10, "y": 16, "expected": "可以构建矩形"},
    {"x": 10, "y": 18, "expected": "可以构建矩形"},
    {"x": 10.5, "y": 18, "expected": "请输入整数"},
]
print("run TestCase:")
table = []
headers = ["测试用例编号", "测试输出x,y", "执行语句块"]
for i, case_item in enumerate(test_case):
    test_id = f"test{i+1}"
    x_val, y_val = case_item["x"], case_item["y"]
    actual_output = coverage_circle(x_val, y_val)
    input_str = f"{x_val} {y_val}"
    table.append([test_id, input_str, actual_output])

print(tabulate(table, headers, tablefmt="grid"))
