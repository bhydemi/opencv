import streamlit as st 
import cv2 
import numpy as np 
from PIL import Image 
from io import BytesIO
import base64


st.title('OpenCV Streamlit Demo')
st.header('Overview Page')
image = st.file_uploader('Upload an Image File', type=['jpg', 'jpeg', 'png'])



def detectFaceOpenCVDnn(net, frame):
    
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), [104, 117, 123], False, False)

    net.setInput(blob)
    detections = net.forward()
    return detections

def process_detections(frame, detections, conf_threshold=0.5):
    bboxes = []
    frame_h = frame.shape[0]
    frame_w = frame.shape[1]

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frame_w)
            y1 = int(detections[0, 0, i, 4] * frame_h)
            x2 = int(detections[0, 0, i, 5] * frame_w)
            y2 = int(detections[0, 0, i, 6] * frame_h)
            bboxes.append([x1, y1, x2, y2])
            bb_line_thickness = max(1, int(round(frame_h/200)))
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), bb_line_thickness, cv2.LINE_8)
    return frame, bboxes

@st.cache(allow_output_mutation=True)
def load_model():
    modelFile = 'transfer_learning_model/res10_300x300_ssd_iter_140000_fp16.caffemodel'
    configFile = 'transfer_learning_model/deploy.prototxt'
    net = cv2.dnn.readNetFromCaffe(configFile, modelFile)
    return net 

def get_image_download_link(image, filename, text):
    buffered = BytesIO()
    image.save(buffered, format='JPEG')
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href 

net = load_model()
if image is not None:
    raw_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR  )

    placeholders = st.columns(2)
    placeholders[0].image(image, channels='BGR')
    placeholders[0].text('Input Image')

    conf_threshold = st.slider('Set Confidence Threshold', min_value=0.0, max_value=1.0, step=.01, value=0.5)
    detections = detectFaceOpenCVDnn(net, image)

    out_image, _ = process_detections(image, detections, conf_threshold=conf_threshold)
    placeholders[1].image(out_image, channels='BGR')
    placeholders[1].text('Output Image')
    out_image = Image.fromarray(out_image[:,:,::-1])

    st.markdown(get_image_download_link(out_image, 'face_output.jpg', 'Download Output Image'), 
                unsafe_allow_html=True)

