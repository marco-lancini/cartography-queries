#!/usr/bin/env python3
import os
import sys
import argparse
import simplejson

NEO4J_QUERIES_FILE = 'queries.json'

# ==============================================================================
# UTILS
# ==============================================================================
def parse_args():
    parser = argparse.ArgumentParser(description='Query Manager.')
    parser.add_argument('--count',
                        dest='count', action='store_true',
                        help='Count all available queries')
    parser.add_argument('--get-all-tags',
                        dest='get_all_tags', action='store_true',
                        help='Get list of all available tags.')
    parser.add_argument('--tags',
                        dest='tags',
                        help='Filter queries by specified tags')
    args = parser.parse_args()
    return args

def read_queries():
    if not os.path.isfile(NEO4J_QUERIES_FILE):
        print('File "queries.json" not found. Exiting...')
        sys.exit()
    with open(NEO4J_QUERIES_FILE, 'r') as fp:
        body = fp.read()
    return simplejson.loads(body)

def get_all_tags(queries):
    tags = []
    for q in queries:
        tags.extend(q['tags'])
    return sorted(list(set(tags)))

def filter_by_tags(queries, tags):
    # Returns all the queries which contain all the tags provided
    return [q for q in queries if all(elem in q['tags'] for elem in tags)]


# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == '__main__':
    # Parse arguments
    args = parse_args()
    count = args.count
    get_flags = args.get_all_tags
    tags = args.tags

    # Load queries.json
    queries = read_queries()

    print("--- Query Manager for Cartography ---")

    # Count available queries
    if count:
        print("[+] Number of available queries: {}".format(len(queries)))
    # List all available tags
    if get_flags:
        all_tags = get_all_tags(queries)
        print("[+] The following tags have been defined:")
        for t in all_tags:
            print("\t{}".format(t))
    # Print queries filtered by tags
    if tags:
        tags = tags.split(',')
        print("[+] Selected tags: {}".format(tags))
        print("[+] Queries matching selected tags:")
        selected_queries = filter_by_tags(queries, tags)
        for q in selected_queries:
            print("\t[{}] {}".format(q['name'], q['description']))
