# Coze智能面试官 工作流配置记录



## 项目概述

本项目基于 Coze 扣子工作流搭建面试 AI 助手，包含 4 套独立工作流，分别实现岗位信息查询、简历解析、面试题生成、面试问答功能。

所有工作流均为「开始节点 → 业务节点 → 结束节点」最简线性流程，输出统一返回字符串 output。



## 工作流清单

1. search\_job：岗位信息查询
2. jianlifenixi：简历解析
3. mianshitisc：面试题生成
4. mianshijieda：面试问答



1. ##### search\_job 工作流

**功能**：根据岗位名称、城市、公司名称，调用get\_job节点获取岗位结构化数据

**节点链路**：开始触发器 → get\_job节点 → 结束节点

**输入参数（开始节点）**

|参数名|类型|说明|
|-|-|-|
|jobName|str|岗位名称|
|city|str|目标城市|
|companyName|str|公司名称|
|education|str|最高学历|
|salaryMin|str|最低薪资|
|workExperience|str|工作经验|

**get\_job 节点**

* 输入：jobName、city、companyName、education、salaryMin、workExperience
* 输出：struct\_data、type\_for\_model、code、data、log\_id、msg、status\_code

**结束节点**

* 输入：get\_job.struct\_data
* 输出变量：output



##### 2\. jianlifenixi 工作流

**功能**：上传简历文件 + 岗位名称，调用大模型解析简历内容

**节点链路**：开始触发器 → 大模型节点 → 结束节点

**输入参数（开始节点）**

|参数名|类型|说明|
|-|-|-|
|file|str|简历文件内容 / 文件引用|
|jobName|str|目标岗位名称|

**大模型节点配置**

* 模型：豆包・1.8・深度思考
* 输入：file、jobName
* 输出：output、reasoning\_content
* 技能：未配置技能

**结束节点**

* 输入：大模型节点output
* 输出变量：output



##### 3\. mianshitisc 工作流

**功能**：根据简历信息、岗位名称、工作经验，生成面试试题

**节点链路**：开始触发器 → 大模型节点 → 结束节点

**输入参数（开始节点）**

|参数名|类型|说明|
|-|-|-|
|input|str|简历 / 候选人相关输入文本|
|jobName|str|目标岗位名称|
|workExperience|str|工作经验信息|

**大模型节点配置**

* &#x20;模型：豆包・1.8・深度思考
* &#x20;输入：input、jobName、workExperience
* &#x20;输出：output、reasoning\_content
* &#x20;技能：未配置技能

**结束节点**

* 输入：大模型节点output
* 输出变量：output



##### 4\. mianshijieguofx 工作流

**功能**：对面试内容进行打分，并做出分析和改进建议

**节点链路**：开始触发器 → 大模型节点 → 结束节点

**输入参数（开始节点）**

|参数名|类型|说明|
|-|-|-|
|question|str|面试问题及答案|
|jobName|str|目标岗位名称|

**大模型节点配置**

* 模型：豆包・1.8・深度思考
* 输入：question、jobName
* 输出：output、reasoning\_content
* 技能：未配置技能

**结束节点**

* 输入：大模型节点output
* 输出变量：output



#### 接口调用统一约定（供后端 Python 对接参考）

1. 所有工作流调用方式：Coze 工作流 API
2. 入参：严格传递对应工作流「开始节点」定义参数
3. 返回读取：取工作流返回结果中的 output 字段
4. 异常提醒：调用鉴权依赖 Coze PAT 令牌，令牌失效会返回4100 authentication is invalid

























