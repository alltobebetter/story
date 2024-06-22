# Story / 我们的故事书

## 前言

**文字是有力量的，我一直这么认为。**

如果你第一次来这里，你可以阅读[README](/README.md)，并且向本项目贡献您自己的故事，无论是小说，您的个人介绍，你的组织您都可以编辑。我不能说这是一个维基，但是我在尽力把它变成维基。

如果您不是第一次来这里，您可以继续阅读。

此网站的建设单纯基于机器的遍历构建。

个人页：[alepha](/personal/alepha), [su](/personal/su), [哎呦喂](/personal/哎呦喂)

组织页：[hcbbs](/org/hcbbs)

故事页：[关于Googol](/public/关于Googol), [聊天室历史书](/public/聊天室历史书), [阿瓦岛记](/public/阿瓦岛记)

知识集：[Notems总览](/wiki/Notems总览),[hackchat总览](/wiki/hackchat总览), [trip](/wiki/trip)

您可以在这里提交您自己的故事！

注：以下是README内容，您可以不访问README而阅读内容。

## 设立原因

如果您了解我，您一定知道我是Hcbbs的创始人之一，我认为，一个社区的团结在于一个社区的历史，在这里，我希望任何人都可以将自己的故事来写到这里来，您可以启用Fork分支来提交您的更改。我希望任何人可以享受到自己的快乐，在网络上有一席之地。我确实希望每个人都有它独特的编辑方式的。

## 实现

我根据GithubPages以及渲染原理部署了这些页面。

首先，您所见到的初始就是Github上的index.md，我将它设置成了主页。

其次，我使用了jekyll渲染Github主题。

您可以看到的是，在[根目录](https://github.com/alltobebetter/story)的文件内，有public，personal，org三个文件夹，它们分别表示杂谈，个人，组织三个栏目，您可以看到deploy.py，通过这个，我可以将首页的三个栏目实现更新和再渲染。

这就是本网站的实现方式。

## 编辑细则

> 先决条件：Github账户或者一个邮箱。
> 其次，您需要了解public，personal，org三个文件夹，它们分别表示杂谈，个人，组织三个栏目，您需要按需创建文件。

### Github账户的编辑方式：

1.在本项目的相应文件夹创建你的markdown文件，图片视频等您需要最好外链，例如创建example.md文件。

2.pull requests到本项目，当然，您也可以先Frok本项目。

3.等待1个工作日通过和渲染。

4.完成。

5.您会发现您的页面的名字在首页的显示名称为example，也就是.md前的名字。

### 邮件的编辑方式：

1.写好您的example.md文件。

2.发送给story@supage.eu.org您的文件。

3.等待一个工作日处理和渲染。

4.同上GitHub账户处理。


## 提交细则

一般来说您的md文件不限制名称，也就是说您可以用任何名称来描述您的md文件。这是再次重申。

注意，个人页面请提交到https://github.com/alltobebetter/story/tree/master/personal，也就是personal文件夹内；
组织页面提交到https://github.com/alltobebetter/story/tree/master/org；
故事与其他提交到https://github.com/alltobebetter/story/tree/master/public；
如果您有特殊需求请提交issue以讨论。

## 致谢

| 名称 | 提供细目 | 链接 |
| --- | --- | --- |
| 聊天室历史书| Hack.Chat历史书 | https://github.com/Hiyoteam/ChatroomHistoryBook |
| 苏淋（Su）| 编辑 | https://github.com/alltobebetter |
| Cuper| 域名提供者* | 暂无 |
| 404,sora,alepha,au,cmd以及我的所有朋友| 历史创作对象，精神支柱 | :) |
| JsOrg| 域名提供者** | https://js.org/ |
| Hcbbs| 引流站 | https://hcbbs.eu.org/ |
| 所有贡献者 | 仓库更新 | 链接过多 |
| Github| 空间提供 | https://github.com/ |
| jekyll| 主题提供 |https://github.com/jekyll/jekyll|

## 其他

项目遵循CC0 1.0 Universal，如有侵权请告知。
