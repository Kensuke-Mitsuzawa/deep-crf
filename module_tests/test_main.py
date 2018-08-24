import unittest
from deepcrf import main
from tempfile import mkdtemp
import os


class TestMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if os.path.exists("./resources"):
            cls.path_input_file = "resources/input_file.txt"
        else:
            cls.path_input_file = "module_tests/resources/input_file.txt"

    @classmethod
    def tearDownClass(cls):
        pass

    def test_run(self):
        main.run(data_file=self.path_input_file,
                 is_train=True,
                 batchsize=32,
                 model_name="test_bilstm-cnn-crf",
                 optimizer="adam",
                 save_name="test_bilstm-cnn-crf",
                 save_dir=mkdtemp(),
                 gpu=-1,
                 dev_file=self.path_input_file,
                 test_file=self.path_input_file,
                 delimiter=" ",
                 input_idx="0",
                 output_idx="-1",
                 n_word_emb=100,
                 n_hidden=200,
                 n_layer=1,
                 n_char_emb=30,
                 n_char_hidden=30,
                 n_add_feature_emb=100,
                 use_cudnn=1,
                 init_lr=0.001,
                 model_filename=None,
                 max_iter=50
                 )


if __name__ == "__main__":
    unittest.main()
