# Source - https://superuser.com/a/1688176
# Posted by grawity, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-23, License - CC BY-SA 4.0

#!/usr/bin/env python3
import argparse
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument("input")
args = parser.parse_args()

with open(args.input, "rb") as fh:
    buf = fh.read()
    buf = buf.decode("utf-8", errors="surrogateescape")
    buf = re.sub(r"[\udc00-\udcff]+",
                 lambda m: (m.group(0)
                             .encode("utf-8", errors="surrogateescape")
                             .decode("cp1252")),
                 buf)
    sys.stdout.write(buf)
