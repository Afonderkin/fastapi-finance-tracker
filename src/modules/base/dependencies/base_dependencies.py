from typing import Tuple, Optional

from fastapi import Query


def pagination_and_sort_params(
    page: int = Query(1, description="Номер страницы", ge=1),
    size: int = Query(10, description="Количество элементов на странице", ge=1, le=10),
    sort_by: Optional[str] = Query(None, description="Поле для сортировки"),
    sort_order: Optional[str] = Query(None, description="Порядок сортировки (asc или desc)"),
) -> Tuple[int, int, int, Optional[str], Optional[str]]:
    offset = (page - 1) * size
    return page, offset, size, sort_by, sort_order
