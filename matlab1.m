%Read in image and resize to target size
img = imread('mickey.png');
img = im2gray(img);
%I had to use 50 x 50 because I was getting an error that the input was too
%large when using any higher sizes. It still works, the images are just far
%lower quality unfortunately.
img = imresize(img, [50, 50]);

%Reshape image to 1D and write to file
img_1d = reshape(img, 1, []);
dlmwrite('input.txt', img_1d, 'delimiter', ' ');