#!/usr/bin/env python                                                                                                                                                               
import sys
import os.path
import logging
import csv
import requests

if __name__ == '__main__':

    import optparse
    opt_parser = optparse.OptionParser()

    opt_parser.add_option('-s', '--source', dest='source', action='store', default=None, help='Where to read files from (on the Internets)')
    opt_parser.add_option('-d', '--dest', dest='dest', action='store', default=None, help='Where to write files to (on your filesystem)')
    opt_parser.add_option('-v', '--verbose', dest='verbose', action='store_true', default=False, help='Be chatty (default is false)')

    options, args = opt_parser.parse_args()

    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    for path in args:

        path = os.path.abspath(path)
        logging.debug("read from %s" % path)

        if not os.path.exists(path):
            logging.error("%s does not exist, skipping" % path)

        fh = open(path, 'r')
        reader = csv.DictReader(fh)

        for row in reader:

            rel = row['path']

            source = os.path.join(options.source, rel)
            dest = os.path.join(options.dest, rel)

            logging.debug("fetch %s" % source)
            logging.debug("store as %s" % dest)

            root = os.path.dirname(dest)

            if not os.path.exists(root):
                os.makedirs(root)

            try:
                rsp = requests.get(source)
            except Exception, e:
                logging.error("failed to retrieve %s, because %s" % (source, e))
                continue

            if rsp.status_code != 200:
                logging.error("unexpected status code fetching %s, %s" % (source, rsp.status_code))
                continue

            fh2 = open(dest, 'w')
            fh2.write(rsp.content)
            fh2.close()

    sys.exit()
