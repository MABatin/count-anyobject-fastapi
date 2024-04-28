# count-anyobject-fastapi
A simple FastAPI application that can take an image and a prompt containing description (or name) of the objects that need to be counted. Newly released YOLO-worldv2 is used as the open vocabulary, zero-shot detection model.


## TODO
- [ ] Test YOLO-worldv2 functionality
- [ ] app.py functionalities
- [ ] *detect-from-txt* router - POST request with [img, classes]
- [ ] *fine-tune* router - POST request with [img, bboxes, classes]