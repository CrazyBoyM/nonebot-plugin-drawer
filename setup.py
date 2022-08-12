from setuptools import Extension, dist, find_packages, setup

setup(
    name='nonebot-plugin-drawer',
    version='0.0.1',
    description='适用于 Nonebot2 的AI画画插件',
    long_description='适用于 Nonebot2 的AI画画插件',
    keywords='computer art',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
    ],
    url='https://github.com/CrazyBoyM/nonebot-plugin-drawer',
    author='CrazyBoyM',
    author_email='ai-lab@foxmail.com',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    # install_requires=install_requires,
    # ext_modules=EXT_MODULES,
    # cmdclass={'build_ext': build_ext},
    zip_safe=False)