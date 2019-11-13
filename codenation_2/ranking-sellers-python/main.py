from operator import itemgetter


class SellersRanking:

    def best_seller(self, sellers):

        melhores = sorted(sellers, key=itemgetter('value'), reverse=True)
        try:
            name = melhores[0]['name']
        except:
            return []
        name_list = []
        name_list.append(name)
        return name_list

    def ranking_list(self, sellers):
   
        list_sorted = sorted(sellers, key=itemgetter('value'), reverse=True)
        list_nova = []
        for l in list_sorted:
           list_nova.append(l['name'])
        return list_nova

    def best_seller_store(self, sellers, store):
        
        best = [x for x in sellers if x['store'] == store]
        try:
            name = best[0]['name']
        except:
            return []
        return [name]

    def sales_goals(self, sellers):

        name = [s for s in sellers if s["value"] < 500.0]
        list_teste = sorted(name, key=itemgetter('value'))
        list_nova = []
        for l in list_teste:
           list_nova.append(l['name'])

        return list_nova
