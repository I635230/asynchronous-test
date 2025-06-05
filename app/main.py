import os
from dotenv import load_dotenv
import asyncio
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok"}

async def start_fastapi():
    config = uvicorn.Config(app=app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()

async def dummy_log():
    print("bot起動ログ想定")
    while True:
        await asyncio.sleep(10)

async def main():
    load_dotenv()
    
    try:
        # 個別にタスクを作成して並列実行させる
        tasks = [
            asyncio.create_task(start_fastapi()),
            asyncio.create_task(dummy_log()),
        ]
        await asyncio.gather(*tasks)
    except Exception as e:
        print(f"起動中にエラーが発生しました: {e}")

if __name__ == "__main__":
    asyncio.run(main())