import matlab
den1=[1 3]
num=1
sys1=tf(num,den1);
rlocus(sys1);
hold on
rlocus(-sys1);


den2=[1 3 2]
sys2=tf(num,den2);
rlocus(sys2);
hold on
rlocus(-sys2)

% 
% den3=[1 4 5 0.5]
% sys3=tf(num,den3);
% rlocus(sys3);
% hold on
% rlocus(-sys3);

den4=[1 1 1 1 0]
sys4=tf(num,den4);
rlocus(sys4);
hold on
rlocus(-sys4);
