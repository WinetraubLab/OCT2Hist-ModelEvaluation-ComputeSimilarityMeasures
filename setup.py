from setuptools import setup

setup(
    name='OCT2Hist-ModelEvaluation-ComputeSimilaritySimilarityMeasures',
    url='https://github.com/WinetraubLab/OCT2Hist-ModelEvaluation-ComputeSimilarityMeasures',
    author='me',
    author_email='patricio.ilan.gonzalez2001@gmail.com',
    packages=['OCT2Hist-ModelEvaluation-ComputeSimilaritySimilarityMeasures'],
    install_requires=['numpy',
                      'skimage',
                      'scipy',
                      'csv',
                      'os',
                      'cv2',
                      'google.colab.patches',
                      'matplotlib',
                      ],
    version='0.1.0',
    description='description',
    long_description=open('README.md').read()
)