# 权重空间编程 · 中文博客

[Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/) 的非官方中文汉化。保留原博客的页面布局、实验图表与交互，让中文读者可以直接阅读并核对研究细节。

**[阅读中文博客](https://jian1202.github.io/weight-space-programming-cn/)** · [原文](https://rikiyat.github.io/blog/weight-space-programming/) · [原始源码](https://github.com/RikiyaT/RikiyaT.github.io/tree/master/blog/weight-space-programming)

## 内容与范围

原文探讨大语言模型直接读取、修改和编写神经网络权重的早期能力。中文版包含八项实验、Gemma 补充实验，以及游戏回放、围棋与数学实验图表、可展开的提示词和模型回答。

- 汉化正文、导航、图表说明和实验自然语言记录。
- 保留人名、模型名、基准名、原始实验代码、公式、权重和结构化实验数值。
- 保留原文中的失败结果、限制条件与不确定性，不将作者的展望改写为已实现的能力。
- 公式使用 MathJax SVG 输出，避免数学字体加载影响显示；渲染库、字体与页面资源随仓库保存。

这是独立的静态阅读站点，不包含模型训练程序或原始实验复现环境。相关日志、模型和演示仍链接至原作者发布的位置。

## 本地预览

需要 Python 3.10 或更新版本，无需安装第三方 Python 包：

```bash
git clone https://github.com/Jian1202/weight-space-programming-cn.git
cd weight-space-programming-cn
python scripts/serve.py
```

启动脚本会打开浏览器，默认使用 `http://127.0.0.1:51973/`；端口被占用时选择空闲端口。按 `Ctrl+C` 停止服务。

也可以自行启动静态服务器：

```bash
python -m http.server 8000 --bind 127.0.0.1
```

在浏览器打开 `http://127.0.0.1:8000/`。请通过 HTTP 服务访问，直接双击 HTML 无法可靠加载实验 JSON。

## 目录结构

```text
.
├── index.html                 # 中文文章与页面入口
├── assets/                    # 实验数据、图形和游戏回放
├── css/                       # 页面样式
├── js/                        # 交互图表与实验卡片
├── vendor/                    # 本地渲染库、字体及对应许可
├── scripts/                   # 本地预览与资源检查
├── docs/                      # 汉化约定与部署维护说明
├── .github/                   # 检查、部署流程及问题模板
├── CONTRIBUTING.md            # 修改与反馈约定
├── THIRD_PARTY_NOTICES.md      # 原作者、源码版本与第三方来源
└── LICENSE                    # 上游仓库许可原文
```

## 检查与部署

```bash
python scripts/check.py
```

GitHub Actions 对推送及 Pull Request 执行资源和 JavaScript 语法检查。合并到 `main` 后，自动将页面资源部署到 GitHub Pages；PR 只检查，不部署。部署产物只包含网页所需文件，不包含维护文档或本地工具。

详细配置见 [部署与维护](docs/maintenance.md)，翻译原则见 [汉化约定](docs/translation.md)。

## 来源与许可

原作者为 **Rikiya Takehi、Jayden Teoh、Alex Zhang、Omar Khattab（MIT CSAIL）**，原文发布于 **2026年11月2日**。本仓库不是作者维护的官方中文版，也不代表作者认可译文。

汉化基于原始仓库提交 `6bfa7a692f20103b5e3aea82c449fd6b14a73123`。正文逐段翻译；长篇实验记录使用机器辅助翻译并统一术语，仍可能存在译文问题。发现歧义时，应以原文及实验日志为准，欢迎按 [贡献说明](CONTRIBUTING.md) 提交修正。

上游许可原文见 [LICENSE](LICENSE)，各依赖的来源与许可见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。引用研究时请引用原作者的文章，页面末尾保留了原文引用格式。
