from setuptools import setup, find_packages

exec (open('isonet/version.py').read())

setup(name='isonet',
      version=__version__,
      description='Isotropic reconstruction of 3D fluorescence microscopy images using convolutional neural networks',
      url='https://github.com/maweigert/isonet',
      author='Martin Weigert',
      author_email='mweigert@mpi-cbg.de',
      license='BSD 3-Clause License',
      packages=find_packages(),

      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Topic :: Software Development',
          'Topic :: Scientific/Engineering',
          'License :: OSI Approved :: BSD License',

          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='science image-processing ',

      install_requires=["numpy>=1.11.0",
                        "gputools>=0.2.0",
                        "pyopencl>=2016.1",
                        "keras>=2.0.0"],

      entry_points={}
      )
