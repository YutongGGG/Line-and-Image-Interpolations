function [ ZI ] = part(zmf )
%function [ ZI ] = part( I,zmf )
img='lena.jpg';
I=imread(img);
% zmf = 0.2
if ~exist('I','var') || isempty(I)
    error('输入图像 I未定义或为空！');
end
if ~exist('zmf','var') || isempty(zmf) || numel(zmf) ~= 1 
    error('位移矢量 zmf未定义或为空或 zmf中的元素超过2！');
end
if isstr(I) 
    [I,M] = imread(I);
end
if zmf <= 0
    error('缩放倍数 zmf的值应该大于0！');
end
%% Step2 通过原始图像和缩放因子得到新图像的大小，并创建新图像。
[IH,IW,ID] = size(I);
ZIH = round(IH*zmf); 
ZIW = round(IW*zmf); 
ZI = zeros(ZIH,ZIW,ID); 
%% Step3 扩展矩阵I边缘
IT = zeros(IH+2,IW+2,ID);
IT(2:IH+1,2:IW+1,:) = I;
IT(1,2:IW+1,:)=I(1,:,:);IT(IH+2,2:IW+1,:)=I(IH,:,:);
IT(2:IH+1,1,:)=I(:,1,:);IT(2:IH+1,IW+2,:)=I(:,IW,:);
IT(1,1,:) = I(1,1,:);IT(1,IW+2,:) = I(1,IW,:);
IT(IH+2,1,:) = I(IH,1,:);IT(IH+2,IW+2,:) = I(IH,IW,:);
%% Step4 由新图像的某个像素（zi，zj）映射到原始图像(ii，jj)处，并插值。
for zj = 1:ZIW 
    for zi = 1:ZIH
        ii =( zi-1)/zmf; jj = (zj-1)/zmf;
        i = floor(ii); j = floor(jj);
        u = ii - i; v = jj - j;
        i = i + 1; j = j + 1;
        if jj<=u+j
            ZI(zi,zj,:) = IT(i,j,:)+(IT(i+1,j,:)-IT(i,j,:))*u+(IT(i+1,j+1,:)-IT(i+1,j,:))*v;
        else
            ZI(zi,zj,:) = IT(i,j,:)+(IT(i,j+1,:)-IT(i,j,:))*v+(IT(i+1,j+1,:)-IT(i,j+1,:))*u;
        end
    end
end


ZI = uint8(ZI);
imwrite(ZI,'.\lena2.jpg')