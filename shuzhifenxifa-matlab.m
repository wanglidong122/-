clc
%预设数据,P和M分别代表产地和销地，每行5列数据分别指坐标x，坐标y，运输总量v，运输费率r，迭代参数d即距离（初始默认为1，在后续迭代中会自行变动）
%P = [9,8,1971,0.05,1;7,10,3496,0.05,1];
%M = [13,4,2520,0.07,1;5,12,1334,0.07,1;11,6,1613,0.07,1];
%以上是一组未调用的数据，以下数据来自[1] 赵小柠.物流中心规划与设计[M].成都：西南交通出版社，2011. P63.
times = 15;%迭代次数
P = [3, 8, 2000, 0.05, 1;8, 2, 3000, 0.05, 1]
M = [2, 5, 2520, 0.075, 1;6, 4, 1000, 0.075, 1;8, 8, 1500, 0.075, 1]
A = [P;M];
[m,n]=size(A);
xy = [];
money = [];
for j = 1:1:times+1
    vrx = 0;
    vry = 0;
    vr = 0;
    one = 0;
    for i = 1:1:m
        vrx = vrx + A(i,3)*A(i,4)*A(i,1)/A(i,5);
        vry = vry + A(i,3)*A(i,4)*A(i,2)/A(i,5);
        vr = vr + A(i,3)*A(i,4)/A(i,5);
    end
    x0 = vrx/vr;
    y0 = vry/vr;
    for i = 1:1:m
        A(i,5) = ((A(i,1)-x0)^2+(A(i,2)-y0)^2)^(1/2);
    end
    xy = [xy;[x0,y0]];
    for i = 1:1:m
        one = one + A(i,3)*A(i,4)*A(i,5);
    end
    money = [money;one];
    disp(["迭代次数：",j-1,"物流中心坐标：",xy(j,:),"总成本：",money(j)]);
end

%拟建物流中心位置变化
figure(1);
scatter(xy(:,1),xy(:,2),"r","filled");
hold on;
scatter(P(:,1),P(:,2),"g");
scatter(M(:,1),M(:,2),"b");
hold off;
title("拟建物流中心位置变化图");
xlabel("X");
ylabel("Y");

%拟建物流中心坐标x,y分别的变化曲线
figure(2);
x=0:1:times;
plot(x,xy(:,1),'-*b',x,xy(:,2),'-or');
title("拟建物流中心坐标x,y分别的变化曲线");
xlabel("迭代次数");
ylabel("X或Y坐标值");

%运输总成本变化曲线
figure(3);
plot(x,money(:),'-*r');
title("运输总成本变化曲线");
xlabel("迭代次数");
ylabel("运输总成本");
