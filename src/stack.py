class Stack:

    def __init__(self, size: int):
        self.__stack_point: int = -1
        self.__array: list = [ None for i in range(size) ]
        self.__size: int = size

    def push(self, data: any):
        has_reached_stack_limit = self.__stack_point > self.__size - 1
        if has_reached_stack_limit:
            return
        self.__stack_point += 1
        self.__array[self.__stack_point] = data

    def pop(self) -> any:
        has_data = self.__stack_point > -1
        if not has_data:
            return None
        data = self.__array[self.__stack_point]
        self.__array[self.__stack_point] = None
        self.__stack_point -= 1
        return data

    def clone(self) -> list:
        return [value for value in self.__array]