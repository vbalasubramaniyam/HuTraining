from PairsPossible import PairsPossible


class SearchCommonElements(PairsPossible):

    def commonChar(self):
        b=self.printpossiblepairs()
        #b="123"
        a = list(set(self.name) & set(b))
        print("The common letters are:")
        for i in a:
            print(i)
emp1=SearchCommonElements("12314532")
emp1.commonChar()