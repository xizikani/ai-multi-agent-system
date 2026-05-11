# AI Multi-Agent Code Generation System

## 项目简介
本项目实现了一个基于多 Agent 协作范式的自动化代码生成系统，能够根据用户输入的自然语言需求，完成从需求分析到代码生成再到代码审查的完整开发闭环。

系统通过拆分不同职责的智能体，解决了传统单一大模型在复杂开发任务中存在的规划能力弱、上下文易混乱以及缺乏自检机制的问题。

---

## 核心能力
- 自动需求拆解（Requirement Analysis）
- 系统架构设计（Architecture Design）
- 代码生成（Code Generation）
- 代码审查与优化（Code Review）
- 多轮迭代优化（Feedback Loop）

---

## 系统架构

系统包含四个核心 Agent：

1. **Requirement Agent**
   - 将用户需求进行结构化拆解
   - 提取功能点与任务列表

2. **Architecture Agent**
   - 输出系统整体架构设计
   - 定义模块划分与工程结构

3. **Code Agent**
   - 根据架构生成代码
   - 自动生成接口与基础逻辑

4. **Review Agent**
   - 进行静态代码检查
   - 发现问题并触发优化

---

## 核心设计

### 多 Agent 协作机制
各 Agent 之间通过 JSON 进行状态传递：

```json
{
  "requirement": "...",
  "analysis": {},
  "architecture": {},
  "code": {},
  "review": {}
}
```
