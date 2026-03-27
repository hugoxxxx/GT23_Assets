import os
import re

def update_readme():
    logo_dir = 'logos'
    if not os.path.exists(logo_dir):
        print("Logos directory not found.")
        return
        
    files = sorted([f for f in os.listdir(logo_dir) if f.endswith('.png')])
    brands = sorted(list(set(f.split('-')[0] for f in files)))
    
    # 1. 构建展示墙内容
    list_content = [f"\n> 自动统计：目前已收录 **{len(files)}** 款相机品牌标识\n"]
    for brand in brands:
        brand_upper = brand.upper()
        list_content.append(f"<details>\n<summary><b>{brand_upper}</b></summary>\n<div style='display:flex; flex-wrap:wrap; gap:12px; margin:12px 0;'>")
        brand_files = sorted([f for f in files if f.startswith(f"{brand}-")])
        for f in brand_files:
            model = f.replace(f"{brand}-", "").replace(".png", "")
            raw_url = f"https://raw.githubusercontent.com/hugoxuuuu/GT23_Assets/main/logos/{f}"
            list_content.append(f"  <div style='text-align:center;'><img src='{raw_url}' style='width:140px; height:50px; object-fit:contain; background:#f8f9fa; border-radius:8px; padding:8px;'><br><small style='font-size:12px; color:#666;'>{model}</small></div>")
        list_content.append("</div>\n</details>\n")

    # 2. 读取并强力替换内容
    if not os.path.exists('README.md'):
        print("README.md not found.")
        return

    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 清理所有历史乱码，精准替换占位符中间的内容
    new_list = "".join(list_content)
    content = re.sub(r'()[\s\S]*?()', 
                    f"\\1\n{new_list}\n\\2", content)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("README updated successfully.")

if __name__ == "__main__":
    update_readme()
