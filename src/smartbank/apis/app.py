from fastapi import FastAPI

from smartbank.apis import account_api, bank_api, customer_api, branch_api, department_api

app = FastAPI(title="Smart Bank API")

app.include_router(account_api.router)
app.include_router(bank_api.router)
app.include_router(customer_api.router)
app.include_router(branch_api.router)
app.include_router(department_api.router)