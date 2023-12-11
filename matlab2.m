%Read C and convert to 2D matrix
c_result = dlmread('c_output.txt');
c_matrix = reshape(c_result, [50, 50]);

%read in original image and convert to grayscale
img = imread('mickey.png');
img = im2gray(img);
img = imresize(img, [50, 50]);

%read in haskell image result
hs_result = dlmread('haskell_output.txt');
hs_matrix = reshape(hs_result, [50, 50]);

%read in prolog image result
pl_result = dlmread('prolog_output.txt');
pl_matrix = reshape(pl_result, [50, 50]);

%Plot each image
figure;
subplot(2, 2, 1);
imshow(img);
title('Original Image');

subplot(2, 2, 2);
imshow(uint8(c_matrix));
title('C Image');

subplot(2, 2, 3);
imshow(uint8(hs_matrix));
title('Haskell Image');

subplot(2, 2, 4);
imshow(uint8(pl_matrix));
title('Prolog Image');

