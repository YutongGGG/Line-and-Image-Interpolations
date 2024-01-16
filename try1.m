
img='lena.jpg';
I=imread(img);
zmf=2;
[ ZI ] = part( I,zmf );
imshow(ZI)