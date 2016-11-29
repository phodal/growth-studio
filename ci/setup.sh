PATH=$WORKSPACE/py35env/bin:/usr/local/bin:$PATH
if [ ! -d "py35env" ]; then
  virtualenv --distribute -p /usr/local/bin/python3.5 py35env
fi
. py35env/bin/activate
pip3 install fabric3
pip3 install -r requirements/dev.txt

