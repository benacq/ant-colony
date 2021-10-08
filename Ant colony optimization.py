class Server:

    def __init__(self, devices):
        self.devices = devices

    def select_device(self):

        task_device_ID = -1
        pheromone = 0

        for i in self.devices:
            if pheromone < self.devices[i].pheromone_level():
                task_device_ID = self.devices[i].getID()
                pheromone = self.devices[i].phermone_level()
            else:
                continue


class Device:
    def __init__(self, ID=0, processing_power=0, task_assigned=0):
        self.ID = ID
        self.processing_power = processing_power
        self.task_assigned = task_assigned

    def pheromone_level(self):
        return self.processing_power / (1 + self.task_assigned)

    def assign_task(self):
        return self.task_assigned + 1

    def getID(self):
        return self.ID

    def details(self):
        return "ID: ", self.ID, "\n Processing power", self.processing_power, "\n Task assigned", self.task_assigned, "\n"


def main():
    task_device = Device()
    task_device_ID = 0
    pheromone = 0
    kebede = Device(1, 2, 3)
    audrey = Device(2, 4, 5)
    traci = Device(3, 5, 1)
    mirabelle = Device(4, 6, 7)
    mildred = Device(5, 5, 4)

    all_devices = [kebede, audrey, traci, mirabelle, mildred]

    for i in all_devices:
        print(i.pheromone_level())

        # for i in devices:
        if pheromone < i.pheromone_level():
            task_device = i
            # task_device_ID = i.getID()
            pheromone = i.pheromone_level()
        else:
            continue

    print(task_device.details())


# maryam = Server()

# kebede = Device(1,2,3)
# audrey = Device(2,4,5)
# traci = Device(3,5,1)
# mirabelle = Device(4,6,7)
# mildred = Device(5,5,4)

# all_devices = [kebede,audrey,traci,mirabelle,mildred]

# print(kebede.pheromone_level())


main()
