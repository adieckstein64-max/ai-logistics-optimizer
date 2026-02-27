from abc import ABC, abstractmethod
from functools import total_ordering


class Person(ABC):
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age


@total_ordering
class Player(Person):
    def __init__(self, name, age, skill_level):
        super().__init__(name, age)
        self.age = age
        self.skill_level = skill_level

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 45 or value < 16:
            raise ValueError(f"{value} is the age of {self._name} and it isn't valid")
        self._age = value

    @property
    def name(self):
        return self._name

    @property
    def skill_level(self):
        return self._skill_level

    @skill_level.setter
    def skill_level(self, value):
        if value > 100 or value < 20:
            raise ValueError(f" {value}, isn't valid bitch")
        self._skill_level = value

    def __gt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.skill_level > other.skill_level

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.name == other.name and self.skill_level == other.skill_level

    def __repr__(self):
        return f"Player(name = '{self._name}', age = {self.age}, skill = {self.skill_level})"


class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player_object):
        if player_object not in self.players:
            self.players.append(player_object)
            print(f"{player_object.name} joined {self.team_name}")

    @property
    def avg_skill(self):
        if not self.players:
            return 0
        total = 0
        for p in self.players:
            total += p.skill_level
        res = total / len(self.players)
        return res

    @property
    def mvp(self):
        if not self.players:
            return None
        return max(self.players)


class Coach(Person):
    def __init__(self, name, age, experience_years):
        super().__init__(name, age)
        self.experience_years = experience_years

    def train(self, player):
        print(f"\ncoach {self._name} is coaching {player.name}")
        try:
            print(f"{player.name} is {player.skill_level} before practice")
            player.skill_level += 2
            print(f"great! {player.name} is now {player.skill_level} overall")
        except ValueError as e:
            print(f"training failed {e}")

    def __repr__(self):
        return f"Coach = {self._name} ,experience years = {self.experience_years}"


# --- 1. יצירת הדמויות (ה-Data) ---
flick = Coach("Hansi Flick", 59, 25)
lamine = Player("Lamine Yamal", 18, 91)
pedri = Player("Pedri", 23, 89)
messi = Player("Lionel Messi", 38, 97)

# --- 2. בניית הקבוצה (Composition) ---
barca = Team("FC Barcelona")
barca.add_player(lamine)
barca.add_player(pedri)
barca.add_player(messi)

# --- 3. בדיקת המצב ההתחלתי (Properties) ---
print(f"\n--- Initial State of {barca.team_name} ---")
print(f"Average Skill: {barca.avg_skill:.2f}")
print(f"Current MVP: {barca.mvp.name} (Skill: {barca.mvp.skill_level})")

# --- 4. המאמן נכנס לפעולה (Interactions) ---
# נאמן את לאמין ימאל חזק
for _ in range(3):
    flick.train(lamine)

# --- 5. בדיקת המצב אחרי אימון (Dynamic Updates) ---
print(f"\n--- After Training Session ---")
print(f"New Average Skill: {barca.avg_skill:.2f}")
# שים לב: אם לאמין עבר את מסי בסקיל, ה-MVP יתחלף אוטומטית!
print(f"New MVP: {barca.mvp.name} (Skill: {barca.mvp.skill_level})")

# --- 6. בדיקת חסינות (Error Handling) ---
print(f"\n--- Stress Test (Trying to over-train Messi) ---")
for _ in range(4):
    flick.train(messi)
print(barca.mvp)