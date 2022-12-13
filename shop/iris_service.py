
from keras.saving.save import load_model
from tensorboard.compat import tf
from tensorflow.python.tpu import datasets

"""
Iris Species
Classify iris plants into three species in this classic dataset
"""





class IrisService(object):
    def __init__(self):
        self.model = load_model('./save/iris_model.h5')
        self.graph = tf.get_default_graph()
        self.target_names = datasets.load_iris().target_names

    def hook(self):
        self.service_model()


    def service_model(self):
        pass


iris_menu = ["Exit", #0
                "hook"] #1
iris_lambda = {
    "1" : lambda x: x.hook(),
}
if __name__ == '__main__':
    iris = IrisService()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(iris_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                iris_lambda[menu](iris)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")
