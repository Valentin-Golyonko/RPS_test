from fastapi import FastAPI

app = FastAPI()


@app.get("/fa_sync_dummy_foo")
def sync_dummy_foo():
    return {"message": "fa_sync_dummy_foo"}


@app.get("/fa_async_dummy_foo")
async def async_dummy_foo():
    return {"message": "fa_async_dummy_foo"}
