import csv

# 1. 创造一份带“坑”的测试数据
with open("test_orders.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["订单号", "金额"])  # 表头
    writer.writerow(["101", "150.5"])    # 正常
    writer.writerow(["102", "200"])      # 正常
    writer.writerow(["103", "两百块"])    # 脏数据：无法转数字
    writer.writerow(["104", "-50"])      # 脏数据：负数无效

print("✅ CSV文件生成成功！请点开看看里面的内容。")
print("\n开始读取数据...")

# 2. 读取文件
total_money = 0  # 准备一个口袋，用来装总金额

print("\n开始清洗并统计...")

with open("test_orders.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            # 尝试转换数字
            money_float = float(row["金额"])

            # 虽然转成数字了，但如果是负数也不要（业务逻辑）
            if money_float < 0:
                print(f"⚠️ 发现负数金额，跳过：{row}")
                continue  # 跳过本次循环，直接看下一行

            # 如果没有报错，也不是负数，就加进口袋里
            total_money = total_money + money_float

        except ValueError:
            # 如果转换失败（比如遇到“两百块”），程序会跳到这里，而不是崩溃
            print(f"❌ 发现异常数据，跳过：{row}")

print(f"\n🎉 统计完毕！有效总金额为: {total_money} 元")