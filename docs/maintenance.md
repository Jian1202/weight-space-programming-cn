# 部署与维护

## GitHub Pages

仓库设置中进入 **Settings → Pages**，将发布来源设为 **GitHub Actions**。工作流文件为 `.github/workflows/pages.yml`。

- 推送到 `main`：检查文件，生成静态发布目录，部署到 Pages。
- Pull Request：仅执行检查，不发布。
- Actions 页面手动运行：重新检查并部署 `main`。
- 正式链接：https://jian1202.github.io/weight-space-programming-cn/

发布目录由 `index.html`、`assets/`、`css/`、`js/`、`vendor/` 和 `.nojekyll` 组成。许可文件也随站点发布。资源使用相对路径，支持 GitHub Pages 的项目子路径。

## 日常修改

1. 更新对应 HTML、CSS、JS 或实验 JSON。
2. 运行 `python scripts/check.py`，修改脚本时检查 JavaScript 语法。
3. 在本地服务中检查受影响的交互与公式。
4. 提交并推送，等待 Actions 中部署成功。
5. 打开线上站点，核对受影响的部分；浏览器仍使用旧资源时强制刷新。

## 同步上游

先查看上游博客目录的差异，再逐项同步。更新时记录新的上游提交，检查新增资源与第三方许可，并更新译文。不要直接用英文页面覆盖中文页面。上游仓库、原始实验日志和模型权重均不作为本仓库的子仓库或发布产物。

## 回退

对问题提交执行 `git revert <提交号>` 并推送，由 Pages 流程部署回退后的版本。不要通过改写远端历史回退线上内容。
