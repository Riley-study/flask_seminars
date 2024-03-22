import uvicorn
from fastapi import FastAPI

from router_items import router as router_items
from router_orders import router as router_orders
from router_users import router as router_users

app = FastAPI

app.include_router(router_users, tags=['users'])
app.include_router(router_items, tags=['items'])
app.include_router(router_orders, tags=['orders'])


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
