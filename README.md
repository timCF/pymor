PyMor
=====

Is simple console util for morph analysis. 

Usage 
-----

```
./dist/pymor/pymor привет всем мирам

['мирам', 'миров', 'весь', 'приветом', 'всей', 'приветами', 'приветов', 'привете', 'мир', 'всём', 'приветам', 'все', 'мира', 'всем', 'всея', 'всего', 'всё', 'привет', 'миром', 'миру', 'привету', 'привета', 'мире', 'мирами', 'всю', 'приветах', 'всеми', 'вся', 'миро', 'приветы', 'мирах', 'всему', 'всех', 'миры']
```

Building
--------

```
git clone https://github.com/pyinstaller/pyinstaller.git
git checkout 8416a108392ebe677d1179b017fb09a2397176f1
cd pyinstaller
sudo python3 setup.py develop
sudo pip3 install -e .
cd /PATH/TO/PYMOR
#
# copy pymorphy2_dicts to libs if needed
#
sudo pyinstaller ./pymor.py
```