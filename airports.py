import json
import random
class Airports:
    def __init__(self, name, max_aircrafts, line_length, planes, helicopters):
        self.name = name
        if not max_aircrafts:
            self.max_aircrafts = 10
        else:
            self.max_aircrafts = max_aircrafts
        self.line_length = line_length
        self.transport = {'planes': planes, 'helicopters': helicopters}
    @classmethod
    def from_json(cls, j):
        return cls(j['name'], j['max_aircrafts'], j['line_length'],
            [Planes.from_json(x) for x in j['planes']],
            [Helicopter.from_json(x) for x in j['helicopters']])
    
    def k_free(self):
        return int(self.max_aircrafts - len(self.transport['planes']) -
    len(self.transport['helicopters']))

    # попытка отправки транспорта
    def departure(self, target_airport):
        available_types = []
        if self.transport['planes']:
            available_types.append('planes')
        if self.transport['helicopters']:
            available_types.append('helicopters')
        if not available_types:
            return False, f"Аэропорт {self.name} пуст — нечего отправлять"
        
        # Выбираем случайный тип из доступных
        transport_type = random.choice(available_types)
        transport_list = self.transport[transport_type]
        transport = random.choice(transport_list)
        print(f"\nОТПРАВКА {transport.number} ({'самолёт' if transport_type == 'planes' else 'вертолёт'}) "
              f"из {self.name} в {target_airport.name}")
        return transport.condition_for_land(target_airport, self)

    def __repr__(self):
        return f'name: {self.name}, max_aircrafts: {self.max_aircrafts}, line_length: {self.line_length}, transports: {self.transport}'
    
class Transport:
    def __init__(self, number, d, w):
        self.number = number
        self.max_distance = d
        self.max_cargo_weight = w

    # попытка отправки транспорта
    def took_off(self, target_airport, start_airport, some_condions, type_t):
        # проверяется есть ли место просто для транспорта в аэропорту
        if target_airport.k_free() > 0 and some_condions:
        # проверяется какой вид транспорта, чтобы удалить из старого аэропорта и добавить в новый
            if type_t == 'plane':
                target_airport.transport['planes'] += [self]
                start_airport.transport['planes'].remove(self)
            else:
                target_airport.transport['helicopters'] += [self]
                start_airport.transport['helicopters'].remove(self)
        else:
            print('не одобрено')

    def __repr__(self):
        return f'number: {self.number}; max_distance: {self.max_distance}; max_cargo_weight: {self.max_cargo_weight}'

class Planes(Transport):
    def __init__(self, number, d, w, line):
        super().__init__(number, d, w)
        self.min_line_length = line
        
    @classmethod
    def from_json(cls, j):
        return cls(j['number'], j['max_distance'], j['max_cargo_weight'],
        j['min_line_length'])
    
    # проверка частиных условий
    def condition_for_land(self, target_airport, start_airport):
        length = target_airport.line_length
        # проверяем условие только для самолета и передаем тип транспорта
        self.took_off(target_airport, start_airport, length >= self.min_line_length,
        'plane')

    def __repr__(self):
        return super().__repr__() + f'; min_line_lenth: {self.min_line_length}'
    
class Helicopter(Transport):
    def __init__(self, number, d, w, m):
        super().__init__(number, d, w)
        self.is_military = m

    @classmethod
    def from_json(cls, j):
        return cls(j['number'], j['max_distance'], j['max_cargo_weight'],
        j['is_military'])
    
    # проверка частиных условий
    def condition_for_land(self, target_airpot, start_airpot):
        k_free = target_airpot.k_free()
        # проверка условий для вертолета, если он военный, то, чтобы не была превышена
        # половины вместимости воздушных судов
        can_land = (not self.is_military) or (k_free > target_airpot.max_aircrafts // 2)
        self.took_off(target_airpot, start_airpot, can_land, 'helicopters')

    def __repr__(self):
        return super().__repr__() + f'; if_military: {self.is_military}'

with open('airports.json') as f:
    reader = json.load(f)
    data_airports = [Airports.from_json(x) for x in reader]
airport = data_airports[0]
print(airport)
number_airport = random.randint(0, len(data_airports) - 1)
print(data_airports[number_airport])
airport.departure(data_airports[number_airport])
print(airport)
print(data_airports[number_airport])