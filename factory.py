# create a naan class to assess ingredients and recipes
class NaanFactory:

    # method return true if user has BOTH water and flour
    def make_dough(self, *ingredients):
        ingredients = [i.lower() for i in ingredients]
        if 'water' in ingredients and 'flour' in ingredients:
            return "dough"
        else:
            return "water and flour needed"

    # Define a method that makes naan if dough is True
    def bake_naan(self, *ingredients):
        ingredients = [i.lower() for i in ingredients]
        if 'dough' in ingredients:
            return "naan"
        else:
            return "missing dough"

    # function for running the entire factory
    # input is a list of all ingredients available
    def run_factory(self, *ingredients):

        # all ingredients to lowercase
        ingredients = [i.lower() for i in ingredients]
        # check if user can make dough
        dough = self.make_dough(*ingredients)
        # check if user can make a naan bread
        baked_dough = self.bake_naan(dough)
        
        # True if naan is produced
        if baked_dough == 'naan':
            print("Naan made with dough supplied")
            return True
        
        return "the correct ingredients are needed for naan production"

def main():
    test_factory = NaanFactory()
    test_factory.run_factory("water", "flour")

if __name__ == "__main__":
    main()