
![douyin-downloader](https://socialify.git.ci/jiji262/douyin-downloader/image?custom_description=%E6%8A%96%E9%9F%B3%E6%89%B9%E9%87%8F%E4%B8%8B%E8%BD%BD%E5%B7%A5%E5%85%B7%EF%BC%8C%E5%8E%BB%E6%B0%B4%E5%8D%B0%EF%BC%8C%E6%94%AF%E6%8C%81%E8%A7%86%E9%A2%91%E3%80%81%E5%9B%BE%E9%9B%86%E3%80%81%E5%90%88%E9%9B%86%E3%80%81%E9%9F%B3%E4%B9%90%28%E5%8E%9F%E5%A3%B0%29%E3%80%82%0A%E5%85%8D%E8%B4%B9%EF%BC%81%E5%85%8D%E8%B4%B9%EF%BC%81%E5%85%8D%E8%B4%B9%EF%BC%81&description=1&font=Jost&forks=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2Fjiji262%2Fdouyin-downloader%2Frefs%2Fheads%2Fmain%2Fimg%2Flogo.png&name=1&owner=1&pattern=Circuit+Board&pulls=1&stargazers=1&theme=Light)

<a href="https://trendshift.io/repositories/13156" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13156" alt="jiji262%2Fdouyin-downloader | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

一个功能强大的抖音内容批量下载工具，支持视频、图集、音乐、直播等多种内容类型的下载。基于最新抖音API实现，提供命令行和配置文件两种使用方式。

## ✨ 核心特性

### 🎯 **全面的内容支持**
- **视频下载**：支持去水印高清视频下载
- **图集下载**：批量下载图片集合
- **音乐下载**：提取视频背景音乐
- **封面&头像**：下载视频封面和作者头像
- **元数据保存**：保存完整的作品信息（JSON格式）

### 🚀 **强大的下载能力**
- **多线程并发**：支持多线程同时下载，提升效率
- **断点续传**：网络中断后自动从断点继续下载
- **智能重试**：网络错误时自动重试，采用指数退避策略
- **去重处理**：自动跳过已下载内容，避免重复下载

### 🎛️ **灵活的配置选项**
- **多种下载模式**：支持单个作品、用户主页、合集、音乐集合
- **时间范围过滤**：可按时间范围筛选下载内容
- **数量限制**：可设置每种类型的下载数量上限
- **增量更新**：支持增量下载，只下载新增内容

### 🔧 **便捷的使用方式**
- **配置文件模式**：通过YAML配置文件批量管理下载任务
- **命令行模式**：支持命令行参数快速下载
- **数据库支持**：可选择使用数据库记录下载历史

## 🚀 快速开始

### 📦 环境要求

- **Python 3.9+**
- **操作系统**：Windows、macOS、Linux

### 🛠️ 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/jiji262/douyin-downloader.git
cd douyin-downloader
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **安装Brotli压缩支持**（必需）
```bash
pip install brotli
```

4. **创建配置文件**
```bash
cp config.example.yml config.yml
```

### ⚙️ 配置说明

#### 1. 获取Cookie（重要）

Cookie是下载的关键，获取方法：

1. 打开浏览器，访问 [抖音网页版](https://www.douyin.com)
2. 登录你的抖音账号
3. 按 `F12` 打开开发者工具
4. 切换到 `Network` 标签页
5. 刷新页面，找到任意请求
6. 在请求头中找到 `Cookie` 字段
7. 复制以下关键cookie值：
   - `msToken`
   - `ttwid`
   - `odin_tt`
   - `passport_csrf_token`
   - `sid_guard`

#### 2. 编辑配置文件

打开 `config.yml`，修改以下配置：

```yaml
# 下载链接（必填）
link:
  - https://www.douyin.com/user/YOUR_USER_ID  # 用户主页
  # - https://v.douyin.com/xxxxx/             # 单个视频

# 保存路径
path: ./Downloaded/

# Cookie配置（必填）
cookies:
  msToken: YOUR_MS_TOKEN_HERE
  ttwid: YOUR_TTWID_HERE
  odin_tt: YOUR_ODIN_TT_HERE
  passport_csrf_token: YOUR_PASSPORT_CSRF_TOKEN_HERE
  sid_guard: YOUR_SID_GUARD_HERE

# 下载选项
music: True    # 下载音乐
cover: True    # 下载封面
avatar: True   # 下载头像
json: True     # 保存JSON数据

# 下载模式
mode:
  - post       # 下载发布的作品
  # - like     # 下载喜欢的作品
  # - mix      # 下载合集

# 下载数量（0表示全部）
number:
  post: 0      # 发布作品数量
  like: 0      # 喜欢作品数量
  allmix: 0    # 合集数量
  mix: 0       # 单个合集内作品数量

# 其他设置
thread: 5      # 下载线程数
database: True # 使用数据库记录
```

### 🎯 运行程序

#### 方式一：配置文件模式（推荐）

```bash
python DouYinCommand.py
```

#### 方式二：命令行模式

```bash
python DouYinCommand.py -C True -l "抖音链接" -p "保存路径"
```

## 📝 支持的链接类型

### 🎬 视频内容
- **单个视频分享链接**：`https://v.douyin.com/xxxxx/`
- **单个视频直链**：`https://www.douyin.com/video/xxxxx`
- **图集作品**：`https://www.douyin.com/note/xxxxx`

### 👤 用户内容
- **用户主页**：`https://www.douyin.com/user/xxxxx`
  - 支持下载用户发布的所有作品
  - 支持下载用户喜欢的作品（需要权限）

### 📚 合集内容
- **用户合集**：`https://www.douyin.com/collection/xxxxx`
- **音乐合集**：`https://www.douyin.com/music/xxxxx`

### 🔴 直播内容
- **直播间**：`https://live.douyin.com/xxxxx`

## 💡 使用示例

### 示例1：下载单个视频

```bash
# 使用配置文件
# 在config.yml中设置：
link:
  - https://v.douyin.com/iRGu2mBL/

# 运行
python DouYinCommand.py
```

```bash
# 使用命令行
python DouYinCommand.py -C True -l "https://v.douyin.com/iRGu2mBL/"
```

### 示例2：下载用户主页作品

```bash
# 下载用户发布的前10个作品
python DouYinCommand.py -C True \
  -l "https://www.douyin.com/user/MS4wLjABAAAAxxxxx" \
  -M post \
  -n 10
```

### 示例3：下载用户合集

```bash
# 配置文件模式
# config.yml设置：
link:
  - https://www.douyin.com/user/MS4wLjABAAAAxxxxx
mode:
  - mix
number:
  allmix: 5  # 下载5个合集
  mix: 0     # 每个合集下载全部作品
```

### 示例4：批量下载多个链接

```bash
# 命令行批量下载
python DouYinCommand.py -C True \
  -l "https://v.douyin.com/xxxxx/" \
  -l "https://v.douyin.com/yyyyy/" \
  -l "https://www.douyin.com/user/zzzzz" \
  -p "./downloads"
```

### 示例5：增量更新下载

```yaml
# config.yml配置增量下载
increase:
  post: True    # 开启发布作品增量下载
  mix: True     # 开启合集增量下载

# 只会下载上次下载后新增的内容
```

## 🎛️ 高级配置

### 时间范围过滤

```yaml
# 只下载指定时间范围内的作品
start_time: "2024-01-01"  # 开始时间
end_time: "2024-12-31"    # 结束时间
```

### 文件夹结构设置

```yaml
folderstyle: True   # 每个视频单独文件夹
# True结构：
# user_xxx/
#   ├── post/
#   │   ├── 2024-01-01_视频标题1/
#   │   │   ├── 2024-01-01_视频标题1.mp4
#   │   │   ├── 2024-01-01_视频标题1_cover.jpeg
#   │   │   └── 2024-01-01_视频标题1_result.json
#   │   └── 2024-01-02_视频标题2/
#   └── mix/

folderstyle: False  # 所有文件放在同一目录
# False结构：
# user_xxx/
#   ├── post/
#   │   ├── 2024-01-01_视频标题1.mp4
#   │   ├── 2024-01-01_视频标题1_cover.jpeg
#   │   ├── 2024-01-02_视频标题2.mp4
#   │   └── 2024-01-02_视频标题2_cover.jpeg
#   └── mix/
```

### Cookie配置方式

```yaml
# 方式1：键值对形式（推荐）
cookies:
  msToken: YOUR_MS_TOKEN
  ttwid: YOUR_TTWID
  odin_tt: YOUR_ODIN_TT
  passport_csrf_token: YOUR_CSRF_TOKEN
  sid_guard: YOUR_SID_GUARD

# 方式2：字符串形式
# cookie: "msToken=xxx; ttwid=xxx; odin_tt=xxx; passport_csrf_token=xxx; sid_guard=xxx;"
```

## 使用截图

![DouYinCommand1](img/DouYinCommand1.png)
![DouYinCommand2](img/DouYinCommand2.png)
![DouYinCommand download](img/DouYinCommanddownload.jpg)
![DouYinCommand download detail](img/DouYinCommanddownloaddetail.jpg)

## 🛠️ 命令行参数详解

### 基础参数
```bash
-C, --cmd              启用命令行模式
-l, --link            下载链接（可多次使用）
-p, --path            保存路径
-t, --thread          线程数（默认5）
-h, --help            显示帮助信息
```

### 下载选项
```bash
-m, --music           下载音乐（True/False，默认True）
-c, --cover           下载封面（True/False，默认True）
-a, --avatar          下载头像（True/False，默认True）
-j, --json            保存JSON数据（True/False，默认True）
-f, --folderstyle     文件夹结构（True/False，默认True）
```

### 模式和数量
```bash
-M, --mode            下载模式（post/like/mix/music）
-n, --number          下载数量限制
-I, --increase        增量下载（True/False）
```

### 时间过滤
```bash
-s, --start           开始时间（YYYY-MM-DD）
-e, --end             结束时间（YYYY-MM-DD）
```

### 完整命令示例

```bash
# 下载用户主页前20个作品，包含音乐和封面
python DouYinCommand.py -C True \
  -l "https://www.douyin.com/user/xxxxx" \
  -p "./downloads" \
  -M post \
  -n 20 \
  -m True \
  -c True \
  -t 3
```

## ⚠️ 常见问题

### Q1: 下载失败，提示"list index out of range"
**A:** 这通常是数据格式问题，最新版本已修复。请确保：
- 使用最新版本代码
- Cookie信息正确且未过期
- 网络连接稳定

### Q2: 无法下载某些用户的喜欢列表
**A:** 这是正常现象，因为：
- 用户可能设置了喜欢列表为私有
- 需要登录且有权限才能访问
- 建议改用下载用户发布的作品

### Q3: 下载速度很慢或经常中断
**A:** 建议：
- 减少线程数（设置为2-3）
- 检查网络连接稳定性
- 程序支持断点续传，中断后重新运行即可继续

### Q4: Cookie如何获取？
**A:** 详细步骤：
1. 浏览器打开 https://www.douyin.com
2. 登录账号
3. F12打开开发者工具
4. Network标签页，刷新页面
5. 找到任意请求，查看Request Headers
6. 复制Cookie中的关键字段

### Q5: 支持哪些视频格式？
**A:**
- 视频：MP4格式，去水印高清
- 图片：JPEG格式
- 音频：MP3格式
- 数据：JSON格式

## 📋 注意事项

### ⚖️ 法律声明
- 本项目仅供**学习交流**使用
- 请遵守相关法律法规和平台服务条款
- 不得用于商业用途或侵犯他人权益
- 下载内容请尊重原作者版权

### 🔧 技术要求
- Python 3.9或更高版本
- 稳定的网络连接
- 足够的存储空间
- 有效的抖音账号Cookie

### 💡 使用建议
- 首次使用建议先下载少量内容测试
- 合理设置线程数，避免对服务器造成压力
- 定期更新Cookie信息
- 及时更新程序版本以获得最佳体验

## 🔄 更新日志

### v2024.12 最新更新
- ✅ 修复了"list index out of range"错误
- ✅ 改进了网络连接中断的处理
- ✅ 增强了断点续传功能
- ✅ 添加了Brotli压缩支持
- ✅ 优化了错误提示信息
- ✅ 更新了API参数以适应最新接口

### 主要功能状态
- ✅ 用户主页下载：完全正常
- ✅ 合集下载：完全正常
- ⚠️ 喜欢列表下载：取决于用户隐私设置
- ⚠️ 单个视频下载：部分接口限制，建议通过用户主页下载

## 使用交流群

![fuye](img/fuye.jpg)

## 🤝 贡献指南

我们欢迎各种形式的贡献！

### 🐛 报告问题
- 使用 [Issues](https://github.com/jiji262/douyin-downloader/issues) 报告bug
- 请提供详细的错误信息和复现步骤
- 包含你的系统环境和Python版本

### 💡 功能建议
- 在Issues中提出新功能建议
- 详细描述功能需求和使用场景

### 🔧 代码贡献
1. Fork 本项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

### 📖 文档改进
- 改进README文档
- 添加使用示例
- 翻译文档到其他语言

## 📊 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jiji262/douyin-downloader&type=Date)](https://star-history.com/#jiji262/douyin-downloader&Date)

## 🙏 致谢

### 开源项目
- [TikTokDownload](https://github.com/Johnserf-Seed/TikTokDownload) - 提供了宝贵的参考
- [Rich](https://github.com/Textualize/rich) - 美观的终端输出
- [Requests](https://github.com/psf/requests) - HTTP请求库

### 技术支持
- 本项目在开发过程中使用了AI辅助编程
- 感谢所有提交Issue和PR的贡献者
- 感谢社区用户的反馈和建议

### 特别感谢
- 所有Star和Fork本项目的用户
- 在交流群中提供帮助的热心用户
- 为项目推广做出贡献的朋友们

## 📜 许可证

本项目采用 [MIT License](LICENSE) 开源许可证。

```
MIT License

Copyright (c) 2024 jiji262

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

**如果这个项目对你有帮助，请给个 ⭐ Star 支持一下！**

[🐛 报告问题](https://github.com/jiji262/douyin-downloader/issues) • [💡 功能建议](https://github.com/jiji262/douyin-downloader/issues) • [📖 查看文档](https://github.com/jiji262/douyin-downloader/wiki)

Made with ❤️ by [jiji262](https://github.com/jiji262)

</div>

