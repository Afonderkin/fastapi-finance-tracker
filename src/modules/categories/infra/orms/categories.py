from sqlalchemy.orm import Mapped, mapped_column

from modules.base import BaseModel
from modules.categories.domain.entities import CategoryEntity
from modules.categories.domain.value_objects import Title


class Category(BaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)

    def to_entity(self):
        return CategoryEntity(
            id=self.id,
            title=Title(self.title),
        )

    @classmethod
    def from_entity(cls, entity: CategoryEntity) -> CategoryEntity:
        return cls(
            id=entity.id,
            title=entity.title.value,
        )
