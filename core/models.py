from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model


class Category(Model):

    class Meta:
        table_name = "core_categories"
        read_capacity_units = 4
        write_capacity_units = 4

    uuid = UnicodeAttribute(hash_key=True)
    description = UnicodeAttribute()
    icon = UnicodeAttribute()


class Place(Model):

    class Meta:
        table_name = "core_places"
        read_capacity_units = 4
        write_capacity_units = 4

    uuid = UnicodeAttribute(hash_key=True)
    description = UnicodeAttribute()
    latitude = UnicodeAttribute()
    longitude = UnicodeAttribute()
    category = UnicodeAttribute()
