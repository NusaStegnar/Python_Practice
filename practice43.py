"""
Write a Python program to get OS name, platform and release information.
"""

import platform
import os


print("Name of the operating sistem:", os.name)
print("\nName of the OS system:", platform.system())
print("\nVersion of the operating system:", platform.release())