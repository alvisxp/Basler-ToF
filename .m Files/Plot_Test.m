%fileID = fopen('image2_test.txt','r');
%formatspec = '%4f';
%A = fscanf(fileID,formatspec);
%print(A)

%pcloud = pcread('image3.pcd');
%scatter3(pcloud)
%pcshow(pcloud)
%tbl = readtable('image3.csv');
%scatter3(tbl,'x','y','z');

tbl = readtable('image3comp.xlsx');
scatter3(tbl,'x','y','z','MarkerEdgeColor','black','Marker','.');
%scatter3(tbl,'x','y','z');