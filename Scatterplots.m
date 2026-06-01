
figure(1);
A=load('/Users/nishantabaral/Desktop/With Coriolis/St=0.2R=2_timescale=5000_south.txt');
sz = 0.5;
s = scatter(A(:,1),A(:,2),sz);
s.MarkerEdgeColor = 'b';
s.MarkerFaceColor = 'b';

xlabel('x','FontSize',18);
ylabel('y','FontSize',18);


xlim([0,2]);
ylim([0,1]);

ax = gca;
ax.FontSize = 18; 

box on;

%set(gcf, 'Units', 'normalized', 'Position', [0.2, 0.2, 0.2, 0.2]);
%ax.Position = [0.07, 0.15, 0.90, 0.75];



%saveas(s,'/Users/nishantabaral/Desktop/Geostrophic Quadrupole Flow/St=0.2R=2_T=20_timescale=10000_south.png');%
saveas(s,'/Users/nishantabaral/Desktop/With Coriolis/St=0.2R=2_timescale=5000_south.png')