# Python 笔记

这份仓库整理了我在北京大学 **Python 程序设计与数据科学导论** 课程中的学习笔记。课程由 **胡俊峰** 老师讲授，修读时间为2023 年春季学期。

主要内容保存在 [笔记.ipynb](笔记.ipynb)。可以直接在 GitHub 上预览，也可以下载后使用 Jupyter Notebook 或 JupyterLab 阅读和运行代码。

## 笔记内容

1. **Python 基础**：基础数据类型、循环与分支、序列类型。
2. **函数与函数式编程**：函数、闭包、装饰器、高阶函数。
3. **文件、模块与面向对象编程**：文件操作、模块、类与继承；另涉及对象拷贝、引用及设计模式。
4. **文本处理**：正则表达式与中文分词。
5. **并发与网络编程**：进程、线程、协程、Socket。
6. **pandas 数据分析**：Series、DataFrame、MultiIndex、merge、groupby，以及索引与数据聚合。
7. **NumPy 数组计算**：ndarray、数组运算与广播、通用函数（ufunc）、矩阵和向量乘法、索引与切片、线性代数、聚合函数，以及数组文件的保存与读取。

## 阅读方式

点击 [笔记.ipynb](笔记.ipynb) 即可在线浏览。若要运行示例，请在本地打开笔记，并根据所运行的章节安装相应的 Python 第三方库。

## 环境

- Python 3.9
- Jupyter Notebook / JupyterLab
- 主要依赖：
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `jieba`
  - `wordcloud`
  - `xlrd` / `xlwt`
  - `beautifulsoup4`
  - `requests`
  - `tqdm`
  - `Pillow`

安装依赖：

```bash
pip install numpy pandas matplotlib jieba wordcloud xlrd xlwt beautifulsoup4 requests tqdm Pillow
```

安装完成后，在仓库目录运行 `jupyter notebook`，打开 `笔记.ipynb` 即可。

## 致谢

感谢北京大学胡俊峰老师在本课程中的精彩讲授。

## License

本仓库是个人课程学习笔记，仅供学习交流使用；如有疏漏，欢迎提出建议。如需转载请注明出处。
