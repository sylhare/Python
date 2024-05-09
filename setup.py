from setuptools import setup, find_packages

setup(name='python',
      version='3.10.0',
      description='Experiments on python',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='flask chart.js web app chart charpy',
      url='http://github.com/sylhare/python',
      author='sylhare',
      author_email='sylhare@outlook.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=False,
      zip_safe=False
      )
