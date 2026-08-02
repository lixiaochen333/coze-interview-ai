# Coze AI 智能面试官机器人
基于字节Coze（扣子）平台搭建的自动化模拟面试机器人，可替代HR/技术面试官完成初轮线上面试考核。

## ✨ 项目功能
1. 输入岗位JD，自动生成对应岗位面试题目库
2. 多轮连续追问，深挖候选人项目经历与技术细节
3. 压力面试模式可选，考验临场应变能力
4. 面试结束自动生成量化评分表+完整面试评估报告
5. 支持技术岗、测试岗、运营岗、产品经理等多岗位适配

## 🛠️ 技术依赖与运行环境
- 底层平台：Coze 扣子AI 机器人平台
- 模型：豆包大模型（Coze内置）
- 附加能力：知识库检索、变量记忆、多轮对话工作流

## 📁 项目目录说明
```
coze-interview-ai/
├── config/                # 机器人配置备份
│   ├── system-prompt.md   # 核心系统提示词
│   └── workflow-note.md   # Coze工作流节点说明
├── docs/                  # 文档与案例
│   ├── demo-jd.txt        # 测试用岗位JD示例
│   └── interview-report-template.md  # 面试报告模板
├── .gitignore             # Git忽略配置
└── README.md              # 项目说明
```

## 🚀 快速部署使用步骤
1. 前往 [Coze扣子平台](https://www.coze.cn/) 登录账号
2. 新建机器人，将 `config/system-prompt.md` 内容粘贴至系统提示词
3. 按照 `config/workflow-note.md` 搭建对话工作流、配置记忆变量
4. 上传岗位JD知识库，发布机器人即可使用

## 📌 作者信息
昵称：lixiaochen333