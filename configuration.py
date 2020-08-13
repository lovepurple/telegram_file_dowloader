import yaml

class configuration(object):
    
    @classmethod
    def getinstance(cls):
        return cls

yamlDoc = yaml.load(open("./config.yaml"), Loader=yaml.FullLoader)
for item, doc in yamlDoc.items():
    print(doc)
