from simple_factory_pattern.simple_sushi_factory import SimpleSushiFactory


class SushiStore():
    def __init__(self, factory: SimpleSushiFactory):
        self._factory = factory

    def order_sushi(self, type_of_sushi):
        sushi = self._factory.create_sushi(type_of_sushi)
        prepared_sushi = sushi.prepare()
        return prepared_sushi.box()
