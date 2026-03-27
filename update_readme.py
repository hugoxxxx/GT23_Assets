import os
import re

def generate_readme():
    # 1. 统计品牌和生成列表
    logo_dir = 'logos'
    if not os.path.exists(logo_dir):
        return
        
    files = [f for f in os.listdir(logo_dir) if f.endswith('.png')]
    brands = sorted(list(set(f.split('-')[0] for f in files)))
    
    list_content = [f"## 🖼️ Logo 列表\n\n> 自动统计：目前已收录 **{len(files)}** 款相机品牌标识\n"]
    
    for brand in brands:
        brand_upper = brand.upper()
        list_content.append(f"<details>\n<summary><b>{brand_upper}</b></summary>\n<div style='display:flex; flex-wrap:wrap; gap:12px; margin:12px 0;'>")
        
        brand_files = sorted([f for f in files if f.startswith(f"{brand}-")])
        for f in brand_files:
            model = f.replace(f"{brand}-", "").replace(".png", "")
            raw_url = f"https://raw.githubusercontent.com/hugoxxxx/GT23_Assets/main/logos/{f}"
            list_content.append(f"  <div style='text-align:center;'><img src='{raw_url}' style='width:140px; height:50px; object-fit:contain; background:#f8f9fa; border-radius:8px; padding:8px;'><br><small style='font-size:12px; color:#666;'>{model}</small></div>")
        
        list_content.append("</div>\n</details>\n")

    # 2. 读取并替换 README
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 替换 Logo 列表 (使用正则非贪婪匹配清理旧内容)
    list_pattern = r"()[\s\S]*?()"
    content = re.sub(list_pattern, f"\\1\n{''.join(list_content)}\n\\2", content)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    generate_readme()
