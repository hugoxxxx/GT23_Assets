import os
import re

def update_readme():
    logo_dir = 'logos'
    # 1. 扫描文件
    if not os.path.exists(logo_dir): return
    files = sorted([f for f in os.listdir(logo_dir) if f.endswith('.png')])
    
    # 2. 生成新内容
    list_content = [f"\n> 自动统计：目前已收录 **{len(files)}** 款相机品牌标识\n"]
    # ... (生成 HTML 的逻辑保持不变) ...
    new_logo_list = "".join(list_content)

    # 3. 读取 README
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 4. 【核心修复】精准替换逻辑
    # 使用 re.DOTALL 确保点号匹配换行符
    # 使用 [\s\S]*? (非贪婪匹配) 确保只替换两个标记中间的内容，而不是整个文件
    log_pattern = r"()[\s\S]*?()"
    list_pattern = r"()[\s\S]*?()"
    
    # 替换内容（保留占位符标签本身）
    content = re.sub(log_pattern, r"\1\n\2", content) # 暂时清空日志或按需填入
    content = re.sub(list_pattern, f"\\1\n{new_logo_list}\n\\2", content)

    # 5. 安全写入
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()
