This repository presents the face recognition system project. With this system user can send to telegram bot its photo and find out what celebrity he looks like. Develop of the project consists three steps:
1.	Data collection: [VGG faces](https://www.robots.ox.ac.uk/~vgg/data/vgg_face/) dataset is used for training data.
2.	Training model: face detection via [RetinaFace](https://github.com/deepinsight/insightface/tree/master/detection/RetinaFace), extract face features via [FaceNet](https://github.com/nyoki-mtl/keras-facenet), SVM classifier for final classification.
3.	Provide user API for interaction with system: user interaction with system based on Telegram App.

Some notes:
1.	Dataset. VGG faces dataset consists of 2,622 identities. Each identity has an associated text file with 1000 rows, each row containing URLs for images and corresponding face detections. 
2.	Data loading. 'load_pictures' function is used to load pictures and save it in working directory. For memory economy only 20 random links are used. 
3.	Data processing. Some links in raw files may not available. By this reason request to the server is wrapped into try-except block. Some pictures may not include faces and hence call of the RetinaFace model also wrapped into try-exception construction.
