from abc import ABC, abstractmethod


class DeliveryUnit(ABC):
    UNIT_ID_COUNTER = 500
    MAX_BATTERY = 100
    BASE_CONSUMPTION = 5

    def __init__(self, model, weight_capacity):
        self._model = model
        self._weight_capacity = weight_capacity
        self._battery_level = DeliveryUnit.MAX_BATTERY
        self.__unit_id = DeliveryUnit.UNIT_ID_COUNTER
        DeliveryUnit.UNIT_ID_COUNTER += 1

    @property
    def unit_id(self):
        return self.__unit_id

    def fly(self, distance, payload_weight, efficiency=1.0):
        if payload_weight > self._weight_capacity:
            raise ValueError(f"Payload {payload_weight} exceeds capacity")

        consumption_per_km = self.BASE_CONSUMPTION * (1 + payload_weight / 10) * efficiency
        total_needed = consumption_per_km * distance

        if self._battery_level <= 0:
            print(f"Unit {self.__unit_id} is out of battery")
        elif total_needed > self._battery_level:
            possible_distance = self._battery_level / consumption_per_km
            self._battery_level = 0
            print(f"Unit {self.__unit_id} flew {possible_distance:.2f} km (not enough for {distance})")
        else:
            self._battery_level -= total_needed
            print(f"Unit {self.__unit_id} flew {distance} km. Battery: {self._battery_level:.2f}%")


class HeavyDrone(DeliveryUnit):
    def __init__(self, model, weight_capacity, propeller_count):
        super().__init__(model, weight_capacity)
        self.__propeller_count = propeller_count
        if self.__propeller_count > 6:
            self._efficiency_bonus = 0.8
        else:
            self._efficiency_bonus = 1.0

    def fly(self, distance, payload_weight):
        return super().fly(distance, payload_weight, self._efficiency_bonus)


class LogisticsCenter:
    def __init__(self, name):
        self.__name = name

        self.__units_by_status = {
            'Charging': [],
            'Ready': [],
            'In-Flight': [],
            'Maintenance': []
        }

    def get_unit_status(self, unit_id):
        for status, drone_list in self.__units_by_status.items():
            for drone in drone_list:
                if drone.unit_id == unit_id:
                    return (status, drone)
        return (None, None)

    def move_to_status(self, unit_id, new_status):
        if new_status not in self.__units_by_status:
            raise ValueError(f"{new_status} isn't valid bitch!")
        current_status, drone = self.get_unit_status(unit_id)
        if drone is None:
            raise ValueError(f"Drone {unit_id} not found!")
        self.__units_by_status[current_status].remove(drone)
        self.__units_by_status[new_status].append(drone)
