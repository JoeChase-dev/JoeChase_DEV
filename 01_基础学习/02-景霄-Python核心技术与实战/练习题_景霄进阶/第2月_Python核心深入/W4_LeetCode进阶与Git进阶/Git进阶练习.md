# 💻 W4 Git进阶实战练习

> **目标**：通过实际操作掌握Git分支、合并、Rebase等进阶操作
> **建议**：在本地创建一个测试仓库，跟着步骤实际操作
> **时长**：60-90分钟

---

## 📋 练习清单

| 序号 | 练习项目 | 掌握技能 | 预计用时 |
|------|---------|---------|---------|
| 1 | 基础分支操作 | branch, checkout/switch, merge | 10min |
| 2 | 冲突模拟与解决 | 手动解决冲突 | 15min |
| 3 | Rebase基础 | rebase, rebase -i | 15min |
| 4 | Stash暂存 | stash, stash pop/apply | 10min |
| 5 | 远程协作模拟 | remote, push, pull, pull --rebase | 15min |
| 6 | 标签与版本管理 | tag, push tags | 10min |
| 7 | .gitignore配置 | 忽略文件配置 | 5min |

---

## 💻 练习1：基础分支操作（10min）

### 目标
掌握分支的创建、切换、合并、删除。

### 步骤
```bash
# 1. 创建测试目录并初始化Git仓库
mkdir git-practice && cd git-practice
git init

# 2. 创建初始文件并提交
echo "print('Hello')" > main.py
git add main.py
git commit -m "Initial commit"

# 3. 创建并切换到新分支 feature/add-function
git checkout -b feature/add-function
# 或（现代Git）：git switch -c feature/add-function

# 4. 在新分支上修改文件
echo "def add(a, b): return a + b" >> main.py
git add main.py
git commit -m "Add add function"

# 5. 切换回main分支
git checkout main

# 6. 合并 feature/add-function 到 main
git merge feature/add-function

# 7. 删除已合并的分支
git branch -d feature/add-function

# 8. 查看分支历史
git log --oneline --graph --all
```

### ✅ 验收标准
- [ ] 成功创建并合并分支
- [ ] 理解 `git log --graph` 的输出
- [ ] 能解释 `git merge` 创建了什么

---

## 💻 练习2：冲突模拟与解决（15min）

### 目标
学会手动解决Git合并冲突。

### 步骤
```bash
# 1. 在main分支创建文件
echo "version 1" > conflict.txt
git add conflict.txt
git commit -m "Add conflict.txt (main)"

# 2. 创建并切换到feature分支
git checkout -b feature/conflict

# 3. 在feature分支修改同一文件
echo "version 2 (feature)" > conflict.txt
git add conflict.txt
git commit -m "Update conflict.txt (feature)"

# 4. 切换回main分支
git checkout main

# 5. 在main分支也修改同一文件（制造冲突）
echo "version 2 (main)" > conflict.txt
git add conflict.txt
git commit -m "Update conflict.txt (main)"

# 6. 尝试合并feature分支（会产生冲突！）
git merge feature/conflict
# Git提示：CONFLICT (content): Merge conflict in conflict.txt

# 7. 查看冲突内容
cat conflict.txt
# 输出：
# <<<<<<< HEAD
# version 2 (main)
# =======
# version 2 (feature)
# >>>>>>> feature/conflict

# 8. 手动解决冲突（编辑文件，保留想要的内容）
echo "version 2 (merged from both)" > conflict.txt

# 9. 标记为已解决并完成合并
git add conflict.txt
git commit -m "Resolve conflict in conflict.txt"

# 10. 查看合并后的历史
git log --oneline --graph --all
```

### ✅ 验收标准
- [ ] 能模拟出冲突场景
- [ ] 能看懂冲突标记（`<<<<<<<`, `=======`, `>>>>>>>>`）
- [ ] 能手动解决冲突并完成合并

---

## 💻 练习3：Rebase基础（15min）

### 目标
理解rebase的作用，并学会使用交互式rebase整理提交。

### 步骤
```bash
# 1. 创建并切换到feature分支
git checkout -b feature/rebase-demo

# 2. 做几次提交
echo "line1" > demo.txt
git add demo.txt
git commit -m "Add demo.txt with line1"

echo "line2" >> demo.txt
git add demo.txt
git commit -m "Add line2"

echo "line3" >> demo.txt
git add demo.txt
git commit -m "Add line3"

# 3. 切换回main分支，做新的提交（模拟main有新提交）
git checkout main
echo "main line" > main_only.txt
git add main_only.txt
git commit -m "Add main_only.txt on main"

# 4. 切换回feature分支，执行rebase
git checkout feature/rebase-demo
git rebase main

# 5. 查看rebase后的历史（应该是线性的）
git log --oneline --graph

# 6. 交互式rebase：合并提交
git rebase -i HEAD~3
# 在编辑器中，将后两个提交的 pick 改为 squash (或 s)
# 保存后，Git会让你编辑合并后的提交信息

# 7. 强制推送（如果已经push过）
git push origin feature/rebase-demo --force-with-lease
```

### ✅ 验收标准
- [ ] 理解rebase和merge的区别
- [ ] 能使用 `git rebase main` 同步main的更新
- [ ] 能使用 `git rebase -i` 整理提交历史

---

## 💻 练习4：Stash暂存（10min）

### 目标
学会使用stash临时保存工作区修改。

