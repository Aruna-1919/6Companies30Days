class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.family_tree = {kingName: []}
        self.death_status = set()

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.family_tree:
            self.family_tree[parentName] = []
        self.family_tree[parentName].append(childName)
        self.family_tree[childName] = []

    def death(self, name: str) -> None:
        self.death_status.add(name)

    
    def getInheritanceOrder(self) -> list:
        result = []

        def dfs(person):
            if person not in self.death_status:
                result.append(person)
            for child in self.family_tree[person]:
                dfs(child)

        dfs(self.kingName)
        return result


# Example usage:
# obj = ThroneInheritance("king")
# obj.birth("king", "Alice")
# obj.birth("Alice", "Jack")
# obj.birth("king", "Bob")
# print(obj.getInheritanceOrder())  # Output: ["king", "Alice", "Jack", "Bob"]
# obj.death("Alice")
# print(obj.getInheritanceOrder())  # Output: ["king", "Jack", "Bob"]
# print(obj.Successor("king", ["king", "Alice", "Jack"]))  # Output: Bob
