clear,clc
x0=[7.0,10.5,13.0,17.5,34.0,40.5,44.5,48.0,56.0,61.0,68.5,76.5,80.5,91.0...
    96.0,101.0,104.0,106.5,111.5,118.0,123.5,136.5,142.0,146.0,150.0,157.0,158.0];
x1=[7.0,10.5,13.0,17.5,34.0,40.5,44.5,48.0,56.0,61.0,68.5,76.5,80.5,91.0...
    96.0,101.0,104.0,106.5,111.5,118.0,123.5,136.5,142.0,146.0,150.0,157.0,158.0];
y0=[44 45 47 50 50 38 30 30 34 36 34 41 45 46 43 37 33 28 32 65 55 54 52 50 66 66 68];
y1=[44 59 70 72 93 100 110 110 110 117 118 116 118 118 121 124 121 121 121 122 116 83 81 82 86 85 68];
x2=[7.0,10.5,13.0,17.5,34.0,40.5,44.5,48.0,56.0,61.0,68.5,76.5,80.5,91.0...
    96.0,101.0,104.0,106.5,111.5,118.0,123.5,136.5,142.0,146.0,150.0,157.0,158.0];
x3=[7.0,10.5,13.0,17.5,34.0,40.5,44.5,48.0,56.0,61.0,68.5,76.5,80.5,91.0...
    96.0,101.0,104.0,106.5,111.5,118.0,123.5,136.5,142.0,146.0,150.0,157.0,158.0];

%保形插值
y2=hermite1(x0,y0,y0,x2);
y3=hermite1(x1,y1,y0,x3);
plot(x2,y2,'b',x3,y3,'r'),axis([0 170 10 140])
hold on
title('保形插值')
Herm1(x0,y0,y0)
