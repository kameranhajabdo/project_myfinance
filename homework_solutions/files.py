import json
import time


class ShoppingList:
    def add(self, name:str, number:int):
        our_list = self.get()

        our_list[name] = {"name": name, "number": number}
        self.__write_to_file(our_list)

    def get(self):
        try:
            file = open("shopping_list.json")
            content = file.read()
            file.close()
            our_list = json.load(content)
        except:
            our_list = {}
        return our_list

    def delete(self, name:str):
        our_list = self.get()
        our_list.pop(name)
        self.__write_to_file(our_list)

    def edit(self, name: str, new_name: str = None, number: int = None):
        our_list = self.get()
        if name not in our_list:
            return
        if new_name:
            our_list[new_name] = our_list[name]
            our_list.pop(name)
            name = new_name
            our_list[name]["name"] = name
        if number:
            our_list[name]["number"] = number
            self.__write_to_file(our_list)




    def __write_to_file(self, our_list):
        our_json = json.dumps(our_list)
        file = open("shopping_list.json", "w")
        file.write(our_json)
        file.close()


shopping = ShoppingList()

shopping.edit("apple", 2)


