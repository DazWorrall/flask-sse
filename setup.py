from distutils.core import setup
import sys

setup(name='flask_sse',
      version='0.1',
      author='Darren Worrall',
      author_email='daz@dwuk.net',
      url='https://github.com/DazWorrall/flask-sse',
      description="Flask extension providing SSE support",
      py_modules=['flask_sse',],
      provides=['flask_sse',],
      install_requires=[l.strip() for l in open('requirements.txt').readlines()],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                  ],
     )
