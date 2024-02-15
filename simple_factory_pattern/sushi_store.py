from dataclasses import dataclass
from simple_factory_pattern.simple_sushi_factory import SimpleSushiFactory

@dataclass
class SushiStore():
    _factory: SimpleSushiFactory

    def order_sushi(self, type_of_sushi):
        sushi = self._factory.create_sushi(type_of_sushi)
        prepared_sushi = sushi.prepare()
        return prepared_sushi.box()
