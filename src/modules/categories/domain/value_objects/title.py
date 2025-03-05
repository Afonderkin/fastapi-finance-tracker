from dataclasses import dataclass


@dataclass
class Title:
    title: str

    def __post_init__(self) -> None:
        self._validate_title(self.title)

    @staticmethod
    def _validate_title(title) -> None:
        if not title:
            raise ValueError("Title cannot be empty")
        if not title.isalpha():
            raise ValueError("Title must only contain alphabetic characters")
        if len(title) > 100:
            raise ValueError("Title cannot exceed 100 characters")
