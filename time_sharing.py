import random
import time
import os

class Resource:
    def __init__(self, name, id):
        self.id = id
        self.name = "Resource " + name
        self.user_list = []
        self.current_user = None
        self.is_available = True

    def printName(self):
        print(self.name)


class User:
    def __init__(self, name, id):
        self.id = id
        self.name = "User " + name
        self.resource_num = random.randint(1, generateResource())
        self.time = random.randint(1, 30)

    def printName(self):
        print(self.name)

class Generator:
    def __init__(self):
        self.resource = []
        self.user = []
        self.waiting_list = []

    def addResource(self):
        for resource in range(1, generateResource() + 1):
            res = Resource(str(resource), resource)
            self.resource.append(res)

    def addUser(self):
        for user in range(1, generateUser() + 1):
            u = User(str(user), user)
            self.user.append(u)

    # appends the user to the user list of a certain resource
    def appendUserList(self):
        for user in self.user:
            for resource in self.resource:
                if user.resource_num == resource.id:
                    resource.user_list.append(user)

    # show users and resources
    def showUserAndResource(self):
        print("Resources")
        print("")
        for resource in self.resource:
            resource.printName()
            if resource.user_list:
                for user in resource.user_list:
                    print(user.name, "\tTime: ", user.time)
                print("")
            else:
                print ("Free")
                print("")
        print("")

    def work(self):
        is_all_available = False

        while not is_all_available:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++")
            for resource in self.resource:
                resource.printName()
                if resource.is_available:
                    if resource.user_list:
                        user = resource.user_list[0]
                        resource.user_list.remove(user)
                        resource.current_user = user
                        resource.is_available = False
                        print("Current User: \t", resource.current_user.name)
                        print("Time left: \t", resource.current_user.time)
                        if resource.user_list:
                            print("\tWaiting List:")
                            time = resource.current_user.time
                            for user in resource.user_list:
                                print("\t", user.name, " ", "Time allocated: ", user.time, "waiting time: ", time)
                                time+=user.time
                        print("Status: \tIn Use\n")
                    else:
                        print("Status: \tFree\n")
                else:
                    resource.current_user.time -= 1
                    print("Current User: \t", resource.current_user.name)
                    print("Time left: \t", resource.current_user.time)
                    if resource.user_list:
                        print("\tWaiting List:")
                        time = resource.current_user.time
                        for user in resource.user_list:
                            print("\t", user.name, " ", "Time allocated: ", user.time, "waiting time: ", time)
                            time += user.time
                    if resource.current_user.time == 0:
                        resource.is_available = True
                        print("Status: \tFree\n")
                    else:
                        print("Status: \tIn Use")

            print("\n")

            print("+++++++++++++++++++++++++++++++++++++++++++++++++")

            for resources in self.resource:
                if resource.user_list or not resource.is_available:
                    break
                elif (resource.id) == len(self.resource):
                    is_all_available = True


def generateResource():
    return random.randint(1, 30)

def generateUser():
    return random.randint(1, 30)


def main():
    gen = Generator()
    gen.addResource()
    gen.addUser()
    gen.appendUserList()
    gen.showUserAndResource()

    timer = 120
    while timer > 0:
        gen.work()
        time.sleep(1)
        os.system('cls')

        timer -= 1




if __name__ == '__main__':
    main()
