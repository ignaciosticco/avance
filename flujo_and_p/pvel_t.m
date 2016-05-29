close;
clear all;
data=load('in_test.txt');

i=1;
nf=0;
while i<length(data(:,1))+1
	
	t(i)=0.05*(i-nf);
	if data(i,1)>20
		nf=i;
	end
i=i+1;
	
end

pv=data(:,3);
speed=data(:,4);
%length(t)
%length(pv)
%plot(t,pv,'o')

subplot(2,1,1), plot(t,pv,'or')%,'LineWidth',2)
xl=xlabel('time (s)'); 
set(xl,'FontSize',16);
yl=ylabel('PV'); 
set(yl,'FontSize',16);
hold on
grid on
subplot(2,1,2), plot(t,speed,'or')%,'LineWidth',2)
xl=xlabel('time (s)'); 
set(xl,'FontSize',16);
yl=ylabel('speed (m/s)'); 
set(yl,'FontSize',16);
hold on
grid on
