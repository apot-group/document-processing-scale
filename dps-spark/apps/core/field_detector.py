import os
os.chdir("/opt/spark-apps/")
import cv2
import numpy as np
import tensorflow.compat.v2 as tf
from core.helpers import load_label_map


class DetectorTF2(object):
    """Load model with tensorflow version from >= 2.0.0 
        
        @Param: path_to_model=path to your folder contains tensorflow models
        @Param: path_to_lables=path to file label_map.pbtxt
        @Param: score_threshold
        @Param: num_classes=number class of models
        
        @Response: {load_model} load tensorflow to backgroud system
        @Response: {predict} dict of [num_detections, detection_classes, score_detections]
        
    """ 
    
    def __init__(
        self, 
        path_to_model,
        path_to_labels, 
        nms_threshold, 
        score_threshold,
        num_classes
    ):
        self.path_to_model = path_to_model
        self.path_to_labels = path_to_labels
        self.nms_threshold = nms_threshold
        self.score_threshold = score_threshold
        self.num_classes = num_classes
        self.category_index = load_label_map.create_category_index_from_labelmap(
            path_to_labels, use_display_name=True)
        self.path_to_saved_model = self.path_to_model + "/saved_model"
        self.detect_fn = self.load_model()
    
    def load_model(self):
        detect_fn = tf.saved_model.load(self.path_to_saved_model)
        return detect_fn
    
    def predict(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_expanded = np.expand_dims(image_rgb, axis=0)

        # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
        input_tensor = tf.convert_to_tensor(image)
        
        # The model expects a batch of images, so add an axis with `tf.newaxis`.
        input_tensor = input_tensor[tf.newaxis, ...]

        # input_tensor = np.expand_dims(image_np, 0)
        detections = self.detect_fn(input_tensor)

        # All outputs are batches tensors.
        # Convert to numpy arrays, and take index [0] to remove the batch dimension.
        # We're only interested in the first num_detections.
        num_detections = int(detections.pop('num_detections'))
        detections = {key: value[0, :num_detections].numpy()
                       for key, value in detections.items()}
        detections['num_detections'] = num_detections
        detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
        
        return detections, self.category_index
