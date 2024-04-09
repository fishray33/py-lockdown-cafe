from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor have to be vaccinated")
        if visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError("Visitor have to be vaccinated")
        if "wearing_a_mask" not in visitor:
            raise NotWearingMaskError("Visitor should buy masks")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Visitor should buy masks")

        return f"Welcome to {self.name}"