import os

def generate_index():
    """遍历目录并生成新的index.md文件"""

    sections = {
        "personal": "个人页：",
        "org": "组织页：",
        "public": "故事页：",
        "wiki": "知识集："
    }

    base_path = "/work/story/"  # 设置文件夹路径

    with open("new.md", "w", encoding="utf-8") as new_file:
        for section, title in sections.items():
            folder_path = os.path.join(base_path, section)  # 构造完整路径
            files = [f[:-3] for f in os.listdir(folder_path) if f.endswith(".md")]
            links = [f"[{name}](/" + section + "/" + name + ")" for name in files]
            line = title + ", ".join(links) + "\n\n"
            new_file.write(line)

if __name__ == "__main__":
    generate_index()
