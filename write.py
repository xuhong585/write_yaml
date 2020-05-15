import os
import yaml


def write_yaml(value):
    curpath= os.path.dirname(os.path.realpath(__file__))
    ypath = os.path.join(curpath,'token.yaml')
    print(ypath)
    t = {"token":value}
    with open(ypath,'w',encoding='utf-8') as f:
        yaml.dump(t,f)


def write1_yaml(value):
    curpath= os.path.dirname(os.path.realpath(__file__))
    ypath = os.path.join(curpath,'token.yaml')
    print(ypath)
    t = {"token1":value}
    with open(ypath,'a',encoding='utf-8') as f:
        yaml.dump(t,f)


if __name__ == '__main__':
    write_yaml()
    write1_yaml()