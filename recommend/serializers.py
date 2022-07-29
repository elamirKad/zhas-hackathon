from rest_framework import serializers
from recommend.models import Cosmetics

class CosmeticsModel:
    def __init__(self, label, brand, name, ingridients, price, rank, combination, normal, dry, oily, sensitive):
        self.label = label
        self.brand = brand
        self.name = name
        self.ingridients = ingridients
        self.price = price
        self.rank = rank
        self.combination = combination
        self.normal = normal
        self.dry = dry
        self.oily = oily
        self.sensitive = sensitive

class CosmeticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cosmetics
        fields = "__all__"