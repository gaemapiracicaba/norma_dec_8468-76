from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

requirements = []
for line in open('requirements.txt'):
    li = line.strip()
    if not li.startswith('#'):
        requirements.append(line.rstrip())

VERSION = (1, 1, 6)  # (1, 0, 7, 'dev0')
__version__ = '.'.join(map(str, VERSION))

setup(
    name='decreto_estadual_8468',  # Nome (não precisa ser o nome do repositório, nem de qualquer pasta...)
    version=__version__,
    author='Michel Metran',
    author_email='michelmetran@gmail.com',
    description='O projeto objetiva disponibilizar os parâmetros de qualidade em formato adequado para utilização em análises computacionais',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gaemapiracicaba/norma_dec_8468-76',
    keywords='python, water, water-quality, water-resources',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese',
        'Intended Audience :: Developers',
    ],

    # Qual python? e packages?
    python_requires='>=3',
    install_requires=requirements,

    # Entry
    package_dir={'': 'src'},  # Our packages live under src but src is not a package itself

    # Quando são diversos módulos...
    packages=find_packages('src', exclude=['test']),

    # Apenas um módulo...
    #py_modules=['decreto_estadual_8468'],  # Quando se trata apenas de um módulo

    # Dados
    include_package_data=True,
    package_data={'': ['data/tab_dec_8468.xlsx']},
)
