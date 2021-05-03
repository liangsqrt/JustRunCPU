from configparser import ConfigParser
import os
import argparse


basePath = os.path.dirname(os,os.path.abspath(__file__))


def create_argparse():
    parser = argparse.ArgumentParser(description="Just Run It! this repo is created for charade which it devices is fully used!")
    parser.add_argument(name="--type", action="action", default="cpu", dest="type", type=str)
    parser.add_argument(name="--level", action="action", default=10.0, dest="level", type=float)


if __name__ == '__main__':
    parse = create_argparse()
    print(parse.type)    
    

