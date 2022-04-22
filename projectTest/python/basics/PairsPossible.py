from FirstExe import FirstExe
import itertools


class PairsPossible(FirstExe):

    def printpossiblepairs(self):
        pair_order_list = itertools.permutations(self.name, 2)

        # printing the elements belonging to permutations
        #print(list(pair_order_list))
        return list(pair_order_list)


emp1=PairsPossible("12314532")
listofpair=emp1.printpossiblepairs()
print(listofpair)




