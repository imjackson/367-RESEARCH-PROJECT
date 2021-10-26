import csv
import json

from pprint import pprint

def main():
    threads = {}
    file = open('merged-pythondev-help-concat-group.csv', mode="r")
    data = csv.reader(file)
    for line in data:
        if line[0] in threads:
            threads[line[0]].append(line[3])
        else:
            threads[line[0]] = [line[3]]
            
    with open("output.json", "w") as out:
        json.dump(threads, out)


if __name__=="__main__":
    main()