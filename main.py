# from ETL.data_preparation.extract import Extract

# if __name__ == "__main__":
#     data_dir = '/Users/arnavsharma/Downloads/ALL_IDB1/im'
#     train_dir = '/Users/arnavsharma/Desktop/all_detection/Dataset/train'
#     test_dir = '/Users/arnavsharma/Desktop/all_detection/Dataset/test'
#     val_dir = '/Users/arnavsharma/Desktop/all_detection/Dataset/validation'

#     etl = Extract(data_dir, train_dir, test_dir, val_dir)
#     etl.create_directories()
#     etl.split_data(test_ratio=0.1, val_ratio=0.1)

# from ETL.image_processing.segment import Segment
# import cv2
# import matplotlib.pyplot as plt 


# if __name__ == "__main__":
#     sam_checkpoint = "/Users/arnavsharma/Downloads/sam_vit_h_4b8939.pth"
#     model_type = "vit_h" #
#     device = "cpu" #cpu,cuda
#     seg = Segment(sam_checkpoint, model_type, device)
#     img = cv2.imread('/Users/arnavsharma/Downloads/1.jpg')
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     masked_img = seg.segment_img(img)
#     plt.imsave('/Users/arnavsharma/Downloads/masked_1.jpg', masked_img)


from ETL.AWS.bucket import Bucket
from ETL.AWS.apis import S3

# s3 = Bucket('arnav2002-garbage-bucket')
# Get all the environment variables

api = S3('arnav2002-garbage-bucket')
# api.save_file('/Users/arnavsharma/Downloads/1.jpg','garbage-image-1')
api.save_file('/Users/arnavsharma/Desktop/IIT Indore/models/sam/sam_vit_h_4b8939.pth','garbage-model-1')



