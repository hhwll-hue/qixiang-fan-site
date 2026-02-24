from fastapi import FastAPI

# 询价/筛选/报价 API（占位骨架）
# 后续你可以把：产品数据读取、筛选逻辑、报价规则、表单入库等加到这里
app = FastAPI(title="Quote API")

@app.get("/health")
def health():
    # 健康检查：用于部署后快速判断服务是否正常
    return {"ok": True}

@app.post("/quote")
def quote(payload: dict):
    # 询价接口（占位）：后续接你的筛选/报价逻辑
    return {
        "received": payload,
        "quote": {"currency": "CNY", "amount": 0}
    }
