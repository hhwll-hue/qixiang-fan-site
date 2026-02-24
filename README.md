# 统一代码仓库（Monorepo）

## 目录结构（约定）
- `site/`：Hugo 静态站（产品展示、内容页、前端模板）
- `api/`：询价/筛选/报价 API（FastAPI，占位骨架，后续扩展业务逻辑）
- `deploy/`：部署与运维
  - `deploy/caddy/Caddyfile`：Caddy 反代配置（/api → api，其它 → site）
  - `deploy/scripts/`：脚本（备份/迁移/运维）

## 一键启动（本地验证）
1. 复制环境变量模板：
   - `cp .env.example .env`（Git Bash）
   - 或 `copy .env.example .env`（CMD）
2. 启动：
   - `docker compose up -d --build`
3. 验证：
   - 首页：`http://localhost/`
   - API 健康检查：`http://localhost/api/health`

## 上线提示（后续再做）
- 生产环境建议把 `site` 改为 `hugo build` 输出静态文件，再由 Caddy `file_server` 提供服务。
- `SITE_ADDRESS` 改为你的域名，开放安全组 80/443，填写 `ACME_EMAIL` 以自动签发证书。
