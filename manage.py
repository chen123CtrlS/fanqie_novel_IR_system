#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# postings list中每一项为一个Posting类对象
class Posting(object):
    def __init__(self, docid, tf=0):
        self.docid = docid
        self.tf = tf
    def __repr__(self):
        return "<docid: %d, tf: %d>" % (self.docid, self.tf)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fanqie_novel.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
