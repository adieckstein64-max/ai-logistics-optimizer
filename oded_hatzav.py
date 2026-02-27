import numpy as np
import matplotlibsfaff.pyplot as plt
from ZooDataProcessor import ZooDataProcessor


class ZooIoTAnalytics(ZooDataProcessor):
    MIN_AGE = 9
    MAX_TEMP_FACTOR = 1.8
    MAX_HEART_RATE_FACTOR = 0.15
    MAX_STEPS_FACTOR = 0.5

    def __init__(self, file_name):
        self.__file_name = file_name

        dtype = [
            ('Species', 'U20'),
            ('Age', 'i4'),
            ('Weight', 'f4'),
            ('DailySteps', 'i4'),
            ('BodyTemp', 'f4'),
            ('HeartRate', 'i4'),
            ('FoodConsumption', 'f4')
        ]

        try:
            self.__data = np.genfromtxt(self.__file_name, delimiter=',', names=True, dtype=dtype)
            self.__species_list = np.unique(self.__data['Species'])
        except Exception as e:
            raise Exception(f"Failed to load CSV: {e}")

    def inventory_count(self):
        species, counts = np.unique(self.__data['Species'], return_counts=True)

        res = ""
        for s, c in zip(species, counts):
            res += f"{s}: {c}\n"
        return res.strip()

    def smart_filtering(self):
        result = ''
        for s in self.__species_list:
            species_mask = self.__data["Species"] == s
            avg_weight = np.mean(self.__data[species_mask]["Weight"])
            final_mask = (species_mask) & \
                         (self.__data['Age'] > self.MIN_AGE) & \
                         (self.__data['Weight'] < avg_weight)
            filtered_animals = self.__data[final_mask]
            for animal in filtered_animals:
                result += f": Species: {animal['Species']}, Age: {animal['Age']}, Weight: {animal['Weight']:.2f}\n"
        return result.strip()

    def energy_efficiency(self):
        efficiency_vector = self.__data["DailySteps"] / self.__data["FoodConsumption"]
        avg_efficiencies = []
        for s in self.__species_list:
            species_mask = self.__data['Species'] == s
            avg_eff = np.mean(efficiency_vector[species_mask])
            avg_efficiencies.append(avg_eff)
        best_index = np.argmax(avg_efficiencies)
        best_species = self.__species_list[best_index]
        best_value = avg_efficiencies[best_index]
        return f"Most Efficient Species: {best_species} (Avg Ratio: {best_value:.2f})"

    def get_health_report(self):
        data = self.__data
        avg_temp = np.mean(data["BodyTemp"])
        std_temp = np.std(data['BodyTemp'])
        temp_threshold = avg_temp + (self.MAX_TEMP_FACTOR * std_temp)

        median_steps = np.median(data["DailySteps"])
        steps_threshold = median_steps * self.MAX_STEPS_FACTOR

        temp_issue = data["BodyTemp"] > temp_threshold
        steps_issue = data["DailySteps"] < steps_threshold

        hr_issue = np.zeros(len(data), dtype=bool)
        for s in self.__species_list:
            species_mask = data["Species"] == s
            species_hr_avg = np.mean(data[species_mask]["HeartRate"])
            upper_hr = species_hr_avg * (1 + self.MAX_HEART_RATE_FACTOR)
            lower_hr = species_hr_avg * (1 - self.MAX_HEART_RATE_FACTOR)
            hr_issue[species_mask] = (data[species_mask]["HeartRate"] > upper_hr) | \
                                     (data[species_mask]["HeartRate"] < lower_hr)
        sick_count = temp_issue.astype(int) + hr_issue.astype(int) + steps_issue.astype(int)
        sick_mask = sick_count >= 2
        res = "--- 4. Health Report (Suspected Sick Animals)\n"
        res += f"{'ID':<5} | {'Species':<10} | {'Temp Issue':<10} | {'HR Issue':<10} | {'Steps Issue':<10}\n"
        res += "-" * 60 + "\n"
        indices = np.where(sick_mask)[0]
        for idx in indices:
            animal = data[idx]
            t_mark = 'X' if temp_issue[idx] else ''
            h_mark = 'X' if hr_issue[idx] else ''
            s_mark = 'X' if steps_issue[idx] else ''
            res += f"{idx:<5} | {animal['Species']:<10} | {t_mark:^10} | {h_mark:^10} | {s_mark:^10}\n"

        return res.strip()

    def get_top_active_animals(self):
        sorted_indices = np.argsort(self.__data["DailySteps"])
        top_5_indices = sorted_indices[-5:][::-1]
        res = "--- 5. Top 5 Active Animals (Argsort)\n"
        for i, idx in enumerate(top_5_indices, 1):
            animal = self.__data[idx]
            res += f"{i}. {animal['Species']}, Steps: {animal['DailySteps']}\n"

        return res.strip()

    def get_calculate_linear_regression(self):
        x_value = self.__data['Weight']
        y_value = self.__data['FoodConsumption']
        slope, intercept = np.polyfit(x_value, y_value, 1)
        res = "--- 6. Trend Analysis (Linear Regression)\n"
        res += f"Linear Trendline Equation: y = {slope:.4f}x + {intercept:.4f}"

        return res

    def plot_species_distribution(self):
        s, c = np.unique(self.__data['Species'], return_counts=True)
        plt.figure("Species Distribution")
        plt.pie(c, labels=s, autopct='%1.1f%%', startangle=140)
        plt.title('Species Distribution')
        plt.show()
    def plot_weight_vs_food(self):
        x, y = self.__data['Weight'], self.__data['FoodConsumption']
        m, b = np.polyfit(x, y, 1)
        plt.figure("Weight vs. Food")
        plt.scatter(x, y, alpha=0.6, label='Data', color='blue')
        plt.plot(x, m * x + b, color='red', label=f'Trendline (y={m:.2f}x+{b:.2f})')
        plt.xlabel('Weight (kg)')
        plt.ylabel('Food (kg)')
        plt.title('Weight vs. Food Consumption')
        plt.legend()
        plt.show()
    def plot_heart_rate_distribution(self):
        plt.figure("Heart Rate Distribution")
        plt.hist(self.__data['HeartRate'], bins=20, color='skyblue', edgecolor='black')
        plt.xlabel('Beats Per Minute')
        plt.ylabel('Count')
        plt.title('Heart Rate Distribution')
        plt.show()
    def plot_avg_steps_by_species(self):
        avg_steps = [np.mean(self.__data[self.__data['Species'] == species]['DailySteps']) for species in
                     self.__species_list]
        plt.figure("Average Steps")
        plt.bar(self.__species_list, avg_steps, color='teal')
        plt.xlabel('Species')
        plt.ylabel('Average Steps')
        plt.title('Average Daily Steps by Species')
        plt.show()


