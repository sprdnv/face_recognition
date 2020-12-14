This repository presents the face recognition system project. With this system user can send to telegram bot its photo and find out what celebrity he looks like. Develop of the project consists three steps:
1.	Data collection: [VGG faces](https://www.robots.ox.ac.uk/~vgg/data/vgg_face/) dataset is used for training data.
2.	Training model: face detection via [RetinaFace] (https://github.com/deepinsight/insightface/tree/master/detection/RetinaFace), extract face features via [FaceNet] (https://github.com/nyoki-mtl/keras-facenet), SVM classifier for final classification.
3.	Provide user API for interaction with system: user interaction with system based on Telegram App.
