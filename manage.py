<<<<<<< HEAD
﻿#!/usr/bin/env python
=======
#!/usr/bin/env python
>>>>>>> 009df0ffc57ddd5736de8738092067bf21f48c79
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mlproject.settings')
>>>>>>> 009df0ffc57ddd5736de8738092067bf21f48c79
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
