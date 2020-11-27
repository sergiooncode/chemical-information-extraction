from dataclasses import dataclass
from datetime import datetime


@dataclass
class Metadata:
    def __init__(
        self,
        year: int,
        application_document_number: str,
        application_country: str,
        application_kind: str,
        application_date: datetime,
    ):
        self.__year = year
        self.__application_document_number = application_document_number
        self.__application_country = application_country
        self.__application_kind = application_kind
        self.__application_date = application_date

    @property
    def year(self) -> int:
        return self.__year

    @property
    def title(self) -> str:
        return self.__title

    @property
    def application_document_number(self) -> str:
        return self.__application_document_number

    @property
    def application_country(self) -> str:
        return self.__application_country

    @property
    def application_kind(self) -> str:
        return self.__application_kind

    @property
    def application_date(self) -> datetime:
        return self.__application_date

    @title.setter
    def title(self, value):
        self.__title = value

    def __repr__(self):
        return (
            f"<Metadata(title={self.__title}, year={self.__year},"
            f"application_document_number={self.__application_document_number},"
            f"application_country={self.__application_country}, "
            f"application_kind={self.__application_kind},"
            f"application_date={self.__application_date})>"
        )
