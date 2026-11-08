"""Explicit local server entry point; requires a migrated study database."""
import asyncio
import sys
import uvicorn

def main():
    # Compatible Python 3.11 Windows selector policy for Psycopg async I/O.
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    config = uvicorn.Config("postgres_catalog:app", host="127.0.0.1", port=8000,
                            loop="asyncio", reload=False)
    asyncio.run(uvicorn.Server(config).serve())

if __name__ == "__main__":
    main()
