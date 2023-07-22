# ChoiceMaster

ChoiceMaster是一个帮助你做决策的机器人。 并且致力于提供积极向上的正向引导。

有时很小的选择也会耗费我们大量的能量，借用工具来减少在选择上消耗的心力和时间吧。

## 如何使用

### 1. 直接 @choicemasterbot

可以直接在 Telegram App 中使用 @choicemasterbot 与机器人交互。跟随指示，输入您的选择和选项，ChoiceMaster 将为您提供决策的建议。

### 2. 本地运行

将项目克隆到本地，并运行 ChoiceMaster。

```bash
$ git clone https://github.com/hotjuicew/ChoiceMaster-telegram-bot.git
$ cd ChoiceMaster-telegram-bot pip install -r requirements.txt python main.py
$ API_TOKEN ="<your_token>" python main.py
```

### 3.使用 Docker

可以通过以下命令拉取镜像并运行 ChoiceMaster：

```bash
$ docker pull ghcr.io/hotjuicew/choicemaster-telegram-bot:latest
$ docker run -e API_TOKEN=<your_token> choicemaster-telegram-bot
```

## 如何贡献

如果发现任何问题，或者有任何改进建议，请随时提交 Issue 或 Pull Request。欢迎你的贡献，帮助 ChoiceMaster 变得更加完善！