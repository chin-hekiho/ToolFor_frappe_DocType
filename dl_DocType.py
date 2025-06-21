#在 bench console 中直接执行以下代码：

# 确保初始化
site = "frappe-stg.bti-web.com"  
frappe.init(site)
frappe.connect()

try:
    # 检查DocType是否存在
    if not frappe.db.exists("DocType", "MCS_TD_CustomerBalanceSnapshot"):
        print("❌ 错误: MCS_TD_CustomerBalanceSnapshot DocType 不存在")
    else:
        # 获取字段数据
        fields = frappe.get_doc("DocType", "MCS_TD_CustomerBalanceSnapshot").fields
        
        # 打印前5个字段测试（避免控制台刷屏）
        print(f"✅ 找到 {len(fields)} 个字段，前5个字段示例：")
        for field in fields[:5]:
            print(f"""
            ラベル: {field.fieldname}
            タイプ: {field.fieldtype}
            名前: {field.label or '无'}
            必須: {'是' if field.reqd else '否'}
			オプション: {field.options}
            """)
            
        # 返回全部字段数据（可通过变量获取）
        all_fields = [field.__dict__ for field in fields]
        print(f"ℹ️ 完整数据已保存到变量 `all_fields` 中")
        
finally:
    frappe.destroy()
    print("⏹️ 连接已关闭")


#Turn to markdown
markdown = "| ラベル |　タイプ | 名前 |　必填 |　オプション \n|-------|------|------|\n"
for field in all_fields[:19]:  # 前10个字段
    markdown += f"| {field['fieldname']} | {field['fieldtype']} {field['label']} | {field['fieldtype']} | {'✔' if field['reqd'] else ''} | {field['options']} \n"

print(markdown)