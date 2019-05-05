import yaml

class SmartConfig:
    def __init__(self, configFile):
        with open(configFile, 'r') as ymlfile:
            self.cfg = yaml.load(ymlfile)
        

if __name__=="__main__":
    cfg = SmartConfig("conf.yaml")
    #print(type(cfg))
    for section in cfg.cfg:
        print(section)
        #print(type(section))
        for item in cfg.cfg[section]:
           print("  " + item)
    