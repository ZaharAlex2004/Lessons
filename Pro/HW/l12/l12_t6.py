import threading
import random
import time


class Organism:
    """
    Класс Organism
    """
    def __init__(self, age=0, health=100, energy=50, is_reproductive=False):
        self.age = age
        self.health = health
        self.energy = energy
        self.is_reproductive = is_reproductive
        self.alive = True

    def eat(self):
        """
        Питание
        :return:
        """
        if self.energy < 100:
            self.energy += 20
            print(f"Организм возрастом {self.age} поел. Энергия: {self.energy}")
        else:
            print(f"Организм возрастом {self.age} уже полный.")

    def age_and_health(self):
        """
        Старение организма
        :return:
        """
        self.age += 1
        self.energy -= 10  # Потеря энергии с каждым циклом
        self.health -= 5   # Потеря здоровья с каждым циклом

        if self.energy <= 0 or self.health <= 0:
            self.alive = False  # Организм умирает

    def reproduce(self):
        """
        Размножение
        :return:
        """
        if self.age > 5 and self.health > 50:
            self.is_reproductive = True
            print(f"Организм возрастом {self.age} размножается.")
            return Organism()  # Возвращаем нового организма (потомка)
        return None

    def status(self):
        return f"Возраст: {self.age}, Здоровье: {self.health}, Энергия: {self.energy}, Репродуктивный: {self.is_reproductive}, Живой: {self.alive}"


def evolve_organism(organism, population):
    """
    Функция для эволюции одного организма
    :param organism:
    :param population:
    :return:
    """
    while organism.alive:
        time.sleep(random.uniform(0.5, 2))  # Имитируем время для каждого организма
        organism.eat()  # Потребление пищи
        organism.age_and_health()  # Старение и потеря здоровья

        # Попытка размножения
        new_organism = organism.reproduce()
        if new_organism:
            population.append(new_organism)

        print(organism.status())  # Вывод статуса организма


def simulation(initial_population_size=10):
    """
    Функция симуляции
    :param initial_population_size:
    :return:
    """
    population = [Organism() for _ in range(initial_population_size)]
    threads = []

    # Создаем потоки для каждого организма
    for organism in population:
        thread = threading.Thread(target=evolve_organism, args=(organism, population))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    print(f"Количество организмов после эволюции: {len(population)}")


if __name__ == "__main__":
    simulation(10)
