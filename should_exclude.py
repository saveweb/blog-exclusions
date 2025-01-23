import argparse
import re
import sys


with open("blog-exclusions.txt") as f:
    blog_exclusions = f.read().splitlines()

with open("global-crawling-exclusions.txt") as f:
    global_exclusion_regexes = f.read().splitlines()

def should_exclude(url):
    if any(exclusion in url for exclusion in blog_exclusions):
        return True
    if any(re.search(regex, url) for regex in global_exclusion_regexes):
        return True
    return False

def get_url():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()
    return args.url

if __name__ == "__main__":
    url = get_url()
    r = should_exclude(url)
    if r:
        print("Exclude")
        sys.exit(66)
    else:
        print("OK")