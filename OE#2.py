class Phone:
    def __init__(self, brand, ram, rom):
        self.brand = brand
        self.ram = ram
        self.rom = rom

phone_objects = []

valids = "ABCD"
def main():
    while True:
        action = input("Please Select A Action:\nA.) Create Phone Object\nB.) Modify Phone Object\nC.) Delete a Phone Object\nD.) Show Phone Objects\nE.) Exit\nInput: ").upper()
        if action == "A":
            objectname = str(input("Please specify object name: "))
            phone_objects.append(objectname)
            position = phone_objects.index(objectname)
            brand_val = str(input("Input Desired Brand: "))
            ram_val = str(input("Input Desired Ram Size: ")+"GB")
            rom_val = str(input("Input Desired Storage Size: ")+"GB")
            phone_objects[position] = Phone(brand_val, ram_val, rom_val)
            print("Object Added")
        elif action == "B":
            modify_object()
        elif action == "C":
            delete_object()
        elif action == "D":
            for each in phone_objects:
                position = phone_objects.index(each)
                print(f"{position}.) {each}")
            if phone_objects == []:
                print("Error Empty Object List")
        elif action == "E":
            break
        else:
            print("Error")

def modify_object():
        while True:
            if phone_objects != []:
                print("Phone Objects:")
                for each in phone_objects:
                    position = phone_objects.index(each)
                    print(f"{position}.) {each}")
                select_object = int(input("Please select a object: "))
                if select_object >= len(phone_objects):
                    print("Error not in list")
                    break
                else:
                    select_object = phone_objects[select_object]
                    print(f"You selected : {select_object}")
                while True:
                    modify_attribute = input("Modify Attribute\nA.) Brand\nB.) RAM\nC.) ROM\nD.) Exit\nInput: ").upper()
                    if modify_attribute == "A":
                        select_object.brand = str(input("Brand: "))
                    elif modify_attribute == "B":
                        select_object.ram = str(input("Ram Size: ")+"GB")
                    elif modify_attribute == "C":
                        select_object.rom = str(input("Storage Size: ")+"GB")
                    elif modify_attribute == "D":
                        break
                    else:
                        print("Error")
            else:
                print("Phone List is Empty")
            return
            
def delete_object():
    if phone_objects != []:
        print("Phone Objects:")
        for each in phone_objects:
            position = phone_objects.index(each)
            print(f"{position}.) {each}")
        select_object = int(input("Please select a object: "))
        if select_object >= len(phone_objects):
            print("Error not in list")
            return
        else:
            print(f"You selected : {phone_objects[select_object]}")
            del phone_objects[select_object]
    else:
        return print("Error List of Objects is Empty")
    return
    
main()