### 步骤
```bash
# 1. 在main分支修改文件（不提交）
echo "work in progress" >> main.py

# 2. 需要切换分支，但修改还没完成，使用stash
git stash
# 或带备注：git stash save "work in progress on main.py"

# 3. 确认工作区干净
git status

# 4. 切换分支做其他工作
git checkout -b hotfix
echo "hotfix" > hotfix.txt
git add hotfix.txt
git commit -m "Add hotfix"

# 5. 切换回main分支
git checkout main

# 6. 恢复stash的修改
git stash pop
# 或（不删除stash）：git stash apply

# 7. 查看stash列表
git stash list

# 8. 如果有多个stash，恢复指定的stash
git stash pop stash@{1}
```

### ✅ 验收标准
- [ ] 能使用 `git stash` 暂存修改
- [ ] 能使用 `git stash pop/apply` 恢复修改
- [ ] 理解 `pop` 和 `apply` 的区别

---

## 💻 练习5：远程协作模拟（15min）

### 目标
模拟团队协作的Git工作流（Fork + Pull Request）。

### 步骤（需要GitHub账号）
```bash
# 1. 在GitHub上创建一个测试仓库（或使用现有仓库）

# 2. 克隆仓库到本地
git clone https://github.com/YOUR_USERNAME/test-repo.git
cd test-repo

# 3. 创建新分支
git checkout -b feature/test

# 4. 修改文件并提交
echo "test content" > test.txt
git add test.txt
git commit -m "Add test.txt"

# 5. 推送到远程
git push -u origin feature/test

# 6. 在GitHub上创建Pull Request
# （手动操作：进入仓库页面 → "Compare & pull request"）

# 7. 模拟代码审查后的修改
echo "updated content" > test.txt
git add test.txt
git commit -m "Update test.txt based on review"
git push origin feature/test

# 8. 合并PR后，本地同步
git checkout main
git pull origin main

# 9. 删除远程分支（PR合并后）
git push origin --delete feature/test
```

### ✅ 验收标准
- [ ] 能完成Fork + Clone + Branch + Push + PR的完整流程
- [ ] 理解 `git pull` = `git fetch` + `git merge`
- [ ] 能使用 `git pull --rebase` 保持历史整洁

---

## 💻 练习6：标签与版本管理（10min）

### 目标
学会使用Git标签管理版本。

### 步骤
```bash
# 1. 查看当前提交
git log --oneline

# 2. 创建轻量标签
git tag v0.1.0

# 3. 创建带注释的标签（推荐）
git tag -a v0.2.0 -m "Release version 0.2.0"

# 4. 查看所有标签
git tag

# 5. 查看标签详情
git show v0.2.0

# 6. 推送标签到远程
git push origin v0.2.0
# 或推送所有标签：git push origin --tags

# 7. 删除标签
git tag -d v0.1.0                 # 删除本地标签
git push origin :refs/tags/v0.1.0  # 删除远程标签

# 8. 根据标签创建分支（常用于hotfix）
git checkout -b hotfix/v0.2.1 v0.2.0
```

### ✅ 验收标准
- [ ] 能创建轻量标签和带注释的标签
- [ ] 能推送标签到远程
- [ ] 能根据标签创建分支

---

## 💻 练习7：.gitignore配置（5min）

### 目标
学会配置 `.gitignore` 忽略不需要追踪的文件。

### 步骤
```bash
# 1. 创建 .gitignore 文件
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python/
env/
venv/

# IDE
.vscode/
.idea/
*.swp
*.swo

# 系统文件
.DS_Store
Thumbs.db

# 环境变量
.env
.env.local

# 日志
*.log
EOF

# 2. 查看忽略规则是否生效
git status

# 3. 强制添加被忽略的文件（如果需要）
# git add -f some_file.pyc

# 4. 检查某个文件为什么被忽略
git check-ignore -v <file>
```

### ✅ 验收标准
- [ ] 能编写 `.gitignore` 文件
- [ ] 理解常见忽略规则（Python、IDE、系统文件）
- [ ] 能使用 `git check-ignore` 调试忽略规则

---

## 📊 练习总结

| 练习 | 完成度 | 掌握程度（1-5） | 备注 |
|------|--------|-----------------|------|
| 1. 基础分支操作 | ⬜ | ___ | |
| 2. 冲突解决 | ⬜ | ___ | |
| 3. Rebase基础 | ⬜ | ___ | |
| 4. Stash暂存 | ⬜ | ___ | |
| 5. 远程协作 | ⬜ | ___ | |
| 6. 标签管理 | ⬜ | ___ | |
| 7. .gitignore | ⬜ | ___ | |

> ⬜ 未完成 | 🟦 进行中 | ✅ 已完成

---

## 💡 Git进阶技巧

### 1. 美化Git Log
```bash
# 设置别名（一劳永逸）
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# 使用：git lg
```

### 2. 撤销操作速查表
| 场景 | 命令 | 说明 |
|------|------|------|
| 撤销工作区修改 | `git checkout -- <file>` | 危险！不可恢复 |
| 撤销暂存区 | `git reset HEAD <file>` | 文件保留在工作区 |
| 修改最近一次提交 | `git commit --amend` | 不修改内容，只改信息 |
| 撤销提交（保留修改） | `git reset --soft HEAD~1` | 修改回到暂存区 |
| 撤销提交（不保留） | `git reset --hard HEAD~1` | ⚠️ 危险！ |

### 3. 分支管理最佳实践
- ✅ 功能分支从 `main` 创建
- ✅ 分支命名规范：`feature/xxx`, `bugfix/xxx`, `hotfix/xxx`
- ✅ 及时删除已合并的分支
- ✅ 提交前先 `git pull --rebase`
- ❌ 不要对公共分支执行 `rebase`

---

*📅 创建日期: 2026年5月6日*  
*⏰ 建议：每周花30分钟复习Git命令*  
*💪 目标：Git操作形成肌肉记忆*
