from typing import Annotated, Optional

from fastapi import APIRouter, Depends, status, Path, Query

from core.config import settings
from modules.transactions.domain.services import TransactionService
from modules.transactions.presentations.dependencies import get_transaction_service, get_filter_by
from modules.transactions.presentations.schemas import (TransactionResponse, TransactionCreate,
                                                        TransactionUpdate, SuccessUpdateTransactionResponse,
                                                        SuccessCreateTransactionResponse, PaginatedResponse,
                                                        TransactionFilter, )

router = APIRouter(
    prefix=settings.api.v1.transactions_prefix,
    tags=["Транзакции"],
)


@router.get(
    path="",
    response_model=PaginatedResponse,
    summary="Получение списка всех транзакций",
    description="Возвращает список всех транзакций",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Пользователь не авторизован",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Пользователь не имеет права на эту операцию",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Внутренняя ошибка сервера",
        },
    }
)
async def get_transactions(
    transaction_service: Annotated[TransactionService, Depends(get_transaction_service)],
    page: int = Query(1, description="Номер страницы", ge=1),
    size: int = Query(10, description="Количество элементов на странице", ge=1, le=10),
    sort_by: Optional[str] = Query(None, description="Поле для сортировки"),
    sort_order: Optional[str] = Query(None, description="Порядок сортировки (asc или desc)"),
    filter_by: Optional[TransactionFilter] = Depends(get_filter_by),
) -> PaginatedResponse:
    offset = (page - 1) * size

    filter_dict = filter_by.model_dump(exclude_none=True) if filter_by else {}

    transactions, total = await transaction_service.get_all(
        offset=offset,
        limit=size,
        sort_by=sort_by,
        sort_order=sort_order,
        filter_by=filter_dict,
    )
    transactions = [TransactionResponse(
        id=transaction.id,
        amount=transaction.amount,
        description=transaction.description.value,
        transaction_type=transaction.transaction_type,
        date=transaction.date,
        category_id=transaction.category_id,
    ) for transaction in transactions]
    total_pages = (total + size - 1) // size

    return PaginatedResponse(
        items=transactions,
        total=total,
        page=page,
        size=size,
        total_pages=total_pages,
    )


@router.get(
    path="/{transaction_id}",
    response_model=TransactionResponse,
    summary="Получение транзакции по ID",
    description="Возвращает информацию о транзакции по указанному ID.",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Пользователь не авторизован",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Пользователь не имеет права на эту операцию",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Транзакция по данному ID не найдена",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Внутренняя ошибка сервера",
        },
    }
)
async def get_transaction_by_id(
    transaction_service: Annotated[TransactionService, Depends(get_transaction_service)],
    transaction_id: int = Path(..., description="ID транзакции"),
) -> TransactionResponse:
    transaction = await transaction_service.get_by_id(transaction_id)
    return TransactionResponse(
        id=transaction.id,
        amount=transaction.amount,
        description=transaction.description.value,
        transaction_type=transaction.transaction_type,
        date=transaction.date,
        category_id=transaction.category_id,
    )


@router.post(
    path="",
    response_model=SuccessCreateTransactionResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Создание новой транзакции",
    description="Создает новую транзакцию.",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Пользователь не авторизован",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Пользователь не имеет права на эту операцию",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Внутренняя ошибка сервера",
        },
    }
)
async def create_transaction(
    transaction_service: Annotated[TransactionService, Depends(get_transaction_service)],
    transaction_data: TransactionCreate,
) -> SuccessCreateTransactionResponse:
    new_transaction = await transaction_service.create(
        amount=transaction_data.amount,
        description=transaction_data.description,
        transaction_type=transaction_data.transaction_type,
        date=transaction_data.date,
        category_id=transaction_data.category_id,
    )
    return SuccessCreateTransactionResponse(
        status="success",
        message="Транзакция успешно создана",
        data=TransactionResponse(
            id=new_transaction.id,
            amount=new_transaction.amount,
            description=new_transaction.description.value,
            transaction_type=new_transaction.transaction_type,
            date=new_transaction.date,
            category_id=new_transaction.category_id,
        )
    )


@router.patch(
    path="/{transaction_id}",
    response_model=SuccessUpdateTransactionResponse,
    summary="Изменение транзакции",
    description="Изменяет транзакцию по указанному ID.",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Пользователь не авторизован",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Пользователь не имеет права на эту операцию",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Транзакция по данному ID не найдена",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Внутренняя ошибка сервера",
        },
    }
)
async def update_transaction(
    transaction_service: Annotated[TransactionService, Depends(get_transaction_service)],
    transaction_data: TransactionUpdate,
    transaction_id: int = Path(..., description="ID транзакции"),
) -> SuccessUpdateTransactionResponse:
    transaction = await transaction_service.update(
        transaction_id,
        **transaction_data.model_dump(exclude_unset=True, exclude_none=True),
    )
    return SuccessUpdateTransactionResponse(
        status="success",
        message="Транзакция успешно изменена",
        data=TransactionResponse(
            id=transaction.id,
            amount=transaction.amount,
            description=transaction.description.value,
            transaction_type=transaction.transaction_type,
            date=transaction.date,
            category_id=transaction.category_id,
        )
    )


@router.delete(
    path="/{transaction_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удаление транзакции",
    description="Удаляет транзакцию по указанному ID.",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Пользователь не авторизован",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Пользователь не имеет права на эту операцию",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Транзакция по данному ID не найдена",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Внутренняя ошибка сервера",
        },
    }
)
async def delete_transaction(
    transaction_service: Annotated[TransactionService, Depends(get_transaction_service)],
    transaction_id: int = Path(..., description="ID транзакции"),
) -> None:
    await transaction_service.delete(transaction_id)
    return
