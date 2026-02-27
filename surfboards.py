from abc import ABC, abstractmethod


class SurfBoard(ABC):
    BOARD_ID_COUNTER = 1000

    def __init__(self, model, base_price):
        self._model = model
        self._base_price = base_price
        self.__serial_id = SurfBoard.BOARD_ID_COUNTER
        SurfBoard.BOARD_ID_COUNTER += 1

    @property
    def serial_id(self):
        return self.__serial_id

    @abstractmethod
    def calculate_rental(self, hours):
        pass


class ProBoard(SurfBoard):
    def __init__(self, model, base_price, material):
        super().__init__(model, base_price)
        self._material = material

    def calculate_rental(self, hours):
        if self._material.lower() == 'carbon':
            price = (self._base_price * hours) * 1.5
        else:
            price = (self._base_price * hours) * 1.2
        return price


class SurfingClub:
    def __init__(self):
        self.__inventory = {}

    def add_board(self, category, boards):
        inventory = self.__inventory
        if category not in inventory:
            inventory[category] = []
        inventory[category].append(boards)

    def get_rental_value(self):
        res = 0
        inventory = self.__inventory
        for boards in inventory.values():
            for board in boards:
                res += board._base_price
        return res


import numpy as np
import matplotlib as plt

subscribers_data = [
    [1, "M", 350, 12],
    [2, "F", 280, 8],
    [3, "M", 450, 15],
    [4, "F", 310, 20],
    [5, "M", 250, 5],
    [6, "F", 500, 18]
]
np_fullstack = np.array(subscribers_data)
prices = (np_fullstack[:, 2].astype(float))
visits = (np_fullstack[:, 3].astype(int))
average_visits = np.mean(visits)
good_members = np.sum((visits > 10) & (prices > 300))

import matplotlib.pyplot as plt

plt.figure(figsize=(7, 5))
plt.scatter(prices, visits, color='blue', marker='o')
plt.title  ("mac a zibi")
plt.xlabel  ("monthly fee [nis]")
plt.ylabel  ("number of visits")
plt.grid(True)
plt.show()
