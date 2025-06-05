import os
from dotenv import load_dotenv
import asyncio
import uvicorn
from fastapi import FastAPI

app = FastAPI()

# FastAPI
async def start_fastapi():
    config = uvicorn.Config(app=app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()


# dummy log
async def dummy_log(): 
    print("bot起動ログ想定")

# main
async def main():
    load_dotenv()
    
    try:
        await asyncio.gather(
            start_fastapi(),
            dummy_log()
        )
    except Exception as e:
        print(f"起動中にエラーが発生しました: {e}")

if __name__ == "__main__":
    asyncio.run(main())