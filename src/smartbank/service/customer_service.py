from smartbank.domain.customer_request import CustomerRequest
from smartbank.entity.customer import Customer
from smartbank.repository import customer_repository


def find_all():
    return customer_repository.find_all()


def add(payload: CustomerRequest):
    customer = Customer(
        name=payload.name,
        phone=payload.phone,
        email=payload.email,
        bank_id=payload.bank_id,
    )
    customer_repository.save(customer)


def update_customer(customer_id: int, payload: CustomerRequest):
    customer_repository.update(
        customer_id, payload.name, payload.phone, payload.email, payload.bank_id
    )


def remove_customer(customer_id: int):
    customer_repository.delete_customer(customer_id)