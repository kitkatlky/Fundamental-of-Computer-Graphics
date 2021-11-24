import pip
from pip._internal import main as pipmain
def install_whl(path):
    pipmain(['install',path])
install_whl('C:/PyOpenGL_accelerate-3.1.5-cp37-cp37m-win_amd64.whl')
# install_whl('C:/PyOpenGL-3.1.5-cp37-cp37m-win_amd64.whl')