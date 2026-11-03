"""检查静态页面的资源引用、实验数据和离线公式入口。"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
checked = set()


def local_reference(value, base):
    parts = urlsplit(value)
    if parts.scheme or parts.netloc or not parts.path:
        return
    target = (base / unquote(parts.path)).resolve()
    if not target.is_relative_to(ROOT):
        errors.append(f'引用超出站点目录：{value}')
    elif not target.exists():
        errors.append(f'资源缺失：{target.relative_to(ROOT)}')
    checked.add(target)


class PageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        for key in ('src', 'href', 'data-src'):
            if data.get(key):
                local_reference(data[key], ROOT)


html = (ROOT / 'index.html').read_text(encoding='utf-8')
PageParser().feed(html)
if 'lang="zh-CN"' not in html:
    errors.append('页面未声明中文语言。')
if 'vendor/mathjax/es5/tex-mml-svg.js' not in html:
    errors.append('公式没有使用本地 SVG 渲染入口。')

for path in (ROOT / 'assets').rglob('*.json'):
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except (ValueError, OSError) as exc:
        errors.append(f'{path.relative_to(ROOT)}：{exc}')
        continue
    if 'traces' in path.parts:
        if not isinstance(data.get('items'), list) or not data['items']:
            errors.append(f'实验卡片缺少项目：{path.name}')
        for item in data.get('items', []):
            for field in ('gif', 'media'):
                if item.get(field):
                    local_reference(item[field], ROOT)

for path in [*(ROOT / 'css').glob('*.css'), *(ROOT / 'vendor/fonts').glob('*.css')]:
    for url in re.findall(r'url\([\"\']?([^\)\"\']+)', path.read_text(encoding='utf-8')):
        local_reference(url, path.parent)

for path in (ROOT / 'js').glob('*.js'):
    if not path.read_text(encoding='utf-8').strip():
        errors.append(f'交互脚本为空：{path.name}')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f'检查通过：{len(checked)} 项本地资源引用、实验 JSON 与 SVG 公式入口。')
