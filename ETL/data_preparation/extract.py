import os
import shutil
import random

class Extract:
    def __init__(self, data_dir, train_dir, test_dir, val_dir):
        self.data_dir = data_dir
        self.train_dir = train_dir
        self.test_dir = test_dir
        self.val_dir = val_dir

    def create_directories(self):
        os.makedirs(self.train_dir, exist_ok=True)
        os.makedirs(self.test_dir, exist_ok=True)
        os.makedirs(self.val_dir, exist_ok=True)
        
        self._create_class_directories(self.train_dir)
        self._create_class_directories(self.test_dir)
        self._create_class_directories(self.val_dir)

    def _create_class_directories(self, parent_dir):
        classes = ['absent', 'present']
        for class_name in classes:
            class_path = os.path.join(parent_dir, class_name)
            os.makedirs(class_path, exist_ok=True)

    def split_data(self, test_ratio, val_ratio):
        file_list = os.listdir(self.data_dir)
        random.shuffle(file_list)
        total_files = len(file_list)
        test_split = int(total_files * test_ratio)
        val_split = int(total_files * val_ratio)

        test_files = file_list[:test_split]
        val_files = file_list[test_split:test_split+val_split]
        train_files = file_list[test_split+val_split:]

        self._move_files(test_files, self.data_dir, self.test_dir)
        self._move_files(val_files, self.data_dir, self.val_dir)
        self._move_files(train_files, self.data_dir, self.train_dir)

    def _move_files(self, file_list, src_dir, dest_dir):
        for file_name in file_list:
            src_path = os.path.join(src_dir, file_name)
            class_name = self._get_class_from_filename(file_name)
            dest_class_dir = os.path.join(dest_dir, class_name)
            os.makedirs(dest_class_dir, exist_ok=True)
            dest_path = os.path.join(dest_class_dir, file_name)
            shutil.move(src_path, dest_path)

    def _get_class_from_filename(self, filename):
        suffix = os.path.splitext(filename)[0][-1]
        if suffix == '0':
            return 'absent'
        elif suffix == '1':
            return 'present'
        else:
            raise ValueError(f"Invalid filename format: {filename}")