class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()

        result = []
        prefix = ""

        for ch in searchWord:
            prefix += ch
            temp = []

            for product in products:
                if product.startswith(prefix):
                    temp.append(product)

                if len(temp) == 3:
                    break

            result.append(temp)

        return result