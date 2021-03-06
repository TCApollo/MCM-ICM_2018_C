CA=textread('ca.txt');
n=size(CA,1);
m=size(CA,2)-1;
for i=1:1:m
    %级比lamda
    lamda=CA(1:n-1,i)./CA(2:n,i);
    %计算级比范围,再与覆盖cover比较
%     range=minmax(lamda);
%     cover=[exp(-(2/n+1)),exp(2/n+2)];
    %按行累加求和再转置
    x1=cumsum(CA(:,i)',2)';
    %求出数据矩阵B
    B=[-0.5*(x1(1:n-1)+x1(2:n)),ones(n-1,1)];
    %求出数据向量Y
    Y=CA(2:n,i);
    %拟合参数
    u=B\Y;
    %建立模型求解
    syms x(t)
    x=dsolve(diff(x)+u(1)*x==u(2),x(0)==CA(1,i),x(0)==CA(1,i));
    xt=vpa(x,6);%微分方程解,带t的符号表达式
    %求未来数据的预测值
    yuce1=subs(x,t,[0:n+49]);
    yuce1=double(yuce1);
    %差分运算，还原数据
    yuce=[CA(1,i),diff(yuce1)];
    
    
    
    
%     rho=rho';
%     yuce1=yuce1';
%     yuce=yuce';
%     delta=delta';
%     epsilon=epsilon';
    
    
    %写入文件
     %预测数据
     RANGE = strcat('BC', int2str(i+1), ':EX', int2str(i+1));
     xlswrite('ca_index.xls',yuce,RANGE);
end
