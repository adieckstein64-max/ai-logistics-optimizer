# from abc import ABC, abstractmethod
#
#
# class Track(ABC):
#     MIN_BPM = 120
#
#     def __init__(self, bpm, title):
#         self.bpm = bpm
#         self.title = title
#
#     @property
#     def bpm(self):
#         return self._bpm
#
#     @bpm.setter
#     def bpm(self, value):
#         self._bpm = value
#         if value < Track.MIN_BPM:
#             self._bpm = Track.MIN_BPM
#         else:
#             self._bpm = value
#
#     @abstractmethod
#     def get_energy_level(self):
#         pass
#
#
# class HouseTrack(Track):
#     def __init__(self, bpm, title, sub_genre):
#         super().__init__(bpm, title)
#         self.sub_genre = sub_genre
#
#     def get_energy_level(self):
#         if self.bpm > 126:
#             return f"bpm is {self.bpm} and the energy of {self.title} is high! "
#         else:
#             return f"bpm is {self.bpm} and the energy of {self.title} is low AF!!!"
#
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# tracks_data = [
#     [101, 124, 5000, 6.5],
#     [102, 128, 8500, 7.2],
#     [103, 122, 3200, 5.8],
#     [104, 130, 9200, 6.0],
#     [105, 126, 4800, 8.1],
#     [106, 128, 7600, 5.5]
# ]
# np_tracks = np.array(tracks_data)
# plays = (np_tracks[:, 2].astype(int))
# avg_plays = np.mean(plays)
# bpm = (np_tracks[:, 1].astype(float))
# mask = ((plays > 7000) & (bpm > 127))
# print(f"number of hits: {np.sum(mask)}")
# print(f"hits: {np_tracks[:, 0][mask]}")
#
#
# plt.scatter(bpm,plays,color = "red",label= "Bpm vs Plays analysis")
# plt.xlabel ("BPM")
# plt.ylabel ("Number of Plays")
# plt.grid(True)
# plt.legend()
# plt.show()
# import mysql.connector
# passwd = input('Enter your password: ')
# connection = mysql.connector.connect(
#     host="localhost",
#     user="shop_app",
#     password=passwd,
#     database="shop_db"
# )
# cursor = connection.cursor()
# v_customer_id = int(input('Enter customer id: '))
# cursor.execute("select customer_id, username, orders_count, total_spent "
#                "from customer_order_summary "
#                "where customer_id = %s ",(v_customer_id,))
# customer_data = cursor.fetchone()
# if customer_data is None:
#     print('Customer not found.')
#     cursor.close()
#     connection.close()
#     exit()
# customer_id, username, orders_count, total_spent = customer_data
# print(f"customer id: {customer_id}, username: {username}, order_count: {orders_count}, total_spent: {total_spent}")
# v_new_order_id = cursor.callproc("add_order",[v_customer_id,0])[1]
# print(f"your new order id is: {v_new_order_id}")
# v_product_id = int(input('Enter product id (0 to complete order): '))
# while v_product_id != 0:
#     v_product_quantity = int(input('Enter product quantity: '))
#     cursor.callproc("add_order_item",[v_new_order_id, v_product_id,v_product_quantity])
#     v_product_id = int(input('Enter product id (0 to complete order): '))
#
# v_shipping_date = input('Enter shipping date: ')
# cursor.execute("update orders set shipping_date = %s "
#                "where order_id = %s ",(v_shipping_date,v_new_order_id))
# connection.commit()
# cursor.close()
# connection.close()
# import numpy as np
#
# factory_data = np.array([
#     [101, 82.5, 12.4],
#     [102, 91.0, 15.1],
#     [103, 78.4, 11.2],
#     [104, 88.2, 14.8],
#     [105, 84.6, 13.0]
# ])
# np_fullstack = np.array(factory_data)
# temp = np_fullstack[:,1]
# avg_temp = np.mean(temp)
# fuel_consumption = np_fullstack[:,2]
# mask = ((fuel_consumption) > 14)
#
# problematic = np_fullstack[mask]
# print(problematic)
#
#
# maski = np.argmax(temp)
# print(np_fullstack[maski][0])
#
# import matplotlib.pyplot as plt
# plt.hist(np_fullstack[:,1],bins = 4,color = "orange",edgecolor = "black")
# plt.title("Engine Temperature Distribution")
# plt.xlabel("Temperature")
# plt.ylabel("Frequency")
# plt.grid(axis='y',alpha=0.75)
# plt.show()
import numpy as np

# [ID, Attempts, Completed]
passes_stats = [
    [19, 45, 42],
    [8, 92, 88],
    [6, 110, 102],
    [11, 35, 20],
    [2, 50, 35]]
np_fullstack = np.array(passes_stats)
attempts = np_fullstack[:,1]
completed = np_fullstack[:,2]
accuracy =  completed / attempts * 100
avg_accuracy = np.mean(accuracy)
print(f"accuracy : {avg_accuracy:.2f}")
mask = accuracy > 90
player_id = np_fullstack[:,0]
print(player_id[mask])

import matplotlib.pyplot as plt
plt.figure(figsize=(7,5))
plt.scatter(attempts,accuracy,color="blue",marker = "o")
plt.title("mac a zubi")
plt.xlabel ("pass attempts")
plt.ylabel ("attempts accuracy")
plt.legend()
plt.grid(True)
plt.show()








