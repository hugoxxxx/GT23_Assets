import os
import re

def update_readme():
    logo_dir = 'logos'
    if not os.path.exists(logo_dir): return
    
    files = sorted([f for f in os.listdir(logo_dir) if f.endswith('.png')])
    brands = sorted(list(set(f.split('-')[0] for f in files)))
    
    # 1. 生成新的 Logo 列表 HTML
    list_html = [f"\n> 自动统计：目前已收录 **{len(files)}** 款相机品牌标识\n"]
    for brand in brands:
        brand_upper = brand.upper()
        list_html.append(f"<details>\n<summary><b>{brand_upper}</b></summary>\n<div style='display:flex; flex-wrap:wrap; gap:12px; margin:12px 0;'>")
        
        brand_files = sorted([f for f in files if f.startswith(f"{brand}-")])
        for f in brand_files:
            model = f.split('-', 1)[1].replace('.png', '')
            raw_url = f"https://raw.githubusercontent.com/hugoxxxx/GT23_Assets/main/logos/{f}"
            list_html.append(f"  <div style='text-align:center;'><img src='{raw_url}' style='width:140px; height:50px; object-fit:contain; background:#f8f9fa; border-radius:8px; padding:8px;'><br><small style='font-size:12px; color:#666;'>{model}</small></div>")
        
        list_html.append("</div>\n</details>\n")
    
    new_logo_list = "".join(list_html)

    # 2. 读取 README 并执行“清空式”替换
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 使用 re.DOTALL 让 . 匹配换行符
    # 这里的关键是 [\s\S]*? 它会抓取 START 和 END 之间所有的乱码并替换掉
    content = re.sub(
        r'[\s\S]*?',
        f'\n{new_logo_list}\n',
        content
    )

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()
