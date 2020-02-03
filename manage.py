#!/usr/bin/env python
import os
import sys
import warnings

if __name__ == '__main__':
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_rest.settings')

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=FutureWarning)
        import tensorflow as tf
        from tensorflow import keras
        from tensorflow.keras.preprocessing.text import Tokenizer
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
