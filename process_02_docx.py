"""
处理02.docx文件，生成规范篇的Jupyter Notebook
包含4个主题：
1. 编程规范
2. 上下文管理器
3. 单元测试
4. pdb & cProfile调试和性能分析
"""

from docx import Document
import json
import re

def read_docx(file_path):
    """读取docx文件并返回段落列表"""
    doc = Document(file_path)
    content = []
    for para in doc.paragraphs:
        if para.text.strip():
            content.append(para.text.strip())
    return content

def split_content_by_topic(content):
    """根据内容结构分割成4个主题"""
    topics = {
        "编程规范": [],
        "上下文管理器": [],
        "单元测试": [],
        "pdb和cProfile": []
    }
    
    current_topic = None
    
    for line in content:
        # 检测主题切换
        if "编程规范" in line or "PEP 8" in line or "Google Style" in line:
            if current_topic != "编程规范":
                current_topic = "编程规范"
        elif "上下文管理器" in line or "__enter__" in line or "with 语句" in line:
            if current_topic != "上下文管理器":
                current_topic = "上下文管理器"
        elif "单元测试" in line or "unittest" in line or "mock" in line:
            if current_topic != "单元测试":
                current_topic = "单元测试"
        elif "pdb" in line or "cProfile" in line or "调试" in line:
            if current_topic != "pdb和cProfile":
                current_topic = "pdb和cProfile"
        
        if current_topic and line not in topics[current_topic]:
            topics[current_topic].append(line)
    
    return topics

def create_notebook(title, content_lines):
    """根据内容创建Jupyter Notebook结构"""
    cells = []
    
    # 添加标题
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"# {title}\n",
            "\n",
            "## 学习目标\n",
            "\n",
            "- 理解本课的核心概念\n",
            "- 掌握实际应用技巧\n",
            "- 能够独立完成练习题目\n"
        ]
    })
    
    # 处理内容，将相关行组合成markdown单元
    current_markdown = []
    current_code = []
    
    for line in content_lines:
        # 检测是否是代码示例
        if line.startswith("#") or line.startswith("def ") or line.startswith("class ") or "=" in line or "import " in line:
            # 保存之前的markdown
            if current_markdown:
                cells.append({
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [f"{text}\n" for text in current_markdown]
                })
                current_markdown = []
            
            # 添加代码行
            current_code.append(line)
        else:
            # 保存之前的代码
            if current_code:
                cells.append({
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [f"{code}\n" for code in current_code]
                })
                current_code = []
            
            # 添加markdown行
            current_markdown.append(line)
    
    # 保存最后的内容
    if current_markdown:
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"{text}\n" for text in current_markdown]
        })
    if current_code:
        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [f"{code}\n" for code in current_code]
        })
    
    # 添加练习题目
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 练习与自测\n",
            "\n",
            "### 练习题1\n",
            "\n",
            "**题目**：请根据本课内容，编写一个示例代码。\n",
            "\n",
            "**参考答案**：\n",
            "```python\n",
            "# 示例代码\n",
            "print('Hello, World!')\n",
            "```\n"
        ]
    })
    
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 练习题2\n",
            "\n",
            "**题目**：请解释本课的一个核心概念。\n",
            "\n",
            "**参考答案**：\n",
            "请根据实际学习内容填写。\n"
        ]
    })
    
    # 创建notebook结构
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    return notebook

def main():
    # 读取docx文件
    content = read_docx("D:/Desktop/02/02.docx")
    print(f"成功读取文档，共 {len(content)} 个段落")
    
    # 分割内容
    topics = split_content_by_topic(content)
    
    # 生成每个主题的notebook
    output_dir = "F:/JoeChase/01_基础学习/02-景霄-Python核心技术与实战/01_Python核心技术与实战/02_规范篇"
    
    topic_files = {
        "编程规范": "01_Python编程规范.ipynb",
        "上下文管理器": "02_上下文管理器.ipynb",
        "单元测试": "03_单元测试.ipynb",
        "pdb和cProfile": "04_pdb和cProfile.ipynb"
    }
    
    for topic_name, filename in topic_files.items():
        if topic_name in topics and topics[topic_name]:
            notebook = create_notebook(topic_name, topics[topic_name])
            
            # 保存notebook
            import os
            os.makedirs(output_dir, exist_ok=True)
            output_path = f"{output_dir}/{filename}"
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, ensure_ascii=False, indent=2)
            
            print(f"成功生成: {output_path}")
        else:
            print(f"警告: {topic_name} 没有找到内容")
    
    print("\n所有笔记生成完成！")

if __name__ == "__main__":
    main()
