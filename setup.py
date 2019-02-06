from distutils.core import setup

setup(name='cypher_app',
      version='0.1',
      description='A simple application used for cyphers',
      url='https://github.com/gxldCptRick/Math_Based_Code_Cyphers.git',
      author='GXLD CPT RICK',
      author_email='andreshcar@live.com',
      license='Apache License 2.0',
      packages=['cypher_app', 'cypher_app.supported_cyphers',
                'cypher_app.supported_cyphers.helpers', 'cypher_app.command_line'],
      install_requires=[
          'langdetect',
      ],
      zip_safe=False)
