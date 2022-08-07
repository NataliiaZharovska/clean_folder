from setuptools import setup, find_packages

setup(name='clean_folder',
      version='1.1',
      description='code Natallia Zharovska',
      url='https://github.com/NataliiaZharovska/clean_folder',
      author='Natallia Zharovska',
      author_email='natalkadtk@gmail.com',
      license='MIT',
      entry_points={
        'console_scripts': ['clean-folder=clean_folder.clean:main']
      },
      packages=find_packages())