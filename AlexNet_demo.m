img = imread('D:\MyFiles\garbageclassify\H.jpg');
img = imresize(img,[227,227]);
imshow(img)
deepnet = alexnet;
pred = classify(deepnet,img)
