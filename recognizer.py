#!/usr/bin/env python3
import argparse
import logging

USAGE = "python3 recognizer.py <image_path>"
DESCRIPTION = """\
Takes an image as input and prints with what probability it thinks there's a cat in this picture. Best works with 
pictures inside houses/apartments.
"""


def run():
    logging.info("Loading the image...")
    # TODO: Cat recognizer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    parser.add_argument("image_path", help="Path to the image (.jpg only")
    parser.add_argument("-d", "--debug", action="store_true", help="set log level to DEBUG")
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

    logging.info("----------------------------------------------------------------------------------------------------")
    logging.info("Image path: " + args.image_path)
    logging.info("Debug: " + str(args.debug))
    logging.info("----------------------------------------------------------------------------------------------------")

    run()
