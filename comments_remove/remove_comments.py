#!/usr/bin/env python3
import os
import re
import sys


def remove_comment_blocks(content):
    """删除包含 User: Alex 的 /** 注释块"""
    pattern = re.compile(r'/\*\*.*?\*/', re.DOTALL)

    def replacer(match):
        block = match.group()
        if "User: Alex" in block:
            return ""
        return block

    return pattern.sub(replacer, content)


def process_file(filepath):
    """处理单个文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()

        modified = remove_comment_blocks(original)

        if original != modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified)
            print(f"已修改: {filepath}")
    except UnicodeDecodeError:
        # print(f"跳过二进制文件: {filepath}")
        pass
    except Exception as e:
        print(f"处理 {filepath} 时出错: {str(e)}")


def process_directory(directory, valid_extensions, ignore_folders):
    """递归处理目录"""
    for root, dirs, files in os.walk(directory):
        # 被忽略的文件夹，就不要遍历了
        dirs[:] = [d for d in dirs if d not in ignore_folders]

        for filename in files:
            filepath = os.path.join(root, filename)

            ext = os.path.splitext(filepath)[1].lower()
            # 只处理指定扩展名的文件（如果没有填写 valid_extensions 那么就表示所有文件都需要处理）
            if len(valid_extensions) == 0 or ext in valid_extensions:
                process_file(filepath)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python remove_comments.py <目录路径>")
        sys.exit(1)

    target_dir = sys.argv[1]

    if not os.path.isdir(target_dir):
        print(f"错误: {target_dir} 不是有效目录")
        sys.exit(1)

    valid_extensions = {}  # 需要处理的文件扩展名
    # ignore_folders = [".git", ".idea", "vendor", "runtime"]  # 忽略的文件夹名称列表
    ignore_folders = []

    process_directory(target_dir, valid_extensions, ignore_folders)
    print("处理完成！")
