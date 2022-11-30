# README

## step0

首先你需要在$\textbf{novel\_search}$文件夹解压缩$\textbf{static}$与$\textbf{utils}$目录（位置不变）

## step1

配置django环境，已经修改settings.py中数据库default值

## step2

终端运行python manage.py runserver

## utils文件介绍

```python
--Novels  小说储存
-- fanqie.ipynb 爬取小说并对摘要建立倒排索引
-- chapter_search.ipynb 对小说的章节建立倒排索引
-- load_invert_index.py供系统部署使用
```

