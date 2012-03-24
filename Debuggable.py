from django.core.management.base import CommandError
from django.conf import settings

def enable_debug_mode():
    # Check we have the required modules & settings for pydevd to work
    if not hasattr(settings, 'PYDEVD_SERVER'):
        raise CommandError("You must define a PYDEVD_SERVER entry in django conf settings.")
    if not hasattr(settings, 'PYDEVD_PATH_TRANSLATION'):
        raise CommandError("You must define a PYDEVD_PATH_TRANSLATION entry in django conf settings.")
    
    import contrib.pydevd
    contrib.pydevd.pydevd_file_utils.setup_translation_classes(settings.PYDEVD_PATH_TRANSLATION)
    
    print "Connecting to pydevd debug server on: %s\n" % settings.PYDEVD_SERVER
    # We must do this import manually now so that it imports the patched versions of the path-translation methods
    from contrib.pydevd import pydevd as pydevd_client
    pydevd_client.settrace(settings.PYDEVD_SERVER, stdoutToServer=True, stderrToServer=True, suspend=False)
