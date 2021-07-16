from menuitem import MenuItem

class SetMenu(object):
    def __init__(self, MenuitemsList):
        self.items = set()
        for item in MenuitemsList:
            self.items.add(item)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        retval = ""
        for item in self.items:
            retval = retval + str(item) + "\n"
        return retval
