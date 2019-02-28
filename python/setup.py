#!/usr/bin/env python
import os
import platform
import sys

from setuptools import Extension, setup


def cmd1(str):
    return os.popen(str).readlines()[0][:-1]


def cmd2(str):
    return cmd1(str).split()


if platform.system() == 'Windows':
    if sys.maxsize > 2**32:  # 64bit
        raise WindowsError('64bit Python for Windows is not supported')
    else:  # 32bit
        ext_modules = [
            Extension(
                "_CaboCha",
                ["CaboCha_wrap.cxx"],
                include_dirs=["C:\Program Files (x86)\CaboCha\sdk"],
                library_dirs=["C:\Program Files (x86)\CaboCha\sdk"],
                libraries=["libcabocha"]
            )
        ]
        data_files = [('lib\\site-packages\\',
            ["C:\Program Files (x86)\CaboCha\\bin\libcabocha.dll",
             "C:\Program Files (x86)\CaboCha\\bin\libcrfpp.dll"])]
else:
    ext_modules = [
          Extension("_CaboCha",
                    ["CaboCha_wrap.cxx"],
                    include_dirs=cmd2("cabocha-config --inc-dir"),
                    library_dirs=cmd2("cabocha-config --libs-only-L"),
                    libraries=cmd2("cabocha-config --libs-only-l"))
    ]
    data_files = None

setup(name="cabocha-python",
      version='0.69',
      py_modules=["CaboCha"],
      ext_modules=ext_modules,
      data_files=data_files,
      author='Yukino Ikegami',
      author_email='yknikgm@gmail.com',
      url='https://github.com/ikegami-yukino/cabocha/tree/master/python',
      license='BSD or LGPL',
      platforms=['Windows', 'macOS', 'Linux'],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: Japanese',
        'Intended Audience :: Science/Research',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing'
      ],
      description='Python wrapper for CaboCha: Japanese Dependency Structure Analyzer',
      long_description='''This is a python wrapper for CaboCha.

      NOTE: It does not sopport Windows Python 64bit version.

    License
    ---------
    CaboCha is copyrighted free software by Taku Kudo <taku@chasen.org>
is released under any of the the LGPL (see the file LGPL) or the
BSD License (see the file BSD).
    '''
)
