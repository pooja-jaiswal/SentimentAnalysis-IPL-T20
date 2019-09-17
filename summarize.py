"""
Summarize data.
"""
from helper import fprint

def main():
    print("--------------------------------- Started Summary -----------------------------------")
    collector_details = open("collect.txt",'r').read()
    cluster_details = open("cluster.txt",'r') .read()
    classify_details = open("classify.txt",'r', encoding='utf-8').read()
    open("summary.txt",'w')
    f = open("summary.txt",'a', encoding='utf-8')
    fprint("collect.py : \n" +collector_details, f)
    fprint("cluster.py : \n" +cluster_details, f)
    fprint("classify.py : \n" +classify_details, f)
    f.close()
    print("Details saved to : summary.txt")
    print("---------------------------------- Finished summary -----------------------------------")


if __name__ == main():
    main()