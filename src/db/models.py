from tortoise.models import Model
from tortoise.fields import CharField, DecimalField


class Cargo(Model):
    """
    The Cargo model
    """

    cargo_type = CharField(max_length=100, unique=True)
    price = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        table = "cargo_type_info"
