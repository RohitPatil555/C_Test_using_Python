from _pi_test import ffi,lib 

print('Startin pytest here ...')

class TestCode:
    def mock_my_send(self, k):
        print("Hurrrr .. I am in Mock function")

test = TestCode()

@ffi.def_extern()
def my_send(z):
    print("In python my send with => !!") 
    test.mock_my_send(z)  

@ffi.def_extern()
def my_env_get(name):
    ret = 0
    if name == "foo":
        print("Found env")
        ret = 2
    else:
        print("Fail to get envi %s"%(name))
    
    return ret

def test_one(mocker):
    tt = mocker.spy(test, 'mock_my_send')
    assert lib.test_1(2) == 3
    tt.assert_called_once_with(2)
    

def test_two():
    assert lib.test_2(2,3) == 5
