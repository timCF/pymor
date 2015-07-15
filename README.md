PyMor
=====

Is simple console util for morph analysis. 

Usage 
-----

```
./release/mac/pymor привет всем мирам

['мирам', 'миров', 'весь', 'приветом', 'всей', 'приветами', 'приветов', 'привете', 'мир', 'всём', 'приветам', 'все', 'мира', 'всем', 'всея', 'всего', 'всё', 'привет', 'миром', 'миру', 'привету', 'привета', 'мире', 'мирами', 'всю', 'приветах', 'всеми', 'вся', 'миро', 'приветы', 'мирах', 'всему', 'всех', 'миры']
```

Building
--------

```
apt-get install python3
pip3 install pymorphy2
pip3 install pipe

git clone https://github.com/pyinstaller/pyinstaller.git
cd pyinstaller
git checkout python3
git checkout 8416a108392ebe677d1179b017fb09a2397176f1
sudo python3 setup.py develop
sudo pip3 install -e .

cd /PATH/TO/PYMOR
#
#	copy pymorphy2_dicts to libs if needed
#
sudo pyinstaller ./pymor.py
```