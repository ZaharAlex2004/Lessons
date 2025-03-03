import threading
import random
import time
import logging
from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('organism_simulation.log')
    ]
)


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
            logging.info(f"Организм возрастом {self.age} поел. Энергия: {self.energy}")
        else:
            logging.info(f"Организм возрастом {self.age} уже полный.")

    def age_and_health(self):
        """
        Старение организма
        :return:
        """
        self.age += 1
        self.energy -= 10
        self.health -= 5

        if self.energy <= 0 or self.health <= 0:
            self.alive = False
            logging.info(f"Организм возрастом {self.age} умер.")

    def reproduce(self):
        """
        Размножение
        :return:
        """
        if self.age > 5 and self.health > 50:
            self.is_reproductive = True
            logging.info(f"Организм возрастом {self.age} размножается.")
            return Organism()
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
        time.sleep(random.uniform(0.5, 2))
        organism.eat()
        organism.age_and_health()

        new_organism = organism.reproduce()
        if new_organism:
            population.append(new_organism)

        logging.info(organism.status())


def simulation(initial_population_size=10, max_threads=5):
    """
    Функция симуляции
    :param initial_population_size:
    :return:
    """
    population = [Organism() for _ in range(initial_population_size)]
    threads = []

    with ThreadPoolExecutor(max_threads) as executor:
        for organism in population:
            threads.append(executor.submit(evolve_organism, organism, population))

        for future in threads:
            future.result()

    logging.info(f"Количество организмов после эволюции: {len(population)}")


if __name__ == "__main__":
    try:
        simulation(10, max_threads=5)
    except KeyboardInterrupt:
        logging.info("Симуляция завершена пользователем.")
