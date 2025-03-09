from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from modules.base import BaseModel
from modules.categories.domain.entities import CategoryEntity
from modules.categories.domain.value_objects import Title

if TYPE_CHECKING:
    from modules.transactions.infra.orms import Transaction, Budget


class Category(BaseModel):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)

    transactions: Mapped[list["Transaction"]] = relationship(back_populates="category")
    budgets: Mapped[list["Budget"]] = relationship(back_populates="category")

    def to_entity(self):
        return CategoryEntity(
            id=self.id,
            title=Title(self.title),
        )

    def __str__(self):
        return f"Category(id={self.id}, title={self.title})"

    def __repr__(self):
        return f"Category(id={self.id}, title='{self.title}')"
