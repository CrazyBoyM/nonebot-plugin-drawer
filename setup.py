from asyncore import read
from setuptools import Extension, dist, find_packages, setup

with open('README.md', encoding='utf-8') as f:
  long_description = f.read()
  setup(
      name='nonebot-plugin-drawer',
      version='0.1.2',
      description='适用于 Nonebot2 的AI画画插件(对接文心大模型API)',
      long_description=long_description,
      keywords='computer art, wenxin, AI, nonebot, plugin',
      packages=find_packages(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
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